import pandas as pd
import logging

# Setup basic logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def clean_sales_data(df):
    """Cleans the CSV sales data with error handling."""
    if df is None or df.empty:
        logging.warning("Sales DataFrame is empty. Skipping transformation.")
        return None
    
    try:
        # 1. Remove exact duplicates
        initial_count = len(df)
        df = df.drop_duplicates()
        
        # 2. Handle Nulls
        # Fill missing quantity with 1, and price with the average price (or 0)
        df['quantity'] = df['quantity'].fillna(1)
        df['price'] = df['price'].fillna(0.0)
        
        # 3. Fix Data Types
        df['price'] = pd.to_numeric(df['price'], errors='coerce') # Converts errors to NaN
        df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
        
        # 4. Remove rows that couldn't be converted (critical for DB loading)
        df = df.dropna(subset=['timestamp'])
        
        logging.info(f"✅ Sales Cleaned: {initial_count - len(df)} duplicates/errors removed.")
        return df
    except Exception as e:
        logging.error(f"❌ Error in clean_sales_data: {e}")
        return None

def clean_user_data(df):
    """Cleans the API user data."""
    if df is None or df.empty:
        logging.warning("User DataFrame is empty.")
        return None
        
    try:
        # Select only the columns we need for the DB
        cleaned_df = df[['id', 'name', 'email']].copy()
        
        # Lowercase emails for consistency (Standard practice)
        cleaned_df['email'] = cleaned_df['email'].str.lower().str.strip()
        
        logging.info("✅ User data cleaned.")
        return cleaned_df
    except KeyError as e:
        logging.error(f"❌ Missing expected column in API data: {e}")
        return None