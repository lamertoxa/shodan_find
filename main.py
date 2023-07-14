import logging
import os
import time
import shodan
from shodan import APIError
import math
import os

SHODAN_KEY = os.getenv("SHODAN_KEY")
print (SHODAN_KEY)
SHODAN_API = SHODAN_KEY


def find_api():
    SHODAN_API_KEY = SHODAN_API
    api = shodan.Shodan(SHODAN_API_KEY)
    request = '195.114.6.34' # "200 OK" http.title:"phpMyAdmin" country:ru
    try:
        # Search Shodan
        results = api.search(request)
        total_results = results["total"]
        pages = math.ceil(total_results / 100) # Retrieve at most 10 pages, or 1000 results
        logging.warning(f"{pages}")
        logging.warning(f"{results}")
        from_page = 0
        print(f'Results found: {total_results}')

        # Use the current time as the file name
        filename = time.strftime("%Y%m%d-%H%M%S.txt")
        filepath = os.path.join("FindShodan", filename)

        with open(filepath, "a",encoding='utf-8') as data:
            # Iterate through the pages
            for page in range(from_page, pages + 1):
                page_results = api.search(request, page=page)
                for result in page_results['matches']:
                    data.write(f'IP: {result["ip_str"]} Port:{result["port"]} HostName:{result["hostnames"]}\n')
                    if "Dahua" in result['data'] or "Hikvision" in result['data']:
                        pass
                    else:
                        # print (f'IP: {result["ip_str"]} Port:{result["port"]} HostName:{result["hostnames"]}\n')
                        # print (result['data'] + '\n')
                        data.write(result['data'] + '\n')
    except APIError as e:
        print(f'Error: {e}')

find_api()