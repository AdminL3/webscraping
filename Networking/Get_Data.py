import requests

base_url = "https://vw1136.a.searchspring.io/api/search/search.json"
params = {'userId': 'f8e0a073-5c3a-4661-9501-05013c946554',
          'domain': 'https://www.fishusa.com/baits-lures/?view=products&p=2',
          'sessionId': 'eed18409-51fd-4e7c-8317-c3ac78ebf467',
          'pageLoadId': '2fe832a4-90d3-4d45-8f1d-af29e003c88d',
          'siteId': 'vw1136',
          'page': '1',
          'bgfilter.custom_ss_hide': 'N',
          'bgfilter.categories_hierarchy': 'Baits & Lures',
          'redirectResponse': 'full',
          'ajaxCatalog': 'Snap',
          'resultsFormat': 'native'
          }


response = requests.get(base_url, params)
data = response.json()

results = data.get("results", [])


with open(f'Networking/data/{params["page"]}.txt', 'w') as file:
    file.write(response.text)
