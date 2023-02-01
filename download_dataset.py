import requests

url = 'https://opendata.arcgis.com/api/v3/datasets/4dabb4afab874804ba121536efaaacb4_0/downloads/data?format=csv&spatialRefId=4326&where=1=1'
path = 'data/ca_covid.csv'
with open(path, 'wb') as f, requests.get(url, stream=True) as r:
    for line in r.iter_lines():
        f.write(line+'\n'.encode())
