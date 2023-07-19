#encoding: iso-8859-1
import os, time, subprocess
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk

gui = Tk()

bottomFrame = Frame(gui)
bottomFrame.pack(side=BOTTOM, anchor = W)

gui.title("PDVCORAL_REMARCA - NAGUMO **(LOJA 23)**")
gui.geometry("600x370")
gui.resizable(0,0)

load = Image.open("logo_2016.png")
render = ImageTk.PhotoImage(load)
img= Label(gui, image=render)
img.image = render
img.place(x=365, y=0)


def sel():
   selection = "ESCOLHIDA OPÇÃO: " + str(var.get()) + " DO MENU!!!"
   label.config(text = selection, bg="red", fg="yellow", font="Terminal 12")
   label.place(x=10, y=50)

var= IntVar()

R1 = Radiobutton(gui, text="1 - Reiniciar PDVCORAL", variable=var, value=1, font="Arial 10", command=sel)
R1.pack( anchor = NW )

R2 = Radiobutton(gui, text="2 - Reiniciar CPU", variable=var, value=2, font="Arial 10", command=sel)
R2.pack( anchor = NW )

mensagem= StringVar()
lbl = Label(gui, text="Remarca - telefone: (11)2755-7911 " , fg="red", font="Arial 15")
lbl.place(x=140, y=225)

mensagem= StringVar()
lbl = Label(gui, text="Versão 2.0" , fg="black", font="Arial 8")
lbl.place(x=1, y=350)
#Versão 2.0 
#- Alteração - tirado pdvcoral.exe e colocado inicia_pdv.bat
#- Inclusão - mata processo Pdvsal Front End(WerFault.exe)

label = Label(gui)
label.pack()

res = " "

lblaguarde = Label(gui, text= res, font="Arial 20", fg= "red")
lblaguarde.place(x=180, y=100)

def Aguarde(event):
	res = "Aguarde..."
	res_texto(res)
	
def res_texto(res):
    lblaguarde.config(text=res)

def Caixa1():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.23.1 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.23.1 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.1 ""c:\\pdv\inicia_pdv.bat", shell=True)
			if ret ==2:
				time.sleep(5)
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
				if resp == "ok":
					res = "LIGUE - REMARCA            erro:" + str(ret)
					res_texto(res)
			else:
				time.sleep(5)
				resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 01")
				if resp == "ok":
					res = "Pronto!!!"
					res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.1 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!           erro:" + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret !=2:
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "CAIXA 01 ESTA SENDO REINICIADO, AGUARDE...")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)


def Caixa2():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.23.2 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.23.2 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.2 ""c:\\pdv\inicia_pdv.bat", shell=True)
			if ret ==2:
				time.sleep(5)
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
				if resp == "ok":
					res = "LIGUE - REMARCA            erro:" + str(ret)
					res_texto(res)
			else:
				time.sleep(5)
				resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 02")
				if resp == "ok":
					res = "Pronto!!!"
					res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.2 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!           erro:" + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret !=2:
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "CAIXA 02 ESTA SENDO REINICIADO, AGUARDE...")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDVCORAL  OU  2 - REINICIAR CPU!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)

def Caixa3():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.23.3 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.23.3 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.3 ""c:\\pdv\inicia_pdv.bat", shell=True)
			if ret ==2:
				time.sleep(5)
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
				if resp == "ok":
					res = "LIGUE - REMARCA            erro:" + str(ret)
					res_texto(res)
			else:
				time.sleep(5)
				resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 03")
				if resp == "ok":
					res = "Pronto!!!"
					res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.3 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!           erro:" + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret !=2:
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "CAIXA 03 ESTA SENDO REINICIADO, AGUARDE...")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDVCORAL  OU  2 - REINICIAR CPU!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)


def Caixa4():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.23.4 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.23.4 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.4 ""c:\\pdv\inicia_pdv.bat", shell=True)
			if ret ==2:
				time.sleep(5)
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
				if resp == "ok":
					res = "LIGUE - REMARCA            erro:" + str(ret)
					res_texto(res)
			else:
				time.sleep(5)
				resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 04")
				if resp == "ok":
					res = "Pronto!!!"
					res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.4 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!           erro:" + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret !=2:
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "CAIXA 04 ESTA SENDO REINICIADO, AGUARDE...")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDVCORAL  OU  2 - REINICIAR CPU!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)


