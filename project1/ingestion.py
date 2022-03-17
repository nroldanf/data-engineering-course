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
from zipfile import ZipFile
from bs4 import BeautifulSoup
import requests

base_path_zip = "files"
base_path_csv = "csv"
downloaded_files = os.listdir(base_path_zip)

urls = []
with open("tripdata.html", "r") as f:
    contents = f.read()
    soup = BeautifulSoup(contents, "html5lib")
    table = soup.find("tbody", attrs={"id":"tbody-content"})
    for row in table.findAll("tr"):
        urls.append(row.find("a")["href"])
# Filter to zip files
urls = [i for i in urls if i.endswith("zip")]
# Download files in files directory
for url in urls[0:5]:
    name = url.split("/")[-1]
    print(name)
    if name not in downloaded_files:
        r = requests.get(url)
        file_path = f"{base_path_zip}/{name}"
        with open(file_path, "wb") as f:
            f.write(r.content)
# Unzip files
for url in urls[0:5]:
    name = url.split("/")[-1]
    file_path = f"{base_path_zip}/{name}"
    with ZipFile(file_path, 'r') as zip:
        print(f'Extracting {file_path}...')
        csv_name = name.split(".")[0]
        zip.extractall(f"{base_path_csv}/{csv_name}")
        print('Done!')
