# can use request module
import requests
import argparse

def call_api():
    parser = argparse.ArgumentParser()

    parser.add_argument("-u", "--username", help='<Required> Set flag', required=True)
    parser.add_argument("-p", "--password", help='<Required> Set flag', required=True)
    parser.add_argument("-i", "--images", nargs='+', help='<Required> Set flag', required=True)

    args = parser.parse_args()
    api = "http://localhost:5000/api/ocr"
    print(args)

    fs = {}
    for i in range(len(args.images)):
        fs[str(i)] = open('./libs/screenshots/'+args.images[i], 'rb')

    print(fs)
    params = {"user_name" : args.username, "password" : args.password}
    print(requests.post(api, params, files=fs).text)

if __name__ == "__main__":
    call_api()