def Caixa5():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.23.5 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.23.5 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.5 ""c:\\pdv\inicia_pdv.bat", shell=True)
			if ret ==2:
				time.sleep(5)
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
				if resp == "ok":
					res = "LIGUE - REMARCA            erro:" + str(ret)
					res_texto(res)
			else:
				time.sleep(5)
				resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 05")
				if resp == "ok":
					res = "Pronto!!!"
					res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.5 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!           erro:" + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret !=2:
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "CAIXA 05 ESTA SENDO REINICIADO, AGUARDE...")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDVCORAL  OU  2 - REINICIAR CPU!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)

def Caixa6():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.23.6 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.23.6 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.6 ""c:\\pdv\inicia_pdv.bat", shell=True)
			if ret ==2:
				time.sleep(5)
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
				if resp == "ok":
					res = "LIGUE - REMARCA            erro:" + str(ret)
					res_texto(res)
			else:
				time.sleep(5)
				resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 06")
				if resp == "ok":
					res = "Pronto!!!"
					res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.6 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!           erro:" + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret !=2:
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "CAIXA 06 ESTA SENDO REINICIADO, AGUARDE...")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDVCORAL  OU  2 - REINICIAR CPU!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)

def Caixa7():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.23.7 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.23.7 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.7 ""c:\\pdv\inicia_pdv.bat", shell=True)
			if ret ==2:
				time.sleep(5)
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
				if resp == "ok":
					res = "LIGUE - REMARCA            erro:" + str(ret)
					res_texto(res)
			else:
				time.sleep(5)
				resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 07")
				if resp == "ok":
					res = "Pronto!!!"
					res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.7 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!           erro:" + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret !=2:
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "CAIXA 07 ESTA SENDO REINICIADO, AGUARDE...")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDVCORAL  OU  2 - REINICIAR CPU!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)

def Caixa8():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.23.8 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.23.8 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.8 ""c:\\pdv\inicia_pdv.bat", shell=True)
			if ret ==2:
				time.sleep(5)
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
				if resp == "ok":
					res = "LIGUE - REMARCA            erro:" + str(ret)
					res_texto(res)
			else:
				time.sleep(5)
				resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 08")
				if resp == "ok":
					res = "Pronto!!!"
					res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.8 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!           erro:" + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret !=2:
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "CAIXA 08 ESTA SENDO REINICIADO, AGUARDE...")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDVCORAL  OU  2 - REINICIAR CPU!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)

def Caixa9():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.23.9 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.23.9 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.9 ""c:\\pdv\inicia_pdv.bat", shell=True)
			if ret ==2:
				time.sleep(5)
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
				if resp == "ok":
					res = "LIGUE - REMARCA            erro:" + str(ret)
					res_texto(res)
			else:
				time.sleep(5)
				resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 09")
				if resp == "ok":
					res = "Pronto!!!"
					res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.9 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!           erro:" + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret !=2:
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "CAIXA 09 ESTA SENDO REINICIADO, AGUARDE...")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDVCORAL  OU  2 - REINICIAR CPU!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)

def Caixa10():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.23.10 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.23.10 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.10 ""c:\\pdv\inicia_pdv.bat", shell=True)
			if ret ==2:
				time.sleep(5)
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
				if resp == "ok":
					res = "LIGUE - REMARCA            erro:" + str(ret)
					res_texto(res)
			else:
				time.sleep(5)
				resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 10")
				if resp == "ok":
					res = "Pronto!!!"
					res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.10 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!           erro:" + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret !=2:
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "CAIXA 10 ESTA SENDO REINICIADO, AGUARDE...")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDVCORAL  OU  2 - REINICIAR CPU!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)

def Caixa11():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.23.11 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.23.11 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.11 ""c:\\pdv\inicia_pdv.bat", shell=True)
			if ret ==2:
				time.sleep(5)
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
				if resp == "ok":
					res = "LIGUE - REMARCA            erro:" + str(ret)
					res_texto(res)
			else:
				time.sleep(5)
				resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 11")
				if resp == "ok":
					res = "Pronto!!!"
					res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.11 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!           erro:" + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret !=2:
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "CAIXA 11 ESTA SENDO REINICIADO, AGUARDE...")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDVCORAL  OU  2 - REINICIAR CPU!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)

def Caixa12():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.23.12 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.23.12 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.12 ""c:\\pdv\inicia_pdv.bat", shell=True)
			if ret ==2:
				time.sleep(5)
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
				if resp == "ok":
					res = "LIGUE - REMARCA            erro:" + str(ret)
					res_texto(res)
			else:
				time.sleep(5)
				resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 12")
				if resp == "ok":
					res = "Pronto!!!"
					res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.12 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!           erro:" + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret !=2:
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "CAIXA 12 ESTA SENDO REINICIADO, AGUARDE...")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDVCORAL  OU  2 - REINICIAR CPU!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)

