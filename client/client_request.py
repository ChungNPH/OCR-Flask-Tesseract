# can use request module
import requests
import argparse

def call_api():
    parser = argparse.ArgumentParser()

    parser.add_argument("--username")
    parser.add_argument("--password")
    parser.add_argument("--image")

    args = parser.parse_args()
    api = "http://localhost:5000/api/ocr"
    files = {'image': open('./libs/screenshots/'+args.image, 'rb')}
    params = {"user_name" : args.username, "password" : args.password}
    print(requests.post(api,params, files=files ).text)

if __name__ == "__main__":
    call_api()