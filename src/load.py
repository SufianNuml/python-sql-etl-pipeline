import psycopg2
from sqlalchemy import create_engine

def load_to_postgres(df, table_name):
    """Loads a Pandas DataFrame into a PostgreSQL table."""
    try:
        # Format: postgresql://username:password@localhost:5432/database_name
        # UPDATE 'password' with your real PostgreSQL password!
        engine = create_engine('postgresql://postgres:1235@localhost:5432/etl_project')
        
        df.to_sql(table_name, engine, if_exists='replace', index=False)
        print(f"✅ Successfully loaded data into table: {table_name}")
    except Exception as e:
        print(f"❌ Error loading to Postgres: {e}")