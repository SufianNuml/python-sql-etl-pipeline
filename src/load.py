import pandas as pd
from sqlalchemy import create_engine
import logging

# Setup logging to track progress
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_to_postgres(df, table_name):
    """Loads a Pandas DataFrame into a PostgreSQL table."""
    # Safety Check: Don't try to load if there is no data
    if df is None or df.empty:
        logging.warning(f"⚠️ No data provided for table: {table_name}. Skipping load.")
        return

    try:
        # Connection string using your credentials
        # Format: postgresql://username:password@localhost:5432/database_name
        engine = create_engine('postgresql://postgres:1235@localhost:5432/etl_project')
        
        # Load data
        # 'replace' drops the table and recreates it. 
        # Use 'append' later if you want to keep old data!
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        
        logging.info(f"✅ Successfully loaded {len(df)} rows into table: {table_name}")
        
    except Exception as e:
        logging.error(f"❌ Error loading to Postgres: {e}")

if __name__ == "__main__":
    print("Load module ready for imports.")