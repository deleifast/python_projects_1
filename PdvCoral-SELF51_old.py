#encoding: iso-8859-1
import os, shutil, subprocess, time, glob, copy, os.path, sys, socket, threading, rarfile, datetime
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
        self.secondary_thread = threading.Thread(target=pdv)
        self.secondary_thread.start()
        self.root.after(10, self.check_thread)
        self.msg = Label(self.root, text='REMARCA/NAGUMO - Versão 3.0S - Lj51', fg="red", font='Arial 8')
        self.msg.pack(anchor=SE)

    def check_thread(self):
        if self.secondary_thread.is_alive():
            self.root.after(10, self.check_thread)
        else:
            self.root.destroy()

						

def pdv():
		time.sleep(0.1)		
		msg = Label(gui.root, text='Aguarde, iniciando SELF-PDV....', fg = "green", font= 'Arial 50')
		msg.pack(fill=BOTH, anchor=N, expand=True)
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

				msg.pack_forget()
				msg = Label(gui.root, text="Sem conexão com o servidor....", fg="red", font= 'Arial 45')
				msg.pack(fill=BOTH, anchor=N, expand=True)	
				time.sleep(5)

				with open('pdv.txt', 'a') as caixa:
					caixa.write(str("PDV e IP {} : {}".format(hostName,ipAddress)))
					caixa.close()

				msg.pack_forget()				
				msg = Label(gui.root, text='Aguarde....', fg = "red", font= 'Arial 50')
				msg.pack(fill=BOTH, anchor=N, expand=True)	
				time.sleep(5)

				msg.pack_forget()
				msg = Label(gui.root, text='Processos inicializados sem atualização!' + '\n' + 'Remarca verificar!', bg = "yellow", fg="red", font= 'Arial 45')
				msg.pack(fill=BOTH, anchor=N, expand=True)	
				time.sleep(20)
				
				os.startfile(r"C:\\pdv\pdvsal.exe")

				sys.exit()

		msg.pack_forget()
		msg = Label(gui.root, text='Copiando arquivos para o PDV' + "\n" + 'Aguarde....', fg="blue", font= 'Arial 45')
		msg.pack(fill=BOTH, anchor=N, expand=True)	
		time.sleep(5)


		PATHPDV='X://loja51s_pdv.rar'
		PATHPLUGIN='X://loja51s_plugin.rar'

		if os.path.isfile(PATHPDV):
			
			dest_dir = "C:\\PDV"
			for file in glob.glob(r'X:/loja51s_pdv.rar'):
				print(file)
			shutil.copy(file, dest_dir)

		else:
			msg.pack_forget()
			msg = Label(gui.root, text="Sem arquivos(PDV) para atualizar no servidor" + '\n' + "Aguarde...", fg="blue", font= 'Arial 35')
			msg.pack(fill=BOTH, anchor=N, expand=True)	
			time.sleep(5)

		if os.path.isfile(PATHPLUGIN):
			
			dest_dir = "C:\\PDV\PLUGIN"
			for file in glob.glob(r'X:/loja51s_plugin.rar'):
				print(file)
			shutil.copy(file, dest_dir)

		else:
			msg.pack_forget()
			msg = Label(gui.root, text="Sem arquivos(PLUGIN) para atualizar no servidor" + '\n' + "Aguarde...", fg="blue", font= 'Arial 30')
			msg.pack(fill=BOTH, anchor=N, expand=True)	
			time.sleep(5)
			
		winCMD = 'NET USE ' + driveLetter + ' /delete /y'
		print(winCMD)
		subprocess.call(winCMD, shell=True)

		if os.path.exists("C:/PDV/work"):
			current_directory = os.path.dirname(os.path.abspath(__file__))
			shutil.rmtree(current_directory + '/WORK/')
		else:
			pass

		PATHPDV='C://PDV/loja51s_pdv.rar'
		PATHPLUGIN='C://PDV/PLUGIN/loja51s_plugin.rar'

		if os.path.isfile(PATHPDV):

			msg.pack_forget()				
			msg = Label(gui.root, text='Aguarde....', fg = "blue", font= 'Arial 45')
			msg.pack(fill=BOTH, anchor=N, expand=True)	
			time.sleep(5)
			
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


			msg.pack_forget()
			msg = Label(gui.root, text="Extraindo todos os arquivos do pdv agora...", fg="blue", font= 'Arial 35')
			msg.pack(fill=BOTH, anchor=N, expand=True)	
			time.sleep(5)
						
			os.chdir("C://pdv")

			file_pdv = "C:\\pdv\loja51s_pdv.rar"
			def unrar(file):
				rf=rarfile.RarFile(file)
				rf.extractall('C:\\pdv')
			unrar(file_pdv)
 
			for raiz, diretorios, arquivos in os.walk('C:/PDV'):
				for arquivo in arquivos:
					if arquivo.endswith('loja51s_pdv.rar'):
					   os.remove(os.path.join(raiz, arquivo))

		else:

			msg.pack_forget()
			msg = Label(gui.root, text="Sem arquivos(PDV) para descompactar" + "\n" + "Aguarde...", fg="blue", font= 'Arial 40')
			msg.pack(fill=BOTH, anchor=N, expand=True)	
			time.sleep(5)
			
		if os.path.isfile(PATHPLUGIN):

			msg.pack_forget()				
			msg = Label(gui.root, text='Aguarde....', fg = "blue", font= 'Arial 45')
			msg.pack(fill=BOTH, anchor=N, expand=True)	
			time.sleep(5)
			
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
	
			msg.pack_forget()
			msg = Label(gui.root, text="Extraindo todos os arquivos do plugin agora...", fg="blue", font= 'Arial 35')
			msg.pack(fill=BOTH, anchor=N, expand=True)		
			time.sleep(5)
				
			os.chdir("C://pdv/")

			file_plugin = "C:\\pdv\plugin\loja51s_plugin.rar"
			def unrar(file):
				rf=rarfile.RarFile(file)
				rf.extractall('C:\\pdv\plugin')
			unrar(file_plugin)

			for raiz, diretorios, arquivos in os.walk('C:/PDV'):
				for arquivo in arquivos:
					if arquivo.endswith('loja51s_plugin.rar'):
					   os.remove(os.path.join(raiz, arquivo))
		 
		else:
			msg.pack_forget()
			msg = Label(gui.root, text="Sem arquivos(PLUGIN) para descompactar" + "\n" + "Aguarde...", fg="blue", font= 'Arial 35')
			msg.pack(fill=BOTH, anchor=N, expand=True)	
			time.sleep(5)
			
		os.chdir('C:\\PDV')

		msg.pack_forget()
		msg = Label(gui.root, text='Processos inicializados com sucesso!' + '\n' + 'Aguarde....', fg="blue", font= 'Arial 45')
		msg.pack(fill=BOTH, anchor=N, expand=True)	
		time.sleep(5)

		os.startfile(r"pdvsal.exe")
		

		def sair():
			gui.root.destroy()
			return

		gui.root.after(3000, sair)
		

gui = GUI_Core()
gui.root.attributes('-fullscreen',True)
gui.root.mainloop()
