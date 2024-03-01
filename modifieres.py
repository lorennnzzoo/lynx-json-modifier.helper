import subprocess
import json
def defaultModifier():    
    filename=input('Please Provide the filename for your json : ')
    variablesForDataScaling=[]
    userInput=input("Please Give inputs for Modbus, Analog, Static Ethernet, Display Name, Auto Reboot Cycle, Data Scaling\nFor Example : 1,1,0,NK Square Solutions,1,1 : ")
    userFourSettings=userInput.split(",")
    modbus=userFourSettings[0]
    analog=userFourSettings[1]
    ethernet=userFourSettings[2]
    displayName=userFourSettings[3]
    autoRebootCycle=userFourSettings[4]
    dataScale=userFourSettings[5]

    data = {
    "modBus": 1,
    "snmp": 0,
    "ethernet": 0,
    "tcpParse": 0,
    "loopDelay": "60",
    "timeSync": "1",
    "lowPowerMode": 0,
    "disableSendStatus": "0",
    "displayName": "NK SQUARE SOLUTIONS",
    "useDefaultCloud": 0,
    "cloudServer": 20,
    "debugFlag": 1,
    "anaToDig": 1,
    "sensor": 0,
    "rtc": 1,
    "debugFourG": 1,
    "dpPerPacket": "9",
    "dio": 0,
    "modBusTcp": 0,
    "rms": 1,
    "rmsStoreData": 1,
    "sdCard": 1,
    "nfh": 1,
    "dataScale": 1,
    "nwFallback": "0",
    "modBus2": 0,
    "autoRebootCycle": "0",
    "whiteLabel": 1
}

