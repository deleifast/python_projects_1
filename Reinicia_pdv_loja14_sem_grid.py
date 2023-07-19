#encoding: iso-8859-1
import os, time, subprocess
from tkinter import messagebox
from tkinter import *

gui = Tk()

gui.title("PDVCORAL_REMARCA - NAGUMO **(LOJA 14)**")
gui.geometry("800x250")
gui.resizable(0,0)

def sel():
   selection = "CLICOU OPÇÃO: " + str(var.get()) + " DO MENU!!!"
   label.config(text = selection, bg="red", fg="yellow", font="Terminal 12")

var= IntVar()

R1 = Radiobutton(gui, text="1 - Reiniciar CAIXA", variable=var, value=1, font="Arial 10", command=sel)
R1.pack( anchor = W )

R2 = Radiobutton(gui, text="2 - Reiniciar WINDOWS", variable=var, value=2, font="Arial 10", command=sel)
R2.pack( anchor = W )

mensagem= StringVar()
lbl = Label(gui, text="ATENÇÃO : Caixas 05 e 06 NÃO FUCIONAM, USAM WINDOWS XP" , bg="yellow", fg="black", font="Arial 16")
lbl.pack(fill=X)

label = Label(gui)
label.pack()

res = " "

lblaguarde = Label(gui, text= res, font="Arial 20", fg= "red")
lblaguarde.place(x=300, y=110)

def Aguarde(event):
	res = "Aguarde..."
	res_texto(res)
	
def res_texto(res):
    lblaguarde.config(text=res)


def Caixa1():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.141.1 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA"
				res_texto(res)
		elif ret == 0:
			subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.1 ""c:\\pdv\pdvcoral.exe", shell=True)
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 01")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique 2!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.1 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "SEM REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!"
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA"
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
				res = "LIGUE - REMARCA"
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDV  OU  2 - REINICIAR WINDOWS!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)


def Caixa2():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.141.2 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA"
				res_texto(res)
		elif ret == 0:
			subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.2 ""c:\\pdv\pdvcoral.exe", shell=True)
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 02")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 1 ou 2!!!!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.2 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "SEM REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!"
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA"
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
				res = "LIGUE - REMARCA"
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDV  OU  2 - REINICIAR WINDOWS!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!!!!"
				res_texto(res)

		
def Caixa3():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.141.3 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA"
				res_texto(res)
		elif ret == 0:
			subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.3 ""c:\\pdv\pdvcoral.exe", shell=True)
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 03")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 1 ou 2!!!!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.3 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "SEM REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!"
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA"
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
				res = "LIGUE - REMARCA"
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDV  OU  2 - REINICIAR WINDOWS!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!!!!"
				res_texto(res)


def Caixa4():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.141.4 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA"
				res_texto(res)
		elif ret == 0:
			subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.4 ""c:\\pdv\pdvcoral.exe", shell=True)
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 04")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 1 ou 2!!!!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.4 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!"
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA"
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
				res = "LIGUE - REMARCA"
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDV  OU  2 - REINICIAR WINDOWS!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!!!!"
				res_texto(res)


def Caixa7():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.141.7 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA"
				res_texto(res)
		elif ret == 0:
			subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.7 ""c:\\pdv\pdvcoral.exe", shell=True)
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 07")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 1 ou 2!!!!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.7 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!"
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA"
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
				res = "LIGUE - REMARCA"
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDV  OU  2 - REINICIAR WINDOWS!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!!!!"
				res_texto(res)

def Caixa8():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.141.8 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA"
				res_texto(res)
		elif ret == 0:
			subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.8 ""c:\\pdv\pdvcoral.exe", shell=True)
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 08")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 1 ou 2!!!!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.8 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!"
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA"
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
				res = "LIGUE - REMARCA"
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDV  OU  2 - REINICIAR WINDOWS!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!!!!"
				res_texto(res)

def Caixa9():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.141.9 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA"
				res_texto(res)
		elif ret == 0:
			subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.9 ""c:\\pdv\pdvcoral.exe", shell=True)
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 09")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 1 ou 2!!!!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.9 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "SEM REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!"
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA"
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
				res = "LIGUE - REMARCA"
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDV  OU  2 - REINICIAR WINDOWS!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!!!!"
				res_texto(res)

def Caixa10():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.141.10 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA"
				res_texto(res)
		elif ret == 0:
			subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.10 ""c:\\pdv\pdvcoral.exe", shell=True)
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 10")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 1 ou 2!!!!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.10 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!"
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA"
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
				res = "LIGUE - REMARCA"
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDV  OU  2 - REINICIAR WINDOWS!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!!!!"
				res_texto(res)

def Caixa11():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.141.11 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA"
				res_texto(res)
		elif ret == 0:
			subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.11 ""c:\\pdv\pdvcoral.exe", shell=True)
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 11")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 1 ou 2!!!!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.11 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!"
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA"
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
				res = "LIGUE - REMARCA"
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDV  OU  2 - REINICIAR WINDOWS!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!!!!"
				res_texto(res)
	
