# Pygmy.com:  A Multi-tier Online Book Store


# Environment Setup

There  is  one  config  file sv_info.csv that has server information in the comma-separated format:Type of Server, IP Address, Port. Modify the config files as required to setup the environment. There are four Python filescatalog.py, order.py, frontend.py and client.py- they represent the catalog server, order server, frontend server and the client respectively.

# Program Execution

Start the servers from their respective machines (as specified in sv_info.csv) using python3 server_name_here.py.  Run client.py from the fourth machine to start operations.

# src File Descriptions

catalog.py - Catalog server

order.py - Order server

frontend.py - Frontend server

client.py - Client

catalog.json - Book details for all books 

order_log.txt - Transaction logs for order server

sv_info.csv - Config file for details of the 3 servers

times - Directory with Response Time logs for search, lookup and buy

time_parser.py - Script to calculate ART (Average Response Time)

conftest.py - Dummy file for pytest


