import requests
import time

def measure_load_time(url):
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    
    load_time = end_time - start_time 
    return load_time, response.status_code

sites = ['https://www.google.com', 'https://www.ynet.co.il', 'https://www.imdb.com', 'https://youtube.com/', 'https://github.com/', 'https://developers.institute/']

for site in sites:
    load_time, status_code = measure_load_time(site)
    print(f"Loading {site} took {load_time:.4f} seconds with status code {status_code}.")