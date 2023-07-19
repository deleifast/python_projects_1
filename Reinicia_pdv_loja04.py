#encoding: iso-8859-1
import os, time, subprocess
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk

gui = Tk()

bottomFrame = Frame(gui)
bottomFrame.pack(side=BOTTOM, anchor = W)

gui.title("PDVCORAL_REMARCA - NAGUMO **(LOJA 04)**")
gui.geometry("600x320")
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
lbl.place(x=1, y=300)
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
		ret = subprocess.call("taskkill /s 192.168.4.1 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.4.1 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.4.1 ""c:\\pdv\inicia_pdv.bat", shell=True)
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
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.4.1 ""c:\\pdv\desligar.bat", shell=True)
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
		ret = subprocess.call("taskkill /s 192.168.4.2 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.4.2 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.4.2 ""c:\\pdv\inicia_pdv.bat", shell=True)
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
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.4.2 ""c:\\pdv\desligar.bat", shell=True)
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
		ret = subprocess.call("taskkill /s 192.168.4.3 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.4.3 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.4.3 ""c:\\pdv\inicia_pdv.bat", shell=True)
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
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.4.3 ""c:\\pdv\desligar.bat", shell=True)
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
		ret = subprocess.call("taskkill /s 192.168.4.4 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.4.4 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.4.4 ""c:\\pdv\inicia_pdv.bat", shell=True)
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
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.4.4 ""c:\\pdv\desligar.bat", shell=True)
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
		ret = subprocess.call("taskkill /s 192.168.4.5 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.4.5 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.4.5 ""c:\\pdv\inicia_pdv.bat", shell=True)
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
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.4.5 ""c:\\pdv\desligar.bat", shell=True)
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
		ret = subprocess.call("taskkill /s 192.168.4.6 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.4.6 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.4.6 ""c:\\pdv\inicia_pdv.bat", shell=True)
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
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.4.6 ""c:\\pdv\desligar.bat", shell=True)
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
		ret = subprocess.call("taskkill /s 192.168.4.7 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.4.7 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.4.7 ""c:\\pdv\inicia_pdv.bat", shell=True)
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
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.4.7 ""c:\\pdv\desligar.bat", shell=True)
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
		ret = subprocess.call("taskkill /s 192.168.4.8 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.4.8 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.4.8 ""c:\\pdv\inicia_pdv.bat", shell=True)
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
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.4.8 ""c:\\pdv\desligar.bat", shell=True)
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
		ret = subprocess.call("taskkill /s 192.168.4.9 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.4.9 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.4.9 ""c:\\pdv\inicia_pdv.bat", shell=True)
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
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.4.9 ""c:\\pdv\desligar.bat", shell=True)
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

btnSair = Button(bottomFrame, text="SAIR", bg="red", fg="yellow", font="Arial 12", command=gui.quit)
#btnSair.pack(anchor=SE, expand=1)
btnSair.grid(column=11, row = 5)

T = Text(gui, height=5, width=80)
T.place(x = 1, y=140 )
T.insert(END, "(PARA REMARCA)Erros:\n1    - Verificar usúario e senha no Windows\n2    - Verificar arquivos (inicia_pdv.bat / desligar.bat) na pasta PDV\n53   - Verificar cabos de rede\n1326 - Verificar usúario e senha no Windows")

gui.mainloop()