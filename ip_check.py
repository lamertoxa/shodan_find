import logging
import os
import time
import requests
from requests.auth import HTTPBasicAuth


from requests.exceptions import SSLError, ConnectionError,ReadTimeout

with open("FindShodan/parsed/tplink2.txt") as data:
    filename = time.strftime("%Y%m%d-%H%M%S.txt")
    filepath = os.path.join("ipchecked", filename)
    for i in data.read().split("\n"):
        try:
            logging.warning(f"{i}")
            first_response = requests.get(f"http://{i.split()[0]}:{i.split()[1]}",verify=False,timeout=10)
            if first_response.headers.get('WWW-Authenticate', None) == None:
                continue
            time.sleep(1)
            response=requests.get(f"http://{i.split()[0]}:{i.split()[1]}",auth=HTTPBasicAuth('admin', 'admin'),verify=False,timeout=10)
            logging.warning(f"RESP:{response.status_code}")
            # logging.warning(f"DATA:{response.text}")
        except SSLError as e:
            print (e)
            continue
        except ConnectionError as e:
            print (e)
            continue
        except  ReadTimeout as e:
            print(e)
        else:
            if response.status_code != 200:
                continue
            elif "input" in response.text:
                continue
            # elif "403 Access Denied" in response.text or "401 Unauthorized" in response.text or "HTTP Status 404 – Not Found" in response.text :
            #     continue
            else:

                with open(filepath,"a",encoding='utf-8') as data:
                    new_line = f"True\nIP:{i.split()[0]}:{i.split()[1]}\n"
                    print (new_line)
                    data.write(new_line)




