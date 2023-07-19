#encoding: iso-8859-1

from cgitb import lookup
from cmath import log
import os, shutil, subprocess, time, glob, copy, os.path, sys, socket, threading, datetime, ntplib, logging, platform, configparser
from zipfile import ZipFile
from pathlib import Path
from datetime import datetime
from subprocess import call
from ctypes             import Structure, windll, pointer
from ctypes.wintypes    import WORD

logging.basicConfig(filename="pdvcoral.log", format="[v.4.6]:%(asctime)s %(message)s", datefmt='%d-%m-%y %H:%M:%S',
                    level=logging.INFO)

config = configparser.ConfigParser(defaults=None, strict=False, allow_no_value=True)
config.optionxform = str

class SYSTEMTIME(Structure):
		_fields_ = [
	( 'wYear',            WORD ),
	( 'wMonth',           WORD ),
	( 'wDayOfWeek',       WORD ),
	( 'wDay',             WORD ),
	( 'wHour',            WORD ),
	( 'wMinute',          WORD ),
	( 'wSecond',          WORD ),
	( 'wMilliseconds',    WORD ),
	]
SetLocalTime = windll.kernel32.SetLocalTime

try: import tkinter
except ImportError:
    import tkinter as tkinter
else: from tkinter import ttk
from tkinter import *

