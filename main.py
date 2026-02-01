from src.extract import extract_from_csv, extract_from_api
from src.transform import clean_sales_data, clean_user_data
from src.load import load_to_postgres  # <--- Add this!

def run_pipeline():
    print("🚀 Starting ETL Pipeline...")
    
    # 1. EXTRACT
    raw_sales = extract_from_csv("data/sample_data.csv")
    raw_users = extract_from_api("https://jsonplaceholder.typicode.com/users")
    
    # 2. TRANSFORM
    print("🧹 Cleaning data...")
    clean_sales = clean_sales_data(raw_sales)
    clean_users = clean_user_data(raw_users)
    
    # 3. LOAD
    print("📥 Loading to Database...")
    if clean_sales is not None:
        load_to_postgres(clean_sales, 'fact_sales')
    if clean_users is not None:
        load_to_postgres(clean_users, 'dim_users')

if __name__ == "__main__":
    run_pipeline()