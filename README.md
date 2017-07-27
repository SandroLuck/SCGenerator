# Smart Contract Generator
This is the Smart Contract Generator Django webapp:
maintained and developed by: Sandro Luck

Additional documentation might be found at https://www.djangoproject.com/

To start this application:
1. Install Python (Versions >=3 should work, yet we have developed this application using 3.5.2) and pip.

2. Install via pip django and naked
```
pip install django naked
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
