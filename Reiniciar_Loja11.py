#encoding: iso-8859-1
import subprocess, os, sys

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.1 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa1Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 01")


ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.2 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa2Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 02")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.3 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa3Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 03")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.4 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa4Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 04")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.5 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa5Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 05")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.6 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa6Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 06")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.7 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa7Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 07")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.8 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa8Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 08")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.9 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa9Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 09")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.10 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa10Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 10")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.11 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa11Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 11")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.12 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa12Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 12")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.13 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa13Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 13")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.14 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa14Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 14")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.15 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa15Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 15")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.16 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa16Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 16")


ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.17 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa17Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 17")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.18 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa18Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 18")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.19 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa19Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 19")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.20 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa20Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 20")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.21 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa21Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 21")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.22 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa22Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 22")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.23 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa23Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 23")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.24 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa24Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 24")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.25 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa25Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 25")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.26 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa26Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 26")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.27 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa27Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 27")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.28 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa28Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 28")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.29 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa29Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 29")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.30 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa30Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 30")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.11.31 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53) or (ret == 1326) or (ret == 2250):
	os.chdir('C:\\ATUAL')
	with open('Caixa31Lj11.txt', 'a') as caixa:
		caixa.write('Pdv n�o reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 31")



input ("Terminado, verificar na pasta ATUAL se existe caixas pendentes!!!")