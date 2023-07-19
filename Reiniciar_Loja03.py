# encoding: iso-8859-1
import subprocess, os, sys

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.3.1 ""c:\\pdv\desligar.bat", shell=True)
print(ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
    os.chdir('C:\\ATUAL')
    with open('Caixa1Lj03.txt', 'a') as caixa:
        caixa.write('Pdv não reiniciado\n')
        caixa.close()
else:
    print("Pdv reiniciado_Caixa 01")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.3.2 ""c:\\pdv\desligar.bat", shell=True)
print(ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
    os.chdir('C:\\ATUAL')
    with open('Caixa2Lj03.txt', 'a') as caixa:
        caixa.write('Pdv não reiniciado\n')
        caixa.close()
else:
    print("Pdv reiniciado_Caixa 02")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.3.3 ""c:\\pdv\desligar.bat", shell=True)
print(ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
    os.chdir('C:\\ATUAL')
    with open('Caixa3Lj03.txt', 'a') as caixa:
        caixa.write('Pdv não reiniciado\n')
        caixa.close()
else:
    print("Pdv reiniciado_Caixa 03")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.3.4 ""c:\\pdv\desligar.bat", shell=True)
print(ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
    os.chdir('C:\\ATUAL')
    with open('Caixa4Lj03.txt', 'a') as caixa:
        caixa.write('Pdv não reiniciado\n')
        caixa.close()
else:
    print("Pdv reiniciado_Caixa 04")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.3.5 ""c:\\pdv\desligar.bat", shell=True)
print(ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
    os.chdir('C:\\ATUAL')
    with open('Caixa5Lj03.txt', 'a') as caixa:
        caixa.write('Pdv não reiniciado\n')
        caixa.close()
else:
    print("Pdv reiniciado_Caixa 05")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.3.6 ""c:\\pdv\desligar.bat", shell=True)
print(ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
    os.chdir('C:\\ATUAL')
    with open('Caixa6Lj03.txt', 'a') as caixa:
        caixa.write('Pdv não reiniciado\n')
        caixa.close()
else:
    print("Pdv reiniciado_Caixa 06")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.3.7 ""c:\\pdv\desligar.bat", shell=True)
print(ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
    os.chdir('C:\\ATUAL')
    with open('Caixa7Lj03.txt', 'a') as caixa:
        caixa.write('Pdv não reiniciado\n')
        caixa.close()
else:
    print("Pdv reiniciado_Caixa 07")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.3.8 ""c:\\pdv\desligar.bat", shell=True)
print(ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
    os.chdir('C:\\ATUAL')
    with open('Caixa8Lj03.txt', 'a') as caixa:
        caixa.write('Pdv não reiniciado\n')
        caixa.close()
else:
    print("Pdv reiniciado_Caixa 08")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.3.9 ""c:\\pdv\desligar.bat", shell=True)
print(ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
    os.chdir('C:\\ATUAL')
    with open('Caixa9Lj03.txt', 'a') as caixa:
        caixa.write('Pdv não reiniciado\n')
        caixa.close()
else:
    print("Pdv reiniciado_Caixa 09")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.3.10 ""c:\\pdv\desligar.bat", shell=True)
print(ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
    os.chdir('C:\\ATUAL')
    with open('Caixa10Lj03.txt', 'a') as caixa:
        caixa.write('Pdv não reiniciado\n')
        caixa.close()
else:
    print("Pdv reiniciado_Caixa 10")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.3.11 ""c:\\pdv\desligar.bat", shell=True)
print(ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
    os.chdir('C:\\ATUAL')
    with open('Caixa11Lj03.txt', 'a') as caixa:
        caixa.write('Pdv não reiniciado\n')
        caixa.close()
else:
    print("Pdv reiniciado_Caixa 11")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.3.12 ""c:\\pdv\desligar.bat", shell=True)
print(ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
    os.chdir('C:\\ATUAL')
    with open('Caixa12Lj03.txt', 'a') as caixa:
        caixa.write('Pdv não reiniciado\n')
        caixa.close()
else:
    print("Pdv reiniciado_Caixa 12")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.3.13 ""c:\\pdv\desligar.bat", shell=True)
print(ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
    os.chdir('C:\\ATUAL')
    with open('Caixa13Lj03.txt', 'a') as caixa:
        caixa.write('Pdv não reiniciado\n')
        caixa.close()
else:
    print("Pdv reiniciado_Caixa 13")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.3.14 ""c:\\pdv\desligar.bat", shell=True)
print(ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
    os.chdir('C:\\ATUAL')
    with open('Caixa14Lj03.txt', 'a') as caixa:
        caixa.write('Pdv não reiniciado\n')
        caixa.close()
else:
    print("Pdv reiniciado_Caixa 14")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.3.15 ""c:\\pdv\desligar.bat", shell=True)
print(ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
    os.chdir('C:\\ATUAL')
    with open('Caixa15Lj03.txt', 'a') as caixa:
        caixa.write('Pdv não reiniciado\n')
        caixa.close()
else:
    print("Pdv reiniciado_Caixa 15")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.3.16 ""c:\\pdv\desligar.bat", shell=True)
print(ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
    os.chdir('C:\\ATUAL')
    with open('Caixa16Lj03.txt', 'a') as caixa:
        caixa.write('Pdv não reiniciado\n')
        caixa.close()
else:
    print("Pdv reiniciado_Caixa 16")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.3.17 ""c:\\pdv\desligar.bat", shell=True)
print(ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
    os.chdir('C:\\ATUAL')
    with open('Caixa17Lj03.txt', 'a') as caixa:
        caixa.write('Pdv não reiniciado\n')
        caixa.close()
else:
    print("Pdv reiniciado_Caixa 17")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.3.18 ""c:\\pdv\desligar.bat", shell=True)
print(ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
    os.chdir('C:\\ATUAL')
    with open('Caixa18Lj03.txt', 'a') as caixa:
        caixa.write('Pdv não reiniciado\n')
        caixa.close()
else:
    print("Pdv reiniciado_Caixa 18")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.3.19 ""c:\\pdv\desligar.bat", shell=True)
print(ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
    os.chdir('C:\\ATUAL')
    with open('Caixa19Lj03.txt', 'a') as caixa:
        caixa.write('Pdv não reiniciado\n')
        caixa.close()
else:
    print("Pdv reiniciado_Caixa 19")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.3.20 ""c:\\pdv\desligar.bat", shell=True)
print(ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
    os.chdir('C:\\ATUAL')
    with open('Caixa20Lj03.txt', 'a') as caixa:
        caixa.write('Pdv não reiniciado\n')
        caixa.close()
else:
    print("Pdv reiniciado_Caixa 20")

input ("Terminado, verificar na pasta ATUAL se existe caixas pendentes!!!")