def Caixa12():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.141.12 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA"
				res_texto(res)
		elif ret == 0:
			subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.12 ""c:\\pdv\pdvcoral.exe", shell=True)
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 12")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 1 ou 2!!!!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.12 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!"
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA"
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
				res = "LIGUE - REMARCA"
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDV  OU  2 - REINICIAR WINDOWS!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!!!!"
				res_texto(res)

def Caixa13():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.141.13 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA"
				res_texto(res)
		elif ret == 0:
			subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.13 ""c:\\pdv\pdvcoral.exe", shell=True)
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 13")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 1 ou 2!!!!!!"
				res_texto(res)
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.13 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!"
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA"
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
				res = "LIGUE - REMARCA"
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDV  OU  2 - REINICIAR WINDOWS!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!!!!"
				res_texto(res)

def Caixa14():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.141.14 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA                 " + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.14 ""c:\\pdv\pdvcoral.exe", shell=True)
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 14")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 2!!!!!!"
				res_texto(res)			
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.14 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!                " + str(ret)
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA                 " + str(ret)
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
				res = "LIGUE - REMARCA                 " + str(ret)
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDV  OU  2 - REINICIAR WINDOWS!")	
		if resp == "ok":
			res = "Clique na opção 1 ou 2!!!!!!"
			res_texto(res)
	
def Caixa15():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.141.15 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA"
				res_texto(res)
		elif ret == 0:
			subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.15 ""c:\\pdv\pdvcoral.exe", shell=True)
			time.sleep(5)
			resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA 15")
			if resp == "ok":
				res = "Pronto!!!"
				res_texto(res)
		else:
			time.sleep(5)
			resp = messagebox.showwarning("Alerta", "CAIXA ESTA NA TELA DO WINDOWS, ESCOLHA O OPÇÃO 2!!!")			
			if resp == "ok":
				res = "Clique na opção 1 ou 2!!!!!!"
				res_texto(res)
			
	elif var.get() == 2:
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.141.15 ""c:\\pdv\desligar.bat", shell=True)
		if ret == 53:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
			if resp == "ok":
				res = "Verificar Rede!!"
				res_texto(res)
		elif ret == 1326:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA"
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
				res = "LIGUE - REMARCA"
				res_texto(res)
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - REINICIAR PDV  OU  2 - REINICIAR WINDOWS!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!!!!"
				res_texto(res)
		
	

btn = Button(gui, text="Caixa 1", bg="white", fg="black", command=Caixa1)
btn.pack(side="left", expand=2)
btn.bind('<Button-1>', Aguarde)

btn = Button(gui, text="Caixa 2", bg="white", fg="black", command=Caixa2)
btn.pack(side="left", expand=2)
btn.bind('<Button-1>', Aguarde)

btn = Button(gui, text="Caixa 3", bg="white", fg="black", command=Caixa3)
btn.pack(side="left", expand=1)
btn.bind('<Button-1>', Aguarde)

btn = Button(gui, text="Caixa 4", bg="white", fg="black", command=Caixa4)
btn.pack(side="left", expand=1)
btn.bind('<Button-1>', Aguarde)

btn = Button(gui, text="Caixa 7", bg="white", fg="black", command=Caixa7)
btn.pack(side="left", expand=1)
btn.bind('<Button-1>', Aguarde)

btn = Button(gui, text="Caixa 8", bg="white", fg="black", command=Caixa8)
btn.pack(side="left", expand=1)
btn.bind('<Button-1>', Aguarde)

btn = Button(gui, text="Caixa 9", bg="white", fg="black", command=Caixa9)
btn.pack(side="left", expand=1)
btn.bind('<Button-1>', Aguarde)

btn = Button(gui, text="Caixa 10", bg="white", fg="black", command=Caixa10)
btn.pack(side="left", expand=1)
btn.bind('<Button-1>', Aguarde)

btn = Button(gui, text="Caixa 11", bg="white", fg="black", command=Caixa11)
btn.pack(side="left", expand=1)
btn.bind('<Button-1>', Aguarde)

btn = Button(gui, text="Caixa 12", bg="white", fg="black", command=Caixa12)
btn.pack(side="left", expand=1)
btn.bind('<Button-1>', Aguarde)

btn = Button(gui, text="Caixa 13", bg="white", fg="black", command=Caixa13)
btn.pack(side="left", expand=1)
btn.bind('<Button-1>', Aguarde)

btn = Button(gui, text="Caixa 14", bg="white", fg="black", command=Caixa14)
btn.pack(side="left", expand=1)
btn.bind('<Button-1>', Aguarde)

btn = Button(gui, text="Caixa 15", bg="white", fg="black", command=Caixa15)
btn.pack(side="left", expand=1)
btn.bind('<Button-1>', Aguarde)

btn = Button(gui, text="SAIR", bg="red", fg="yellow", font="Arial 12", command=gui.quit)
btn.pack(side="bottom")

mensagem1= StringVar()
lblobs = Label(gui, text="TESTE" , bg="yellow", fg="black", font="Arial 16")
lblobs.pack(fill=X)

label = Label(gui)
label.pack()


gui.mainloop()