# Update specific values
    data["modBus"] = int(modbus)
    data["anaToDig"] = int(analog)
    data["dataScale"] = int(dataScale)
    data["displayName"] = str(displayName)
    data["ethernet"] = int(ethernet)
    data["autoRebootCycle"] = str(autoRebootCycle)
    dotfourstring = json.dumps(data)
    dotFourSettingsBlock= "\"dotFourSettings\": "+dotfourstring+""
    print('dotFourSettingsBlock Generated')

    print('adding additional settings')

    dotFourSettingsBlock+=',\"whiteLabelSettings":{\"deviceName":\"NK Envion",\"line1":\"NK Square",\"line2":\"Envion-Y"}'
    dotFourSettingsBlock+=',\"nfhSettings":{\"nfhMode":10,\"maxLoopCnt":4,\"nfhDataDir":\"/nfhTmpDir"}'
    dotFourSettingsBlock+=',\"rtcSettings":{\"bootupNtpSync":1,\"timeZoneMinutes":\"330",\"poolServerName":\"pool.ntp.org"}'

    if int(modbus) == 1:
        userInputModbus=input('\n\nPlease Give Inputs For Modbus baudrate and parity For \nExample 9600,1 : ')
        baudrate=userInputModbus.split(',')[0]
        parity=userInputModbus.split(',')[1]
        modBusSettingsBlock = {
        "mbBaudRate": "9600",
        "mbParity": "1",
        "mbSlaveCnt": 1,
        "mbReadTryCount": "1",
        "mbHwSerial": 0
    }
        modBusSettingsBlock['mbBaudRate']=baudrate
        modBusSettingsBlock["mbParity"]=parity
        modbusSettingsString=json.dumps(modBusSettingsBlock)
        
        dotFourSettingsBlock+=", \"modBusSettings\": "+modbusSettingsString+""    
        print('modbus Settings block is generated')

        userInputModbusSlavesAndRegisters=input('\n\nPlease Provide slave id and no of regsters you want to read \nfor example 1,4 : ')
        slaveId=userInputModbusSlavesAndRegisters.split(',')[0]
        registersCount=userInputModbusSlavesAndRegisters.split(',')[1]
        print('You will be asked to enter registers data '+str(registersCount)+' times')
        mbarray = '['
        for i in range(int(registersCount)):
            userInputRegistersData = input('\n\nPlease enter varName,registerNo,dataType,factor \nfor example MODBUS,40004,1,204: ')
            registerName = userInputRegistersData.split(',')[0]
            variablesForDataScaling.append(registerName)
            registerNumber = userInputRegistersData.split(',')[1]
            dataType = userInputRegistersData.split(',')[2]
            factor = userInputRegistersData.split(',')[3]

            if i > 0:
                mbarray += ',{"varName":"' + str(registerName) + '","mbReg":"' + str(registerNumber) + '","varType":"' + str(dataType) + '","varFactor":"' + str(factor) + '"}'
            else:
                mbarray += '{"varName":"' + str(registerName) + '","mbReg":"' + str(registerNumber) + '","varType":"' + str(dataType) + '","varFactor":"' + str(factor) + '"}'

        mbarray += ']'

        slaveAndRegistersBlock ='{"slaveID": "'+slaveId+'","mbRegCnt": '+parity+',"mbArray": '+mbarray+'}'
        dotFourSettingsBlock+=',"modBusSlaves":['+str(slaveAndRegistersBlock)+']'                    
        print('\n\nregister data and slave data block is generated')
    if int(analog) == 1:

        userInputAnalogSettings=input('\n\nPlease enter the no of analog channels and its values count \nfor example 1 to 8 : ')    
        if int(userInputAnalogSettings)>8:
            print('length cannot exceed more than 8')
        else:
            analogchannels=userInputAnalogSettings
            print('you will be asked to enter analog channels data for '+analogchannels+' times')
            anaToDigArray=str()
            for i in range(int(analogchannels)):
                userinputAnalogData=input('\n\nPlease enter analog data for channel '+str(i+1)+' varname,varname2,factor\nfor example PM,PM_ma,1 : ')        
                varName=userinputAnalogData.split(',')[0]
                variablesForDataScaling.append(varName)
                varName2=userinputAnalogData.split(',')[1]
                factor=userinputAnalogData.split(',')[2]
                if i>0:
                    anaToDigArray +=',{\"anaToDigType":1,\"minOutVal":0,\"maxOutVal":20,\"minmA":0,\"maxmA":20,\"dcRes":150,\"varName":\"'+(varName)+'",\"varName2":\"'+(varName2)+'",\"varFactor":'+factor+'}'
                else:
                    anaToDigArray +='{\"anaToDigType":1,\"minOutVal":0,\"maxOutVal":20,\"minmA":0,\"maxmA":20,\"dcRes":150,\"varName":\"'+(varName)+'",\"varName2":\"'+(varName2)+'",\"varFactor":'+factor+'}'
            analogSettingsBlock=',\"anaToDigSettings":{ \"anaToDigCnt":'+analogchannels+',\"anaToDigArray":['+str(anaToDigArray)+']}'
            

            dotFourSettingsBlock+=analogSettingsBlock
            print('\n\n analog settings block generated')

    if int(ethernet)  == 1:
        userInputEtherNetSettings=input('\n\nPlease enter IP,SUBNETMASK,GATEWAY,DNS \nFor example 192.168.1.243,255.255.255.0,192.168.1.1,8.8.8.8  if not needed enter F : ')
        if(userInputEtherNetSettings=='F'):
            dotFourSettingsBlock+=',\"ethernetSettings":{\"userStaticIP":0,\"etherIP":[\"192",\"168",\"1,\"143"],\"etherSubnet":[\"255",\"255",\"255",\"0"],\"etherGateway":[\"192",\"168",\"1",\"1"],\"etherDns":[\"8",\"8",\"8",\"8]}'
        else:
            ip=userInputEtherNetSettings.split(',')[0]
            subnet=userInputEtherNetSettings.split(',')[1]
            gateway=userInputEtherNetSettings.split(',')[2]
            dns=userInputEtherNetSettings.split(',')[3]
            ipArray=ip.split('.')
            subnetArray=subnet.split('.')
            gatewayArray=gateway.split('.')
            dnsArray=dns.split('.')
            dotFourSettingsBlock+=',\"ethernetSettings":{\"userStaticIP":1,\"etherIP":[\"'+ipArray[0]+'",\"'+ipArray[1]+'",\"'+ipArray[2]+'",\"'+ipArray[3]+'"],\"etherSubnet":[\"'+subnetArray[0]+'",\"'+subnetArray[1]+'",\"'+subnetArray[2]+'",\"'+subnetArray[3]+'"],\"etherGateway":[\"'+gatewayArray[0]+'",\"'+gatewayArray[1]+'",\"'+gatewayArray[2]+'",\"'+gatewayArray[3]+'"],\"etherDns":[\"'+dnsArray[0]+'",\"'+dnsArray[1]+'",\"'+dnsArray[2]+'",\"'+dnsArray[3]+'"]}'
            print('\n\nEthernet Settings Block Generated')
    
    userInputHttpSettings=input('\n\nPlease enter ServerURL,EndPoint\nfor example 20.205.179.148,/NkssLiveData/api/readlivedata : ')
    httpServer=userInputHttpSettings.split(',')[0]
    httpApiName=userInputHttpSettings.split(',')[1]
    dotFourSettingsBlock+=',\"httpSettings":{\"httpServer":"'+httpServer+'",\"httpApiName":"'+httpApiName+'",\"httpPort":\"80",\"httpSSL":0,\"httpSuccessCode":\"200"}'

    print('\n\nHttpSettings Block generated')


    dataScaleString='\"dataScaleSettings":{\"scaleVariables":{'
    varScale=[]
    if variablesForDataScaling != None:
        userInputIsDataScale=input('\n\nthere are '+str(len(variablesForDataScaling))+' variables you added do you want to apply data scaling for them?\nenter S if yes F if no ')
        if userInputIsDataScale == 'S':
            for var in variablesForDataScaling:
                userInputDataScaleSettings=input('\n\nPlease enter min input,max input,min range,max range,min cutoff,max cutoff if not need press F\nfor '+var+'\nfor example 4,20,0,1000,0,1000 : ')
                if userInputDataScaleSettings != 'F':
                    minIn=userInputDataScaleSettings.split(',')[0]
                    maxIn=userInputDataScaleSettings.split(',')[1]
                    minOut=userInputDataScaleSettings.split(',')[2]
                    maxOut=userInputDataScaleSettings.split(',')[3]
                    minOutLimit=userInputDataScaleSettings.split(',')[4]
                    maxOutLimit=userInputDataScaleSettings.split(',')[5]
                    varScale.append('\"'+var+'":{\"minIn":'+minIn+',\"maxIn":'+maxIn+',\"minOut":'+minOut+',\"maxOut":'+maxOut+',\"minOutLimit":'+minOutLimit+',\"maxOutLimit":'+maxOutLimit+',\"maxOutRandom":0,\"maxOutLimitR1":430,\"maxOutLimitR2":490}')
    for i, var in enumerate(varScale):
        if i > 0:
            dataScaleString += ',' + var
        else:
            dataScaleString += var
    dataScaleString+='}}'
    dotFourSettingsBlock+=','+dataScaleString

    print('\n\ndatascalesettings block generated')

    userInputPayloadSettings=input('\n\nPlease enter deviceid : ')    
    deviceId=userInputPayloadSettings
    payloadString=',\"payloadSettings":{\"payloadType":\"14",\"sendTimeStamp":1,\"key1":\"Variablename",\"key2":\"Value",\"tskey":\"Datetime",\"tsType":\"65",\"metaData":{\"FunctionName":\"53",\"Name":\"JSW",\"Password":\"JSW",\"DeviceID":\"'+deviceId+'",\"additionalInfo":{\"SoftwareNameVersion":\"NK2EnviroMonitor-V1.0",\"Lattitude":\"17.53",\"Longitude":\"78.45"}}'
    varDataString=',\"varData":{'
    mapdata=str()
    for i,var in enumerate(variablesForDataScaling):
        userInputMapping=input('\nPlease enter DeviceidChannelName,Unit for '+str(var)+' if not needed enter F\nfor example NO,mg/nm3 : ')
        if userInputMapping != 'F':
            DeviceIdChannelName=userInputMapping.split(',')[0]
            Unit=userInputMapping.split(',')[1]
            if i>0:
                mapdata+=',\"'+var+'":{\"varName":\"'+DeviceIdChannelName+'",\"metaData":{\"Unit":\"'+Unit+'",\"Flags":""}}'
            else:
                mapdata+='\"'+var+'":{\"varName":\"'+DeviceIdChannelName+'",\"metaData":{\"Unit":\"'+Unit+'",\"Flags":""}}'
    payloadString+=varDataString
    payloadString+=mapdata
    dotFourSettingsBlock+=payloadString+'}}'
            
    json_data = json.loads('{'+dotFourSettingsBlock+'}')    
    with open(filename+'.json', 'w') as json_file:
        json.dump(json_data, json_file, indent=4)    
        json_file.close()    
