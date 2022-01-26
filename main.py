# Made by SuchBlue -=- https://github.com/MoneroOceanThresholdUpdater #

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
        threshold = float(input("Enter Threshold: "))
        timeout = float(input("Enter Timeout (minutes): "))
        address = str(input("Enter XMR Address: "))
        out = [address]

        def otherAddress():
            # Change string to array
            newAddress = str(input("Please enter another XMR address. "))
            out.append(newAddress)

        def oaDialog():
            choice = str(input("Do you want to enter another address? (y/n): "))
            if(choice.startswith("y")):
                otherAddress()
                oaDialog()
            elif(choice.startswith("n")):
                pass
            else:
                print("Invalid choice.")
                oaDialog()

        oaDialog()
        
        if not (out == [address]):
            address = out

        # print(f"[DEBUG] {address}")
        # print(f"[DEBUG] {type(address)}")

        if type(address) == list:
            while True:
                for s in address:
                    payload = {"username":s,"threshold":threshold}
                    r = requests.post("https://api.moneroocean.stream/user/updateThreshold", data=json.dumps(payload), headers=headers)
                    print(f"Sent a request for address {str(s)}. Total times: {str(i)}")
                    i += 1
                sleep(timeout * 60)

        elif type(address) == str:
            if address.lower() == "default":
                address = "enter your address here"

            payload = {"username":address,"threshold":threshold}
            while True:
                r = requests.post("https://api.moneroocean.stream/user/updateThreshold", data=json.dumps(payload), headers=headers)
                print(f"Sent a request. Total times: {str(i)}")
                sleep(timeout * 60)
                i += 1
        
    except ValueError:
        print("An error occurred. (Did you put a real number?)")
        pass
