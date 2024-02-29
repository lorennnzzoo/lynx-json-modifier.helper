import json
def defaultModifier():    
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
    "autoRebootCycle": "0"
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


    userInputModbus=input('\n\nPlease Give Inputs For Modbus baudrate and parity For \nExample 9600,1 : ')
    baudrate=userInputModbus.split(',')[0]
    parity=userInputModbus.split(',')[1]
    modBusSettingsBlock = {
    "mbBaudRate": "9600",
    "mbParity": "1",
    "mbSlaveCnt": 1,
    "mbReadTryCount": "1"
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

    userInputAnalogSettings=input('\n\nPlease enter the no of analog channels and its values count \nfor example : 1to8')    
    analogchannels=userInputAnalogSettings
    print('you will be asked to enter analog channels data for '+analogchannels+' times')
    for i in range(int(analogchannels)):
        userinputAnalogData=input('Please enter analog data for channel '+str(i+1)+' flag,varname,varname2,minrange,maxrange,factor\nfor example 1,PM,0,1000')
        flag=userinputAnalogData.split(',')[0]
        varName=userinputAnalogData.split(',')[1]
        varName2=userinputAnalogData.split(',')[2]
        minRange=userinputAnalogData.split(',')[3]
        maxRange=userinputAnalogData.split(',')[4]
        factor=userinputAnalogData.split(',')[5]
        if(1>0):
            anaToDigArray=',{\"anaToDigType":'+flag+',\"minOutVal":0,\"maxOutVal":20,\"minmA":0,\"maxmA":20,\"varName":'+str(varName)+',\"varName2":'+str(varName2)+',\"varFactor":'+factor+'}'
        else:
            anaToDigArray='{\"anaToDigType":'+flag+',\"minOutVal":0,\"maxOutVal":20,\"minmA":0,\"maxmA":20,\"varName":'+str(varName)+',\"varName2":'+str(varName2)+',\"varFactor":'+factor+'}'
    analogSettingsBlock=',\"anaToDigSettings":{ \"anaToDigCnt":'+analogchannels+',\"anaToDigArray":['+str(anaToDigArray)+']}'
    print('\n\n analog settings block generated')

    dotFourSettingsBlock+=analogSettingsBlock


    print('\n\n '+dotFourSettingsBlock)
    json_data = json.loads('{'+dotFourSettingsBlock+'}')
    print(json_data)
def threeSevenModifier():
    pass
def threeNineOneModifier():
    pass
def fourZeroOneModifier():
    pass