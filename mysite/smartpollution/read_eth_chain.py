from Naked.toolshed.shell import muterun_js


#Note this path below needs to be the abs path to the getContractInfo script
def get_contract_info(abi, address):
    print("GEnerating info:"+str(abi))
    response = muterun_js('C:\Solidity\SmartPollution\getContractInfo.js "'+str(abi)+'" "'+str(address)+'"')
    print("REsponse:"+str(response._getAttributeDict().get('stderr')))
    print("stdout:"+str(response._getAttributeDict().get('stdout')))
    contr_info = response._getAttributeDict().get('stdout')
    return contr_info