# Data Pipeline

## 1. Ingestion

### Download

### Process (Unzip and choose CSV)

## 2. Data Warehouse

### Create Dataset and Tables

### Check data quality

### Load data into db

## 3. Data Quality

### Check for null values

To run everything:

```
make
```

## Generate Graph view from makefile

```
wget https://raw.githubusercontent.com/vak/makefile2dot/master/makefile2dot.py
```
```
python makefile2dot.py dag.makefile | dot -Tpng > example-dag.png
```