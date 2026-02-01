import pandas as pd
import requests

def extract_from_csv(file_path):
    """Reads data from a local CSV file."""
    try:
        df = pd.read_csv(file_path)
        print(f"✅ CSV Extracted: {len(df)} rows found.")
        return df
    except Exception as e:
        print(f"❌ Error reading CSV: {e}")
        return None

def extract_from_api(url):
    """Fetches data from a public JSON API."""
    try:
        response = requests.get(url)
        response.raise_for_status() # Check for errors
        data = response.json()
        df = pd.DataFrame(data)
        print(f"✅ API Extracted: {len(df)} rows found.")
        return df
    except Exception as e:
        print(f"❌ Error fetching API: {e}")
        return None

if __name__ == "__main__":
    # 1. Test CSV Extraction
    csv_df = extract_from_csv("data/sample_data.csv")
    
    # 2. Test API Extraction (Using a free test API)
    api_url = "https://jsonplaceholder.typicode.com/users"
    api_df = extract_from_api(api_url)
    
    # Show the results
    if api_df is not None:
        print("\n--- Preview of API Data ---")
        print(api_df[['id', 'name', 'email']].head())