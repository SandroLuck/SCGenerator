from Naked.toolshed.shell import muterun_js
import os
import json


#Note this path below needs to be the abs path to the getContractInfo script
def get_contract_info(abi, address):
    print("Generating info:")

    abi_formatted=str(abi).replace('"',"@StringDelimiter@")
    script_path=os.path.join(os.getcwd(),'smartpollution','static','smartcontracts','getContractInfo.js')
    response = muterun_js(script_path+' "'+str(abi_formatted)+'" "'+str(address)+'"')
    #print("REsponse:"+str(response._getAttributeDict().get('stderr')))
    #print("stdout:"+str(response._getAttributeDict().get('stdout')))
    contr_info = response._getAttributeDict().get('stdout')
    info=str(contr_info).replace('\\n','').replace('[','').replace(']','').replace('{','').replace('}','').replace(',',' \t ').replace('b\'','')
    info=info.split("Event:")
    del info[0]
    return info

def get_contract_gas(path):
    script_path=os.path.join(os.getcwd(),'smartpollution','static','smartcontracts','estimateCosts.js')
    response = muterun_js(script_path+' "'+path+'"')
    print("REsponse:"+str(response._getAttributeDict().get('stderr')))
    print("stdout:"+str(response._getAttributeDict().get('stdout')))
    contr_info = response._getAttributeDict().get('stdout')
    print('CONTR_info:'+str(contr_info))
    return contr_info