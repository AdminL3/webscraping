from urllib.parse import urlparse, parse_qs

url = "https://vw1136.a.searchspring.io/api/search/search.json?userId=f8e0a073-5c3a-4661-9501-05013c946554&domain=https%3A%2F%2Fwww.fishusa.com%2Fbaits-lures%2F%3Fview%3Dproducts%26p%3D2&sessionId=eed18409-51fd-4e7c-8317-c3ac78ebf467&pageLoadId=2fe832a4-90d3-4d45-8f1d-af29e003c88d&siteId=vw1136&page=1&bgfilter.custom_ss_hide=N&bgfilter.categories_hierarchy=Baits%20%26%20Lures&redirectResponse=full&ajaxCatalog=Snap&resultsFormat=native"
# url = input("Enter the URL to parse: ")

parsed_url = urlparse(url)
base_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"
params = {key: value[0] for key, value in parse_qs(parsed_url.query).items()}

output = f'base_url="{base_url}"\nparams={str(params).replace(", ", ",\n")}'
with open('Networking/url.txt', 'w') as file:
    file.write(output)
