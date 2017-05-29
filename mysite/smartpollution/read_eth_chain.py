from Naked.toolshed.shell import muterun_js
import os
import json


#Note this path below needs to be the abs path to the getContractInfo script
def get_contract_info(abi, address):
    print("GEnerating info:"+str(abi))

    abi_formatted=str(abi).replace('"',"@StringDelimiter@")
    print(abi_formatted)

    script_path=os.path.join(os.getcwd(),'smartpollution','static','smartcontracts','getContractInfo.js')
    response = muterun_js(script_path+' "'+str(abi_formatted)+'" "'+str(address)+'"')
    print("REsponse:"+str(response._getAttributeDict().get('stderr')))
    print("stdout:"+str(response._getAttributeDict().get('stdout')))
    contr_info = response._getAttributeDict().get('stdout')

    parsed = json.loads(contr_info)
    info=str(json.dumps(parsed, indent=4, separators=(':',',')))
    return info