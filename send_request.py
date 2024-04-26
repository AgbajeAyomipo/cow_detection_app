import requests

def send_api_get_request(url):

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

send_api_get_request('http/google.com')
