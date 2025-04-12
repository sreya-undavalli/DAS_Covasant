import requests
from bs4 import BeautifulSoup
from concurrent.futures import ThreadPoolExecutor
 
def download_page(url):
    try:
        response = requests.get(url)
        print(f"Downloaded:{url}")
        return response
    except requests.RequestException as e:
        print(f"Failed to Download {url}: {e}")
        return None
        
def extract_links(response):
    if not response:
        return []
    soup = BeautifulSoup(response.text,"html.parser")
    links=[]
    for tag in soup.find_all("a", href=True):
        href = tag["href"]
        if href.startswith("http"):
            links.append(href)
    return links
def download_all(url):
    current_url =[url]
    with ThreadPoolExecutor(max_workers=5) as executor:
        results = list(executor.map(download_page,current_url))
        for res in results:
            if res:
                links = extract_links(res)
                print("Extracted Links:")
                for link in links:
                    print("-",link)
                    
                    
if __name__=='__main__':
    url ="https://theuselessweb.com/"
    download_all(url)