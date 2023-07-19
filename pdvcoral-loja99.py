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

logging.basicConfig(filename="pdvcoral.log", format="[v.4.5]: %(asctime)s %(message)s", datefmt='%d-%m-%y %H:%M:%S',
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
			msg = Label(gui.root, text='Sem arquivo config.ini na pasta PDV..' + '\n' + 'Remarca verificar!', bg = "yellow", fg="red", font= 'Arial 18')
			msg.pack()
			logging.info('Sem arquivo config.ini na pasta PDV')

			os.chdir("C://PDV")			  
	
			os.startfile(r"pdvsal.exe")
			logging.info("Executado pdvsal.exe")

			sys.exit()


		if exitcode == 0:
			logging.info("Conectado com o servidor")

		else:
				exitcode == 2
				logging.info("Sem conexão com o servidor")

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
				msg.pack_forget()
				msg = Label(gui.root, text="Sem conexão com o Servidor, enviando e-mail....", fg="red", font= 'Arial 18')
				msg.pack()
				logging.info("Sem conexão com o Servidor, enviando e-mail....")

				with open('pdv.txt', 'a') as caixa:
					caixa.write(str("PDV e IP {} : {}".format(hostName,ipAddress)))
					caixa.close()

				time.sleep(2)
				msg.pack_forget()				
				msg = Label(gui.root, text='Aguarde....', fg = "red", font= 'Arial 18')
				msg.pack()
				logging.info('Aguarde....')
				
				os.startfile(r"enviando_email_i.exe")
				logging.info("Enviado e-mail")

				time.sleep(2)

				os.startfile(r"C:\\pdv\pdvsal.exe")
				logging.info('Executado pdvsal.exe')

				time.sleep(2)

				msg.pack_forget()
				msg = Label(gui.root, text='Processos inicializados sem atualização!' + '\n' + 'Remarca verificar!', bg = "yellow", fg="red", font= 'Arial 18')
				msg.pack()
				logging.info('Processos inicializados sem atualização!' + ' Erro: ' + str(exitcode) + ' - O caminho da rede não foi encontrado')
				sys.exit()



		msg.pack_forget()
		msg = Label(gui.root, text='Copiando arquivos para o PDV, aguarde....', fg="blue", font= 'Arial 18')
		msg.pack()
		logging.info('Copiando arquivos para o PDV, aguarde....')

		PATHPDV='X://loja99_pdv.rar'
		PATHPLUGIN='X://loja99_plugin.rar'

		if os.path.isfile(PATHPDV):
			
			dest_dir = "C:\\PDV"
			for file in glob.glob(r'X:/loja99_pdv.rar'):
				print(file)
			shutil.copy(file, dest_dir)
			logging.info("Copiado arquivo: " + file)

		else:
			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Sem arquivos(PDV) para atualizar no Servidor", fg="blue", font= 'Arial 18')
			msg.pack()
			logging.info("Sem arquivos(PDV) para atualizar no Servidor")

		if os.path.isfile(PATHPLUGIN):
			
			dest_dir = "C:\\PDV\PLUGIN"
			for file in glob.glob(r'X:/loja99_plugin.rar'):
				print(file)
			shutil.copy(file, dest_dir)
			logging.info("Copiado arquivo: " + file)

		else:
			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Sem arquivos(PLUGIN) para atualizar no Servidor", fg="blue", font= 'Arial 18')
			msg.pack()
			logging.info("Sem arquivos(PLUGIN) para atualizar no Servidor")

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

		PATHPDV='C://PDV/loja99_pdv.rar'
		PATHPLUGIN='C://PDV/PLUGIN/loja99_plugin.rar'

		if os.path.isfile(PATHPDV):

			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Cópia dos arquivos antigos pdv...", fg="blue", font= 'Arial 18')
			msg.pack()
			logging.info("Cópia dos arquivos antigos pdv...")

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

#			t = datetime.now().strftime("%d-%m-%Y %H:%M:%S").replace(":","_")
#			d = './versões_anteriores_'+(t)


			try:	
				pasta = 'c://pdv/ultimas_versoes_pdv'
				if os.path.isdir(pasta): 
					shutil.rmtree(pasta)
					os.mkdir(pasta)
				else:
					os.mkdir(pasta) 
			except PermissionError:
				logging.info('Arquivos não copiados do PDV')

			
			source = os.listdir("C://pdv")
			destination = 'C://pdv/ultimas_versoes_pdv'
			for files in source:
				if files.startswith("pdvsal.exe"):
					try:
						ret = shutil.move(files,destination)
						logging.info("Arquivo: copiado para: " + ret)
					except shutil.Error:
						logging.info("Não copiado: " + files)

			source = os.listdir("C://pdv")
			destination = 'C://pdv/ultimas_versoes_pdv'
			for files in source:
				if files.startswith("satsal.dll"):
					try:
						ret = shutil.move(files,destination)
						logging.info("Arquivo: copiado para: " + ret)
					except shutil.Error:
						logging.info("Não copiado: " + files)
					

			source = os.listdir("C://pdv")
			destination = 'C://pdv/ultimas_versoes_pdv'
			for files in source:
				if files.startswith("nfce.dll"):
					try:
						ret = shutil.move(files,destination)
						logging.info("Arquivo: copiado para: " + ret)
					except shutil.Error:
						logging.info("Não copiado: " + files)

			source = os.listdir("C://pdv")
			destination = 'C://pdv/ultimas_versoes_pdv'
			for files in source:
				if files.startswith("nfe2ws4.exe"):
					try:						
						ret = shutil.move(files,destination)
						logging.info("Arquivo: copiado para: " + ret)
					except shutil.Error:
						logging.info("Não copiado: " + files)

			source = os.listdir("C://pdv")
			destination = 'C://pdv/ultimas_versoes_pdv'
			for files in source:
				if files.startswith("salcomm.exe"):
					try:
						ret = shutil.move(files,destination)
						logging.info("Arquivo: copiado para: " + ret)					
					except shutil.Error:
						logging.info("Não copiado: " + files)

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
			logging.info("Extraindo todos os arquivos do pdv agora...")
			
			path = 'c://pdv/loja99_pdv.rar'
			result = subprocess.run(['unrar', 'x', '-y', path], stdout=subprocess.PIPE)
			logging.info(str(result.stdout))

			for raiz, diretorios, arquivos in os.walk('C:/PDV'):
				for arquivo in arquivos:
					if arquivo.endswith('loja99_pdv.rar'):
						os.remove(os.path.join(raiz, arquivo))
						logging.info("Deletado arquivo : " + arquivo)
		else:
			time.sleep(2)
			msg.pack_forget()
			msg = Label(gui.root, text="Sem arquivos(PDV) para descompactar", fg="blue", font= 'Arial 18')
			msg.pack()
			logging.info("Sem arquivos(PDV) para descompactar")

		if os.path.isfile(PATHPLUGIN):
			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Cópia dos arquivos antigos plugin...", fg="blue", font= 'Arial 18')
			msg.pack()
			logging.info("Cópia dos arquivos antigos plugin...")

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
					try:
						ret = shutil.move(files,destination)
						logging.info("Arquivo: copiado para: " + ret)					
					except shutil.Error:
						logging.info("Não copiado: " + files)

			source = os.listdir("C://pdv/plugin")
			destination = 'C://pdv/ultimas_versoes_plugin'
			for files in source:
				if files.startswith("clitef.dll"):
					try:
						ret = shutil.move(files,destination)
						logging.info("Arquivo: copiado para: " + ret)					
					except shutil.Error:
						logging.info("Não copiado: " + files)

			source = os.listdir("C://pdv/plugin")
			destination = 'C://pdv/ultimas_versoes_plugin'
			for files in source:
				if files.startswith("compcanc.dll"):
					try:
						ret = shutil.move(files,destination)
						logging.info("Arquivo: copiado para: " + ret)					
					except shutil.Error:
						logging.info("Não copiado: " + files)

			source = os.listdir("C://pdv/plugin")
			destination = 'C://pdv/ultimas_versoes_plugin'
			for files in source:
				if files.startswith("compfina.dll"):
					try:
						ret = shutil.move(files,destination)
						logging.info("Arquivo: copiado para: " + ret)					
					except shutil.Error:
						logging.info("Não copiado: " + files)

			source = os.listdir("C://pdv/plugin")
			destination = 'C://pdv/ultimas_versoes_plugin'
			for files in source:
				if files.startswith("prevenc.dll"):
					try:
						ret = shutil.move(files,destination)
						logging.info("Arquivo: copiado para: " + ret)					
					except shutil.Error:
						logging.info("Não copiado: " + files)

			source = os.listdir("C://pdv/plugin")
			destination = 'C://pdv/ultimas_versoes_plugin'
			for files in source:
				if files.startswith("estac.dll"):
					try:
						ret = shutil.move(files,destination)
						logging.info("Arquivo: copiado para: " + ret)					
					except shutil.Error:
						logging.info("Não copiado: " + files)

			source = os.listdir("C://pdv/plugin")
			destination = 'C://pdv/ultimas_versoes_plugin'
			for files in source:
				if files.startswith("frete.dll"):
					try:
						ret = shutil.move(files,destination)
						logging.info("Arquivo: copiado para: " + ret)					
					except shutil.Error:
						logging.info("Não copiado: " + files)


			fonte = 'C://pdv/ultimas_versoes_plugin'
			destino = 'C://pdv/plugin'

			if sys.platform=='win32':
				os.system('xcopy "%s" "%s"' % (fonte, destino) + " /Y /M /S /E")
			else:
				shutil.copyfile(fonte, os.path.join(destino,'dir'))
			
			time.sleep(5)
			msg.pack_forget()
			msg = Label(gui.root, text="Aguarde...", fg="blue", font= 'Arial 18')
			msg.pack()

			logging.info("Extraindo todos os arquivos do plugin agora...")

			path = 'c://pdv/plugin/loja99_plugin.rar'
			result = subprocess.run(['c://pdv/unrar', 'x', '-y', path], stdout=subprocess.PIPE)
			logging.info(str(result.stdout))

			for raiz, diretorios, arquivos in os.walk('C:/PDV/PLUGIN'):
				for arquivo in arquivos:
					if arquivo.endswith('loja99_plugin.rar'):
						os.remove(os.path.join(raiz, arquivo))
						logging.info("Deletado arquivo: " + arquivo)
		else:
			msg.pack_forget()
			msg = Label(gui.root, text="Sem arquivos(PLUGIN) para descompactar", fg="blue", font= 'Arial 18')
			msg.pack()
			logging.info("Sem arquivos(PLUGIN) para descompactar")

		os.chdir('C:\\PDV')

		msg.pack_forget()				
		msg = Label(gui.root, text='Aguarde....', fg = "blue", font= 'Arial 18')
		msg.pack()

		time.sleep(5)
		
		os.startfile(r"socket_cliente36.exe")
		logging.info("Chamado socket_cliente36.exe")

		if os.path.exists("key.exe"):
			os.startfile(r"key.exe")
			logging.info("Chamado key.exe")
		else:
			with open("key.txt", "w") as stream:
				print('KEY.EXE NÃO EXISTE, VERIFICAR!', file=stream)
				logging.info('KEY.EXE Não EXISTE, VERIFICAR!')
		try:
			
			if platform.release() == '7':

				logging.info('Windows 7')

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
				logging.info("Windows 10")

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
		logging.info("Encerrando log...")

gui = GUI_Core()
gui.root.title("REMARCA/NAGUMO - lj99 - 4.5")
gui.root.mainloop()
#Versão 4.3 - incluso o log --> pdvcoral.log para monitoração.
#Versão 4.4 - novo servidor --> 10.0.48.28
#Versão 4.5 - criado arquivo rede.ini com as configurações de conexão com o servidor(UNIDADE, IP/PASTA, USUARIO, SENHA)