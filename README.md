# Smart Contract Generator
This is the Smart Contract Generator Django webapp:
maintained and developed by: Sandro Luck


Blockchains have made tremendouse changes during the last years on financial and non financial applications. 
A promising new usage of the blockchain technology have been Smart Contracts, Turing complete programms globally evaluated on the blockchain. 
Generating vast amounts of Smart Contract for Sensor based use cases has been a time consuming and difficult task. 
The Smart Contract Generator Framework allows the user to automate the creation of Smart Contracts for Internet of Things related use cases and speed up the creation and monitoring process. 
The Django based graphical web application aids the user at generating and writing these Smart Contracts.

Examples of the produced Smart Cotracts might be found at https://github.com/SandroLuck/SCGenerator/tree/master/ExampleSmartContracts




Additional documentation might be found at https://www.djangoproject.com/

# Install & Start:
1. Install Python (Versions >=3 should work, yet we have developed this application using 3.5.2) and pip.

2. Install via pip django, psycopg2 and naked
```
pip install django naked psycopg2
```
3. cd to /"Path to this app"/mysite/
3.1 locate the manage.py file (you have to be in the folder where manage.py is)

4. run the django migrations in cases something went wrong, it should return nothing to change
```
python manage.py makemigrations
``` 
```
python manage.py migrate
```
5. run the application 
```
python manage.py runserver
```
6. Open your browser and go to localhost:8000/smartGenerator/

Switching Database:
Since setting up the application is easiest with SQLite it is the default database.
However if you wish to use a different database choose one from https://docs.djangoproject.com/en/1.11/ref/databases/ and follow the django documentation.

Optional:
To create an admin user: 
```
python manage.py createsuperuser
```
You can now go to localhost:8000/admin/ and modify the database directly

To get the full Blockchain support (Mainly the Smart Contractg Monitor):
1. Install nodejs https://nodejs.org/en/download/ and npm (or any package manager)
```
npm install web3 solc fs
```
2. Install geth https://github.com/ethereum/go-ethereum/wiki/geth
```
geth --rpc --testnet --rpcapi="db,eth,net,web3,personal" --rpcport "8545" --rpcaddr "127.0.0.1" --rpccorsdomain "localhost"
```
Note that this will start the testnet ropsten. 
The application will listen to every eth-blockchain running on the port 8545, so you can switch it with te mainnet or any other net.

This project follows the,
# The MIT License (MIT)

Copyright (c) 2017, University of Zürich

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