def Caixa13():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.23.13 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.23.13 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.13 ""c:\\pdv\inicia_pdv.bat", shell=True)
			if ret ==2:
				time.sleep(5)
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
				if resp == "ok":
					res = "LIGUE - REMARCA            erro:" + str(ret)
					res_texto(res)
			else:
				time.sleep(5)
				resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 13")
				if resp == "ok":
					res = "Pronto!!!"
					res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.13 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!           erro:" + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret !=2:
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "CAIXA 13 ESTA SENDO REINICIADO, AGUARDE...")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDVCORAL  OU  2 - REINICIAR CPU!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)

def Caixa14():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.23.14 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.23.14 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.14 ""c:\\pdv\inicia_pdv.bat", shell=True)
			if ret ==2:
				time.sleep(5)
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
				if resp == "ok":
					res = "LIGUE - REMARCA            erro:" + str(ret)
					res_texto(res)
			else:
				time.sleep(5)
				resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 14")
				if resp == "ok":
					res = "Pronto!!!"
					res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.14 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!           erro:" + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret !=2:
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "CAIXA 14 ESTA SENDO REINICIADO, AGUARDE...")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDVCORAL  OU  2 - REINICIAR CPU!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)

def Caixa15():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.23.15 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.23.15 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.15 ""c:\\pdv\inicia_pdv.bat", shell=True)
			if ret ==2:
				time.sleep(5)
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
				if resp == "ok":
					res = "LIGUE - REMARCA            erro:" + str(ret)
					res_texto(res)
			else:
				time.sleep(5)
				resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 15")
				if resp == "ok":
					res = "Pronto!!!"
					res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.15 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!           erro:" + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret !=2:
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "CAIXA 15 ESTA SENDO REINICIADO, AGUARDE...")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDVCORAL  OU  2 - REINICIAR CPU!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)

def Caixa16():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.23.16 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.23.16 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.16 ""c:\\pdv\inicia_pdv.bat", shell=True)
			if ret ==2:
				time.sleep(5)
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
				if resp == "ok":
					res = "LIGUE - REMARCA            erro:" + str(ret)
					res_texto(res)
			else:
				time.sleep(5)
				resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 16")
				if resp == "ok":
					res = "Pronto!!!"
					res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.16 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!           erro:" + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret !=2:
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "CAIXA 16 ESTA SENDO REINICIADO, AGUARDE...")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDVCORAL  OU  2 - REINICIAR CPU!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)

def Caixa17():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.23.17 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.23.17 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.17 ""c:\\pdv\inicia_pdv.bat", shell=True)
			if ret ==2:
				time.sleep(5)
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
				if resp == "ok":
					res = "LIGUE - REMARCA            erro:" + str(ret)
					res_texto(res)
			else:
				time.sleep(5)
				resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 17")
				if resp == "ok":
					res = "Pronto!!!"
					res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.17 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!           erro:" + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret !=2:
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "CAIXA 17 ESTA SENDO REINICIADO, AGUARDE...")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDVCORAL  OU  2 - REINICIAR CPU!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)

def Caixa18():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.23.18 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.23.18 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.18 ""c:\\pdv\inicia_pdv.bat", shell=True)
			if ret ==2:
				time.sleep(5)
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
				if resp == "ok":
					res = "LIGUE - REMARCA            erro:" + str(ret)
					res_texto(res)
			else:
				time.sleep(5)
				resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 18")
				if resp == "ok":
					res = "Pronto!!!"
					res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.18 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!           erro:" + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret !=2:
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "CAIXA 18 ESTA SENDO REINICIADO, AGUARDE...")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDVCORAL  OU  2 - REINICIAR CPU!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)

def Caixa19():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.23.19 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.23.19 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.19 ""c:\\pdv\inicia_pdv.bat", shell=True)
			if ret ==2:
				time.sleep(5)
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
				if resp == "ok":
					res = "LIGUE - REMARCA            erro:" + str(ret)
					res_texto(res)
			else:
				time.sleep(5)
				resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 19")
				if resp == "ok":
					res = "Pronto!!!"
					res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.19 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!           erro:" + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret !=2:
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "CAIXA 19 ESTA SENDO REINICIADO, AGUARDE...")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDVCORAL  OU  2 - REINICIAR CPU!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)

def Caixa20():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.23.20 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.23.20 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.20 ""c:\\pdv\inicia_pdv.bat", shell=True)
			if ret ==2:
				time.sleep(5)
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
				if resp == "ok":
					res = "LIGUE - REMARCA            erro:" + str(ret)
					res_texto(res)
			else:
				time.sleep(5)
				resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 20")
				if resp == "ok":
					res = "Pronto!!!"
					res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.20 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!           erro:" + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret !=2:
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "CAIXA 20 ESTA SENDO REINICIADO, AGUARDE...")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDVCORAL  OU  2 - REINICIAR CPU!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)

