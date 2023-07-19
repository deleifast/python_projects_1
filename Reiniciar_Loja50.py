#encoding: iso-8859-1
import subprocess, os, sys

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.1 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa1Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 01")


ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.2 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa2Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 02")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.3 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa3Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 03")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.4 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa4Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 04")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.5 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa5Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 05")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.6 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa6Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 06")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.7 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa7Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 07")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.8 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa8Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 08")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.9 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa9Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 09")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.10 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa10Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 10")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.11 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa11Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 11")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.12 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa12Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 12")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.13 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa13Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 13")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.14 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa14Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 14")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.15 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa15Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 15")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.16 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa16Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 16")


ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.17 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa17Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 17")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.18 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa18Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 18")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.19 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa19Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 19")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.20 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa20Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 20")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.21 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa21Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 21")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.22 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa22Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 22")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.23 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa23Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 23")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.24 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa24Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 24")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.25 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa25Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 25")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.26 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa26Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 26")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.50.27 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa27Lj50.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 27")


input ("Terminado, verificar na pasta ATUAL se existe caixas pendentes!!!")
