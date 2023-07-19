#encoding: iso-8859-1
import subprocess, os, sys

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.12.1 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa1Lj12.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 01")


ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.12.2 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa2Lj12.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 02")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.12.3 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa3Lj12.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 03")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.12.4 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa4Lj12.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 04")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.12.5 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa5Lj12.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 05")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.12.6 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa6Lj12.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 06")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.12.7 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa7Lj12.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 07")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.12.8 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa8Lj12.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 08")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.12.9 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa9Lj12.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 09")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.12.10 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa10Lj12.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 10")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.12.11 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa11Lj12.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 11")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.12.12 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa12Lj12.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 12")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.12.13 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa13Lj12.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 13")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.12.14 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa14Lj12.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 14")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.12.15 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa15Lj12.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 15")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.12.16 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa16Lj12.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 16")


ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.12.17 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa17Lj12.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 17")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.12.18 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa18Lj12.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 18")



input ("Terminado, verificar na pasta ATUAL se existe caixas pendentes!!!")