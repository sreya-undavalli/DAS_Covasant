import asyncio
import aiohttp
from bs4 import BeautifulSoup
from urllib.parse import urlparse,urljoin,urldefrag
async def fetch(session, url):
    try:
        async with session.get(url) as response:
            response.raise_for_status()
            return await response.text()
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return None

async def download_page(session,url):
    html = await fetch (session,url)
    if html:
        print(f"Downloaded : {url}")
        return url ,html
    return url,None
    
def extract_links(base_url,html): 
    soup = BeautifulSoup(html, 'html.parser')
    links = set()
    for a_tag in soup.find_all('a', href=True):
        link = urljoin(base_url,a_tag['href'])
        if urlparse(link).scheme in['http','https']:
            links.add(link)
    return list(links)
       
async def main(start_url):
    async with aiohttp.ClientSession() as session:
        url,html = await download_page(session,start_url)
        if html:
            links = extract_links(url,html)
            print(f"Found {len(links)} links.")
            tasks = [download_page(session,link) for link in links]
            results = await asyncio.gather(*tasks)
            for link,content in results:
                if content:
                    print(f"Successfully Downloaded:{link}")
                else:
                    print(f"Failed to Download:{link}")

if __name__ == "__main__":
    start_url = "https://www.w3schools.com/"
    print(start_url)
    asyncio.run(main(start_url))