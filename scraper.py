import requests
from bs4 import BeautifulSoup
import pandas as pd

def scrape_category():
    url = "https://books.toscrape.com/"
    response = requests.get(url)
    
    # FIX 1: Force Python to read the page using UTF-8 encoding
    response.encoding = "utf-8" 
    
    soup = BeautifulSoup(response.text, "html.parser")
    products = soup.select("article.product_pod")
    rating_map = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
    scraped_data = []

    for item in products:
        name = item.select_one("h3 a")["title"]
        raw_price = item.select_one("p.price_color").text
        
        # FIX 2: Keep ONLY digits and periods, ignoring all currency symbols/ghost characters
        clean_price_str = "".join(char for char in raw_price if char.isdigit() or char == ".")
        clean_price = float(clean_price_str)
        
        rating_text = item.select_one("p.star-rating")["class"][1]
        numeric_rating = rating_map.get(rating_text, 0)
        
        scraped_data.append({
            "Product Name": name,
            "Price": clean_price,
            "Rating": numeric_rating
        })
        
    return scraped_data

if __name__ == "__main__":
    data = scrape_category()
    df = pd.DataFrame(data)
    df.to_csv("competitor_intelligence.csv", index=False)
    print("Scraping complete! Saved to competitor_intelligence.csv")