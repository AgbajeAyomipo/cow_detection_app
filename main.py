# https://app.roboflow.com/fiverr-bvwjh/cow-detection-thxuy/
from PyQt5.QtWidgets import QApplication, QMainWindow, QInputDialog, QMessageBox
from PyQt5.QtGui import QImage, QPixmap
from PyQt5.QtCore import pyqtSignal, QThread, QTimer

import sys
import cv2
from resources.ui_gui import Ui_MainWindow
import os
import requests
from ultralytics import YOLO
import shutil

API_URL = "http://127.0.0.1:5000/detect_cows"
VIDEO_PATH = ''
USE_SERVER = ''
CWD = os.getcwd()

class VideoThread(QThread):
	update_signal = pyqtSignal(list)

	def __init__(self, parent=None):
		super().__init__(parent)
		self.model = YOLO('resources/models/best.pt')

	def call_detection_api(self, frame):
		
		results = self.model(frame,conf=0.4)
		# results = model(frame,conf=0.4, device='0')

		locations = []

		for r in results:
			boxes = r.boxes
			for box in boxes:
				b = box.xyxy[0]
				conf = round(box.conf[0].item(), 2)
				name = r.names[box.cls[0].item()]
				x1,y1,x2,y2 = int(b[0].item()),int(b[1].item()),int(b[2].item()), int(b[3].item())
				
				cv2.rectangle(frame,(x1,y1),(x2,y2),(0,255,0),2)
				cv2.putText(frame,f'{str(name)} {str(conf)}',(x1,y1-5),cv2.FONT_HERSHEY_COMPLEX_SMALL,1.5,(0,255,0),1)

				locations.append([x1,y1,x2,y2])

		return frame, locations
	
	def run(self):
		global VIDEO_PATH, USE_SERVER
		if VIDEO_PATH!='':
			cap = cv2.VideoCapture(VIDEO_PATH)

			while True:
				ret, frame = cap.read()
				display_frame = frame.copy()

				if not ret:
					print('VIDEO ENDED')

				if USE_SERVER != '':
					display_frame, locations = self.call_detection_api(frame)
				
				self.update_signal.emit([frame, display_frame, locations])

	def stop(self):
		global USE_SERVER
		USE_SERVER = '1'

