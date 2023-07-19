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
        self.progbar = ttk.Progressbar(self.root)
        self.msg = Label(self.root, text='Aguarde...', fg="red", font='Arial 18')
        self.progbar.config(orient ="horizontal",length = 500, mode='determinate')
        self.progbar.pack(side='bottom', fill='y', expand=True)
        self.msg.pack(anchor=N)

        self.progbar.start()
        self.secondary_thread = threading.Thread(target=pdv)
        self.secondary_thread.start()
        self.root.after(10, self.check_thread)




    def check_thread(self):
        if self.secondary_thread.is_alive():
            self.root.after(10, self.check_thread)
        else:
            self.progbar.stop()


def pdv():

		time.sleep(30)
		# initialize
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
				msg = Label(gui.root, text="Sem conexão com o Servidor, enviando e-mail....", fg="blue", font= 'Arial 18')
				msg.pack()

				with open('pdv.txt', 'a') as caixa:
					caixa.write(str("PDV e IP {} : {}".format(hostName,ipAddress)))
					caixa.close()

				winCMD = 'NET USE ' + driveLetter + ' /delete /y'
				print(winCMD)
				subprocess.call(winCMD, shell=True)
				
				os.startfile(r"Enviando_Email_i.exe")

				time.sleep(10)

				os.startfile(r"Acertar_horario_i.exe")

				time.sleep(10)

				if os.path.exists("dllsat32bits.dll"):
					os.startfile(r"SAT_DIMEP.exe")
				else:
					pass
				
				if os.path.exists("satdll.dll"):
					os.startfile(r"SAT_SWEDA.exe")
				else:
					pass


				time.sleep(10)	 


				os.startfile(r"c:\\pdv\pdvsal.exe")

				time.sleep(10)

				msg.pack_forget()	
				msg = Label(gui.root, text='Processos inicializados sem atualização!' + '\n' + 'Remarca verificar!', bg = "yellow", fg="red", font= 'Arial 18')
				msg.pack()


				sys.exit()

		msg = Label(gui.root, text='Copiando arquivos para o PDV....', fg="blue", font= 'Arial 18')
		msg.pack()



		PATHPDV='X://loja14_pdv.rar'
		PATHPLUGIN='X://loja14_plugin.rar'

		if os.path.isfile(PATHPDV):
			
			dest_dir = "C:\\PDV"
			for file in glob.glob(r'X:/loja14_pdv.rar'):
				print(file)
			shutil.copy(file, dest_dir)

		else:
			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Sem arquivos(PDV) para atualizar no Servidor", fg="blue", font= 'Arial 18')
			msg.pack()


		if os.path.isfile(PATHPLUGIN):
			
			dest_dir = "C:\\PDV\PLUGIN"
			for file in glob.glob(r'X:/loja14_plugin.rar'):
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

		PATHPDV='C://PDV/loja14_pdv.rar'
		PATHPLUGIN='C://PDV/PLUGIN/loja14_plugin.rar'

		if os.path.isfile(PATHPDV):
			
			t = datetime.now().strftime("%d-%m-%Y %H:%M:%S").replace(":","_")
			d = './versões_anteriores_'+(t)
			os.makedirs(d)


			source = os.listdir("c://pdv")
			destination = 'c://pdv/versões_anteriores_'+(t)
			for files in source:
				if files.endswith("EXE"):
					shutil.move(files,destination)

			source = os.listdir("c://pdv")
			destination = 'c://pdv/versões_anteriores_'+(t)
			for files in source:
				if files.endswith("DLL"):
					shutil.move(files,destination)

					
			fonte = 'c://pdv/versões_anteriores_'+(t)
			destino = 'c://pdv'

			if sys.platform=='win32':
				os.system('xcopy "%s" "%s"' % (fonte, destino) + " /Y /M /S /E")
			else:
				shutil.copyfile(fonte, os.path.join(destino,'dir'))

			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Extraindo todos os arquivos do pdv agora...", fg="blue", font= 'Arial 18')
			msg.pack()
			
			os.chdir("c://pdv")

			file_pdv = "c:\\pdv\loja14_pdv.rar"
			def unrar(file):
				rf=rarfile.RarFile(file)
				rf.extractall('c:\\pdv')
			unrar(file_pdv)
 

			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Pdv OK!", fg="blue", font= 'Arial 18')
			msg.pack()

			print('Pronto pdv!' + '\n')

		else:
			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Sem arquivos(PDV) para descompactar", fg="blue", font= 'Arial 18')
			msg.pack()

			print("Sem arquivos(PDV) para descompactar" + "\n")

		if os.path.isfile(PATHPLUGIN):
			
			os.chdir("c://pdv/plugin")

			source = os.listdir("c://pdv/plugin")
			destination = 'c://pdv/versões_anteriores_'+(t)
			for files in source:
				if files.endswith("DLL"):
					shutil.move(files,destination)

					
			fonte = 'c://pdv/versões_anteriores_'+(t)
			destino = 'c://pdv/plugin'

			if sys.platform=='win32':
				os.system('xcopy "%s" "%s"' % (fonte, destino) + " /Y /M /S /E")
			else:
				shutil.copyfile(fonte, os.path.join(destino,'dir'))
			
			os.chdir("c://pdv")

			file_plugin = "c:\\pdv\plugin\loja14_plugin.rar"
			def unrar(file):
				rf=rarfile.RarFile(file)
				rf.extractall('c:\\pdv\plugin')
			unrar(file_plugin)
		 
			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Extraindo todos os arquivos do plugin agora...", fg="blue", font= 'Arial 18')
			msg.pack()

			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Plugin OK!", fg="blue", font= 'Arial 18')
			msg.pack()

			print('Pronto plugin!' + '\n')

		else:
			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Sem arquivos(PLUGIN) para descompactar", fg="blue", font= 'Arial 18')
			msg.pack()

			print("Sem arquivos(PLUGIN) para descompactar" + "\n")	


		os.chdir('C:\\PDV')

		os.startfile(r"Acertar_horario_i.exe")

		time.sleep(20)

		os.startfile(r"Deleta_Arquivo_Loja14.exe")

		time.sleep(10)

		if os.path.exists("dllsat32bits.dll"):
			os.startfile(r"SAT_DIMEP.exe")
		
		else:
			os.startfile(r"SAT_SWEDA.exe")

		time.sleep(20)

		msg.pack_forget()
		msg = Label(gui.root, text='Processos inicializados com sucesso!', fg="blue", font= 'Arial 18')
		msg.pack()

		time.sleep(10)

		os.startfile(r"pdvsal.exe")
		

		def sair():
			gui.root.destroy()
			return

		gui.root.after(3000, sair)




gui = GUI_Core()
gui.root.title("REMARCA/NAGUMO - Versao 2.2 - Lj14")
#gui.root.resizable(False, False)  # This code helps to disable windows from resizing

#window_height = 80
#window_width = 500

#screen_width = gui.root.winfo_screenwidth()
#screen_height = gui.root.winfo_screenheight()

#x_cordinate = int((screen_width/2) - (window_width/2))
#y_cordinate = int((screen_height/2) - (window_height/2))

#gui.root.geometry("{}x{}+{}+{}".format(window_width, window_height, x_cordinate, y_cordinate))

gui.root.mainloop()