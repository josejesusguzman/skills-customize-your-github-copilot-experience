# 📘 Assignment: Web Scraping with BeautifulSoup

## 🎯 Objective

Learn to fetch and parse web pages using HTTP requests and BeautifulSoup to extract structured data, bridging your Python skills with real-world web data applications.

## 📝 Tasks

### 🛠️ Fetch and Parse HTML

#### Description
Write a program that fetches a web page using the `requests` library and parses its HTML structure using BeautifulSoup to explore DOM elements.

#### Requirements
Completed program should:

- Use the `requests` library to fetch the HTML content of a webpage.
- Parse the HTML using BeautifulSoup.
- Identify and print the page title (`<title>` tag).
- Find and display all headings (`<h1>`, `<h2>`) from the page.
- Handle potential errors (e.g., connection failures).

### 🛠️ Extract and Filter Data

#### Description
Extract specific data from a webpage by using CSS selectors and BeautifulSoup methods to locate and filter elements based on criteria.

#### Requirements
Completed program should:

- Use CSS selectors or tag/class attributes to target specific elements.
- Extract data from multiple elements (e.g., all links, all paragraphs, specific classes).
- Store extracted data in a list or dictionary.
- Display the data in a readable format (e.g., printed list or CSV-like output).
- Example: Extract all article headlines and their links from a news site.

### 🛠️ Transform and Save Scraped Data

#### Description
Process and save the scraped data into a structured format (JSON or CSV) for further analysis or storage.

#### Requirements
Completed program should:

- Transform scraped data into a structured format (list of dictionaries).
- Write the data to a JSON or CSV file.
- Include error handling for file operations.
- Clean and normalize the data (e.g., strip whitespace, remove duplicates).
- Example output: A JSON file with headline objects containing title, link, and date.
