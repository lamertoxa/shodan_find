import shodan
from shodan import APIError
import asyncio
async def find_api(api_code):
    SHODAN_API_KEY = api_code

    api = shodan.Shodan(SHODAN_API_KEY)

    try:
        # Search Shodan
        results = api.search('country:ua')

        # Show the results
        print(f'api:{api_code}\nResults found: {results["total"]}')
        for result in results['matches']:
            print('IP: {}'.format(result['ip_str']))
            print(result['data'])
            print('')
    except APIError as e:
        print(f'Error: {e}.api:{api_code}')

async def main():
    with open("wow.txt") as rows:
        list_rows=rows.read().split("\n")
    list_tasks = []
    for i in list_rows:
        new_task=asyncio.create_task(find_api(i))
        list_tasks.append(new_task)
    await asyncio.gather(*list_tasks)

asyncio.run(main())