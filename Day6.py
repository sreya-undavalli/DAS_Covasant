import asyncio
import aiohttp
from bs4 import BeautifulSoup

async def fetch(session, url):
    try:
        async with session.get(url) as response:
            return await response.text()
    except Exception as e:
        print(f"Failed to fetch {url}: {e}")
        return None

async def download_all_links(url):
    async with aiohttp.ClientSession() as session:
        print(f"Fetching {url}...")
        html_content = await fetch(session, url)
        if html_content is None:
            return
        
        soup = BeautifulSoup(html_content, 'html.parser')
        links = [a.get('href') for a in soup.find_all('a', href=True)]
        print(f"Found {len(links)} links.")

        tasks = []
        for link in links:
            if link.startswith('http'):  # Ensure the link is absolute
                tasks.append(fetch(session, link))

        # Fetch all links concurrently
        contents = await asyncio.gather(*tasks)
        print("Downloaded contents of all links.")
        return contents

if __name__ == "__main__":
    url = "https://www.ajio.com/?utm_source=cuelinks&utm_medium=affiliate&utm_campaign=cuelinks_9485&utm_term=20250415clt8yz8zou8m&clickid=67fde2c6ae687b0001bee47d&pid=19&offer_id=2&attribution_window=1D&return_cancellation_window=45D"  # Replace with the URL you want to process
    asyncio.run(download_all_links(url))