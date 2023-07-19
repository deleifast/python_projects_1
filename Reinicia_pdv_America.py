#encoding: iso-8859-1
import os, time, subprocess
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk


gui = Tk()

bottom13 = Frame(gui)
bottom13.place(x=50, y=270)

bottom14 = Frame(gui)
bottom14.place(x=150, y=270)

bottom15 = Frame(gui)
bottom15.place(x=250, y=270)

bottom16 = Frame(gui)
bottom16.place(x=350, y=270)

bottom17 = Frame(gui)
bottom17.place(x=450, y=270)

bottomSair = Frame(gui)
bottomSair.pack(side=BOTTOM, anchor = SE)


gui.title("PDVCORAL_REMARCA - REDE OMEGA **(LOJA AMERICA)**")
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


def Caixa13():
	if var.get() == 1:
		ret = subprocess.call("taskkill /s 192.168.1.118 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.1.118 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.1.118 ""c:\\pdv\inicia_pdv.bat", shell=True)
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
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.1.118 ""c:\\pdv\desligar.bat", shell=True)
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
		ret = subprocess.call("taskkill /s 192.168.1.104 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.1.104 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.1.104 ""c:\\pdv\inicia_pdv.bat", shell=True)
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
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.1.104 ""c:\\pdv\desligar.bat", shell=True)
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
		ret = subprocess.call("taskkill /s 192.168.1.105 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.1.105 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.1.105 ""c:\\pdv\inicia_pdv.bat", shell=True)
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
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.1.105 ""c:\\pdv\desligar.bat", shell=True)
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
		ret = subprocess.call("taskkill /s 192.168.1.116 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.1.116 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.1.116 ""c:\\pdv\inicia_pdv.bat", shell=True)
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
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.1.116 ""c:\\pdv\desligar.bat", shell=True)
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
		ret = subprocess.call("taskkill /s 192.168.1.106 /u PDV /p pdv /im PDVSAL.EXE", shell=True)
		if ret == 1:
			time.sleep(5)
			resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
			if resp == "ok":
				res = "LIGUE - REMARCA            erro:" + str(ret)
				res_texto(res)
		elif ret == 0:
			subprocess.call("taskkill /s 192.168.1.106 /u PDV /p pdv /im WerFault.exe", shell=True)
			ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.1.106 ""c:\\pdv\inicia_pdv.bat", shell=True)
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
		ret = subprocess.call("psexec.exe -d -i -u pdv\PDV -p pdv \\\\192.168.1.106 ""c:\\pdv\desligar.bat", shell=True)
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


btn13 = Button(bottom13, text="Caixa 13", bg="yellow", width=10, height=2, font="Arial 10", fg="black", command=Caixa13)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn13.bind('<Button-1>', Aguarde)
btn13.pack()

btn14 = Button(bottom14, text="Caixa 14", bg="yellow", width=10, height=2, font="Arial 10", fg="black", command=Caixa14)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn14.bind('<Button-1>', Aguarde)
btn14.pack()

btn15 = Button(bottom15, text="Caixa 15", bg="yellow", width=10, height=2, font="Arial 10", fg="black", command=Caixa15)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn15.bind('<Button-1>', Aguarde)
btn15.pack()

btn16 = Button(bottom16, text="Caixa 16", bg="yellow", width=10, height=2, font="Arial 10", fg="black", command=Caixa16)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn16.bind('<Button-1>', Aguarde)
btn16.pack()

btn17 = Button(bottom17, text="Caixa 17", bg="yellow", width=10, height=2, font="Arial 10", fg="black", command=Caixa17)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn17.bind('<Button-1>', Aguarde)
btn17.pack()

btnSair = Button(bottomSair, text='Sair', bg="red", fg="yellow", width=10, height=2, font="Arial 10", command=gui.quit)
btnSair.bind('<Button-1>', Aguarde)
btnSair.pack()

T = Text(gui, bg="red", fg="yellow", font="Calibri 15", height=5, width=80)
T.place(x = 1, y=140 )
T.insert(END, "(PARA REMARCA)Erros:\n1    - Verificar usúario e senha no Windows(PDV)\n2    - Verificar arquivos (inicia_pdv.bat / desligar.bat) na pasta PDV\n53   - Verificar cabos de rede\n1326 - Verificar usúario e senha no Windows(PDV)")

gui.mainloop()