import os
from .models import *


def create_new_smart_contract1(template_name='PollutionTracker', metric_name='DefaultMetricName', lower_trigger=-6666,
                               upper_trigger=6666):
    with open(os.path.join(os.getcwd(), template_name + '.sol'), 'w', encoding='utf-8') as out_file, open(
            os.path.join(os.getcwd(), 'smartpollution', 'static', 'smartcontracts', 'template_smartcontract.sol'), 'r',
            encoding='utf-8') as template_f:
        for lin in template_f:
            if not "@" in lin:
                out_file.write(lin)
            else:
                if "@ContractName@" in lin:
                    out_file.write(lin.replace('@ContractName@', str(template_name).replace('-', '')))
                if "@MetricName@" in lin:
                    out_file.write(lin.replace('@MetricName@', str(r'"' + metric_name + r'"').replace('-', '')))
                if "@LowerTrigger@" in lin:
                    out_file.write(lin.replace('@LowerTrigger@', str(int(lower_trigger))))
                if "@UpperTrigger@" in lin:
                    out_file.write(lin.replace('@UpperTrigger@', str(int(upper_trigger))))
    return os.path.join(os.getcwd(), template_name + '.sol')


def create_new_smart_contract(template_name='PollutionTracker', metrics=[]):
    with open(os.path.join(os.getcwd(), template_name + '.sol'), 'w', encoding='utf-8') as out_file, open(
            os.path.join(os.getcwd(), 'smartpollution', 'static', 'smartcontracts',
                         'simple_template_smartcontract.sol'), 'r', encoding='utf-8') as template_f:
        for lin in template_f:
            if not "@" in lin:
                out_file.write(lin)
            else:
                if "@contractName@" in lin:
                    out_file.write(lin.replace('@contractName@', str(template_name).replace('-', '')))
                if "@singleEvents@" in lin:
                    for met in metrics:
                        out_file.write('\t\tevent ' + str(met) + '(' + 'int16 _val' + str(met) + ',' + 'string _id);\n')
                if "@singleUpdate@" in lin:
                    for met in metrics:
                        out_file.write('\t\tfunction alarm' + str(met) + '(' + 'int16 _val' + str(
                            met) + ',' + 'string _id) onlyOwner{' + str(met) + '(' + '_val' + str(
                            met) + ', ' + '_id);}\n')
                if "@paramsAlarmAll@" in lin:
                    out_file.write('\t\t\t')
                    for met in metrics:
                        out_file.write(' int16 _val' + str(met) + ',')
                    out_file.write(' string _id\n')

                if "@paramsUpdateAll@" in lin:
                    for met in metrics:
                        out_file.write('\t\t\t\tint16 _val' + str(met) + ',')
                    out_file.write(' string _id\n')
                if "@codeUpdateAll@" in lin:
                    out_file.write('\t\t\t\tAlarmAll(')
                    for met in metrics:
                        out_file.write(' _val' + str(met) + ',')
                    out_file.write(' _id);\n')

    return os.path.join(os.getcwd(), template_name + '.sol')


