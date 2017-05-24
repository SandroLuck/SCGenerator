import subprocess

#Note this path below needs to be the abs path to the getContractInfo script
def get_Contract_Info(abi, address):
    subprocess.run("geth --exec loadScript('C:/Solidity/SmartPollution/getContractInfo.js "+str(abi)+" "+str(address)+"') attach", stdout=subprocess.PIPE).stdout.decode('utf-8')