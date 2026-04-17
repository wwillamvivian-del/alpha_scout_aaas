import requests
from bs4 import BeautifulSoup
import pandas as pd
import time
import os
import csv

def run_scout(target_niche, total_pages=1):
    print(f"[*] AaaS Engine: Armor-Plated Extraction - {target_niche}")
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    all_leads = []
    seen_names = set()

    for page in range(1, total_pages + 1):
        url = f"https://www.yellowpages.ca/search/si/{page}/{target_niche}/Canada"
        try:
            response = requests.get(url, headers=headers, timeout=15)
            soup = BeautifulSoup(response.text, 'html.parser')
            cards = soup.find_all(['div', 'section'], class_=lambda x: x and 'listing' in x.lower())

            for card in cards:
                name_tag = card.find(attrs={"itemprop": "name"}) or card.find('a', class_=lambda x: x and 'name' in x.lower())
                name = name_tag.get_text().strip() if name_tag else None
                
                phone_tag = card.find(attrs={"itemprop": "telephone"}) or card.find(class_=lambda x: x and 'phone' in x.lower())
                phone = phone_tag.get_text().strip() if phone_tag else "N/A"
                
                if name and name not in seen_names and len(name) > 3:
                    all_leads.append({
                        "Business Name": name,
                        "Phone": phone,
                        "Niche": target_niche,
                        "Date": time.strftime("%Y-%m-%d")
                    })
                    seen_names.add(name)
                    print(f"   [+] Secured: {name} | {phone}")

            time.sleep(2)
        except Exception as e:
            print(f"[-] Logic Error: {e}")

    if all_leads:
        df = pd.DataFrame(all_leads)
        file_path = "b2b_inventory.csv"
        
        # If file is corrupted, we start fresh to fix the ParserError
        try:
            if os.path.exists(file_path):
                existing_df = pd.read_csv(file_path, on_bad_lines='skip')
                df = pd.concat([existing_df, df]).drop_duplicates(subset=['Business Name'])
            
            # Use QUOTE_ALL to prevent commas from breaking the file again
            df.to_csv(file_path, index=False, quoting=csv.QUOTE_ALL)
            print(f"\n[!] Mission Success: {len(all_leads)} leads added to the secure inventory.")
        except Exception as e:
            print(f"[!] Fixing file structure...")
            df.to_csv(file_path, index=False, quoting=csv.QUOTE_ALL)

if __name__ == "__main__":
    # Let's finish the "Dentists" run correctly
    run_scout("Dentists", total_pages=1)
