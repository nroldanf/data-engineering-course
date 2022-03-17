"""
- Build corresponding environments:
    - Pull image for postgres and create the db
    - Create image for Python
- Run the script for ingestion downloading (lake):
    - Look for the file that corresponds to the specific date in the list.
    - Download the specific file
- Run the script for unzipping
    - unzip the file
    - Extract the csv of interest (according to the date)
- Run the script for data quality
    - Load the csv into memory and check for problems with data (e.g. null values). This could be with pandas.
- Run the script for loading the data into the warehouse
    - Load csv to postgres db using sqlaclhemy
- Check with Falcon and get visualizations over the data
    - Run a sql query that allows to visualize the question
"""
import os
import logging
from utils import (
    create_directory,
    get_file_name, 
    get_all_urls,
    download_file
)

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

def main():
    year : int = 2020
    month : int = 12
    path_zip = "datalake/zip/"
    html_path = "tripdata.html"
    
    create_directory(path_zip)
    
    file_name = get_file_name(year, month)
    downloaded_zip_files = os.listdir(path_zip)
    # Check if exists
    if file_name in downloaded_zip_files:
        print("File already exists. Skipping file downloading...")
        exit(0)
    
    urls = get_all_urls(html_path)
    # TODO: Remove JC zip files or the others
    for i in urls:
        if i.endswith(file_name):
            url = i
            break
    download_file(path_zip, url)
    
    
if __name__ == '__main__':
    main()