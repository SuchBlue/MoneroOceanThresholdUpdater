from time import sleep
import requests
import json

i = 1

url = "https://api.moneroocean.stream/user/updateThreshold"
headers = {
    "accept": "*/*",
    "accept-language": "en-US;q=0.8",
    "content-type": "application/json",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Unknown\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "Referer": "https://moneroocean.stream/",
    "Referrer-Policy": "strict-origin-when-cross-origin"
}

while True:
    try:
        threshold = float(input("enter threshold: "))
        timeout = float(input("enter timeout (minutes): "))
        address = str(input("enter address: "))
        if address.lower() == "default":
            address = "enteryouraddresshere"
        payload = {"username":address,"threshold":threshold}
        while True:
            r = requests.post("https://api.moneroocean.stream/user/updateThreshold", data=json.dumps(payload), headers=headers)
            if str(i).endswith("1") and (i < 11 or i > 19):
                print(f"Sent a request for the {str(i)}st time.")
            elif str(i).endswith("2") and (i < 11 or i > 19):
                print(f"Sent a request for the {str(i)}nd time.")
            elif str(i).endswith("3") and (i < 11 or i > 19):
                print(f"Sent a request for the {str(i)}rd time.")
            else:
                print(f"Sent a request for the {str(i)}th time.")
            sleep(timeout * 60)
            i += 1
    except ValueError:
        print("An error occurred. (Did you put a real number?)")
        pass