class GUI_Core(object):

    def __init__(self):
        self.root = tkinter.Tk()
        self.style = ttk.Style()
        self.style.theme_use('classic')
        self.progbar = ttk.Progressbar(self.root)
        self.progbar.config(orient ="horizontal", style="red.Horizontal.TProgressbar", length = 600, mode='determinate')
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
		msg = Label(gui.root, text='Iniciando, aguarde....', fg = "green", font= 'Arial 18')
		msg.pack()
		time.sleep(5)
		logging.info("Iniciando log...")


		try:

			config.read('rede.ini')
			letra = config.get('servidor', 'path')
			endereco = config.get('servidor','ip')
			usuario = config.get('servidor', 'user')
			senha = config.get('servidor', 'senha')

			winCMD = 'NET USE ' + letra + ' ' + '\\\\'  + endereco + ' ' + '/User:' + usuario + ' ' + senha
			exitcode = subprocess.call(winCMD, shell=True)
			print (exitcode)
			logging.info(winCMD)

		except:
			msg.pack_forget()
			msg = Label(gui.root, text='Sem arquivo rede.ini na pasta PDV..' + '\n' + 'Remarca verificar!', bg = "yellow", fg="red", font= 'Arial 18')
			msg.pack()
			logging.info('Sem arquivo rede.ini na pasta PDV')

			os.chdir("C://PDV")			  
	
			os.startfile(r"pdvsal.exe")
			logging.info("Executado pdvsal.exe")

			sys.exit()


		if exitcode == 0:
			print(winCMD)
			logging.info("Conectado no servidor")

		else:
				exitcode == 2
				logging.info("Sem conexão com a internet/servidor")

				os.chdir('C:\\PDV')

				path = 'C:\\PDV'
				dir = os.listdir(path)
				for file in dir:
					if file == "pdv.txt":
						os.remove(file)
						logging.info("Removendo arquivo: " + file)
												
				hostName    = ""

				ipAddress   = socket.gethostbyname_ex(socket.gethostname())

				time.sleep(2)

				with open('pdv.txt', 'a') as caixa:
					caixa.write(str("PDV e IP {} : {}".format(hostName,ipAddress)))
					caixa.close()

				time.sleep(2)
				msg.pack_forget()				
				msg = Label(gui.root, text='Aguarde....', fg = "red", font= 'Arial 18')
				msg.pack()
				logging.info('Aguarde....')

				os.startfile(r"C:\\pdv\pdvsal.exe")
				logging.info('Executado pdvsal.exe')

				time.sleep(2)

				msg.pack_forget()
				msg = Label(gui.root, text='Processos inicializados sem atualização!' + '\n' + 'Remarca verificar!', bg = "yellow", fg="red", font= 'Arial 18')
				msg.pack()
				logging.info('Processos inicializados sem atualização!')

				sys.exit()

		PATHPDV='X://loja48_pdv.rar'

		if os.path.isfile(PATHPDV):

			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text='Copiando arquivos para pasta PDV...', fg="blue", font= 'Arial 18')
			msg.pack()
			logging.info('Copiando arquivos para pasta PDV...')
			
			dest_dir = "C:\\PDV"
			for file in glob.glob(r'X:/loja48_pdv.rar'):
				print(file)
			shutil.copy(file, dest_dir)
			logging.info("Copiado arquivo: " + file)

		PATHPDV='C://PDV/loja48_pdv.rar'

		if os.path.isfile(PATHPDV):

			try:
				for arquivo in os.listdir('c://pdv'):
					x = arquivo
					os.rename(x,x.lower())
			except OSError:
				pass

			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Extraindo todos os arquivos para pasta pdv agora...", fg="blue", font= 'Arial 18')
			msg.pack()
			
			os.chdir("C://pdv")
			logging.info("Extraindo todos os arquivos para pasta pdv agora...")
			
			path = 'c://pdv/loja48_pdv.rar'
			result = subprocess.run(['unrar', 'x', '-y', path], stdout=subprocess.PIPE)
			logging.info(str(result.stdout))

			for raiz, diretorios, arquivos in os.walk('C:/PDV'):
				for arquivo in arquivos:
					if arquivo.endswith('loja48_pdv.rar'):
						os.remove(os.path.join(raiz, arquivo))
						logging.info("Deletado arquivo : " + arquivo)

		else:
			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Sem atualização na pasta PDV.", fg="blue", font= 'Arial 18')
			msg.pack()
			logging.info("Sem arquivos para a pasta PDV.")


      
		PATHPLUGIN='X://loja48_plugin.rar'

		if os.path.isfile(PATHPLUGIN):

			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text='Copiando arquivos para pasta \PDV\PLUGIN, aguarde....', fg="blue", font= 'Arial 18')
			msg.pack()
			logging.info('Copiando arquivos para pasta PDV\PLUGIN, aguarde....')
			
			dest_dir = "C:\\PDV\PLUGIN"
			for file in glob.glob(r'X:/loja48_plugin.rar'):
				print(file)
			shutil.copy(file, dest_dir)
			logging.info("Copiado arquivo: " + file)

		os.chdir("c://pdv/plugin")

		PATHPLUGIN='C://PDV/PLUGIN/loja48_plugin.rar'

		if os.path.isfile(PATHPLUGIN):
	
			try:
				for arquivo in os.listdir('c://pdv/plugin'):
					x = arquivo
					os.rename(x,x.lower())
			except OSError:
				pass
			
			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Extraindo todos os arquivos para a pasta pdv\plugin agora...", fg="blue", font= 'Arial 18')
			msg.pack()

			logging.info("Extraindo todos os arquivos para a pasta pdv\plugin agora...")

			path = 'c://pdv/plugin/loja48_plugin.rar'
			result = subprocess.run(['c://pdv/unrar', 'x', '-y', path], stdout=subprocess.PIPE)
			logging.info(str(result.stdout))

			for raiz, diretorios, arquivos in os.walk('C:/PDV/PLUGIN'):
				for arquivo in arquivos:
					if arquivo.endswith('loja48_plugin.rar'):
						os.remove(os.path.join(raiz, arquivo))
						logging.info("Deletado arquivo: " + arquivo)

		else:
			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Sem atualização na pasta \PDV\PLUGIN...", fg="blue", font= 'Arial 18')
			msg.pack()
			logging.info("Sem arquivos na pasta PDV\PLUGIN...")

		winCMD = 'NET USE ' + letra + ' /delete /y'
		print(winCMD)
		subprocess.call(winCMD, shell=True)
		logging.info(winCMD)
		logging.info("Desconectado servidor")

		os.chdir("C://PDV")			  

		if os.path.exists("work"):
			try:
				current_directory = "c://pdv"
				shutil.rmtree(current_directory + '/WORK/')
				logging.info("Deletado pasta WORK")
				os.mkdir('work')
				logging.info("Gerado pasta WORK")
			except PermissionError:
				print('Erro')
		else:
			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Não encontrada pasta WORK", fg="red", font= 'Arial 18')
			msg.pack()
			logging.info("Não encontrada pasta WORK")
			os.mkdir('work')
			
		os.chdir('C:\\PDV')
		time.sleep(5)
  
		msg.pack_forget()				
		msg = Label(gui.root, text='Aguarde....', fg = "blue", font= 'Arial 18')
		msg.pack()
		logging.info('Aguarde....')
		time.sleep(5)

		if os.path.exists("dllsat32bits.dll"):
			msg.pack_forget()
			msg = Label(gui.root, text='SAT Dimep, aguarde....', fg="blue", font= 'Arial 18')
			msg.pack()
			logging.info('SAT Dimep, extraindo dados.')
			time.sleep(5)

			os.startfile(r"sat_dimep.exe")
		
		elif os.path.exists("satdll.dll"):
			msg.pack_forget()
			msg = Label(gui.root, text='SAT Sweda, aguarde....', fg="blue", font= 'Arial 18')
			msg.pack()
			logging.info('SAT Sweda, extraindo dados.')
			time.sleep(5)
			
			os.startfile(r"sat_sweda.exe")
			
		elif os.path.exists("sat.dll"):
			msg.pack_forget()
			msg = Label(gui.root, text='SAT Jetway, aguarde....', fg="blue", font= 'Arial 18')
			msg.pack()
			logging.info('SAT Jetway, extraindo dados.')
			time.sleep(5)
			
			os.startfile(r"sat_jet.exe")

		else:
			msg.pack_forget()
			msg = Label(gui.root, text='SAT Crt_ID, aguarde....', fg="blue", font= 'Arial 18')
			msg.pack()
			logging.info('SAT Crt_ID, extraindo dados.')
			time.sleep(5)
			
			os.startfile(r"sat_id.exe")

		msg.pack_forget()
		msg = Label(gui.root, text='Aguarde....', fg="blue", font= 'Arial 18')
		msg.pack()
		logging.info('Aguarde....')
		time.sleep(5)
		
		os.startfile(r"socket_cliente.exe")
		logging.info("Chamado socket_cliente.exe")
		
		if os.path.exists("key.exe"):
			os.startfile(r"key.exe")
			logging.info("Chamado key.exe")
		else:
			with open("key.txt", "w") as stream:
				print('KEY.EXE NÃO EXISTE, VERIFICAR!', file=stream)
				logging.info('KEY.EXE Não EXISTE, VERIFICAR!')
		try:
			
			if platform.release() == '7':

				c = ntplib.NTPClient()
				response = c.request('a.ntp.br', version=3)
				dt_ = datetime.fromtimestamp( response.tx_time )
				res = dt_.strftime( '%d-%m-%Y %H:%M:%S')
				
				msg.pack_forget()
				msg = Label(gui.root, text='Data-Hora atual: ' + res, fg="blue", font= 'Arial 18')
				msg.pack()
				logging.info('Data-Hora atual: ' + res)
				time.sleep(5)

				dt_tuple = dt_.timetuple()
				st = SYSTEMTIME()
				st.wYear            = dt_tuple.tm_year
				st.wMonth           = dt_tuple.tm_mon
				st.wDayOfWeek       = ( dt_tuple.tm_wday + 1 ) % 7
				st.wDay             = dt_tuple.tm_mday
				st.wHour            = dt_tuple.tm_hour
				st.wMinute          = dt_tuple.tm_min
				st.wSecond          = dt_tuple.tm_sec
				st.wMilliseconds    = 0
				
				ret = SetLocalTime( pointer( st ) )
				if ret == 0:
					msg.pack_forget()
					msg = Label(gui.root, text='Erro. Chame Administrador.', fg="red", font= 'Arial 18')
					msg.pack()
					logging.info('Erro. Chame Administrador. -- retorno: ' + str(ret))
					time.sleep(5)
				else:
					msg.pack_forget()
					msg = Label(gui.root, text='Horário sincronizado com sucesso.', fg="blue", font= 'Arial 18')
					msg.pack()
					logging.info('Horário sincronizado com sucesso. -- retorno: ' + str(ret))
					time.sleep(2)
			else:
				pass

		except socket.gaierror:
			msg.pack_forget()
			msg = Label(gui.root, text='Erro no DNS, verificar...', fg="red", font= 'Arial 18')
			msg.pack()
			logging.info('Erro no DNS, verificar...')
			time.sleep(5)

		msg.pack_forget()
		msg = Label(gui.root, text='Processos inicializados com sucesso!', fg="blue", font= 'Arial 18')
		msg.pack()
		logging.info('Processos inicializados com sucesso!')

		time.sleep(5)

		os.startfile(r"pdvsal.exe")
		logging.info("Executado pdvsal.exe")
	
		def sair():
			gui.root.destroy()
			return

		gui.root.after(3000, sair)
		logging.info("Fechado programa")
	
gui = GUI_Core()
gui.root.title("REMARCA/NAGUMO - lj48 - 4.6")
gui.root.mainloop()
#Versão 4.3 - incluso o log --> pdvcoral.log para monitoração.
#Versão 4.4 - novo servidor --> 10.0.48.28
#Versão 4.5 - criado arquivo rede.ini com as configurações de conexão com o servidor(UNIDADE, IP/PASTA, USUARIO, SENHA)