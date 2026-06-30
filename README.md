# E-commerce Competitor Intelligence Scraper 🛒📊

## Overview
This project is an automated web scraper built in Python to extract competitor product data from e-commerce category pages. It pulls product names, pricing, and customer ratings, then cleans and structures the raw data into a Pandas DataFrame for market analysis. 

## Tech Stack
* **Language:** Python 3.13.11
* **Libraries:** `requests`, `BeautifulSoup4`, `pandas`

## Data Pipeline
1. **Extraction:** Navigates the target e-commerce sandbox (`books.toscrape.com`).
2. **Parsing:** Locates specific HTML nodes for `title`, `price_color`, and `star-rating`.
3. **Cleaning:** Strips currency symbols, converts price strings to floats, and maps text-based star ratings (e.g., "Three") to numerical integers.
4. **Storage:** Exports the structured DataFrame to `competitor_intelligence.csv`.

## Market Insights
* The scraped category reveals a highly competitive pricing landscape with an average product price of roughly £53.00, though top-rated (5-star) items command a slight premium. 
* Interestingly, there is a cluster of products priced slightly below the category average (around £50.00 to £51.00) that suffer from middling 1-to-3-star ratings. 
* This indicates a clear correlation between lower price points and lower perceived quality in this segment. 
* **Actionable Takeaway:** For a new market entrant, pricing a high-quality product right around the £52.00 mark presents a strong opportunity to undercut premium competitors while standing out against poorly rated mid-tier alternatives.

## How to Run
1. Clone the repository.
2. Install dependencies: 
   ```bash
   pip install requests beautifulsoup4 pandas