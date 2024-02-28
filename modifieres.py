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

    lynxdefualt = {
        "dotFourSettings": {
    "modBus": int(modbus),
    "snmp": 0,
    "ethernet": int(ethernet),
    "tcpParse": 0,
    "loopDelay": "60",
    "timeSync": "1",
    "lowPowerMode": 0,
    "disableSendStatus": "0",
    "displayName": str(displayName),
    "useDefaultCloud": 0,
    "cloudServer": 20,
    "debugFlag": 1,
    "anaToDig": int(analog),
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
    "dataScale": int(dataScale),
    "nwFallback": "0",
    "modBus2": 0,
    "autoRebootCycle": str(autoRebootCycle)
  }
    }
    dotFourSettingsBlock= "{"+str(lynxdefualt).replace("{","").replace("}","")+"}"



def threeSevenModifier():
    pass
def threeNineOneModifier():
    pass
def fourZeroOneModifier():
    pass