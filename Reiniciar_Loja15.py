#encoding: iso-8859-1
import subprocess, os, sys

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.15.1 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa1Lj15.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 01")


ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.15.2 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa2Lj15.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 02")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.15.3 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa3Lj15.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 03")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.15.4 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa4Lj15.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 04")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.15.5 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa5Lj15.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 05")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.15.6 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa6Lj15.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 06")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.15.7 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa7Lj15.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 07")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.15.8 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa8Lj15.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 08")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.15.9 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa9Lj15.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 09")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.15.10 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa10Lj15.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 10")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.15.11 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa11Lj15.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 11")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.15.12 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa12Lj15.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 12")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.15.13 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa13Lj15.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 13")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.15.14 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa14Lj15.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 14")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.15.15 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa15Lj15.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 15")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.15.16 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa16Lj15.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 16")


ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.15.17 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa17Lj15.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 17")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.15.18 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa18Lj15.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 18")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.15.19 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa19Lj15.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 19")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.15.20 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa20Lj15.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 20")



input ("Terminado, verificar na pasta ATUAL se existe caixas pendentes!!!")