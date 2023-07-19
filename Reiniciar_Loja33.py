#encoding: iso-8859-1
import subprocess, os, sys

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.33.1 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa1Lj33.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 01")


ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.33.2 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa2Lj33.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 02")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.33.3 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa3Lj33.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 03")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.33.4 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa4Lj33.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 04")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.33.5 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa5Lj33.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 05")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.33.6 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa6Lj33.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 06")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.33.7 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa7Lj33.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 07")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.33.8 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa8Lj33.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 08")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.33.9 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa9Lj33.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 09")

ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.33.10 ""c:\\pdv\desligar.bat", shell=True)
print (ret)
if (ret == 2) or (ret == 53):
	os.chdir('C:\\ATUAL')
	with open('Caixa10Lj33.txt', 'a') as caixa:
		caixa.write('Pdv não reiniciado\n')
		caixa.close()
else:
	print("Pdv reiniciado_Caixa 10")



input ("Terminado, verificar na pasta ATUAL se existe caixas pendentes!!!")