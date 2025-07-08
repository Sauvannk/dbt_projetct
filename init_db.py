import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database

# Paramètres de connexion.
username = "root"
password = "Yfd6d84c*Sql!"  # <-- à adapter si besoin
host = "localhost"
port = 3306
database = "my_dbt_db"

# Connexion à la base de données
DATABASE_URI = f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}'
engine = create_engine(DATABASE_URI)

# Créer la BDD si elle n'existe pas
if not database_exists(engine.url):
    create_database(engine.url)

liste_tables = ["customers", "items", "orders", "products", "stores", "supplies"]

for table in liste_tables:
    csv_url = f"https://raw.githubusercontent.com/dsteddy/jaffle_shop_data/main/raw_{table}.csv"
    df = pd.read_csv(csv_url)
    df.to_sql(table, con=engine, if_exists="replace", index=False)
