import logging
import os
import time
import asyncio
import aiofiles
import aiohttp
from aiohttp import BasicAuth,ClientTimeout
from aiohttp.client_exceptions import ClientResponseError,ClientConnectionError,ClientConnectorSSLError,ClientSSLError,ServerTimeoutError



async def check_ip(ip,filepath):

    timeout = ClientTimeout(20)
    async with sem:
        try:
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(f"http://{ip.split()[0]}:{ip.split()[1]}", ssl=False) as resp:
                    first_response = resp.headers
                if first_response.get('WWW-Authenticate') == None:
                    pass
                async with session.get(f"http://{ip.split()[0]}:{ip.split()[1]}", auth=BasicAuth('admin', 'admin'),ssl=False) as resp:
                    text_response = await resp.read()
                    status =  resp.status
                try:
                    text_response = text_response.decode('utf-8')
                except UnicodeDecodeError:
                    logging.warning(f"CHEEEK")
                    text_response = text_response.decode('utf-8', errors='replace')
                    status = resp.status


        except ClientResponseError as e:
            logging.warning(f"1 {ip}")
            print(e)
        except ClientConnectionError as e:
            logging.warning(f"2 {ip}")
            print(e)
        except  ClientConnectorSSLError as e:
            logging.warning(f"3 {ip}")
            print(e)
        except  ClientSSLError as e:
            logging.warning(f"4 {ip}")
            print(e)
        except  asyncio.TimeoutError as e:
            logging.warning(f"5 {ip}")
            print(e)
        else:

            if status != 200:
                pass
            elif "input" in text_response:
                pass
            else:
                async with aiofiles.open(filepath, "a", encoding='utf-8') as data:
                    new_line = f"True\nIP:{ip.split()[0]}:{ip.split()[1]}\n"
                    print(new_line)
                    await data.write(new_line)


async def main():
    async with aiofiles.open(file="FindShodan/parsed/tplink2.txt") as data:
        content=await data.read()

    filename = time.strftime("%Y%m%d-%H%M%S.txt")
    filepath = os.path.join("ipchecked", filename)
    find_ips = [check_ip(i,filepath) for i in content.split("\n")]
    await asyncio.gather(*find_ips)

sem = asyncio.Semaphore(20)

asyncio.run(main())







