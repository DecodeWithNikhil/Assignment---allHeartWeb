import requests
from bs4 import BeautifulSoup
import random
import pandas as pd
import traceback
import time

# Updated list of user-agents
user_agents = [
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:91.0) Gecko/20100101 Firefox/91.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:92.0) Gecko/20100101 Firefox/92.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.2 Safari/605.1.15',
]

def get_meta_data(soup):
    meta_title = soup.find('title').get_text() if soup.find('title') else ''
    meta_description = ''
    meta_desc_tag = soup.find('meta', attrs={'name': 'description'})
    if meta_desc_tag:
        meta_description = meta_desc_tag.get('content')
    return meta_title, meta_description

def get_social_media_links(soup):
    social_media = []
    links = soup.find_all('a', href=True)
    for link in links:
        href = link['href']
        if any(social in href for social in ['facebook.com', 'twitter.com', 'linkedin.com', 'instagram.com']):
            social_media.append(href)
    return ', '.join(social_media)

def identify_tech_stack(soup):
    scripts = soup.find_all('script')
    tech_stack = []
    for script in scripts:
        src = script.get('src', '')
        if 'jquery' in src:
            tech_stack.append('jQuery')
        elif 'react' in src:
            tech_stack.append('React')
        elif 'vue' in src:
            tech_stack.append('Vue.js')
    return ', '.join(set(tech_stack))

def get_payment_gateways(soup):
    gateways = []
    text = soup.get_text().lower()
    if 'paypal' in text:
        gateways.append('PayPal')
    if 'stripe' in text:
        gateways.append('Stripe')
    if 'razorpay' in text:
        gateways.append('Razorpay')
    return ', '.join(gateways)

def get_website_language(soup):
    html_tag = soup.find('html')
    return html_tag.get('lang', 'Unknown') if html_tag else 'Unknown'

def scrape_website(url, proxies=None):
    try:
        headers = {'User-Agent': random.choice(user_agents)}
        response = requests.get(url, headers=headers, proxies=proxies)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, 'html.parser')

        meta_title, meta_description = get_meta_data(soup)
        social_media_links = get_social_media_links(soup)
        tech_stack = identify_tech_stack(soup)
        payment_gateways = get_payment_gateways(soup)
        language = get_website_language(soup)
        
        return {
            'url': url,
            'meta_title': meta_title,
            'meta_description': meta_description,
            'social_media_links': social_media_links,
            'tech_stack': tech_stack,
            'payment_gateways': payment_gateways,
            'language': language
        }
    except Exception as e:
        print(f"Failed to scrape {url}: {e}")
        traceback.print_exc()
        return None

# Read URLs from Excel file
excel_file = 'excel_file.xlsx'
df = pd.read_excel(excel_file)

# Verify the column names in the DataFrame
print("Column names in the Excel file:", df.columns.tolist())

# Check if the 'url' column exists and rename it if necessary
if 'url' not in df.columns:
    # Attempt to handle common variations
    if 'URL' in df.columns:
        df.rename(columns={'URL': 'url'}, inplace=True)
    elif 'Url' in df.columns:
        df.rename(columns={'Url': 'url'}, inplace=True)
    else:
        raise KeyError("The Excel file does not contain a 'url' column. Please check the column names.")

# List to store scraped data
scraped_data_list = []

# Iterate over each URL in the DataFrame
for index, row in df.iterrows():
    url = row['url']
    print(f"Scraping {url}...")
    
    # Use a proxy (optional)
    # proxies = {
    #     'http': 'http://your.proxy.address:port',
    #     'https': 'https://your.proxy.address:port'
    # }
    
    scraped_data = scrape_website(url)
    
    if scraped_data:
        scraped_data_list.append(scraped_data)
    
    # Be polite and wait before making the next request
    time.sleep(random.uniform(1, 3))

# Convert the list to a DataFrame and save it to an Excel file
scraped_df = pd.DataFrame(scraped_data_list)
scraped_df.to_excel('scraped_data.xlsx', index=False)
print("Scraping completed and data saved to 'scraped_data.xlsx'")