class MainWindow(QMainWindow):

	def __init__(self):
		global CWD

		super().__init__()
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)
		self.setWindowTitle('Cow monitoring')
		# self.setWindowIcon(QIcon('resources/icon.png'))
		

		self.ui.video_source_btn.clicked.connect(lambda: self.select_video())
		self.ui.start_stop_btn.clicked.connect(lambda: self.toggle_start_stop())
		self.ui.snapshot_btn.clicked.connect(lambda: self.take_snapshot())

		if not os.path.exists('resources'):
			os.mkdir('resources')

		if not os.path.exists('resources/locations'):
			os.mkdir('resources/locations')

		with open(f"resources/theme.qss", "r") as f:
			self.setStyleSheet(f.read())

		self.video_source = ''
		self.snapshot_path = ''
		self.start_detection = False
		self.fence_data = []
		self.sent_ids = {}
		self.api_url = ''
		
		self.load_paths()
		self.camera_thread = VideoThread()
		self.camera_thread.update_signal.connect(self.showcam)
		self.timer = QTimer()
		self.timer.timeout.connect(self.reset_values)
		self.timer.start(5)

	def take_snapshot(self):
		if not os.path.exists('snapshots'):
			os.mkdir('snapshots')
		self.snapshot_path = f'snapshots/{len(os.listdir("snapshots"))+1}/'
		os.mkdir(self.snapshot_path)

	def load_paths(self):
		list_of_files = os.listdir('resources/locations')

		for index, file in enumerate(list_of_files):
			path = f'resources/locations/{file}'

			data = ''
			with open(path, 'r') as r:
				data = r.read()
			
			if data != '': data = data.split(',')

			if len(data) == 5:
				x1,y1,x2,y2,url = int(data[0]),int(data[1]),int(data[2]),int(data[3]),data[4]
				fence_midpoint = ((x1 + x2) // 2, (y1 + y2) // 2)
				self.fence_data.append([x1,y1,x2,y2,fence_midpoint,url,index])

	def select_video(self):
		global VIDEO_PATH

		answer, done = QInputDialog.getText(self, 'Video Source', 'Enter video source')
		if done:
			if str(answer).isnumeric():
				answer = int(answer)
			
			cap = cv2.VideoCapture(answer)
			
			for _ in range(30):
				ret, img = cap.read()

			if ret is False:
				print('ERROR READING VIDEO')
				return
			
			if len(self.fence_data) == 8:
				resp = QMessageBox.question(self,'Reload', "Existing data found, do you want to reload?", QMessageBox.Yes | QMessageBox.No)

				if resp == QMessageBox.No:
					VIDEO_PATH = answer
					self.toggle_start_stop()
					self.camera_thread.start()
					return

			self.fence_data.clear()

			shutil.rmtree('resources/locations')
			os.mkdir('resources/locations')

			for i in range(8):
				for coord in self.fence_data:
					cv2.rectangle(img,(coord[0],coord[1]),(coord[2],coord[3]),(0,0,0),2)

				rectangle_coords = cv2.selectROI("Frame", img, fromCenter=False,showCrosshair=True)
				x1, y1, w, h = rectangle_coords
				x2 = x1+w
				y2 = y1+h

				url = ''

				while url == '':
					url, _ = QInputDialog.getText(self, 'Url', f'Enter url for {i}:') 

				with open(f'resources/locations/{i}.txt', 'w') as w:
					w.write(f'{x1},{y1},{x2},{y2},{url}')

				fence_midpoint = ((x1 + x2) // 2, (y1 + y2) // 2)
				self.fence_data.append([x1,y1,x2,y2,fence_midpoint,url,i])

			cv2.destroyAllWindows()
			VIDEO_PATH = answer
			self.toggle_start_stop()
			self.camera_thread.start()

	def toggle_start_stop(self):
		global USE_SERVER

		if self.ui.start_stop_btn.text() == 'Start':
			self.ui.start_stop_btn.setText('Stop')
			USE_SERVER = '1'
		else:
			self.ui.start_stop_btn.setText('Start')
			USE_SERVER = ''

	def send_api_get_request(self, url):
		print('SENDING REQUEST TO URL: ',url)
		if url == '':
			print('URL NOT FOUND ')
			return False
		
		try:
			response = requests.get(url)

			# Check if the request was successful (status code 200)
			if response.status_code == 200:
				print("GET request successful.")
				print("Response content:")
				print(response.text)
			else:
				print(f"Error: {response.status_code} - {response.text}")

		except requests.exceptions.RequestException as e:
			print(f"Request failed: {e}\n'{url}'")
			return False

		return True

	# -------------------------- Detection functions ----------------------------
	def showcam(self, frames):
		"""
		This method processes and displays frame of given camera

		Camera input is taken by a timer
		"""
		frame, display_frame, cow_locations = frames

		for coord in self.fence_data:
			cv2.rectangle(display_frame,(coord[0],coord[1]),(coord[2],coord[3]),(0,0,255),2)
		
		for x1, y1, x2, y2 in cow_locations:
			cv2.rectangle(display_frame,(x1,y1),(x2,y2),(0,0,255),2)
			cow_midpoint = ((x1 + x2) // 2, (y1 + y2) // 2)

			for fence_coord in self.fence_data:
				if fence_coord[6] in self.sent_ids.keys():
					continue

				fence_midpoint = fence_coord[4]
				
				if (fence_coord[0] <= cow_midpoint[0] <= fence_coord[2]) and (fence_coord[1] <= cow_midpoint[1] <= fence_coord[3]):
				
					if cow_midpoint[1] > fence_midpoint[1]:
						self.send_api_get_request(fence_coord[5])
						self.sent_ids[fence_coord[6]] = 0

		if self.snapshot_path != '':
			cv2.imwrite(self.snapshot_path+'simple.jpg', frame)
			cv2.imwrite(self.snapshot_path+'detection.jpg', display_frame)
			self.snapshot_path = ''

		# --------------------------Main Image------------------------------------
		display_frame = cv2.cvtColor(display_frame, cv2.COLOR_BGR2RGB)
		heightt, widthh, channel = display_frame.shape
		step = channel * widthh
		qImg = QImage(display_frame.data, widthh, heightt, step, QImage.Format_RGB888)
		
		# Displaying frame in window
		self.ui.display_lbl.setPixmap(QPixmap.fromImage(qImg))
		# --------------------------------------------------------------------------
	
	def reset_values(self):
		sent_ids = self.sent_ids.copy()
		for val in sent_ids:
			self.sent_ids[val] += 1
			if self.sent_ids[val] >= 1800:
				print('\n\n\n\n\nPOPPPINGGG\n\n\n\n\n')
				self.sent_ids.pop(val)
	# ---------------------------------------------------------------------------

if __name__ == '__main__':
	app = QApplication(sys.argv)
	mainWindow = MainWindow()
	mainWindow.show()
	sys.exit(app.exec_())
