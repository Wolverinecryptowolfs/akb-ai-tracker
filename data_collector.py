import requests
from bs4 import BeautifulSoup
import json
import os

# Define the directory for saving raw data
RAW_DATA_DIR = "raw_data"
os.makedirs(RAW_DATA_DIR, exist_ok=True)

def scrape_arxiv_ai_papers(max_papers=5):
    """
    Scrapes the latest AI-related papers from the arXiv computer science section.
    Focuses on titles, abstracts, and links.
    """
    print("Starting to scrape arXiv for the latest AI papers...")
    url = "https://arxiv.org/list/cs.AI/new"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching arXiv page: {e}")
        return []

    soup = BeautifulSoup(response.content, 'html.parser')
    
    # ArXiv structure: dl tag contains all papers
    papers = []
    
    # Find all paper entries
    dt_tags = soup.find_all('dt')
    dd_tags = soup.find_all('dd')
    
    if not dt_tags or not dd_tags:
        print("Could not find paper entries on arXiv page.")
        return []

    # Iterate through the papers, assuming dt and dd tags are paired
    for dt, dd in zip(dt_tags, dd_tags):
        if len(papers) >= max_papers:
            break
            
        # Extract title
        title_tag = dd.find('div', class_='list-title')
        title = title_tag.text.replace('Title:', '').strip() if title_tag else "No Title Found"
        
        # Extract abstract link
        abs_link_tag = dt.find('a', title='Abstract')
        abs_link = "https://arxiv.org" + abs_link_tag['href'] if abs_link_tag else "No Link Found"
        
        # Extract abstract text (requires a second request, which we'll skip for now
        # to keep the initial scraping fast and simple, and rely on the LLM to process
        # the abstract page content in the next phase if needed, or just use the title/link)
        
        # For simplicity in this phase, we'll just use the title and link
        
        paper_data = {
            "source": "arXiv",
            "title": title,
            "url": abs_link,
            "raw_content": f"Title: {title}. Abstract URL: {abs_link}" # Placeholder for raw content
        }
        
        papers.append(paper_data)
        
    print(f"Successfully scraped {len(papers)} papers from arXiv.")
    return papers

def save_raw_data(data):
    """Saves the collected raw data to a JSON file."""
    file_path = os.path.join(RAW_DATA_DIR, "arxiv_raw_data.json")
    with open(file_path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
    print(f"Raw data saved to {file_path}")
    return file_path

def main():
    # We will only scrape arXiv for the initial version
    arxiv_papers = scrape_arxiv_ai_papers(max_papers=5)
    
    if arxiv_papers:
        save_raw_data(arxiv_papers)
    else:
        print("No data collected. Skipping save.")

if __name__ == "__main__":
    main()
