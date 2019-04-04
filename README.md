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

# test File Descriptions 

 E2E Tests:

Setup - Start the catalog, order and frontend servers in their respective machines. Run python3 end2end.py after 
uncommenting the relevant test. 
Tests ensure distributedness and consistency.

 Unit Tests:

Framework used - pytest version 3.10.1

Setup - Run pytest from the test directory. Filenames with 'test' token in the them are automatically picked up and run as unit tests.
Tests ensure logical consistency of REST API calls

# docs File Descriptions

* CS677_Lab_2.pdf - Design document
* CS677_Lab_2_Tests.pdf -  Design document showing output of tests.
* Output file showing sample output from runs is included in the Design Document. 
* Performance analysis is included in the Design Document.




