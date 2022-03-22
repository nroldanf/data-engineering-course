import pandas as pd
from sqlalchemy import create_engine
from utils import (
    get_file_name
)

def main():
    year : int = 2020
    month : int = 12
    table = "rawdata"
    path_csv = "datalake/csv/"
    file_name_zip = get_file_name(year, month)
    file_name_csv = file_name_zip.split(".")[0] + ".csv"

    db_url = "postgresql://root:root@my_host:54321/bikes"
    engine = create_engine(db_url)

    # Load data
    df = pd.read_csv(f"../{path_csv}{file_name_csv}")
    
    # TODO: Evaluate data quality
    
    # Insert data into database
    df.to_sql(table, engine, if_exists="append")

if __name__ == '__main__':
    main()

