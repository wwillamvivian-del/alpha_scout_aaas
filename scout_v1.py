import csv
import time
import random
import requests
from bs4 import BeautifulSoup

# --- CONFIGURATION ---
FILE_NAME = "inventory/dental_leads_premium.csv"
# Add your proxy list here (Format: "http://user:pass@host:port")
PROXIES = [
    None, # Start with your local IP
    # "http://proxy1_address:port",
    # "http://proxy2_address:port",
]

class AlphaScoutV3_Armor:
    def __init__(self):
        self.headers = ["Company Name", "Phone", "Website", "Decision Maker", "Intelligence_Score"]
        self.inventory = []

    def get_proxy(self):
        """Picks a random proxy from your list to stay invisible."""
        p = random.choice(PROXIES)
        return {"http": p, "https": p} if p else None

    def deep_enrichment(self, url):
        """Scans sites for Doctors/Owners using rotated IPs."""
        try:
            proxy = self.get_proxy()
            headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
            
            # Visiting the site through the proxy 'armor'
            response = requests.get(url, headers=headers, proxies=proxy, timeout=7)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            keywords = ["Doctor", "Dr.", "Owner", "Founder", "CEO"]
            page_content = soup.get_text()
            
            found = [w for w in keywords if w in page_content]
            return (f"Verified: {found[0]}", 95) if found else ("No title", 35)
        except:
            return "Site Protected/Unreachable", 15

    def scrape_logic(self, target_count=50): # Scaling up to 50
        print(f"--- Launching Alpha-Scout V3: GLOBAL SCALE ACTIVE ---")
        for i in range(1, target_count + 1):
            name = f"Premium Practice {i}"
            site = f"https://dental-example-{i}.com"
            
            print(f"[*] Lead {i}: Scaling through Proxy...")
            decision_maker, score = self.deep_enrichment(site)
            
            self.inventory.append({
                "Company Name": name, "Phone": f"+1-555-SCAL-{i}",
                "Website": site, "Decision Maker": decision_maker,
                "Intelligence_Score": f"{score}%"
            })
            time.sleep(random.uniform(0.5, 1.5)) # Faster speed with proxies

    def save(self):
        with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as f:
            writer = csv.DictWriter(f, fieldnames=self.headers)
            writer.writeheader()
            writer.writerows(self.inventory)
        print(f"[SUCCESS] Scale-ready data saved to {FILE_NAME}")

if __name__ == "__main__":
    bot = AlphaScoutV3_Armor()
    bot.scrape_logic(target_count=50) 
    bot.save()
    print("\n[GOAL]: $1M | STATUS: Proxy Armor Deployed")
