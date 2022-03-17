import os
import logging
from utils import (
    get_file_name,
    create_directory,
    unzip_file
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def main():
    year : int = 2020
    month : int = 12
    path_zip = "datalake/zip/"
    path_csv = "datalake/csv/"

    create_directory(path_csv)

    file_name_zip = get_file_name(year, month)
    file_name_csv = file_name_zip.split(".")[0] + ".csv"
    downloaded_csv_files = os.listdir(path_csv)
    # Check if exists
    if file_name_csv in downloaded_csv_files:
        print("File already exists. Skipping file unzipping...")
        exit(1)
    
    path_zip = f"{path_zip}/{file_name_zip}"
    unzip_file(path_csv, path_zip, file_name_csv)
    
    
if __name__ == '__main__':
    main()