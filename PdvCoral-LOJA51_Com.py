#encoding: iso-8859-1

import os, shutil, subprocess, time, glob, copy, os.path, sys, socket, threading, rarfile, datetime, win32gui, win32con
from zipfile import ZipFile
from pathlib import Path
from datetime import datetime


try: import tkinter
except ImportError:
    import Tkinter as tkinter
    import ttk
else: from tkinter import ttk
from tkinter import *




class GUI_Core(object):

    def __init__(self):
        self.root = tkinter.Tk()
        self.style = ttk.Style()
        self.style.theme_use('classic')
        self.progbar = ttk.Progressbar(self.root)
        self.progbar.config(orient ="horizontal", style="red.Horizontal.TProgressbar", length = 500, mode='determinate')
        self.progbar.pack(side='bottom', fill='y', expand=True)
        self.progbar.start()
        self.secondary_thread = threading.Thread(target=pdv)
        self.secondary_thread.start()
        self.root.after(10, self.check_thread)
					

    def check_thread(self):
        if self.secondary_thread.is_alive():
            self.root.after(10, self.check_thread)
        else:
            self.progbar.stop()
            self.progbar.destroy()

						

def pdv():
	

		time.sleep(0.1)
		msg = Label(gui.root, text='Aguarde....', fg = "green", font= 'Arial 18')
		msg.pack()
		time.sleep(10)
		driveLetter = 'X:' 
		networkPath = '\\\\10.0.20.42\Atual' 
		user = 'compartilhar' 
		password = 'ruaf305'

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

				time.sleep(5)
				msg.pack_forget()
				msg = Label(gui.root, text="Sem conexão com o Servidor, enviando e-mail....", fg="red", font= 'Arial 18')
				msg.pack()

				with open('pdv.txt', 'a') as caixa:
					caixa.write(str("PDV e IP {} : {}".format(hostName,ipAddress)))
					caixa.close()

				time.sleep(5)
				msg.pack_forget()				
				msg = Label(gui.root, text='Aguarde....', fg = "red", font= 'Arial 18')
				msg.pack()

				
				os.startfile(r"enviando_email_i.exe")

				time.sleep(5)

				os.startfile(r"acertar_horario_i.exe")

				time.sleep(5)

				os.startfile(r"C:\\pdv\pdvsal.exe")

				time.sleep(5)

				msg.pack_forget()
				msg = Label(gui.root, text='Processos inicializados sem atualização!' + '\n' + 'Remarca verificar!', bg = "yellow", fg="red", font= 'Arial 18')
				msg.pack()


				sys.exit()

		msg.pack_forget()
		msg = Label(gui.root, text='Copiando arquivos para o PDV, aguarde....', fg="blue", font= 'Arial 18')
		msg.pack()

		PATHPDV='X://loja51_pdv.rar'
		PATHPLUGIN='X://loja51_plugin.rar'

		if os.path.isfile(PATHPDV):
			
			dest_dir = "C:\\PDV"
			for file in glob.glob(r'X:/loja51_pdv.rar'):
				print(file)
			shutil.copy(file, dest_dir)

		else:
			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Sem arquivos(PDV) para atualizar no Servidor", fg="blue", font= 'Arial 18')
			msg.pack()


		if os.path.isfile(PATHPLUGIN):
			
			dest_dir = "C:\\PDV\PLUGIN"
			for file in glob.glob(r'X:/loja51_plugin.rar'):
				print(file)
			shutil.copy(file, dest_dir)

		else:
			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Sem arquivos(PLUGIN) para atualizar no Servidor", fg="blue", font= 'Arial 18')
			msg.pack()


		winCMD = 'NET USE ' + driveLetter + ' /delete /y'
		print(winCMD)
		subprocess.call(winCMD, shell=True)

		if os.path.exists("C:/PDV/work"):
			current_directory = os.path.dirname(os.path.abspath(__file__))
			shutil.rmtree(current_directory + '/WORK/')
		else:
			pass

		PATHPDV='C://PDV/loja51_pdv.rar'
		PATHPLUGIN='C://PDV/PLUGIN/loja51_plugin.rar'

		if os.path.isfile(PATHPDV):

			msg.pack_forget()				
			msg = Label(gui.root, text='Aguarde....', fg = "blue", font= 'Arial 18')
			msg.pack()			

			try:
				for arquivo in os.listdir('c://pdv'):
				  x = arquivo
				  os.rename(x,x.lower())
			except OSError:
				pass

			pasta = 'c://pdv/ultimas_versoes_pdv'
			if os.path.isdir(pasta): 
				shutil.rmtree(pasta)
				os.mkdir(pasta)
			else:
				os.mkdir(pasta) 

			source = os.listdir("C://pdv")
			destination = 'C://pdv/ultimas_versoes_pdv'
			for files in source:
				if files.startswith("pdvsal.exe"):
					shutil.move(files,destination)

			source = os.listdir("C://pdv")
			destination = 'C://pdv/ultimas_versoes_pdv'
			for files in source:
				if files.startswith("satsal.dll"):
					shutil.move(files,destination)

			source = os.listdir("C://pdv")
			destination = 'C://pdv/ultimas_versoes_pdv'
			for files in source:
				if files.startswith("nfce.dll"):
					shutil.move(files,destination)

			source = os.listdir("C://pdv")
			destination = 'C://pdv/ultimas_versoes_pdv'
			for files in source:
				if files.startswith("nfe2ws4.exe"):
					shutil.move(files,destination)

			source = os.listdir("C://pdv")
			destination = 'C://pdv/ultimas_versoes_pdv'
			for files in source:
				if files.startswith("salcomm.exe"):
					shutil.move(files,destination)
					
			fonte = 'C://pdv/ultimas_versoes_pdv'
			destino = 'C://pdv'

			if sys.platform=='win32':
				os.system('xcopy "%s" "%s"' % (fonte, destino) + " /Y /M /S /E")
			else:
				shutil.copyfile(fonte, os.path.join(destino,'dir'))

			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Extraindo todos os arquivos do pdv agora...", fg="blue", font= 'Arial 18')
			msg.pack()
			
			os.chdir("C://pdv")

			file_pdv = "C:\\pdv\loja51_pdv.rar"
			def unrar(file):
				rf=rarfile.RarFile(file)
				rf.extractall('C:\\pdv')
			unrar(file_pdv)
 
			for raiz, diretorios, arquivos in os.walk('C:/PDV'):
				for arquivo in arquivos:
					if arquivo.endswith('loja51_pdv.rar'):
					   os.remove(os.path.join(raiz, arquivo))

		else:
			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Sem arquivos(PDV) para descompactar", fg="blue", font= 'Arial 18')
			msg.pack()

		if os.path.isfile(PATHPLUGIN):

			msg.pack_forget()				
			msg = Label(gui.root, text='Aguarde....', fg = "blue", font= 'Arial 18')
			msg.pack()

			os.chdir("c://pdv/plugin")

			try:
				for arquivo in os.listdir('c://pdv/plugin'):
				  x = arquivo
				  os.rename(x,x.lower())
			except OSError:
				pass

			pasta = 'c://pdv/ultimas_versoes_plugin'
			if os.path.isdir(pasta): 
				shutil.rmtree(pasta)
				os.mkdir(pasta)
			else:
				os.mkdir(pasta) 
				
			source = os.listdir("C://pdv/plugin")
			destination = 'C://pdv/ultimas_versoes_plugin'
			for files in source:
				if files.startswith("apromos.dll"):
					shutil.move(files,destination)
					
			source = os.listdir("C://pdv/plugin")
			destination = 'C://pdv/ultimas_versoes_plugin'
			for files in source:
				if files.startswith("clitef.dll"):
					shutil.move(files,destination)

			source = os.listdir("C://pdv/plugin")
			destination = 'C://pdv/ultimas_versoes_plugin'
			for files in source:
				if files.startswith("compcanc.dll"):
					shutil.move(files,destination)

			source = os.listdir("C://pdv/plugin")
			destination = 'C://pdv/ultimas_versoes_plugin'
			for files in source:
				if files.startswith("compfina.dll"):
					shutil.move(files,destination)

			source = os.listdir("C://pdv/plugin")
			destination = 'C://pdv/ultimas_versoes_plugin'
			for files in source:
				if files.startswith("prevenc.dll"):
					shutil.move(files,destination)

			source = os.listdir("C://pdv/plugin")
			destination = 'C://pdv/ultimas_versoes_plugin'
			for files in source:
				if files.startswith("estac.dll"):
					shutil.move(files,destination)

			source = os.listdir("C://pdv/plugin")
			destination = 'C://pdv/ultimas_versoes_plugin'
			for files in source:
				if files.startswith("frete.dll"):
					shutil.move(files,destination)



			fonte = 'C://pdv/ultimas_versoes_plugin'
			destino = 'C://pdv/plugin'

			if sys.platform=='win32':
				os.system('xcopy "%s" "%s"' % (fonte, destino) + " /Y /M /S /E")
			else:
				shutil.copyfile(fonte, os.path.join(destino,'dir'))
			
			os.chdir("C://pdv")

			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Extraindo todos os arquivos do plugin agora...", fg="blue", font= 'Arial 18')
			msg.pack()

			file_plugin = "C:\\pdv\plugin\loja51_plugin.rar"
			def unrar(file):
				rf=rarfile.RarFile(file)
				rf.extractall('C:\\pdv\plugin')
			unrar(file_plugin)

			for raiz, diretorios, arquivos in os.walk('C:/PDV'):
				for arquivo in arquivos:
					if arquivo.endswith('loja51_plugin.rar'):
					   os.remove(os.path.join(raiz, arquivo))

		else:
			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Sem arquivos(PLUGIN) para descompactar", fg="blue", font= 'Arial 18')
			msg.pack()

		os.chdir('C:\\PDV')

		msg.pack_forget()				
		msg = Label(gui.root, text='Aguarde....', fg = "blue", font= 'Arial 18')
		msg.pack()

		time.sleep(5)

		if os.path.exists("dllsat32bits.dll"):
			msg.pack_forget()
			msg = Label(gui.root, text='SAT Dimep, aguarde....', fg="blue", font= 'Arial 18')
			msg.pack()

			time.sleep(5)

			os.startfile(r"sat_dimep.exe")
		
		elif os.path.exists("satdll.dll"):
			msg.pack_forget()
			msg = Label(gui.root, text='SAT Sweda, aguarde....', fg="blue", font= 'Arial 18')
			msg.pack()

			time.sleep(5)
			
			os.startfile(r"sat_sweda.exe")
			
		elif os.path.exists("sat.dll"):
			msg.pack_forget()
			msg = Label(gui.root, text='SAT Jetway, aguarde....', fg="blue", font= 'Arial 18')
			msg.pack()

			time.sleep(5)
			
			os.startfile(r"sat_jet.exe")

		else:
			msg.pack_forget()
			msg = Label(gui.root, text='SAT Crt_ID, aguarde....', fg="blue", font= 'Arial 18')
			msg.pack()

			time.sleep(5)
			
			os.startfile(r"sat_id.exe")


		msg.pack_forget()
		msg = Label(gui.root, text='Aguarde....', fg="blue", font= 'Arial 18')
		msg.pack()

		time.sleep(5)

		os.startfile(r"agenda.exe")	

		msg.pack_forget()
		msg = Label(gui.root, text='Processos inicializados com sucesso!', fg="blue", font= 'Arial 18')
		msg.pack()

		time.sleep(5)

		os.startfile(r"ventanarf_central.exe")

		time.sleep(15)
		
		os.startfile(r"pdvsal.exe")
		
	
		def sair():
			gui.root.destroy()
			return

		gui.root.after(3000, sair)
		
	
gui = GUI_Core()
#gui.root.wm_iconbitmap('icon1.ico')
gui.root.title("REMARCA/NAGUMO - lj51/Comanda - 1.0")
gui.root.focus_force()
gui.root.mainloop()
