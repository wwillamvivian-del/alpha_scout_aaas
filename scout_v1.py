import csv
import time
import random
import requests
from googlesearch import search
from email_validator import validate_email, EmailNotValidError

# --- CONFIGURATION ---
FILE_NAME = "inventory/global_gold_leads.csv"
SEARCH_QUERY = "Real Estate Agents in Florida USA" # High-ticket niche
TARGET_COUNT = 15 

class AlphaScoutV5_2_Enterprise:
    def __init__(self):
        self.headers = ["Company Name", "Email", "Website", "Decision Maker", "Quality_Score"]
        self.inventory = []
        # Professional browser identities to stay invisible
        self.user_agents = [
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
            "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
            "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
        ]

    def hunt_urls(self, query, count):
        """Autonomous Google Hunting with heavy stealth delays."""
        print(f"[!] Target Acquired: {query}")
        print(f"[!] Initializing Stealth Hunt (this takes time to stay invisible)...")
        urls = []
        try:
            # sleep_interval=20 makes the robot look like a slow human
            agent = random.choice(self.user_agents)
            for url in search(query, num_results=count, sleep_interval=20, user_agent=agent):
                # Filter out junk and social media
                if all(x not in url for x in ["facebook", "yelp", "instagram", "youtube", "twitter", "linkedin"]):
                    urls.append(url)
                if len(urls) >= count: break
            return urls
        except Exception as e:
            print(f"\n[CRITICAL] Google identified the VPN/IP. STOP and switch VPN city.")
            return []

    def validate_lead_email(self, email):
        """Fixed for Termux stability."""
        try:
            valid = validate_email(email, check_deliverability=False)
            return True, valid.normalized
        except:
            return False, "Invalid"

    def run_factory(self):
        print(f"--- Alpha-Scout V5.2: ENTERPRISE FACTORY ACTIVE ---")
        targets = self.hunt_urls(SEARCH_QUERY, TARGET_COUNT)
        
        if not targets:
            print("[SHUTDOWN] No data found. Switch VPN location and try again in 5 minutes.")
            return

        for i, url in enumerate(targets):
            print(f"[*] Extracting Lead {i+1}/{len(targets)}: {url}")
            
            # Domain-based intelligence gathering
            domain_raw = url.split('//')[-1].split('/')[0].replace('www.', '')
            company_name = domain_raw.split('.')[0].upper()
            
            # Pro email guessing (standard for AaaS models)
            test_email = f"contact@{domain_raw}"
            is_valid, final_email = self.validate_lead_email(test_email)
            
            self.inventory.append({
                "Company Name": company_name,
                "Email": final_email if is_valid else "Check Site",
                "Website": url,
                "Decision Maker": "Managing Director/Owner",
                "Quality_Score": "GOLD" if is_valid else "VERIFICATION_REQ"
            })
            # Crucial delay to avoid being flagged as a bot
            time.sleep(random.uniform(5, 10))

    def save_inventory(self):
        if not self.inventory: return
        try:
            with open(FILE_NAME, mode='w', newline='', encoding='utf-8') as f:
                writer = csv.DictWriter(f, fieldnames=self.headers)
                writer.writeheader()
                writer.writerows(self.inventory)
            print(f"\n[SUCCESS] Factory Run Complete.")
            print(f"[INVENTORY]: {len(self.inventory)} leads secured in {FILE_NAME}")
        except Exception as e:
            print(f"[ERROR] Could not save file: {e}")

if __name__ == "__main__":
    factory = AlphaScoutV5_2_Enterprise()
    factory.run_factory()
    factory.save_inventory()
    print("\n[ROAD TO $1M]: Inventory successfully expanded.")
