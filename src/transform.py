import pandas as pd

def clean_sales_data(df):
    """Cleans the CSV sales data."""
    if df is None:
        return None
    
    # 1. Remove exact duplicates
    df = df.drop_duplicates()
    
    # 2. Fill missing values (Nulls)
    # Let's assume if quantity is null, it was at least 1
    df['quantity'] = df['quantity'].fillna(1)
    
    # 3. Convert types
    df['price'] = df['price'].astype(float)
    df['timestamp'] = pd.to_datetime(df['timestamp'])
    
    print(f"✅ Transformation complete. Remaining rows: {len(df)}")
    return df

def clean_user_data(df):
    """Cleans the API user data."""
    # Example: Just keep relevant columns
    if df is None:
        return None
    
    cleaned_df = df[['id', 'name', 'email']].copy()
    return cleaned_df