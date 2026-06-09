import requests
from bs4 import BeautifulSoup
import json

# TODO: Task 1 - Fetch and Parse HTML
# Write a function to fetch a webpage and parse it with BeautifulSoup

def fetch_and_parse(url):
    """
    Fetches a web page and returns a BeautifulSoup object.
    
    Args:
        url (str): The URL to fetch
        
    Returns:
        BeautifulSoup: Parsed HTML content
    """
    pass


# TODO: Task 2 - Extract and Filter Data
# Write a function to extract specific data using CSS selectors

def extract_data(soup, selector):
    """
    Extracts data from the parsed HTML using a CSS selector.
    
    Args:
        soup (BeautifulSoup): Parsed HTML content
        selector (str): CSS selector to find elements
        
    Returns:
        list: List of extracted data
    """
    pass


# TODO: Task 3 - Transform and Save Data
# Write a function to save data to a file

def save_to_file(data, filename, file_format='json'):
    """
    Saves scraped data to a JSON or CSV file.
    
    Args:
        data (list): List of dictionaries containing scraped data
        filename (str): Output filename
        file_format (str): 'json' or 'csv'
    """
    pass


# Main execution
if __name__ == "__main__":
    # TODO: Replace with a real URL (e.g., a news site, project page, etc.)
    url = "https://example.com"
    
    # Fetch and parse
    # soup = fetch_and_parse(url)
    
    # Extract data
    # data = extract_data(soup, "a")  # Example: extract all links
    
    # Save data
    # save_to_file(data, "scraped_data.json")
    
    print("Web scraping assignment starter code. Follow the TODOs above!")
