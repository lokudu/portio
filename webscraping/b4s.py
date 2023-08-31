import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse


class WebScraper:
    def __init__(self, url):
        self.url = url
        self.domain = urlparse(url).netloc
        self.robots_url = f"https://{self.domain}/robots.txt"
        try:
            self.robots = requests.get(self.robots_url)
            if self.robots.status_code == 200:
                print(self.robots.text)
            else:
                print(f"robots.txt not found for {self.domain}")
        except:
            print(f"{self.url} is invalid")
        self.html_content = self.fetch_webpage()
        self.parsed_html = self.parse_html()
    
    def fetch_webpage(self):
        try:
            response = requests.get(self.url)
            response.raise_for_status()
            return response.text
        except requests.exceptions.RequestException as e:
            print(f"Error: {e}")
            return None
    
    def parse_html(self):
        try:
            soup = BeautifulSoup(self.html_content, 'html.parser')
            return soup
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def extract_data(self, selectors):
        try:
            extracted_data = {}
            for selector in selectors:
                elements = self.parsed_html.select(selector)
                extracted_data[selector] = [element.text.strip() for element in elements]
            return extracted_data
        except Exception as e:
            print(f"Error: {e}")
            return None

scraper = WebScraper("https://example.com")
selectors = ["h1", "p"]
data = scraper.extract_data(selectors)