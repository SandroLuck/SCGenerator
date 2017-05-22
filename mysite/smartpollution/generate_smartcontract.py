import os

def create_new_smart_contract(template_name='PollutionTracker', metric_name='DefaultMetricName', lower_trigger=-6666, upper_trigger=6666):
    with open(os.path.join(os.getcwd(),template_name+'.sol'),'w',encoding='utf-8') as out_file, open(os.path.join(os.getcwd(),'smartpollution','static','smartcontracts','template_smartcontract.sol'),'r',encoding='utf-8') as template_f:
        for lin in template_f:
            if not "@" in lin:
                out_file.write(lin)
            else:
                if "@ContractName@" in lin:
                    out_file.write(lin.replace('@ContractName@',str(template_name).replace('-','')))
                if "@MetricName@" in lin:
                    out_file.write(lin.replace('@MetricName@',str(r'"'+metric_name+r'"').replace('-','')))
                if "@LowerTrigger@" in lin:
                    out_file.write(lin.replace('@LowerTrigger@',str(int(lower_trigger))))
                if "@UpperTrigger@" in lin:
                    out_file.write(lin.replace('@UpperTrigger@',str(int(upper_trigger))))
    return os.path.join(os.getcwd(),template_name+'.sol')