def Caixa21():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.23.21 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.23.21 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.21 ""c:\\pdv\inicia_pdv.bat", shell=True)
			if ret ==2:
				time.sleep(5)
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
				if resp == "ok":
					res = "LIGUE - REMARCA            erro:" + str(ret)
					res_texto(res)
			else:
				time.sleep(5)
				resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 21")
				if resp == "ok":
					res = "Pronto!!!"
					res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.21 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!           erro:" + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret !=2:
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "CAIXA 21 ESTA SENDO REINICIADO, AGUARDE...")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDVCORAL  OU  2 - REINICIAR CPU!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)

def Caixa22():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.23.22 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.23.22 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.22 ""c:\\pdv\inicia_pdv.bat", shell=True)
			if ret ==2:
				time.sleep(5)
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
				if resp == "ok":
					res = "LIGUE - REMARCA            erro:" + str(ret)
					res_texto(res)
			else:
				time.sleep(5)
				resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 22")
				if resp == "ok":
					res = "Pronto!!!"
					res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.22 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!           erro:" + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret !=2:
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "CAIXA 22 ESTA SENDO REINICIADO, AGUARDE...")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDVCORAL  OU  2 - REINICIAR CPU!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)

def Caixa23():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.23.23 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.23.23 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.23 ""c:\\pdv\inicia_pdv.bat", shell=True)
			if ret ==2:
				time.sleep(5)
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
				if resp == "ok":
					res = "LIGUE - REMARCA            erro:" + str(ret)
					res_texto(res)
			else:
				time.sleep(5)
				resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 23")
				if resp == "ok":
					res = "Pronto!!!"
					res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.23 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!           erro:" + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret !=2:
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "CAIXA 23 ESTA SENDO REINICIADO, AGUARDE...")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDVCORAL  OU  2 - REINICIAR CPU!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)

def Caixa24():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.23.24 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.23.24 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.24 ""c:\\pdv\inicia_pdv.bat", shell=True)
			if ret ==2:
				time.sleep(5)
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
				if resp == "ok":
					res = "LIGUE - REMARCA            erro:" + str(ret)
					res_texto(res)
			else:
				time.sleep(5)
				resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 24")
				if resp == "ok":
					res = "Pronto!!!"
					res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.24 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!           erro:" + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret !=2:
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "CAIXA 24 ESTA SENDO REINICIADO, AGUARDE...")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDVCORAL  OU  2 - REINICIAR CPU!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)

def Caixa25():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.23.25 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.23.25 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.25 ""c:\\pdv\inicia_pdv.bat", shell=True)
			if ret ==2:
				time.sleep(5)
				resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
				if resp == "ok":
					res = "LIGUE - REMARCA            erro:" + str(ret)
					res_texto(res)
			else:
				time.sleep(5)
				resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 25")
				if resp == "ok":
					res = "Pronto!!!"
					res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.23.25 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!           erro:" + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret !=2:
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "CAIXA 25 ESTA SENDO REINICIADO, AGUARDE...")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")	
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDVCORAL  OU  2 - REINICIAR CPU!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)


btn1 = Button(bottomFrame, text="Caixa 01", bg="white", fg="black", command=Caixa1)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn1.bind('<Button-1>', Aguarde)
btn1.grid(column=0, row = 1)

btn2 = Button(bottomFrame, text="Caixa 02", bg="white", fg="black", command=Caixa2)
#btn2.pack(side=LEFT, anchor=W, fill=X, expand=0)
btn2.bind('<Button-1>', Aguarde)
btn2.grid(column=1, row = 1)

btn3 = Button(bottomFrame, text="Caixa 03", bg="white", fg="black", command=Caixa3)
#btn3.pack(side=LEFT, anchor=W, expand=0)
btn3.bind('<Button-1>', Aguarde)
btn3.grid(column=2, row = 1)

btn4 = Button(bottomFrame, text="Caixa 04", bg="white", fg="black", command=Caixa4)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn4.bind('<Button-1>', Aguarde)
btn4.grid(column=3, row = 1)

btn5 = Button(bottomFrame, text="Caixa 05", bg="white", fg="black", command=Caixa5)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn5.bind('<Button-1>', Aguarde)
btn5.grid(column=4, row = 1)

btn6 = Button(bottomFrame, text="Caixa 06", bg="white", fg="black", command=Caixa6)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn6.bind('<Button-1>', Aguarde)
btn6.grid(column=5, row = 1)

