import os
import logging
from typing import List
from zipfile import ZipFile
from bs4 import BeautifulSoup
import requests

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

def create_directory(path):
    try:
        os.makedirs(path, exist_ok=True)
        print("Directory created successfully")
    except OSError as error:
        print("Directory can not be created")

def get_file_name(year: int, month: int) -> str:
    if year > 2016:
        file_name = f"{year}{month}-citibike-tripdata.csv.zip"
    else:
        file_name = f"{year}{month}-citibike-tripdata.zip"
    return file_name

def get_all_urls(html_path: str) -> List[str]:
    """
    Get all URLs from dataset.
    
    :param path: Path where the HTML document is.
    :return: List of URLs
    """
    urls = []
    with open(html_path, "r") as f:
        contents = f.read()
        soup = BeautifulSoup(contents, "html5lib")
        table = soup.find("tbody", attrs={"id":"tbody-content"})
        for row in table.findAll("tr"):
            urls.append(row.find("a")["href"])
    # Filter to zip files
    urls = [i for i in urls if i.endswith("zip")]    
    return urls

def download_file(base_zip_path: str, url: str):
    """
    Downloads a zip file given an URL.
    """
    r = requests.get(url)
    name = url.split("/")[-1]
    file_path = f"{base_zip_path}/{name}"
    logger.debug("Downloading file...")
    with open(file_path, "wb") as f:
        f.write(r.content)
    logger.debug("File downloaded successfully!")
    
def unzip_file(destination_path: str, file_path: str, csv_name: str):
    """
    Unzip a .zip file contents.
    
    """
    # name = url.split("/")[-1]
    # file_path = f"{zip_path}/{name}"
    with ZipFile(file_path, 'r') as zip:
        logger.info(f'Extracting {file_path}...')
        # csv_name = name.split(".")[0]
        zip.extractall(f"{destination_path}/{csv_name}")
        logger.info('Done!')

