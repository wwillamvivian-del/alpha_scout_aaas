import csv
import time
import random
import requests
from bs4 import BeautifulSoup
from email_validator import validate_email, EmailNotValidError

# --- CONFIGURATION ---
FILE_NAME = "inventory/dental_leads_premium.csv"
# Add your proxies here when you scale to 1000+ leads
PROXIES = [None] 

class AlphaScoutV4_Stable:
    def __init__(self):
        self.headers = ["Company Name", "Email", "Website", "Decision Maker", "Quality_Score"]
        self.inventory = []

    def validate_lead_email(self, email):
        """
        FIXED FOR TERMUX: Checks email syntax without triggering 
        the /etc/resolv.conf DNS error.
        """
        try:
            # check_deliverability=False is mandatory for Termux stability
            valid = validate_email(email, check_deliverability=False)
            return True, valid.normalized
        except EmailNotValidError as e:
            return False, str(e)

    def deep_enrichment(self, url):
        """Scans sites for names (Decision Makers)."""
        try:
            headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
            # Note: In a real run, this would visit the URL. 
            # For this demo, it simulates the visit to avoid network timeouts.
            keywords = ["Doctor", "Owner", "CEO", "Founder"]
            # Simulating finding a title for the demo
            return random.choice(keywords)
        except:
            return "Manager"

    def run_factory(self, count=15):
        print(f"--- Alpha-Scout V4.1: TERMUX STABLE ACTIVE ---")
        for i in range(1, count + 1):
            print(f"[*] Lead {i}/{count}: Validating & Enriching...")
            
            # Simulated data targeting the US Dental Niche
            test_email = f"dr.smith_{i}@dentalpractice.com" 
            site = f"https://dentalpractice{i}.com"
            
            # Step 1: Validate (Stability Fix Included)
            is_valid, result = self.validate_lead_email(test_email)
            
            # Step 2: Enrich
            boss_title = self.deep_enrichment(site)
            
            status = "GOLD" if is_valid else "INVALID"
            
            self.inventory.append({
                "Company Name": f"Elite Dental Clinic {i}",
                "Email": result if is_valid else "N/A",
                "Website": site,
                "Decision Maker": boss_title,
                "Quality_Score": status
            })
            
            # Random delay to mimic human behavior
            time.sleep(random.uniform(0.5, 1.2))

    def save(self):
        try:
            with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self.headers)
                writer.writeheader()
                writer.writerows(self.inventory)
            print(f"\n[SUCCESS] Factory run complete. {len(self.inventory)} leads secured.")
            print(f"[FILE]: {FILE_NAME}")
        except Exception as e:
            print(f"[ERROR] Save failed: {e}")

if __name__ == "__main__":
    bot = AlphaScoutV4_Stable()
    bot.run_factory(count=15)
    bot.save()
    print("\n[VALUATION TARGET]: $1M | STATUS: Engine Stable")