btn7 = Button(bottomFrame, text="Caixa 07", bg="white", fg="black", command=Caixa7)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn7.bind('<Button-1>', Aguarde)
btn7.grid(column=6, row = 1)

btn8 = Button(bottomFrame, text="Caixa 08", bg="white", fg="black", command=Caixa8)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn8.bind('<Button-1>', Aguarde)
btn8.grid(column=7, row = 1)

btn9 = Button(bottomFrame, text="Caixa 09", bg="white", fg="black", command=Caixa9)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn9.bind('<Button-1>', Aguarde)
btn9.grid(column=8, row = 1)

btn10 = Button(bottomFrame, text="Caixa 10", bg="white", fg="black", command=Caixa10)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn10.bind('<Button-1>', Aguarde)
btn10.grid(column=9, row = 1)

btn11 = Button(bottomFrame, text="Caixa 11", bg="white", fg="black", command=Caixa11)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn11.bind('<Button-1>', Aguarde)
btn11.grid(column=0, row = 2)

btn12 = Button(bottomFrame, text="Caixa 12", bg="white", fg="black", command=Caixa12)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn12.bind('<Button-1>', Aguarde)
btn12.grid(column=1, row = 2)

btn13 = Button(bottomFrame, text="Caixa 13", bg="white", fg="black", command=Caixa13)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn13.bind('<Button-1>', Aguarde)
btn13.grid(column=2, row = 2)

btn14 = Button(bottomFrame, text="Caixa 14", bg="white", fg="black", command=Caixa14)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn14.bind('<Button-1>', Aguarde)
btn14.grid(column=3, row = 2)

btn15 = Button(bottomFrame, text="Caixa 15", bg="white", fg="black", command=Caixa15)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn15.bind('<Button-1>', Aguarde)
btn15.grid(column=4, row = 2)

btn16 = Button(bottomFrame, text="Caixa 16", bg="white", fg="black", command=Caixa16)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn16.bind('<Button-1>', Aguarde)
btn16.grid(column=5, row = 2)

btn17 = Button(bottomFrame, text="Caixa 17", bg="white", fg="black", command=Caixa17)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn17.bind('<Button-1>', Aguarde)
btn17.grid(column=6, row = 2)

btn18 = Button(bottomFrame, text="Caixa 18", bg="white", fg="black", command=Caixa18)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn18.bind('<Button-1>', Aguarde)
btn18.grid(column=7, row = 2)

btn19 = Button(bottomFrame, text="Caixa 19", bg="white", fg="black", command=Caixa19)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn19.bind('<Button-1>', Aguarde)
btn19.grid(column=8, row = 2)

btn20 = Button(bottomFrame, text="Caixa 20", bg="white", fg="black", command=Caixa20)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn20.bind('<Button-1>', Aguarde)
btn20.grid(column=9, row = 2)

btn21 = Button(bottomFrame, text="Caixa 21", bg="white", fg="black", command=Caixa21)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn21.bind('<Button-1>', Aguarde)
btn21.grid(column=0, row = 3)

btn22 = Button(bottomFrame, text="Caixa 22", bg="white", fg="black", command=Caixa22)
#btn2.pack(side=LEFT, anchor=W, fill=X, expand=0)
btn22.bind('<Button-1>', Aguarde)
btn22.grid(column=1, row = 3)

btn23 = Button(bottomFrame, text="Caixa 23", bg="white", fg="black", command=Caixa23)
#btn3.pack(side=LEFT, anchor=W, expand=0)
btn23.bind('<Button-1>', Aguarde)
btn23.grid(column=2, row = 3)

btn24 = Button(bottomFrame, text="Caixa 24", bg="white", fg="black", command=Caixa24)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn24.bind('<Button-1>', Aguarde)
btn24.grid(column=3, row = 3)

btn25 = Button(bottomFrame, text="Caixa 25", bg="white", fg="black", command=Caixa25)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn25.bind('<Button-1>', Aguarde)
btn25.grid(column=4, row = 3)

btnSair = Button(bottomFrame, text="SAIR", bg="red", fg="yellow", font="Arial 12", command=gui.quit)
#btnSair.pack(anchor=SE, expand=1)
btnSair.grid(column=11, row = 5)

T = Text(gui, height=5, width=80)
T.place(x = 1, y=140 )
T.insert(END, "(PARA REMARCA)Erros:\n1    - Verificar usúario e senha no Windows\n2    - Verificar arquivos (inicia_pdv.bat / desligar.bat) na pasta PDV\n53   - Verificar cabos de rede\n1326 - Verificar usúario e senha no Windows")

gui.mainloop()