def create_new_smart_contract_with_thresholds(template_name='PollutionTracker', thresholds=[]):
    print('Creating thresholds contract.')
    with open(os.path.join(os.getcwd(), template_name + '.sol'), 'w', encoding='utf-8') as out_file, open(
            os.path.join(os.getcwd(), 'smartpollution', 'static', 'smartcontracts',
                         'simple_template_smartcontract_with_thresholds.sol'), 'r', encoding='utf-8') as template_f:
        for lin in template_f:
            if not "@" in lin:
                out_file.write(lin)
            else:
                if "@tresholdsInit@" in lin:
                    for thres in thresholds:
                        out_file.write('\t\tint16 constant ' + str(thres.metric.physical_property) + str(
                            thres.metric.unit_of_measurement) + 'LT =' + str(int(thres.lower_trigger)) + ';\n')
                        out_file.write('\t\tint16 constant ' + str(thres.metric.physical_property) + str(
                            thres.metric.unit_of_measurement) + 'UT =' + str(int(thres.upper_trigger)) + ';\n')
                if "@contractName@" in lin:
                    out_file.write(lin.replace('@contractName@', str(template_name).replace('-', '')))
                if "@singleEvents@" in lin:
                    for thres in thresholds:
                        out_file.write('\t\tevent Alarm' + str(thres.metric.physical_property) + str(
                            thres.metric.unit_of_measurement) + '(' + 'int16 _val' + str(
                            thres.metric.physical_property) + str(
                            thres.metric.unit_of_measurement) + ',' + 'string _id);\n')
                if "@paramsAlarmAll@" in lin:
                    out_file.write('\t\t')
                    a=0
                    for thres in thresholds:
                        out_file.write(' int16 _val' + str(thres.metric.physical_property) + str(
                            thres.metric.unit_of_measurement) + ',')
                    out_file.write(' string _id\n')

                if "@paramsUpdateAll@" in lin:
                    out_file.write('\t\t\t')
                    for thres in thresholds:
                        out_file.write('int16 _val' + str(thres.metric.physical_property) + str(
                            thres.metric.unit_of_measurement) + ',')
                    out_file.write(' string _id\n')
                if "@codeUpdateAllIf" in lin:
                    i = 0;
                    for thres in thresholds:
                        i = i + 1
                        out_file.write('\t\t\t(' + str(thres.metric.physical_property) + str(
                            thres.metric.unit_of_measurement) + 'LT' + ' > ' + '_val' + str(
                            thres.metric.physical_property) + str(thres.metric.unit_of_measurement) + ' || ' +
                                       str(thres.metric.physical_property) + str(
                            thres.metric.unit_of_measurement) + 'UT' + ' < ' + '_val' + str(
                            thres.metric.physical_property) + str(thres.metric.unit_of_measurement) + ')')
                        print('Length:' + str(len(thresholds)) + ' I:' + str(i))
                        if i < len(thresholds):
                            out_file.write(' && \n')

                if "@codeUpdateAll@" in lin:
                    out_file.write('\t\t\t\tAlarmAll(')
                    for thres in thresholds:
                        out_file.write(' _val' + str(thres.metric.physical_property) + str(
                            thres.metric.unit_of_measurement) + ',')
                    out_file.write(' _id);\n')
                if "@singleUpdate@" in lin:
                    for thres in thresholds:
                        out_file.write('\t\tfunction update' + str(thres.metric.physical_property) + str(
                            thres.metric.unit_of_measurement) + '(' + 'int16 _val' + str(
                            thres.metric.physical_property) + str(thres.metric.unit_of_measurement)
                                       + ',' + 'string _id) onlyOwner{' +
                                       'if(' + str(thres.metric.physical_property) + str(
                            thres.metric.unit_of_measurement) + 'LT' + ' > ' + '_val' + str(
                            thres.metric.physical_property) + str(thres.metric.unit_of_measurement) + ' || ' +
                                       str(thres.metric.physical_property) + str(
                            thres.metric.unit_of_measurement) + 'UT' + ' < ' + '_val' + str(
                            thres.metric.physical_property) + str(thres.metric.unit_of_measurement) + '){'
                                       + 'Alarm'+str(thres.metric.physical_property) + str(
                            thres.metric.unit_of_measurement) + '(' + '_val' + str(
                            thres.metric.physical_property) + str(
                            thres.metric.unit_of_measurement) + ', ' + '_id);}}\n')
                if "@codeUpdateAllElse@" in lin:
                    for thres in thresholds:
                        out_file.write('\t\t\t'+
                                       'if(' + str(thres.metric.physical_property) + str(
                            thres.metric.unit_of_measurement) + 'LT' + ' > ' + '_val' + str(
                            thres.metric.physical_property) + str(thres.metric.unit_of_measurement) + ' || ' +
                                       str(thres.metric.physical_property) + str(
                            thres.metric.unit_of_measurement) + 'UT' + ' < ' + '_val' + str(
                            thres.metric.physical_property) + str(thres.metric.unit_of_measurement) + '){'
                                       + 'Alarm'+str(thres.metric.physical_property) + str(
                            thres.metric.unit_of_measurement) + '(' + '_val' + str(
                            thres.metric.physical_property) + str(
                            thres.metric.unit_of_measurement) + ', ' + '_id);}\n')
                if "@triggerReturns@" in lin:
                    i = 0;
                    for thres in thresholds:
                        i = i + 1
                        out_file.write('\t\tint16 ' + str(thres.metric.physical_property) + str(
                            thres.metric.unit_of_measurement) +'LT ,int16 ' + str(
                            thres.metric.physical_property) + str(thres.metric.unit_of_measurement)
                                       + 'UT');
                        if i < len(thresholds):
                            out_file.write(' ,')
                if "@triggerRealReturn@" in lin:
                    i = 0
                    out_file.write('\t\treturn(')
                    for thres in thresholds:
                        print('GOGOGO')
                        i = i + 1
                        out_file.write(str(int(thres.lower_trigger)) + ' ,' + str(int(thres.upper_trigger)))
                        if i < len(thresholds):
                            out_file.write(', ')
                        else:
                            out_file.write(');')
                            print('END')

    return os.path.join(os.getcwd(), template_name + '.sol')
