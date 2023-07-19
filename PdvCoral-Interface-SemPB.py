#encoding: iso-8859-1
import os, shutil, subprocess, time, glob, copy, os.path, sys, socket, threading
from zipfile import ZipFile

import tkinter.ttk
from tkinter import *

gui = Tk()

gui.geometry('410x100')
gui.title('Pdvcoral - Remarca')
gui.resizable(0,0)

msg = Label(gui, text='Aguarde, iniciando serviços do Pdv...', fg="red", font='Arial 18')
msg.place(x=1, y=1)

pb = tkinter.ttk.Progressbar(gui,orient ="horizontal",length = 400, mode ="determinate")
pb.place(x=1, y=40)
pb.start()

def stop_pb():

		# initialize
		driveLetter = 'X:' 
		networkPath = '\\\\10.0.20.42\Atual' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)
		print (exitcode)

		if exitcode == 0:
			print(winCMD)

		else:
				exitcode == 2

				os.chdir('C:\\PDV')

				path = 'C:\\PDV'
				dir = os.listdir(path)
				for file in dir:
					if file == "pdv.txt":
						os.remove(file)

				hostName    = ""

				ipAddress   = socket.gethostbyname_ex(socket.gethostname())

				print("PDV e IP {} : {}".format(hostName,ipAddress))

				with open('pdv.txt', 'a') as caixa:
					caixa.write(str("PDV e IP {} : {}".format(hostName,ipAddress)))
					caixa.close()

				
				os.startfile(r"Enviando_Email_i.exe")

				time.sleep(10)

				os.startfile(r"Acertar_horario_i.exe")

				time.sleep(10)

				os.startfile(r"c:\\pdv\pdvsal.exe")




		print('Copiando arquivos para o PDV e SAT sendo iniciado, aguarde....' + '\n')	


		PATHPDV='X://PDV.ZIP'
		PATHPLUGIN='X://PLUGIN.ZIP'

		if os.path.isfile(PATHPDV):
			
			dest_dir = "C:\\PDV"
			for file in glob.glob(r'X:/PDV.ZIP'):
				print(file)
			shutil.copy(file, dest_dir)

		else:
			print("Sem arquivos(PDV) para atualizar no Servidor" + "\n")

		if os.path.isfile(PATHPLUGIN):
			
			dest_dir = "C:\\PDV\PLUGIN"
			for file in glob.glob(r'X:/PLUGIN.ZIP'):
				print(file)
			shutil.copy(file, dest_dir)

		else:
			print("Sem arquivos(PLUGIN) para atualizar no Servidor" + "\n")

		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete /y'
		print(winCMD)
		subprocess.call(winCMD, shell=True)

		PATHPDV='C://PDV/PDV.ZIP'
		PATHPLUGIN='C://PDV/PLUGIN/PLUGIN.ZIP'

		if os.path.isfile(PATHPDV):

		# specifying the zip file name
			file_pdv = "c:\\pdv\pdv.zip"
		 
		# opening the zip file in READ mode
			with ZipFile(file_pdv, 'r') as zip:
			# printing all the contents of the zip file
				zip.printdir()
		 
			# extracting all the files
				print('Extraindo todos os arquivos agora...')
				zip.extractall('c:\\pdv')
				print('Pronto pdv!' + '\n')
		else:
			print("Sem arquivos(PDV) para descompactar" + "\n")

		if os.path.isfile(PATHPLUGIN):

		# specifying the zip file name
			file_plugin = "c:\\pdv\plugin\plugin.zip"
		 
		# opening the zip file in READ mode
			with ZipFile(file_plugin, 'r') as zip:
			# printing all the contents of the zip file
				zip.printdir()
		 
			# extracting all the files
				print('Extraindo todos os arquivos agora...')
				zip.extractall('c:\\pdv\plugin')
				print('Pronto plugin!' + '\n')

		else:
			print("Sem arquivos(PLUGIN) para descompactar" + "\n")	


		os.chdir('C:\\PDV')

		os.startfile(r"Acertar_horario_i.exe")

		time.sleep(10)

		os.startfile(r"pdvsal.exe")

		time.sleep(10)
		
		pb.stop()
		
		sys.exit()


pb.after(5000,stop_pb)


gui.mainloop()