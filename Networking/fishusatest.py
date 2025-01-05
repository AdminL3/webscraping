import requests
import time

base_url = "https://vw1136.a.searchspring.io/api/search/search.json"

for i in range(1, 51):
    params = {'userId': 'f8e0a073-5c3a-4661-9501-05013c946554',
              'domain': 'https://www.fishusa.com/baits-lures/?view=products&p=2',
              'sessionId': 'eed18409-51fd-4e7c-8317-c3ac78ebf467',
              'pageLoadId': '2fe832a4-90d3-4d45-8f1d-af29e003c88d',
              'siteId': 'vw1136',
              'page': i,
              'bgfilter.custom_ss_hide': 'N',
              'bgfilter.categories_hierarchy': 'Baits & Lures',
              'redirectResponse': 'full',
              'ajaxCatalog': 'Snap',
              'resultsFormat': 'native'
              }

    response = requests.get(base_url, params)
    data = response.json()

    results = data.get("results", [])
    print(f"Page {i} has {len(results)} results")
    with open(f'Networking/data/{i}.txt', 'w') as file:
        file.write(response.text)

        time.sleep(1)
