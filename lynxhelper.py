import os
import subprocess
import modifieres as d


versionSelec=input("Please Provide The Version Number For File ex: default,3.7,3.91,4.01 \nPress F if you want to create your a modified json : ")
if(versionSelec=="default"):
    process = subprocess.run(os.getcwd()+"/base-version-files/lynx testing.json", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
elif(versionSelec=="3.7"):
    process = subprocess.run(os.getcwd()+"/base-version-files/lynx testing 3.7.json", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
elif(versionSelec=="3.91"):
    process = subprocess.run(os.getcwd()+"/base-version-files/lynx testing 3.91.json", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
elif(versionSelec=="4.01"):
    process = subprocess.run(os.getcwd()+"/base-version-files/lynx testing 4.01.json", shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

elif(versionSelec=='F'):
    selectVersion=input("Please Provide The Version Number For File You Want To Edit ex: default,3.7,3.91,4.01 : ")
    if(selectVersion=="default"):
        d.defaultModifier()
    elif(selectVersion=="3.7"):
        d.threeSevenModifier()
    elif(selectVersion=="3.91"):
        d.threeNineOneModifier()
    elif(selectVersion=="4.01"):
        d.fourZeroOneModifier()