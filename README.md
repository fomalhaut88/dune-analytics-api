# dune-analytics-api

It is a Python library to make SQL queries to databases provided by [Dune Analytics](https://duneanalytics.com/). 
First, **dune-analytics-api** has tools to interact with Dune Analytics from Python scripts.
Second, there is a command-line script that emulates terminal where you can query and download the data.

## Installation

```
pip install git+https://github.com/fomalhaut88/dune-analytics-api.git
```

## Use from command line

You must be registered on Dune Analytics to have username and password.

To run:

```
dune-analytics-api
```

If you set environment variables **DUNE_USERNAME** and **DUNE_PASSWORD**, you can run
command line without authorization questions:

```
dune-analytics-api -e
```

### Query example

```
$ dune-analytics-api -e
Trying to get username and password from environment...
Creating a session...
Welcome to dune-analytics-api (version 1.0) where you can perform SQL queries as at https://duneanalytics.com/
> SELECT count(*) FROM ethereum.blocks;
+----------+
|  count   |
+----------+
| 11620094 |
+----------+
```

### Download to CSV

```
$ dune-analytics-api -e
Trying to get username and password from environment...
Creating a session...
Welcome to dune-analytics-api (version 1.0) where you can perform SQL queries as at https://duneanalytics.com/
> download data.csv
> SELECT * FROM ethereum.blocks LIMIT 100;
Saved to data.csv
```

## Use from Python

A simple script that gets last 10 transactions in Ethereum.

```python
# Import Session and QueryMaker
from dune_analytics_api import Session, QueryMaker

# The query
query = """
    SELECT * FROM ethereum.blocks
    ORDER BY "time" DESC
    LIMIT 10
"""

# You need to be registered on Dune Analytics to have username and password
session = Session.from_login('your_username', 'your_password')

# Create a QueryMaker object
query_maker = QueryMaker(session)

# Execute the query
rows = query_maker.exec(query)

# Print the result
for row in rows:
    print(row)
```
