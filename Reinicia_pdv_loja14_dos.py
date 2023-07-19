#encoding: iso-8859-1
import os, shutil, subprocess, time, glob, sys, os.path

caixa = input("LOJA14" " Pdv - 1 ate 15 - Digite o número do pdv sem o zero: ")
modo = input("Digite 0 - somente se o pdv estiver na tela do Windows!!""Atenção""!!!\nDigite 1 para reiniciar: ")

if caixa == "1":
	if modo == "0":
		ret = os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.1 ""c:\\pdv\pdvcoral.exe")
		if ret == 53:
			print("Pdv desconectado da rede, favor verificar!!!!")
			sys.exit(1)
		elif ret ==1326:
			print("Pdv desconectado da rede, favor verificar!!!!")	
			sys.exit(1)
		else:
			time.sleep(5)
			print("Pdv iniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
	if modo == "1":
		ret = os.system("taskkill /s 192.168.141.1 /u PDV /p pdv /im PDVSAL.EXE")
		if ret == 0:
			os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.1 ""c:\\pdv\pdvcoral.exe")
			time.sleep(5)
			print("Pdv reiniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
		else:
			print("Pdv desconectado ou sistema na tela do Windows, verficar!!!")
			sys.exit(1)

if caixa == "2":
	if modo == "0":
		ret = os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.2 ""c:\\pdv\pdvcoral.exe")
		if ret == 53:
			print("Pdv desconectado da rede, favor verificar!!!!")
			sys.exit(1)
		elif ret ==1326:
			print("Pdv desconectado da rede, favor verificar!!!!")	
			sys.exit(1)
		else:
			time.sleep(5)
			print("Pdv iniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
	if modo == "1":
		ret = os.system("taskkill /s 192.168.141.2 /u PDV /p pdv /im PDVSAL.EXE")
		if ret == 0:
			os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.2 ""c:\\pdv\pdvcoral.exe")
			time.sleep(5)
			print("Pdv reiniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
		else:
			print("Pdv desconectado ou sistema na tela do Windows, verficar!!!")
			sys.exit(1)

if caixa == "3":
	if modo == "0":
		ret = os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.3 ""c:\\pdv\pdvcoral.exe")
		if ret == 53:
			print("Pdv desconectado da rede, favor verificar!!!!")
			sys.exit(1)
		elif ret ==1326:
			print("Pdv desconectado da rede, favor verificar!!!!")	
			sys.exit(1)
		else:
			time.sleep(5)
			print("Pdv iniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
	if modo == "1":
		ret = os.system("taskkill /s 192.168.141.3 /u PDV /p pdv /im PDVSAL.EXE")
		if ret == 0:
			os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.3 ""c:\\pdv\pdvcoral.exe")
			time.sleep(5)
			print("Pdv reiniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
		else:
			print("Pdv desconectado ou sistema na tela do Windows, verficar!!!")
			sys.exit(1)

if caixa == "4":
	if modo == "0":
		ret = os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.4 ""c:\\pdv\pdvcoral.exe")
		if ret == 53:
			print("Pdv desconectado da rede, favor verificar!!!!")
			sys.exit(1)
		elif ret ==1326:
			print("Pdv desconectado da rede, favor verificar!!!!")	
			sys.exit(1)
		else:
			time.sleep(5)
			print("Pdv iniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
	if modo == "1":
		ret = os.system("taskkill /s 192.168.141.4 /u PDV /p pdv /im PDVSAL.EXE")
		if ret == 0:
			os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.4 ""c:\\pdv\pdvcoral.exe")
			time.sleep(5)
			print("Pdv reiniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
		else:
			print("Pdv desconectado ou sistema na tela do Windows, verficar!!!")
			sys.exit(1)

if caixa == "5":
	if modo == "0":
		print("FAVOR USAR O VNC, CAIXA COM WINDOWS XP!!!")
		sys.exit(1)
		'''os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.5 ""c:\\pdv\pdvcoral.exe")
		time.sleep(5)
		print("Pdv iniciado com sucesso!!")
		input("PRESSIONE ENTRA PARA TERMINAR")
		sys.exit(1)'''
	if modo == "1":
		print("FAVOR USAR O VNC, CAIXA COM WINDOWS XP!!!")
		sys.exit(1)
		'''ret = os.system("taskkill /s 192.168.141.5 /u PDV /p pdv /im PDVSAL.EXE")
		if ret == 0:
			os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.5 ""c:\\pdv\pdvcoral.exe")
			time.sleep(5)
			print("Pdv reiniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
		else:
			print("Pdv desconectado ou sistema na tela do Windows, verficar!!!")
			sys.exit(1)'''

if caixa == "6":
	if modo == "0":
		print("FAVOR USAR O VNC, CAIXA COM WINDOWS XP!!!")
		sys.exit(1)
		'''os.system("psexec.exe -d -i -u PDV -p pdv \\\\192.168.141.6 ""c:\\pdv\pdvcoral.exe")
		time.sleep(5)
		print("Pdv iniciado com sucesso!!")
		input("PRESSIONE ENTRA PARA TERMINAR")
		sys.exit(1)'''
	if modo == "1":
		print("FAVOR USAR O VNC, CAIXA COM WINDOWS XP!!!")
		sys.exit(1)
		'''ret = os.system("taskkill /s 192.168.141.6 /u PDV /p pdv /im PDVSAL.EXE")
		if ret == 0:
			os.system("psexec.exe -d -i -u PDV -p pdv \\\\192.168.141.6 ""c:\\pdv\pdvcoral.exe")
			time.sleep(5)
			print("Pdv reiniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
		else:
			print("Pdv desconectado ou sistema na tela do Windows, verficar!!!")
			sys.exit(1)'''

if caixa == "7":
	if modo == "0":
		ret = os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.7 ""c:\\pdv\pdvcoral.exe")
		if ret == 53:
			print("Pdv desconectado da rede, favor verificar!!!!")
			sys.exit(1)
		elif ret ==1326:
			print("Pdv desconectado da rede, favor verificar!!!!")	
			sys.exit(1)
		else:
			time.sleep(5)
			print("Pdv iniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
	if modo == "1":
		ret = os.system("taskkill /s 192.168.141.7 /u PDV /p pdv /im PDVSAL.EXE")
		if ret == 0:
			os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.7 ""c:\\pdv\pdvcoral.exe")
			time.sleep(5)
			print("Pdv reiniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
		else:
			print("Pdv desconectado ou sistema na tela do Windows, verficar!!!")
			sys.exit(1)

if caixa == "8":
	if modo == "0":
		ret = os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.8 ""c:\\pdv\pdvcoral.exe")
		if ret == 53:
			print("Pdv desconectado da rede, favor verificar!!!!")
			sys.exit(1)
		elif ret ==1326:
			print("Pdv desconectado da rede, favor verificar!!!!")	
			sys.exit(1)
		else:
			time.sleep(5)
			print("Pdv iniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
	if modo == "1":
		ret = os.system("taskkill /s 192.168.141.8 /u PDV /p pdv /im PDVSAL.EXE")
		if ret == 0:
			os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.8 ""c:\\pdv\pdvcoral.exe")
			time.sleep(5)
			print("Pdv reiniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
		else:
			print("Pdv desconectado ou sistema na tela do Windows, verficar!!!")
			sys.exit(1)

if caixa == "9":
	if modo == "0":
		ret = os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.9 ""c:\\pdv\pdvcoral.exe")
		if ret == 53:
			print("Pdv desconectado da rede, favor verificar!!!!")
			sys.exit(1)
		elif ret ==1326:
			print("Pdv desconectado da rede, favor verificar!!!!")	
			sys.exit(1)
		else:
			time.sleep(5)
			print("Pdv iniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
	if modo == "1":
		ret = os.system("taskkill /s 192.168.141.9 /u PDV /p pdv /im PDVSAL.EXE")
		if ret == 0:
			os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.9 ""c:\\pdv\pdvcoral.exe")
			time.sleep(5)
			print("Pdv reiniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
		else:
			print("Pdv desconectado ou sistema na tela do Windows, verficar!!!")
			sys.exit(1)

if caixa == "10":
	if modo == "0":
		ret = os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.10 ""c:\\pdv\pdvcoral.exe")
		if ret == 53:
			print("Pdv desconectado da rede, favor verificar!!!!")
			sys.exit(1)
		elif ret ==1326:
			print("Pdv desconectado da rede, favor verificar!!!!")	
			sys.exit(1)
		else:
			time.sleep(5)
			print("Pdv iniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
	if modo == "1":
		ret = os.system("taskkill /s 192.168.141.10 /u PDV /p pdv /im PDVSAL.EXE")
		if ret == 0:
			os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.10 ""c:\\pdv\pdvcoral.exe")
			time.sleep(5)
			print("Pdv reiniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
		else:
			print("Pdv desconectado ou sistema na tela do Windows, verficar!!!")
			sys.exit(1)

if caixa == "11":
	if modo == "0":
		ret = os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.11 ""c:\\pdv\pdvcoral.exe")
		if ret == 53:
			print("Pdv desconectado da rede, favor verificar!!!!")
			sys.exit(1)
		elif ret ==1326:
			print("Pdv desconectado da rede, favor verificar!!!!")	
			sys.exit(1)
		else:
			time.sleep(5)
			print("Pdv iniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
	if modo == "1":
		ret = os.system("taskkill /s 192.168.141.11 /u PDV /p pdv /im PDVSAL.EXE")
		if ret == 0:
			os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.11 ""c:\\pdv\pdvcoral.exe")
			time.sleep(5)
			print("Pdv reiniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
		else:
			print("Pdv desconectado ou sistema na tela do Windows, verficar!!!")
			sys.exit(1)

if caixa == "12":
	if modo == "0":
		ret = os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.12 ""c:\\pdv\pdvcoral.exe")
		if ret == 53:
			print("Pdv desconectado da rede, favor verificar!!!!")
			sys.exit(1)
		elif ret ==1326:
			print("Pdv desconectado da rede, favor verificar!!!!")	
			sys.exit(1)
		else:
			time.sleep(5)
			print("Pdv iniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
	if modo == "1":
		ret = os.system("taskkill /s 192.168.141.12 /u PDV /p pdv /im PDVSAL.EXE")
		if ret == 0:
			os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.12 ""c:\\pdv\pdvcoral.exe")
			time.sleep(5)
			print("Pdv reiniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
		else:
			print("Pdv desconectado ou sistema na tela do Windows, verficar!!!")
			sys.exit(1)

if caixa == "13":
	if modo == "0":
		ret = os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.13 ""c:\\pdv\pdvcoral.exe")
		if ret == 53:
			print("Pdv desconectado da rede, favor verificar!!!!")
			sys.exit(1)
		elif ret ==1326:
			print("Pdv desconectado da rede, favor verificar!!!!")	
			sys.exit(1)
		else:
			time.sleep(5)
			print("Pdv iniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
	if modo == "1":
		ret = os.system("taskkill /s 192.168.141.13 /u PDV /p pdv /im PDVSAL.EXE")
		if ret == 0:
			os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.13 ""c:\\pdv\pdvcoral.exe")
			time.sleep(5)
			print("Pdv reiniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
		else:
			print("Pdv desconectado ou sistema na tela do Windows, verficar!!!")
			sys.exit(1)

if caixa == "14":
	if modo == "0":
		ret = os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.14 ""c:\\pdv\pdvcoral.exe")
		if ret == 53:
			print("Pdv desconectado da rede, favor verificar!!!!")
			sys.exit(1)
		elif ret ==1326:
			print("Pdv desconectado da rede, favor verificar!!!!")	
			sys.exit(1)
		else:
			time.sleep(5)
			print("Pdv iniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
	if modo == "1":
		ret = os.system("taskkill /s 192.168.141.14 /u PDV /p pdv /im PDVSAL.EXE")
		if ret == 0:
			os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.14 ""c:\\pdv\pdvcoral.exe")
			time.sleep(5)
			print("Pdv reiniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
		else:
			print("Pdv desconectado ou sistema na tela do Windows, verficar!!!")
			sys.exit(1)

if caixa == "15":
	if modo == "0":
		ret = os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.15 ""c:\\pdv\pdvcoral.exe")
		if ret == 53:
			print("Pdv desconectado da rede, favor verificar!!!!")
			sys.exit(1)
		elif ret ==1326:
			print("Pdv desconectado da rede, favor verificar!!!!")	
			sys.exit(1)
		else:
			time.sleep(5)
			print("Pdv iniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
	if modo == "1":
		ret = os.system("taskkill /s 192.168.141.15 /u PDV /p pdv /im PDVSAL.EXE")
		if ret == 0:
			os.system("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.15 ""c:\\pdv\pdvcoral.exe")
			time.sleep(5)
			print("Pdv reiniciado com sucesso!!")
			input("PRESSIONE ENTRA PARA TERMINAR")
			sys.exit(1)
		else:
			print("Pdv desconectado ou sistema na tela do Windows, verficar!!!")
			sys.exit(1)
else:
	print("Número de pdv inválido!!!")
	sys.exit(1)
