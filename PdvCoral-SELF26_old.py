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
        self.msg = Label(self.root, text='REMARCA/NAGUMO - Versão 2.2S - Lj26', fg="red", font='Arial 8')
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
		time.sleep(30)
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

				time.sleep(5)
				msg.pack_forget()
				msg = Label(gui.root, text="Sem conexão com o servidor, enviando e-mail....", fg="red", font= 'Arial 45')
				msg.pack(fill=BOTH, anchor=N, expand=True)	

				with open('pdv.txt', 'a') as caixa:
					caixa.write(str("PDV e IP {} : {}".format(hostName,ipAddress)))
					caixa.close()

				time.sleep(5)
				msg.pack_forget()				
				msg = Label(gui.root, text='Aguarde....', fg = "red", font= 'Arial 50')
				msg.pack(fill=BOTH, anchor=N, expand=True)	

				
				os.startfile(r"Enviando_Email_i.exe")

				time.sleep(10)

				os.startfile(r"Acertar_horario_i.exe")

				time.sleep(10)

				os.startfile(r"C:\\pdv\pdvsal.exe")

				time.sleep(10)

				msg.pack_forget()
				msg = Label(gui.root, text='Processos inicializados sem atualização!' + '\n' + 'Remarca verificar!', bg = "yellow", fg="red", font= 'Arial 45')
				msg.pack(fill=BOTH, anchor=N, expand=True)	


				sys.exit()

		msg.pack_forget()
		msg = Label(gui.root, text='Copiando arquivos para o PDV' + "\n" + 'Aguarde....', fg="blue", font= 'Arial 45')
		msg.pack(fill=BOTH, anchor=N, expand=True)	



		PATHPDV='X://loja26s_pdv.rar'
		PATHPLUGIN='X://loja26s_plugin.rar'

		if os.path.isfile(PATHPDV):
			
			dest_dir = "C:\\PDV"
			for file in glob.glob(r'X:/loja26s_pdv.rar'):
				print(file)
			shutil.copy(file, dest_dir)

		else:
			time.sleep(10)
			msg.pack_forget()
			msg = Label(gui.root, text="Sem arquivos(PDV) para atualizar no servidor" + '\n' + "Aguarde...", fg="blue", font= 'Arial 35')
			msg.pack(fill=BOTH, anchor=N, expand=True)	


		if os.path.isfile(PATHPLUGIN):
			
			dest_dir = "C:\\PDV\PLUGIN"
			for file in glob.glob(r'X:/loja26s_plugin.rar'):
				print(file)
			shutil.copy(file, dest_dir)

		else:
			time.sleep(10)
			msg.pack_forget()
			msg = Label(gui.root, text="Sem arquivos(PLUGIN) para atualizar no servidor" + '\n' + "Aguarde...", fg="blue", font= 'Arial 30')
			msg.pack(fill=BOTH, anchor=N, expand=True)	

		winCMD = 'NET USE ' + driveLetter + ' /delete /y'
		print(winCMD)
		subprocess.call(winCMD, shell=True)

		PATHPDV='C://PDV/loja26s_pdv.rar'
		PATHPLUGIN='C://PDV/PLUGIN/loja26s_plugin.rar'

		if os.path.isfile(PATHPDV):
			
			t = datetime.now().strftime("%d-%m-%Y %H:%M:%S").replace(":","_")
			d = './versões_anteriores_'+(t)
			os.makedirs(d)


			source = os.listdir("C://pdv")
			destination = 'C://pdv/versões_anteriores_'+(t)
			for files in source:
				if files.startswith("PDVSAL.EXE"):
					shutil.move(files,destination)

			source = os.listdir("C://pdv")
			destination = 'C://pdv/versões_anteriores_'+(t)
			for files in source:
				if files.startswith("satsal.dll"):
					shutil.move(files,destination)

			source = os.listdir("C://pdv")
			destination = 'C://pdv/versões_anteriores_'+(t)
			for files in source:
				if files.startswith("NFCe.dll"):
					shutil.move(files,destination)

			source = os.listdir("C://pdv")
			destination = 'C://pdv/versões_anteriores_'+(t)
			for files in source:
				if files.startswith("NFE2WS4.EXE"):
					shutil.move(files,destination)

			source = os.listdir("C://pdv")
			destination = 'C://pdv/versões_anteriores_'+(t)
			for files in source:
				if files.startswith("npromo.mdb"):
					shutil.move(files,destination)

			source = os.listdir("C://pdv")
			destination = 'C://pdv/versões_anteriores_'+(t)
			for files in source:
				if files.startswith("Salcomm.exe"):
					shutil.move(files,destination)
					
			fonte = 'C://pdv/versões_anteriores_'+(t)
			destino = 'C://pdv'

			if sys.platform=='win32':
				os.system('xcopy "%s" "%s"' % (fonte, destino) + " /Y /M /S /E")
			else:
				shutil.copyfile(fonte, os.path.join(destino,'dir'))

			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Extraindo todos os arquivos do pdv agora" + "\n" + "Aguarde...", fg="blue", font= 'Arial 35')
			msg.pack(fill=BOTH, anchor=N, expand=True)	
			
			os.chdir("C://pdv")

			file_pdv = "C:\\pdv\loja26s_pdv.rar"
			def unrar(file):
				rf=rarfile.RarFile(file)
				rf.extractall('C:\\pdv')
			unrar(file_pdv)
 

			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Pdv OK, aguarde...", fg="blue", font= 'Arial 50')
			msg.pack(fill=BOTH, anchor=N, expand=True)	

		else:
			time.sleep(10)
			msg.pack_forget()
			msg = Label(gui.root, text="Sem arquivos(PDV) para descompactar" + "\n" + "Aguarde...", fg="blue", font= 'Arial 40')
			msg.pack(fill=BOTH, anchor=N, expand=True)	

		if os.path.isfile(PATHPLUGIN):
			
			os.chdir("C://pdv/plugin")

			source = os.listdir("C://pdv/plugin")
			destination = 'C://pdv/versões_anteriores_'+(t)
			for files in source:
				if files.startswith("apromos.dll"):
					shutil.move(files,destination)

			source = os.listdir("C://pdv/plugin")
			destination = 'C://pdv/versões_anteriores_'+(t)
			for files in source:
				if files.startswith("Clitef.dll"):
					shutil.move(files,destination)

			source = os.listdir("C://pdv/plugin")
			destination = 'C://pdv/versões_anteriores_'+(t)
			for files in source:
				if files.startswith("CompCanc.dll"):
					shutil.move(files,destination)

			source = os.listdir("C://pdv/plugin")
			destination = 'C://pdv/versões_anteriores_'+(t)
			for files in source:
				if files.startswith("CompFina.dll"):
					shutil.move(files,destination)

			source = os.listdir("C://pdv/plugin")
			destination = 'C://pdv/versões_anteriores_'+(t)
			for files in source:
				if files.startswith("PreVenc.dll"):
					shutil.move(files,destination)

			source = os.listdir("C://pdv/plugin")
			destination = 'C://pdv/versões_anteriores_'+(t)
			for files in source:
				if files.startswith("estac.dll"):
					shutil.move(files,destination)

			source = os.listdir("C://pdv/plugin")
			destination = 'C://pdv/versões_anteriores_'+(t)
			for files in source:
				if files.startswith("Frete.dll"):
					shutil.move(files,destination)
					
			fonte = 'C://pdv/versões_anteriores_'+(t)
			destino = 'C://pdv/plugin'

			if sys.platform=='win32':
				os.system('xcopy "%s" "%s"' % (fonte, destino) + " /Y /M /S /E")
			else:
				shutil.copyfile(fonte, os.path.join(destino,'dir'))
			
			os.chdir("C://pdv")

			file_plugin = "C:\\pdv\plugin\loja26s_plugin.rar"
			def unrar(file):
				rf=rarfile.RarFile(file)
				rf.extractall('C:\\pdv\plugin')
			unrar(file_plugin)
		 
			time.sleep(10)
			msg.pack_forget()
			msg = Label(gui.root, text="Extraindo todos os arquivos do plugin agora" + "\n" + "Aguarde...", fg="blue", font= 'Arial 35')
			msg.pack(fill=BOTH, anchor=N, expand=True)	

			time.sleep(10)
			msg.pack_forget()
			msg = Label(gui.root, text="Plugin OK, aguarde...", fg="blue", font= 'Arial 50')
			msg.pack(fill=BOTH, anchor=N, expand=True)	

		else:
			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Sem arquivos(PLUGIN) para descompactar" + "\n" + "Aguarde...", fg="blue", font= 'Arial 35')
			msg.pack(fill=BOTH, anchor=N, expand=True)	

		os.chdir('C:\\PDV')

		os.startfile(r"Acertar_horario_i.exe")

		time.sleep(20)

		os.startfile(r"Deleta_Arquivo_loja26.exe")

		time.sleep(10)

		msg.pack_forget()
		msg = Label(gui.root, text='Processos inicializados com sucesso!' + '\n' + 'Aguarde....', fg="blue", font= 'Arial 45')
		msg.pack(fill=BOTH, anchor=N, expand=True)	

		time.sleep(10)

		os.startfile(r"pdvsal.exe")
		

		def sair():
			gui.root.destroy()
			return

		gui.root.after(3000, sair)
		

gui = GUI_Core()
#gui.root.wm_iconbitmap('icon1.ico')
#gui.root.title("REMARCA/NAGUMO - Versão 2.2S - Lj11")
#gui.root.resizable(0,0)
gui.root.attributes('-fullscreen',True)
gui.root.mainloop()
