import csv
import time
import random
import requests
from bs4 import BeautifulSoup

# --- CONFIGURATION ---
FILE_NAME = "inventory/dental_leads_premium.csv"
NICHE = "Dental Clinic"

class AlphaScoutEliteV2:
    def __init__(self):
        self.headers = ["Company Name", "Phone", "Website", "Decision Maker", "Intelligence_Score"]
        self.inventory = []

    def get_user_agent(self):
        agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_6 like Mac OS X) AppleWebKit/605.1.15",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36"
        ]
        return random.choice(agents)

    def deep_enrichment(self, url):
        """The 'Eyes' of the robot: Scans the site for high-value names."""
        if not url.startswith("http"):
            return "Invalid URL", 0
        
        try:
            headers = {'User-Agent': self.get_user_agent()}
            response = requests.get(url, headers=headers, timeout=5)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Keywords that increase lead value
            keywords = ["Doctor", "Dr.", "Owner", "Founder", "CEO", "Principal"]
            page_content = soup.get_text()
            
            found_titles = [word for word in keywords if word in page_content]
            
            if found_titles:
                return f"Verified: {found_titles[0]} spotted", 90
            return "No title found", 30
        except:
            return "Site Unreachable", 10

    def scrape_logic(self, target_count=10):
        print(f"--- Launching Deep Scraper V2: Targeting {NICHE} ---")
        
        for i in range(1, target_count + 1):
            print(f"[*] Processing Lead {i}/{target_count}...")
            
            # Simulated Data for the Demo (Replace with your scraper source)
            name = f"Global Dental Care {i}"
            site = f"https://example-dental-site-{i}.com" # Replace with real URLs
            
            # Launch Deep Enrichment
            print(f"    [>] Scanning website for Decision Makers...")
            decision_maker, score = self.deep_enrichment(site)
            
            lead = {
                "Company Name": name,
                "Phone": f"+1-800-SCAN-{i:02d}",
                "Website": site,
                "Decision Maker": decision_maker,
                "Intelligence_Score": f"{score}%"
            }
            
            self.inventory.append(lead)
            time.sleep(random.uniform(1, 2))

    def save_to_inventory(self):
        try:
            with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as file:
                writer = csv.DictWriter(file, fieldnames=self.headers)
                writer.writeheader()
                for data in self.inventory:
                    writer.writerow(data)
            print(f"\n[SUCCESS] {len(self.inventory)} Deep-Enriched leads saved to {FILE_NAME}")
        except Exception as e:
            print(f"[ERROR] Could not save: {e}")

if __name__ == "__main__":
    bot = AlphaScoutEliteV2()
    bot.scrape_logic(target_count=15)
    bot.save_to_inventory()
    print("[TARGET]: $1,000,000 | STATUS: Scaled Enrichment Active")
