#encoding: iso-8859-1
import os, time, subprocess, shutil, os.path, sys, glob
from tkinter import messagebox
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk


gui = Tk()

bottom = Frame(gui)
bottom.pack(side=BOTTOM, anchor = SE)

chkFrame = Frame(gui)
chkFrame.pack(side=LEFT, anchor = S)

rdButton1 = Frame(gui)
rdButton1.pack(anchor = NW)

rdButton2 = Frame(gui)
rdButton2.pack(anchor = NW)

chkTodas = Frame(gui)
chkTodas.pack(anchor = NW)


gui.title("Reinicia SALCOMM")
gui.geometry("700x570")
gui.resizable(0,0)

load = Image.open("logo_2016.png")
render = ImageTk.PhotoImage(load)
img= Label(gui, image=render)
img.image = render
img.place(x=0, y=0)

def sel():
	res_texto(res)
	selection = "   OPÇÃO: " + str(var.get()) + " DO MENU!!!"
	label.config(text = selection, bg="red", fg="yellow", font="Terminal 12")
	label.place(x=250, y=90)

var= IntVar()
var1 = IntVar()
var2 = IntVar()
var3 = IntVar()
var4 = IntVar()
var6 = IntVar()
var7 = IntVar()
var8 = IntVar()
var9 = IntVar()
var10 = IntVar()
var11 = IntVar()
var12 = IntVar()
var13 = IntVar()
var14 = IntVar()
var15 = IntVar()
var16 = IntVar()
var17 = IntVar()
var18 = IntVar()
var19 = IntVar()
var20 = IntVar()
var21 = IntVar()
var22 = IntVar()
var23 = IntVar()
var24 = IntVar()
var25 = IntVar()
var26 = IntVar()
var27 = IntVar()
var28 = IntVar()
var29 = IntVar()
var30 = IntVar()
var31 = IntVar()
var32 = IntVar()
var33 = IntVar()
var34 = IntVar()
var35 = IntVar()
var36 = IntVar()
var37 = IntVar()
var38 = IntVar()
var39 = IntVar()
var40 = IntVar()
var41 = IntVar()
var42 = IntVar()
var43 = IntVar()
var44 = IntVar()
var45 = IntVar()
var46 = IntVar()
var47 = IntVar()
var48 = IntVar()
var49 = IntVar()


R1 = Radiobutton(rdButton1, text="1 - Programar PRINI", variable=var, value=1, command=sel)
R1.grid(column=0, row = 1)

R2 = Radiobutton(rdButton2, text="2 - Enviar PRINI(RETAG)", variable=var, value=2, command=sel)
R2.grid(column=1, row =1)


def var_states():

	lbltodas = Label(gui, text="                                               ", font = "Arial 15").place(x=260, y=115)

	if (var.get() == 1) or (var.get() == 2):
		
		if var1.get() == 1:
			Loja01()
			chk1.configure(state = 'disabled')
										
		if var2.get() == 1:
			Loja02()
			chk2.configure(state = 'disabled')

		if var3.get() == 1:
			Loja03()
			chk3.configure(state = 'disabled')

		if var4.get() == 1:
			Loja04()
			chk4.configure(state = 'disabled')

		if var6.get() == 1:
			Loja06()
			chk6.configure(state = 'disabled')
	
		if var7.get() == 1:
			Loja07()
			chk7.configure(state = 'disabled')

		if var8.get() == 1:
			Loja08()
			chk8.configure(state = 'disabled')

		if var9.get() == 1:
			Loja09()
			chk9.configure(state = 'disabled')

		if var10.get() == 1:
			Loja10()
			chk10.configure(state = 'disabled')
	
		if var11.get() == 1:
			Loja11()
			chk11.configure(state = 'disabled')

		if var12.get() == 1:
			Loja12()
			chk12.configure(state = 'disabled')

		if var13.get() == 1:
			Loja13()
			chk13.configure(state = 'disabled')

		if var14.get() == 1:
			Loja14()
			chk14.configure(state = 'disabled')
	
		if var15.get() == 1:
			Loja15()
			chk15.configure(state = 'disabled')

		if var16.get() == 1:
			Loja16()
			chk16.configure(state = 'disabled')

		if var17.get() == 1:
			Loja17()
			chk17.configure(state = 'disabled')

		if var18.get() == 1:
			Loja18()
			chk18.configure(state = 'disabled')
	
		if var19.get() == 1:
			Loja19()
			chk19.configure(state = 'disabled')

		if var20.get() == 1:
			Loja20()
			chk20.configure(state = 'disabled')

		if var21.get() == 1:
			Loja21()
			chk21.configure(state = 'disabled')

		if var22.get() == 1:
			Loja22()
			chk22.configure(state = 'disabled')
	
		if var23.get() == 1:
			Loja23()
			chk23.configure(state = 'disabled')

		if var24.get() == 1:
			Loja24()
			chk24.configure(state = 'disabled')

		if var25.get() == 1:
			Loja25()
			chk25.configure(state = 'disabled')

		if var26.get() == 1:
			Loja26()
			chk26.configure(state = 'disabled')
	
		if var27.get() == 1:
			Loja27()
			chk27.configure(state = 'disabled')

		if var28.get() == 1:
			Loja28()
			chk28.configure(state = 'disabled')

		if var29.get() == 1:
			Loja29()
			chk29.configure(state = 'disabled')

		if var30.get() == 1:
			Loja30()
			chk30.configure(state = 'disabled')
	
		if var31.get() == 1:
			Loja31()
			chk31.configure(state = 'disabled')

		if var32.get() == 1:
			Loja32()
			chk32.configure(state = 'disabled')

		if var33.get() == 1:
			Loja33()
			chk33.configure(state = 'disabled')

		if var34.get() == 1:
			Loja34()
			chk34.configure(state = 'disabled')
	
		if var35.get() == 1:
			Loja35()
			chk35.configure(state = 'disabled')

		if var36.get() == 1:
			Loja36()
			chk36.configure(state = 'disabled')

		if var37.get() == 1:
			Loja37()
			chk37.configure(state = 'disabled')

		if var38.get() == 1:
			Loja38()
			chk38.configure(state = 'disabled')
	
		if var39.get() == 1:
			Loja39()
			chk39.configure(state = 'disabled')

		if var40.get() == 1:
			Loja40()
			chk40.configure(state = 'disabled')

		if var41.get() == 1:
			Loja41()
			chk41.configure(state = 'disabled')

		if var42.get() == 1:
			Loja42()
			chk42.configure(state = 'disabled')
	
		if var43.get() == 1:
			Loja43() 
			chk43.configure(state = 'disabled')

		if var44.get() == 1:
			Loja44()
			chk44.configure(state = 'disabled')

		if var45.get() == 1:
			Loja45()
			chk45.configure(state = 'disabled')

		if var46.get() == 1:
			Loja46()
			chk46.configure(state = 'disabled')
	
		if var47.get() == 1:
			Loja47()
			chk47.configure(state = 'disabled')

		if var48.get() == 1:
			Loja48()
			chk48.configure(state = 'disabled')

		if var49.get() == 1:
			Loja49()
			chk49.configure(state = 'disabled')
	
		
		elif(var1.get() != 1) and (var2.get() != 1) and (var3.get() != 1) and (var4.get() != 1) and (var6.get() != 1) and (var7.get() != 1) and (var8.get() != 1) and (var9.get() != 1) and (var10.get() != 1) and (var11.get() != 1) and (var12.get() != 1) and (var13.get() != 1) and (var14.get() != 1) and (var15.get() != 1) and (var16.get() != 1) and (var17.get() != 1) and (var18.get() != 1) and (var19.get() != 1) and (var20.get() != 1) and (var21.get() != 1) and (var22.get() != 1) and (var23.get() != 1) and (var24.get() != 1) and (var25.get() != 1) and (var26.get() != 1) and (var27.get() != 1) and (var28.get() != 1) and (var29.get() != 1) and (var30.get() != 1) and (var31.get() != 1) and (var32.get() != 1) and (var33.get() != 1) and (var34.get() != 1) and (var35.get() != 1) and (var36.get() != 1) and (var37.get() != 1) and (var38.get() != 1) and (var39.get() != 1) and (var40.get() != 1) and (var41.get() != 1) and (var42.get() != 1) and (var43.get() != 1) and (var44.get() != 1) and (var45.get() != 1) and (var46.get() != 1) and (var47.get() != 1) and (var48.get() != 1) and (var49.get() != 1):
			resp = messagebox.showwarning("Alerta", "ESCOLHA UMA LOJA")	
			if resp == "ok":
				res = "Selecione uma ou mais lojas!!!"
				res_texto(res)
		else:
			pass
	else:
		resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Programar PRINI  OU  2 - Enviar PRINI(RETAG)!")	
		if resp == "ok":
				res = "Clique na opção 1 ou 2!!!"
				res_texto(res)

#	lblok = Label(gui, text = "LOJA01: %d\nLOJA02: %d\nLOJA03: %d\nLOJA04: %d" % (var1.get(), var2.get(), var3.get(), var4.get()))
#	lblok.place(x=600, y=350)

def limpar():
	
	lbltodas = Label(gui, text="                                               ", font = "Arial 15").place(x=260, y=115)

	chk1.configure(state = 'normal')
	chk1.deselect()
	chk2.configure(state = 'normal')
	chk2.deselect()
	chk3.configure(state = 'normal')
	chk3.deselect()
	chk4.configure(state = 'normal')
	chk4.deselect()
	chk6.configure(state = 'normal')
	chk6.deselect()
	chk7.configure(state = 'normal')
	chk7.deselect()
	chk8.configure(state = 'normal')
	chk8.deselect()
	chk9.configure(state = 'normal')
	chk9.deselect()
	chk10.configure(state = 'normal')
	chk10.deselect()
	chk11.configure(state = 'normal')
	chk11.deselect()
	chk12.configure(state = 'normal')
	chk12.deselect()
	chk13.configure(state = 'normal')
	chk13.deselect()
	chk14.configure(state = 'normal')
	chk14.deselect()
	chk15.configure(state = 'normal')
	chk15.deselect()
	chk16.configure(state = 'normal')
	chk16.deselect()
	chk17.configure(state = 'normal')
	chk17.deselect()
	chk18.configure(state = 'normal')
	chk18.deselect()
	chk19.configure(state = 'normal')
	chk19.deselect()
	chk20.configure(state = 'normal')
	chk20.deselect()
	chk21.configure(state = 'normal')
	chk21.deselect()
	chk22.configure(state = 'normal')
	chk22.deselect()
	chk23.configure(state = 'normal')
	chk23.deselect()
	chk24.configure(state = 'normal')
	chk24.deselect()
	chk25.configure(state = 'normal')
	chk25.deselect()
	chk26.configure(state = 'normal')
	chk26.deselect()
	chk27.configure(state = 'normal')
	chk27.deselect()
	chk28.configure(state = 'normal')
	chk28.deselect()
	chk29.configure(state = 'normal')
	chk29.deselect()
	chk30.configure(state = 'normal')
	chk30.deselect()
	chk31.configure(state = 'normal')
	chk31.deselect()
	chk32.configure(state = 'normal')
	chk32.deselect()
	chk33.configure(state = 'normal')
	chk33.deselect()
	chk34.configure(state = 'normal')
	chk34.deselect()
	chk35.configure(state = 'normal')
	chk35.deselect()
	chk36.configure(state = 'normal')
	chk36.deselect()
	chk37.configure(state = 'normal')
	chk37.deselect()
	chk38.configure(state = 'normal')
	chk38.deselect()
	chk39.configure(state = 'normal')
	chk39.deselect()
	chk40.configure(state = 'normal')
	chk40.deselect()
	chk41.configure(state = 'normal')
	chk41.deselect()
	chk42.configure(state = 'normal')
	chk42.deselect()
	chk43.configure(state = 'normal')
	chk43.deselect()
	chk44.configure(state = 'normal')
	chk44.deselect()
	chk45.configure(state = 'normal')
	chk45.deselect()
	chk46.configure(state = 'normal')
	chk46.deselect()
	chk47.configure(state = 'normal')
	chk47.deselect()
	chk48.configure(state = 'normal')
	chk48.deselect()
	chk49.configure(state = 'normal')
	chk49.deselect()
	
	Chk.configure(state = 'normal')
	Chk.deselect()

	res = "Escolha novamente a loja(s)     "
	res_texto(res)

def todas():
	res = " "
	res_texto(res)

	chk1.configure(state = 'normal')
	chk1.select()
	chk2.configure(state = 'normal')
	chk2.select()
	chk3.configure(state = 'normal')
	chk3.select()
	chk4.configure(state = 'normal')
	chk4.select()
	chk6.configure(state = 'normal')
	chk6.select()
	chk7.configure(state = 'normal')
	chk7.select()
	chk8.configure(state = 'normal')
	chk8.select()
	chk9.configure(state = 'normal')
	chk9.select()
	chk10.configure(state = 'normal')
	chk10.select()
	chk11.configure(state = 'normal')
	chk11.select()
	chk12.configure(state = 'normal')
	chk12.select()
	chk13.configure(state = 'normal')
	chk13.select()
	chk14.configure(state = 'normal')
	chk14.select()
	chk15.configure(state = 'normal')
	chk15.select()
	chk16.configure(state = 'normal')
	chk16.select()
	chk17.configure(state = 'normal')
	chk17.select()
	chk18.configure(state = 'normal')
	chk18.select()
	chk19.configure(state = 'normal')
	chk19.select()
	chk20.configure(state = 'normal')
	chk20.select()
	chk21.configure(state = 'normal')
	chk21.select()
	chk22.configure(state = 'normal')
	chk22.select()
	chk23.configure(state = 'normal')
	chk23.select()
	chk24.configure(state = 'normal')
	chk24.select()
	chk25.configure(state = 'normal')
	chk25.select()
	chk26.configure(state = 'normal')
	chk26.select()
	chk27.configure(state = 'normal')
	chk27.select()
	chk28.configure(state = 'normal')
	chk28.select()
	chk29.configure(state = 'normal')
	chk29.select()
	chk30.configure(state = 'normal')
	chk30.select()
	chk31.configure(state = 'normal')
	chk31.select()
	chk32.configure(state = 'normal')
	chk32.select()
	chk33.configure(state = 'normal')
	chk33.select()
	chk34.configure(state = 'normal')
	chk34.select()
	chk35.configure(state = 'normal')
	chk35.select()
	chk36.configure(state = 'normal')
	chk36.select()
	chk37.configure(state = 'normal')
	chk37.select()
	chk38.configure(state = 'normal')
	chk38.select()
	chk39.configure(state = 'normal')
	chk39.select()
	chk40.configure(state = 'normal')
	chk40.select()
	chk41.configure(state = 'normal')
	chk41.select()
	chk42.configure(state = 'normal')
	chk42.select()
	chk43.configure(state = 'normal')
	chk43.select()
	chk44.configure(state = 'normal')
	chk44.select()
	chk45.configure(state = 'normal')
	chk45.select()
	chk46.configure(state = 'normal')
	chk46.select()
	chk47.configure(state = 'normal')
	chk47.select()
	chk48.configure(state = 'normal')
	chk48.select()
	chk49.configure(state = 'normal')
	chk49.select()

	if vartodas.get() == 1:
			Chk.configure(state = 'disabled')


	lbltodas = Label(gui, text="Escolhido todas as lojas!!!    ", fg="red", bg="yellow", font="Arial 15").place(x=260, y=115)
	
vartodas = IntVar()

Chk = Checkbutton(chkTodas, text="Escolher TODAS AS LOJAS", variable=vartodas, command=todas)
Chk.grid(column=1, row =1)

mensagem= StringVar()
lbl = Label(gui, text="Digite os parâmetros separados por virgula: " , fg="red", font="Arial 10")
lbl.place(x=1, y=145)

chave = tk.StringVar()
#entry = tk.Entry(gui, textvariable=chave, width=50).place(x=260, y=145)
entry = tk.Entry(gui, textvariable=chave, width=50, bd =4)
entry.place(x=260, y=145)
entry.focus()


mensagem= StringVar()
lbl = Label(gui, text="Escolha a loja: " , fg="blue", font="Calibri 12 bold")
lbl.place(x=1, y=285)

mensagem= StringVar()
lbl = Label(gui, text="Versão 1.0" , fg="black", font="Arial 8")
lbl.place(x=1, y=550)

label = Label(gui)
label.pack()

res = " "

lblaguarde = Label(gui, text= res, font="Arial 15", fg= "red")
lblaguarde.place(x=250, y=90)

def Aguarde(event):
	res = "        Aguarde...                     "
	res_texto(res)

	
def res_texto(res):
    lblaguarde.config(text=res)

def Loja01():
	if var.get() == 1:
		os.chdir('c:\\PDV\PRINI')
		if os.path.exists("C:\PDV\PRINI\loja1"):
			res = "Pasta loja1 já existe, será apagada!!!                       "
			res_texto(res)
#			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja1')
			dir = './loja1'
			os.makedirs(dir)
#			resp = messagebox.showinfo("Informação", "Recriado Pasta loja1")
		else:
			dir = './loja1'
			os.makedirs(dir)
#			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja1")
			res = "Criado nova pasta loja1                                     "
			res_texto(res)

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?")
		if result == 'yes':
#			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA01.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA01.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA01.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja1'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja1')
		for el in range(101, 125):
			shutil.copy('PRINI_LOJA01.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 01"
		res_texto(res)
		


	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.1.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja1/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 01'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 01, verificar!"
			res_texto(res)

		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja02():
	os.chdir('c:\\PDV\PRINI')
	if var.get() == 1:
		if os.path.exists("C:\PDV\PRINI\loja2"):
			res = "Pasta loja2 já existe, será apagada!!!                       "
			res_texto(res)
#			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja2')
			dir = './loja2'
			os.makedirs(dir)
#			resp = messagebox.showinfo("Informação", "Recriado Pasta loja2")
		else:
			dir = './loja2'
			os.makedirs(dir)
			time.sleep(5)
#			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja2")
			res = "Criado nova pasta loja2                                     "
			res_texto(res)

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
#			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA02.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA02.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA02.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja2'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja2')
		for el in range(101, 121):
			shutil.copy('PRINI_LOJA02.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 02"
		res_texto(res)

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.2.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja2/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 02'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 02, verificar!"
			res_texto(res)
				

		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja03():
	if var.get() == 1:
		os.chdir('c:\\PDV\PRINI')
		if os.path.exists("C:\PDV\PRINI\loja3"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja3')
			dir = './loja3'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja3")
		else:
			dir = './loja3'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja3")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA03.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA03.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA03.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja3'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja3')
		for el in range(101, 121):
			shutil.copy('PRINI_LOJA03.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 03"
		res_texto(res)
			

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.3.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja3/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 03'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 03, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja04():
	os.chdir('c:\\PDV\PRINI')
	if var.get() == 1:
		if os.path.exists("C:\PDV\PRINI\loja4"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja4')
			dir = './loja4'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja4")
		else:
			dir = './loja4'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja4")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA04.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA04.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA04.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja4'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja4')
		for el in range(101, 110):
			shutil.copy('PRINI_LOJA04.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 04"
		res_texto(res)

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.4.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja4/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 04'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 04, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)

def Loja06():
	if var.get() == 1:
		os.chdir('c:\\PDV\PRINI')
		if os.path.exists("C:\PDV\PRINI\loja6"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja6')
			dir = './loja6'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja6")
		else:
			dir = './loja6'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja6")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA06.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA06.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA06.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja6'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja6')
		for el in range(101, 110):
			shutil.copy('PRINI_LOJA06.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 06"
		res_texto(res)
			

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.6.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja6/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 06'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 06, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja07():
	os.chdir('c:\\PDV\PRINI')
	if var.get() == 1:
		if os.path.exists("C:\PDV\PRINI\loja7"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja7')
			dir = './loja7'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja7")
		else:
			dir = './loja7'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja7")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA07.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA07.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA07.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja7'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja7')
		for el in range(101, 132):
			shutil.copy('PRINI_LOJA07.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 07"
		res_texto(res)

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.7.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja7/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 07'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 07, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja08():
	if var.get() == 1:
		os.chdir('c:\\PDV\PRINI')
		if os.path.exists("C:\PDV\PRINI\loja8"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja8')
			dir = './loja8'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja8")
		else:
			dir = './loja8'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja8")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA08.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA08.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA08.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja8'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja8')
		for el in range(101, 141):
			shutil.copy('PRINI_LOJA08.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 08"
		res_texto(res)
			

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.8.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja8/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 08'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 08, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja09():
	os.chdir('c:\\PDV\PRINI')
	if var.get() == 1:
		if os.path.exists("C:\PDV\PRINI\loja9"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja9')
			dir = './loja9'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja9")
		else:
			dir = './loja9'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja9")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA09.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA09.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA09.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja9'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja9')
		for el in range(101, 120):
			shutil.copy('PRINI_LOJA09.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 09"
		res_texto(res)

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.9.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja9/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 09'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 09, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)

def Loja10():
	if var.get() == 1:
		os.chdir('c:\\PDV\PRINI')
		if os.path.exists("C:\PDV\PRINI\loja1"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja10')
			dir = './loja10'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja10")
		else:
			dir = './loja10'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja10")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA10.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA10.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA10.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja10'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja10')
		for el in range(101, 110):
			shutil.copy('PRINI_LOJA10.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 10"
		res_texto(res)
			

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.10.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja10/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 10'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 10, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja11():
	os.chdir('c:\\PDV\PRINI')
	if var.get() == 1:
		if os.path.exists("C:\PDV\PRINI\loja11"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja11')
			dir = './loja11'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja11")
		else:
			dir = './loja11'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja11")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA11.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA11.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA11.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja11'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja11')
		for el in range(101, 132):
			shutil.copy('PRINI_LOJA11.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 11"
		res_texto(res)

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.11.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja11/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 11'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 11, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja12():
	if var.get() == 1:
		os.chdir('c:\\PDV\PRINI')
		if os.path.exists("C:\PDV\PRINI\loja12"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja12')
			dir = './loja12'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja12")
		else:
			dir = './loja12'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja12")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA12.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA12.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA12.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja12'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja12')
		for el in range(101, 119):
			shutil.copy('PRINI_LOJA12.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 12"
		res_texto(res)
			

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.12.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja12/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 12'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 12, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja13():
	os.chdir('c:\\PDV\PRINI')
	if var.get() == 1:
		if os.path.exists("C:\PDV\PRINI\loja13"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja13')
			dir = './loja13'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja13")
		else:
			dir = './loja13'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja13")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA13.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA13.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA13.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja13'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja13')
		for el in range(101, 121):
			shutil.copy('PRINI_LOJA13.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 13"
		res_texto(res)

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.13.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja13/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 13'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 13, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)

def Loja14():
	if var.get() == 1:
		os.chdir('c:\\PDV\PRINI')
		if os.path.exists("C:\PDV\PRINI\loja14"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja14')
			dir = './loja14'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja14")
		else:
			dir = './loja14'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja14")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA14.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA14.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
	
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA14.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja14'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja14')
		shutil.copy('PRINI_LOJA14.TXT' , 'PRINI.101')
		shutil.copy('PRINI_LOJA14.TXT' , 'PRINI.102')
		shutil.copy('PRINI_LOJA14.TXT' , 'PRINI.105')
		shutil.copy('PRINI_LOJA14.TXT' , 'PRINI.110')
		shutil.copy('PRINI_LOJA14.TXT' , 'PRINI.111')
		shutil.copy('PRINI_LOJA14.TXT' , 'PRINI.115')
		shutil.copy('PRINI_LOJA14.TXT' , 'PRINI.118')
		shutil.copy('PRINI_LOJA14.TXT' , 'PRINI.119')
		shutil.copy('PRINI_LOJA14.TXT' , 'PRINI.120')
		shutil.copy('PRINI_LOJA14.TXT' , 'PRINI.121')
		shutil.copy('PRINI_LOJA14.TXT' , 'PRINI.122')
		shutil.copy('PRINI_LOJA14.TXT' , 'PRINI.123')
		shutil.copy('PRINI_LOJA14.TXT' , 'PRINI.124')
		shutil.copy('PRINI_LOJA14.TXT' , 'PRINI.125')
		shutil.copy('PRINI_LOJA14.TXT' , 'PRINI.126')

		res = "Copiados com sucesso na pasta loja 14"
		res_texto(res)
			

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.141.150\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja14/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 14'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 14, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja15():
	os.chdir('c:\\PDV\PRINI')
	if var.get() == 1:
		if os.path.exists("C:\PDV\PRINI\loja15"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja15')
			dir = './loja15'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja15")
		else:
			dir = './loja15'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja15")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA15.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA15.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA15.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja15'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja15')
		for el in range(101, 121):
			shutil.copy('PRINI_LOJA15.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 15"
		res_texto(res)

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.15.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja15/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 15'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 15, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja16():
	if var.get() == 1:
		os.chdir('c:\\PDV\PRINI')
		if os.path.exists("C:\PDV\PRINI\loja16"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja16')
			dir = './loja16'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja16")
		else:
			dir = './loja16'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja16")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA16.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA16.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA16.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja16'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja16')
		for el in range(101, 117):
			shutil.copy('PRINI_LOJA16.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 16"
		res_texto(res)
			

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.16.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja16/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 16'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 16, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja17():
	os.chdir('c:\\PDV\PRINI')
	if var.get() == 1:
		if os.path.exists("C:\PDV\PRINI\loja17"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja17')
			dir = './loja17'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja17")
		else:
			dir = './loja17'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja17")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA17.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA17.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA17.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja17'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja17')
		for el in range(101, 125):
			shutil.copy('PRINI_LOJA17.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 17"
		res_texto(res)

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.17.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja17/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 17'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 17, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)

def Loja18():
	if var.get() == 1:
		os.chdir('c:\\PDV\PRINI')
		if os.path.exists("C:\PDV\PRINI\loja18"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja18')
			dir = './loja18'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja18")
		else:
			dir = './loja18'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja18")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA18.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA18.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA18.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja18'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja18')
		for el in range(101, 118):
			shutil.copy('PRINI_LOJA18.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 18"
		res_texto(res)
			

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.18.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja18/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 18'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 18, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja19():
	os.chdir('c:\\PDV\PRINI')
	if var.get() == 1:
		if os.path.exists("C:\PDV\PRINI\loja19"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja19')
			dir = './loja19'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja19")
		else:
			dir = './loja19'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja19")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA19.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA19.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA19.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja19'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja19')
		for el in range(101, 110):
			shutil.copy('PRINI_LOJA19.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 19"
		res_texto(res)

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.19.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja19/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 19'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 19, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja20():
	if var.get() == 1:
		os.chdir('c:\\PDV\PRINI')
		if os.path.exists("C:\PDV\PRINI\loja20"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja20')
			dir = './loja20'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja20")
		else:
			dir = './loja20'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja20")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA20.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA20.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA20.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja20'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja20')
		shutil.copy('PRINI_LOJA20.TXT', 'PRINI.101')
		shutil.copy('PRINI_LOJA20.TXT', 'PRINI.102')
		shutil.copy('PRINI_LOJA20.TXT', 'PRINI.103')
		shutil.copy('PRINI_LOJA20.TXT', 'PRINI.104')
		shutil.copy('PRINI_LOJA20.TXT', 'PRINI.106')
		shutil.copy('PRINI_LOJA20.TXT', 'PRINI.107')
		shutil.copy('PRINI_LOJA20.TXT', 'PRINI.109')
		shutil.copy('PRINI_LOJA20.TXT', 'PRINI.110')
		shutil.copy('PRINI_LOJA20.TXT', 'PRINI.111')
		shutil.copy('PRINI_LOJA20.TXT', 'PRINI.112')
		shutil.copy('PRINI_LOJA20.TXT', 'PRINI.113')
		shutil.copy('PRINI_LOJA20.TXT', 'PRINI.114')
		shutil.copy('PRINI_LOJA20.TXT', 'PRINI.115')
		shutil.copy('PRINI_LOJA20.TXT', 'PRINI.116')
		shutil.copy('PRINI_LOJA20.TXT', 'PRINI.118')
		shutil.copy('PRINI_LOJA20.TXT', 'PRINI.119')
	
		res = "Copiados com sucesso na pasta loja 20"
		res_texto(res)
			

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.20.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja20/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 20'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 20, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja21():
	os.chdir('c:\\PDV\PRINI')
	if var.get() == 1:
		if os.path.exists("C:\PDV\PRINI\loja21"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja21')
			dir = './loja21'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja21")
		else:
			dir = './loja21'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja21")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA21.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA21.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA21.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja21'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja21')
		for el in range(101, 124):
			shutil.copy('PRINI_LOJA21.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 21"
		res_texto(res)

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.21.100\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja21/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 21'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 21, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)

def Loja22():
	if var.get() == 1:
		os.chdir('c:\\PDV\PRINI')
		if os.path.exists("C:\PDV\PRINI\loja22"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja22')
			dir = './loja22'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja22")
		else:
			dir = './loja22'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja22")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA22.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA22.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA22.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja22'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja22')
		for el in range(101, 123):
			shutil.copy('PRINI_LOJA22.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 22"
		res_texto(res)
			

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.22.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja22/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 22'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 22, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja23():
	os.chdir('c:\\PDV\PRINI')
	if var.get() == 1:
		if os.path.exists("C:\PDV\PRINI\loja23"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja23')
			dir = './loja23'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja23")
		else:
			dir = './loja23'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja23")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA23.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA23.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA23.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja23'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja23')
		for el in range(101, 126):
			shutil.copy('PRINI_LOJA23.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 23"
		res_texto(res)

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.23.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja23/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 23'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 23, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja24():
	if var.get() == 1:
		os.chdir('c:\\PDV\PRINI')
		if os.path.exists("C:\PDV\PRINI\loja24"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja24')
			dir = './loja24'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja24")
		else:
			dir = './loja24'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja24")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA24.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA24.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA24.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja24'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja24')
		for el in range(101, 122):
			shutil.copy('PRINI_LOJA24.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 24"
		res_texto(res)
			

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.24.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja24/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 24'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 24, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja25():
	os.chdir('c:\\PDV\PRINI')
	if var.get() == 1:
		if os.path.exists("C:\PDV\PRINI\loja25"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja25')
			dir = './loja25'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja25")
		else:
			dir = './loja25'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja25")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA25.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA25.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA25.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja25'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja25')
		for el in range(101, 117):
			shutil.copy('PRINI_LOJA25.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 25"
		res_texto(res)

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.25.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja25/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 25'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 25, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)

def Loja26():
	if var.get() == 1:
		os.chdir('c:\\PDV\PRINI')
		if os.path.exists("C:\PDV\PRINI\loja26"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja26')
			dir = './loja26'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja26")
		else:
			dir = './loja26'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja26")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA26.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA26.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA26.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja26'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja26')
		for el in range(101, 132):
			shutil.copy('PRINI_LOJA26.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 26"
		res_texto(res)
			

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.26.150\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja26/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 26'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 26, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja27():
	os.chdir('c:\\PDV\PRINI')
	if var.get() == 1:
		if os.path.exists("C:\PDV\PRINI\loja27"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja27')
			dir = './loja27'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja27")
		else:
			dir = './loja27'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja27")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA27.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA27.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA27.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja27'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja27')
		for el in range(101, 122):
			shutil.copy('PRINI_LOJA27.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 27"
		res_texto(res)

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.27.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja27/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 27'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 27, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja28():
	if var.get() == 1:
		os.chdir('c:\\PDV\PRINI')
		if os.path.exists("C:\PDV\PRINI\loja28"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja28')
			dir = './loja28'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja28")
		else:
			dir = './loja28'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja28")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA28.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA28.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA28.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja28'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja28')
		for el in range(101, 116):
			shutil.copy('PRINI_LOJA28.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja28"
		res_texto(res)
			

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.28.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja28/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 28'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 28, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja29():
	os.chdir('c:\\PDV\PRINI')
	if var.get() == 1:
		if os.path.exists("C:\PDV\PRINI\loja29"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja29')
			dir = './loja29'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja29")
		else:
			dir = './loja29'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja29")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA29.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA29.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA29.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja29'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja29')
		for el in range(101, 116):
			shutil.copy('PRINI_LOJA29.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 29"
		res_texto(res)

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.29.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja29/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 29'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 29, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)

def Loja30():
	if var.get() == 1:
		os.chdir('c:\\PDV\PRINI')
		if os.path.exists("C:\PDV\PRINI\loja30"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja30')
			dir = './loja30'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja30")
		else:
			dir = './loja30'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja30")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA30.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA30.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA30.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja30'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja30')
		shutil.copy('PRINI_LOJA30.TXT' , 'PRINI.002')
		shutil.copy('PRINI_LOJA30.TXT' , 'PRINI.003')
		shutil.copy('PRINI_LOJA30.TXT' , 'PRINI.004')
		shutil.copy('PRINI_LOJA30.TXT' , 'PRINI.005')
		shutil.copy('PRINI_LOJA30.TXT' , 'PRINI.006')
		shutil.copy('PRINI_LOJA30.TXT' , 'PRINI.007')
		shutil.copy('PRINI_LOJA30.TXT' , 'PRINI.010')
		shutil.copy('PRINI_LOJA30.TXT' , 'PRINI.011')
		shutil.copy('PRINI_LOJA30.TXT' , 'PRINI.012')
		shutil.copy('PRINI_LOJA30.TXT' , 'PRINI.013')
		shutil.copy('PRINI_LOJA30.TXT' , 'PRINI.014')
		shutil.copy('PRINI_LOJA30.TXT' , 'PRINI.015')
		shutil.copy('PRINI_LOJA30.TXT' , 'PRINI.016')
		shutil.copy('PRINI_LOJA30.TXT' , 'PRINI.017')
		shutil.copy('PRINI_LOJA30.TXT' , 'PRINI.018')
		shutil.copy('PRINI_LOJA30.TXT' , 'PRINI.019')
		shutil.copy('PRINI_LOJA30.TXT' , 'PRINI.020')
		shutil.copy('PRINI_LOJA30.TXT' , 'PRINI.021')
		shutil.copy('PRINI_LOJA30.TXT' , 'PRINI.022')
		shutil.copy('PRINI_LOJA30.TXT' , 'PRINI.023')
		shutil.copy('PRINI_LOJA30.TXT' , 'PRINI.024')
		shutil.copy('PRINI_LOJA30.TXT' , 'PRINI.025')
		shutil.copy('PRINI_LOJA30.TXT' , 'PRINI.026')
		shutil.copy('PRINI_LOJA30.TXT' , 'PRINI.027')

		res = "Copiados com sucesso na pasta loja 30"
		res_texto(res)
			

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.30.102\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja30/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 30'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 30, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja31():
	os.chdir('c:\\PDV\PRINI')
	if var.get() == 1:
		if os.path.exists("C:\PDV\PRINI\loja31"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja31')
			dir = './loja31'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja31")
		else:
			dir = './loja31'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja31")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA31.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA31.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA31.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja31'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja31')
		shutil.copy('PRINI_LOJA31.TXT' , 'PRINI.101')
		shutil.copy('PRINI_LOJA31.TXT' , 'PRINI.102')
		shutil.copy('PRINI_LOJA31.TXT' , 'PRINI.104')
		shutil.copy('PRINI_LOJA31.TXT' , 'PRINI.106')
		shutil.copy('PRINI_LOJA31.TXT' , 'PRINI.108')
		shutil.copy('PRINI_LOJA31.TXT' , 'PRINI.110')
		shutil.copy('PRINI_LOJA31.TXT' , 'PRINI.114')
		shutil.copy('PRINI_LOJA31.TXT' , 'PRINI.115')
		shutil.copy('PRINI_LOJA31.TXT' , 'PRINI.116')
		shutil.copy('PRINI_LOJA31.TXT' , 'PRINI.117')
		shutil.copy('PRINI_LOJA31.TXT' , 'PRINI.118')
		shutil.copy('PRINI_LOJA31.TXT' , 'PRINI.119')

		res = "Copiados com sucesso na pasta loja 31"
		res_texto(res)

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.31.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja31/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 31'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 31, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja32():
	if var.get() == 1:
		os.chdir('c:\\PDV\PRINI')
		if os.path.exists("C:\PDV\PRINI\loja32"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja32')
			dir = './loja32'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja32")
		else:
			dir = './loja32'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja32")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA32.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA32.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA32.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja32'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja32')
		shutil.copy('PRINI_LOJA32.TXT' , 'PRINI.102')
		shutil.copy('PRINI_LOJA32.TXT' , 'PRINI.104')
		shutil.copy('PRINI_LOJA32.TXT' , 'PRINI.105')
		shutil.copy('PRINI_LOJA32.TXT' , 'PRINI.106')
		shutil.copy('PRINI_LOJA32.TXT' , 'PRINI.111')
		shutil.copy('PRINI_LOJA32.TXT' , 'PRINI.112')
		shutil.copy('PRINI_LOJA32.TXT' , 'PRINI.113')
		shutil.copy('PRINI_LOJA32.TXT' , 'PRINI.114')
		shutil.copy('PRINI_LOJA32.TXT' , 'PRINI.115')
		shutil.copy('PRINI_LOJA32.TXT' , 'PRINI.118')
		shutil.copy('PRINI_LOJA32.TXT' , 'PRINI.119')
		shutil.copy('PRINI_LOJA32.TXT' , 'PRINI.120')

		res = "Copiados com sucesso na pasta loja 32"
		res_texto(res)
			

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.32.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja32/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 32'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 32, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja33():
	os.chdir('c:\\PDV\PRINI')
	if var.get() == 1:
		if os.path.exists("C:\PDV\PRINI\loja33"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja33')
			dir = './loja33'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja33")
		else:
			dir = './loja33'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja33")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA33.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA33.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA33.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja33'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja33')
		shutil.copy('PRINI_LOJA33.TXT' , 'PRINI.105')
		shutil.copy('PRINI_LOJA33.TXT' , 'PRINI.107')
		shutil.copy('PRINI_LOJA33.TXT' , 'PRINI.109')
		shutil.copy('PRINI_LOJA33.TXT' , 'PRINI.110')
		shutil.copy('PRINI_LOJA33.TXT' , 'PRINI.111')
		shutil.copy('PRINI_LOJA33.TXT' , 'PRINI.113')
		shutil.copy('PRINI_LOJA33.TXT' , 'PRINI.114')
		shutil.copy('PRINI_LOJA33.TXT' , 'PRINI.115')
		shutil.copy('PRINI_LOJA33.TXT' , 'PRINI.116')
		shutil.copy('PRINI_LOJA33.TXT' , 'PRINI.117')

		res = "Copiados com sucesso na pasta loja 33"
		res_texto(res)

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.33.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja33/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 33'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 33, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)

def Loja34():
	if var.get() == 1:
		os.chdir('c:\\PDV\PRINI')
		if os.path.exists("C:\PDV\PRINI\loja34"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja34')
			dir = './loja34'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja34")
		else:
			dir = './loja34'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja34")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA34.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA34.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA34.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja34'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja34')
		shutil.copy('PRINI_LOJA34.TXT' , 'PRINI.101')
		shutil.copy('PRINI_LOJA34.TXT' , 'PRINI.102')
		shutil.copy('PRINI_LOJA34.TXT' , 'PRINI.104')
		shutil.copy('PRINI_LOJA34.TXT' , 'PRINI.105')
		shutil.copy('PRINI_LOJA34.TXT' , 'PRINI.106')
		shutil.copy('PRINI_LOJA34.TXT' , 'PRINI.110')
		shutil.copy('PRINI_LOJA34.TXT' , 'PRINI.111')
		shutil.copy('PRINI_LOJA34.TXT' , 'PRINI.112')
		shutil.copy('PRINI_LOJA34.TXT' , 'PRINI.113')

		res = "Copiados com sucesso na pasta loja 34"
		res_texto(res)
			

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.34.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja34/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 34'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 34, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja35():
	os.chdir('c:\\PDV\PRINI')
	if var.get() == 1:
		if os.path.exists("C:\PDV\PRINI\loja35"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja35')
			dir = './loja35'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja35")
		else:
			dir = './loja35'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja35")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA35.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA35.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA35.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja35'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja35')
		shutil.copy ('PRINI_LOJA35.TXT' , 'PRINI.101')
		shutil.copy ('PRINI_LOJA35.TXT' , 'PRINI.102')
		shutil.copy ('PRINI_LOJA35.TXT' , 'PRINI.103')
		shutil.copy ('PRINI_LOJA35.TXT' , 'PRINI.104')
		shutil.copy ('PRINI_LOJA35.TXT' , 'PRINI.105')
		shutil.copy ('PRINI_LOJA35.TXT' , 'PRINI.106')
		shutil.copy ('PRINI_LOJA35.TXT' , 'PRINI.110')
		shutil.copy ('PRINI_LOJA35.TXT' , 'PRINI.111')
		shutil.copy ('PRINI_LOJA35.TXT' , 'PRINI.112')
		shutil.copy ('PRINI_LOJA35.TXT' , 'PRINI.113')

		res = "Copiados com sucesso na pasta loja 35"
		res_texto(res)

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.35.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja35/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 35'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 35, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja36():
	if var.get() == 1:
		os.chdir('c:\\PDV\PRINI')
		if os.path.exists("C:\PDV\PRINI\loja36"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja36')
			dir = './loja36'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja36")
		else:
			dir = './loja36'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja36")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA36.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA36.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA36.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja36'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja36')
		for el in range(101, 119):
			shutil.copy('PRINI_LOJA36.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 36"
		res_texto(res)
			

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.36.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja36/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 36'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 36, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja37():
	os.chdir('c:\\PDV\PRINI')
	if var.get() == 1:
		if os.path.exists("C:\PDV\PRINI\loja37"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja37')
			dir = './loja37'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja37")
		else:
			dir = './loja37'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja37")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA37.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA37.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA37.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja37'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja37')
		for el in range(101, 122):
			shutil.copy('PRINI_LOJA37.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 37"
		res_texto(res)

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.37.101C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja37/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 37'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 37, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)

def Loja38():
	if var.get() == 1:
		os.chdir('c:\\PDV\PRINI')
		if os.path.exists("C:\PDV\PRINI\loja38"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja38')
			dir = './loja38'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja38")
		else:
			dir = './loja38'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja38")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA38.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA38.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA38.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja38'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja38')
		shutil.copy ('PRINI_LOJA38.TXT' , 'PRINI.102')
		shutil.copy ('PRINI_LOJA38.TXT' , 'PRINI.103')
		shutil.copy ('PRINI_LOJA38.TXT' , 'PRINI.106')
		shutil.copy ('PRINI_LOJA38.TXT' , 'PRINI.107')
		shutil.copy ('PRINI_LOJA38.TXT' , 'PRINI.108')
		shutil.copy ('PRINI_LOJA38.TXT' , 'PRINI.111')
		shutil.copy ('PRINI_LOJA38.TXT' , 'PRINI.112')
		shutil.copy ('PRINI_LOJA38.TXT' , 'PRINI.113')
		shutil.copy ('PRINI_LOJA38.TXT' , 'PRINI.114')
		shutil.copy ('PRINI_LOJA38.TXT' , 'PRINI.115')
		shutil.copy ('PRINI_LOJA38.TXT' , 'PRINI.116')
		shutil.copy ('PRINI_LOJA38.TXT' , 'PRINI.117')
		shutil.copy ('PRINI_LOJA38.TXT' , 'PRINI.118')
		shutil.copy ('PRINI_LOJA38.TXT' , 'PRINI.119')
		shutil.copy ('PRINI_LOJA38.TXT' , 'PRINI.121')
		shutil.copy ('PRINI_LOJA38.TXT' , 'PRINI.122')
		shutil.copy ('PRINI_LOJA38.TXT' , 'PRINI.124')
		shutil.copy ('PRINI_LOJA38.TXT' , 'PRINI.125')
		shutil.copy ('PRINI_LOJA38.TXT' , 'PRINI.126')
		shutil.copy ('PRINI_LOJA38.TXT' , 'PRINI.127')

		res = "Copiados com sucesso na pasta loja 38"
		res_texto(res)
			

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.38.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja38/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 38'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 38, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja39():
	os.chdir('c:\\PDV\PRINI')
	if var.get() == 1:
		if os.path.exists("C:\PDV\PRINI\loja39"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja39')
			dir = './loja39'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja39")
		else:
			dir = './loja39'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja39")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA39.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA39.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA39.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja39'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja39')
		for el in range(101, 124):
			shutil.copy('PRINI_LOJA39.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 39"
		res_texto(res)

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.39.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja39/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 39'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 39, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja40():
	if var.get() == 1:
		os.chdir('c:\\PDV\PRINI')
		if os.path.exists("C:\PDV\PRINI\loja40"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja40')
			dir = './loja40'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja40")
		else:
			dir = './loja40'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja40")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA40.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA40.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA40.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja40'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja40')
		for el in range(101, 117):
			shutil.copy('PRINI_LOJA40.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 40"
		res_texto(res)
			

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.40.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja40/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 40'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 40, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja41():
	os.chdir('c:\\PDV\PRINI')
	if var.get() == 1:
		if os.path.exists("C:\PDV\PRINI\loja41"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja41')
			dir = './loja41'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja41")
		else:
			dir = './loja41'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja41")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA41.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA41.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA41.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja41'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja41')
		shutil.copy ('PRINI_LOJA41.TXT' , 'PRINI.002')
		shutil.copy ('PRINI_LOJA41.TXT' , 'PRINI.003')
		shutil.copy ('PRINI_LOJA41.TXT' , 'PRINI.004')
		shutil.copy ('PRINI_LOJA41.TXT' , 'PRINI.005')
		shutil.copy ('PRINI_LOJA41.TXT' , 'PRINI.006')
		shutil.copy ('PRINI_LOJA41.TXT' , 'PRINI.007')
		shutil.copy ('PRINI_LOJA41.TXT' , 'PRINI.008')
		shutil.copy ('PRINI_LOJA41.TXT' , 'PRINI.009')
		shutil.copy ('PRINI_LOJA41.TXT' , 'PRINI.010')
		shutil.copy ('PRINI_LOJA41.TXT' , 'PRINI.011')
		shutil.copy ('PRINI_LOJA41.TXT' , 'PRINI.012')
		shutil.copy ('PRINI_LOJA41.TXT' , 'PRINI.013')
		shutil.copy ('PRINI_LOJA41.TXT' , 'PRINI.014')
		shutil.copy ('PRINI_LOJA41.TXT' , 'PRINI.015')
		shutil.copy ('PRINI_LOJA41.TXT' , 'PRINI.016')
		shutil.copy ('PRINI_LOJA41.TXT' , 'PRINI.017')
		shutil.copy ('PRINI_LOJA41.TXT' , 'PRINI.018')

		res = "Copiados com sucesso na pasta loja 41"
		res_texto(res)

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.41.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja41/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 41'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 41, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)

def Loja42():
	if var.get() == 1:
		os.chdir('c:\\PDV\PRINI')
		if os.path.exists("C:\PDV\PRINI\loja42"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja42')
			dir = './loja42'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja42")
		else:
			dir = './loja42'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja42")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA42.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA42.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA42.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja42'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja42')
		shutil.copy ('PRINI_LOJA42.TXT' , 'PRINI.002')
		shutil.copy ('PRINI_LOJA42.TXT' , 'PRINI.003')
		shutil.copy ('PRINI_LOJA42.TXT' , 'PRINI.004')
		shutil.copy ('PRINI_LOJA42.TXT' , 'PRINI.005')
		shutil.copy ('PRINI_LOJA42.TXT' , 'PRINI.006')
		shutil.copy ('PRINI_LOJA42.TXT' , 'PRINI.007')
		shutil.copy ('PRINI_LOJA42.TXT' , 'PRINI.008')
		shutil.copy ('PRINI_LOJA42.TXT' , 'PRINI.009')
		shutil.copy ('PRINI_LOJA42.TXT' , 'PRINI.010')
		shutil.copy ('PRINI_LOJA42.TXT' , 'PRINI.011')
		shutil.copy ('PRINI_LOJA42.TXT' , 'PRINI.012')
		shutil.copy ('PRINI_LOJA42.TXT' , 'PRINI.013')
		shutil.copy ('PRINI_LOJA42.TXT' , 'PRINI.014')
		shutil.copy ('PRINI_LOJA42.TXT' , 'PRINI.015')
		shutil.copy ('PRINI_LOJA42.TXT' , 'PRINI.016')
		shutil.copy ('PRINI_LOJA42.TXT' , 'PRINI.017')

		res = "Copiados com sucesso na pasta loja 42"
		res_texto(res)
			

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.42.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja42/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 42'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 42, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja43():
	os.chdir('c:\\PDV\PRINI')
	if var.get() == 1:
		if os.path.exists("C:\PDV\PRINI\loja43"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja43')
			dir = './loja43'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja43")
		else:
			dir = './loja43'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja43")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA43.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA43.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA43.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja43'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja43')
		shutil.copy ('PRINI_LOJA43.TXT' , 'PRINI.002')
		shutil.copy ('PRINI_LOJA43.TXT' , 'PRINI.003')
		shutil.copy ('PRINI_LOJA43.TXT' , 'PRINI.004')
		shutil.copy ('PRINI_LOJA43.TXT' , 'PRINI.005')
		shutil.copy ('PRINI_LOJA43.TXT' , 'PRINI.006')
		shutil.copy ('PRINI_LOJA43.TXT' , 'PRINI.007')
		shutil.copy ('PRINI_LOJA43.TXT' , 'PRINI.008')
		shutil.copy ('PRINI_LOJA43.TXT' , 'PRINI.009')
		shutil.copy ('PRINI_LOJA43.TXT' , 'PRINI.010')
		shutil.copy ('PRINI_LOJA43.TXT' , 'PRINI.011')
		shutil.copy ('PRINI_LOJA43.TXT' , 'PRINI.012')
		shutil.copy ('PRINI_LOJA43.TXT' , 'PRINI.013')
		shutil.copy ('PRINI_LOJA43.TXT' , 'PRINI.014')
		shutil.copy ('PRINI_LOJA43.TXT' , 'PRINI.015')
		shutil.copy ('PRINI_LOJA43.TXT' , 'PRINI.016')
		shutil.copy ('PRINI_LOJA43.TXT' , 'PRINI.017')
		shutil.copy ('PRINI_LOJA43.TXT' , 'PRINI.018')
		shutil.copy ('PRINI_LOJA43.TXT' , 'PRINI.019')
		shutil.copy ('PRINI_LOJA43.TXT' , 'PRINI.020')
		shutil.copy ('PRINI_LOJA43.TXT' , 'PRINI.021')
		shutil.copy ('PRINI_LOJA43.TXT' , 'PRINI.022')
		shutil.copy ('PRINI_LOJA43.TXT' , 'PRINI.023')

		res = "Copiados com sucesso na pasta loja 43"
		res_texto(res)

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.43.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja43/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 43'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 43, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja44():
	if var.get() == 1:
		os.chdir('c:\\PDV\PRINI')
		if os.path.exists("C:\PDV\PRINI\loja44"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja44')
			dir = './loja44'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja44")
		else:
			dir = './loja44'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja44")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA44.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA44.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA44.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja44'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja44')
		shutil.copy ('PRINI_LOJA44.TXT' , 'PRINI.002')
		shutil.copy ('PRINI_LOJA44.TXT' , 'PRINI.003')
		shutil.copy ('PRINI_LOJA44.TXT' , 'PRINI.004')
		shutil.copy ('PRINI_LOJA44.TXT' , 'PRINI.005')
		shutil.copy ('PRINI_LOJA44.TXT' , 'PRINI.006')
		shutil.copy ('PRINI_LOJA44.TXT' , 'PRINI.007')
		shutil.copy ('PRINI_LOJA44.TXT' , 'PRINI.008')
		shutil.copy ('PRINI_LOJA44.TXT' , 'PRINI.009')
		shutil.copy ('PRINI_LOJA44.TXT' , 'PRINI.010')
		shutil.copy ('PRINI_LOJA44.TXT' , 'PRINI.011')
		shutil.copy ('PRINI_LOJA44.TXT' , 'PRINI.012')
		shutil.copy ('PRINI_LOJA44.TXT' , 'PRINI.013')
		shutil.copy ('PRINI_LOJA44.TXT' , 'PRINI.014')
		shutil.copy ('PRINI_LOJA44.TXT' , 'PRINI.015')

		res = "Copiados com sucesso na pasta loja 44"
		res_texto(res)
			

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.44.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja44/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 44'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 44, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja45():
	os.chdir('c:\\PDV\PRINI')
	if var.get() == 1:
		if os.path.exists("C:\PDV\PRINI\loja45"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja45')
			dir = './loja45'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja45")
		else:
			dir = './loja45'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja45")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA45.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA45.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA45.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja45'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja45')
		for el in range(69, 99):
			shutil.copy('PRINI_LOJA45.TXT',f'PRINI.0{el}')
		res = "Copiados com sucesso na pasta loja 45"
		res_texto(res)

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.45.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja45/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 45'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 45, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)

def Loja46():
	if var.get() == 1:
		os.chdir('c:\\PDV\PRINI')
		if os.path.exists("C:\PDV\PRINI\loja46"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja46')
			dir = './loja46'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja46")
		else:
			dir = './loja46'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja46")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA46.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA46.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA46.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja46'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja46')
		shutil.copy ('PRINI_LOJA46.TXT' , 'PRINI.003')
		shutil.copy ('PRINI_LOJA46.TXT' , 'PRINI.004')
		shutil.copy ('PRINI_LOJA46.TXT' , 'PRINI.005')
		shutil.copy ('PRINI_LOJA46.TXT' , 'PRINI.007')
		shutil.copy ('PRINI_LOJA46.TXT' , 'PRINI.009')
		shutil.copy ('PRINI_LOJA46.TXT' , 'PRINI.010')
		shutil.copy ('PRINI_LOJA46.TXT' , 'PRINI.011')
		shutil.copy ('PRINI_LOJA46.TXT' , 'PRINI.012')
		shutil.copy ('PRINI_LOJA46.TXT' , 'PRINI.013')
		shutil.copy ('PRINI_LOJA46.TXT' , 'PRINI.015')
		shutil.copy ('PRINI_LOJA46.TXT' , 'PRINI.016')
		shutil.copy ('PRINI_LOJA46.TXT' , 'PRINI.020')
		shutil.copy ('PRINI_LOJA46.TXT' , 'PRINI.021')
		shutil.copy ('PRINI_LOJA46.TXT' , 'PRINI.023')
		shutil.copy ('PRINI_LOJA46.TXT' , 'PRINI.025')
		shutil.copy ('PRINI_LOJA46.TXT' , 'PRINI.026')
		shutil.copy ('PRINI_LOJA46.TXT' , 'PRINI.027')
		shutil.copy ('PRINI_LOJA46.TXT' , 'PRINI.028')
		shutil.copy ('PRINI_LOJA46.TXT' , 'PRINI.029')
		shutil.copy ('PRINI_LOJA46.TXT' , 'PRINI.030')
		shutil.copy ('PRINI_LOJA46.TXT' , 'PRINI.031')

		res = "Copiados com sucesso na pasta loja 46"
		res_texto(res)
			

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.46.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja46/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 46'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 46, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja47():
	os.chdir('c:\\PDV\PRINI')
	if var.get() == 1:
		if os.path.exists("C:\PDV\PRINI\loja47"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja47')
			dir = './loja47'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja47")
		else:
			dir = './loja47'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja47")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA47.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA47.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA47.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja47'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja47')
		for el in range(101, 119):
			shutil.copy('PRINI_LOJA47.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 47"
		res_texto(res)

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.47.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja47/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 47'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 47, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja48():
	if var.get() == 1:
		os.chdir('c:\\PDV\PRINI')
		if os.path.exists("C:\PDV\PRINI\loja48"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja48')
			dir = './loja48'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja48")
		else:
			dir = './loja48'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja48")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA48.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA48.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA48.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja48'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja48')
		for el in range(101, 123):
			shutil.copy('PRINI_LOJA48.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 48"
		res_texto(res)
			

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\192.168.48.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja48/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 48'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 48, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)


def Loja49():
	os.chdir('c:\\PDV\PRINI')
	if var.get() == 1:
		if os.path.exists("C:\PDV\PRINI\loja49"):
			resp = messagebox.showwarning("Alerta", "Pasta já existe, será apagada!!")
			shutil.rmtree('C:\PDV\PRINI\loja49')
			dir = './loja49'
			os.makedirs(dir)
			resp = messagebox.showinfo("Informação", "Recriado Pasta loja49")
		else:
			dir = './loja49'
			os.makedirs(dir)
			time.sleep(5)
			resp = messagebox.showinfo("Informação", "Criado Nova Pasta loja49")

		result = messagebox.askquestion("Exclusão", "Apaga PRINI?", icon='warning')
		if result == 'yes':
			resp = messagebox.showwarning("Alerta", "Arquivo apagado")
			path = "C:\PDV\PRINI"
			dir = os.listdir(path)
			for file in dir:
				if file == "PRINI_LOJA49.TXT":
					os.remove(file)
		else:
			resp = messagebox.showinfo("Informação", "Arquivo sendo alterado!")
			
		c = chave.get()
		with open("PRINI_LOJA49.TXT","a") as PRINI:
			PRINI.write("%s \n" % c)
					
			resp = messagebox.showinfo("Informação", "PRINI GRAVADO!!!")
			
		pasta_ori = 'C://PDV/PRINI'
		arquivo = 'C://PDV/PRINI/PRINI_LOJA49.TXT'
		diretorio = os.listdir(pasta_ori)
		pasta_dest = 'C://PDV/PRINI/loja49'


		shutil.copy(arquivo, pasta_dest)  
		os.chdir('c:\pdv\prini\loja49')
		for el in range(101, 128):
			shutil.copy('PRINI_LOJA49.TXT',f'PRINI.{el}')
		res = "Copiados com sucesso na pasta loja 49"
		res_texto(res)

	elif var.get() == 2:
		# initialize
		driveLetter = 'Q:' 
		networkPath = '\\\\10.132.49.101\C$' 
		user = 'compartilhar' 
		password = 'ruaf305'

		# Connect to map network drive to letter Q
		winCMD = 'NET USE ' + driveLetter + ' ' + networkPath + ' /User:' + user + ' ' + password
		exitcode = subprocess.call(winCMD, shell=True)

		if exitcode == 0:
			
			os.chdir('C:\\')
	
			dest_dir = "Q:\\PDV\TX"
			for file in glob.glob(r'C:/PDV/PRINI/loja49/*.*'):
				shutil.copy(file, dest_dir)
		
				res = 'Copiados com sucesso para a loja 49'
				res_texto(res)
				time.sleep(5)

		else:
			
			exitcode != 0
			
			messagebox.showerror('Erro', 'Arquivos não copiados para o Retag, verifique!')
			res = "Erro conectando Loja 49, verificar!"
			res_texto(res)
				


		# Disconnect anything on drive letter Q
		winCMD = 'NET USE ' + driveLetter + ' /delete'
		subprocess.call(winCMD, shell=True)




chk1 = Checkbutton(chkFrame, text="Loja 01", variable=var1)
chk1.grid(column=0, row =1)

chk2 = Checkbutton(chkFrame, text="Loja 02", variable=var2)
chk2.grid(column=1, row = 1)


chk3 = Checkbutton(chkFrame, text="Loja 03", variable=var3)
chk3.grid(column=2, row =1)


chk4 = Checkbutton(chkFrame, text="Loja 04", variable=var4)
chk4.grid(column=3, row = 1)


chk6 = Checkbutton(chkFrame, text="Loja 06", variable=var6)
chk6.grid(column=4, row = 1)


chk7 = Checkbutton(chkFrame, text="Loja 07", variable=var7)
chk7.grid(column=5, row =1)


chk8 = Checkbutton(chkFrame, text="Loja 08", variable=var8)
chk8.grid(column=6, row = 1)


chk9 = Checkbutton(chkFrame, text="Loja 09", variable=var9)
chk9.grid(column=7, row =1)


chk10 = Checkbutton(chkFrame, text="Loja 10", variable=var10)
chk10.grid(column=0, row = 2)


chk11 = Checkbutton(chkFrame, text="Loja 11", variable=var11)
chk11.grid(column=1, row =2)


chk12 = Checkbutton(chkFrame, text="Loja 12", variable=var12)
chk12.grid(column=2, row = 2)


chk13 = Checkbutton(chkFrame, text="Loja 13", variable=var13)
chk13.grid(column=3, row =2)


chk14 = Checkbutton(chkFrame, text="Loja 14", variable=var14)
chk14.grid(column=4, row = 2)


chk15 = Checkbutton(chkFrame, text="Loja 15", variable=var15)
chk15.grid(column=5, row =2)


chk16 = Checkbutton(chkFrame, text="Loja 16", variable=var16)
chk16.grid(column=6, row = 2)


chk17 = Checkbutton(chkFrame, text="Loja 17", variable=var17)
chk17.grid(column=7, row =2)


chk18 = Checkbutton(chkFrame, text="Loja 18", variable=var18)
chk18.grid(column=0, row = 3)


chk19 = Checkbutton(chkFrame, text="Loja 19", variable=var19)
chk19.grid(column=1, row =3)


chk20 = Checkbutton(chkFrame, text="Loja 20", variable=var20)
chk20.grid(column=2, row = 3)


chk21 = Checkbutton(chkFrame, text="Loja 21", variable=var21)
chk21.grid(column=3, row =3)


chk22 = Checkbutton(chkFrame, text="Loja 22", variable=var22)
chk22.grid(column=4, row = 3)


chk23 = Checkbutton(chkFrame, text="Loja 23", variable=var23)
chk23.grid(column=5, row =3)


chk24 = Checkbutton(chkFrame, text="Loja 24", variable=var24)
chk24.grid(column=6, row = 3)


chk25 = Checkbutton(chkFrame, text="Loja 25", variable=var25)
chk25.grid(column=7, row = 3)


chk26 = Checkbutton(chkFrame, text="Loja 26", variable=var26)
chk26.grid(column=0, row =4)


chk27 = Checkbutton(chkFrame, text="Loja 27", variable=var27)
chk27.grid(column=1, row = 4)


chk28 = Checkbutton(chkFrame, text="Loja 28", variable=var28)
chk28.grid(column=2, row = 4)


chk29 = Checkbutton(chkFrame, text="Loja 29", variable=var29)
chk29.grid(column=3, row =4)


chk30 = Checkbutton(chkFrame, text="Loja 30", variable=var30)
chk30.grid(column=4, row = 4)


chk31 = Checkbutton(chkFrame, text="Loja 31", variable=var31)
chk31.grid(column=5, row =4)


chk32 = Checkbutton(chkFrame, text="Loja 32", variable=var32)
chk32.grid(column=6, row = 4)


chk33 = Checkbutton(chkFrame, text="Loja 33", variable=var33)
chk33.grid(column=7, row =4)


chk34 = Checkbutton(chkFrame, text="Loja 34", variable=var34)
chk34.grid(column=0, row = 5)


chk35 = Checkbutton(chkFrame, text="Loja 35", variable=var35)
chk35.grid(column=1, row =5)


chk36 = Checkbutton(chkFrame, text="Loja 36", variable=var36)
chk36.grid(column=2, row = 5)


chk37 = Checkbutton(chkFrame, text="Loja 37", variable=var37)
chk37.grid(column=3, row =5)


chk38 = Checkbutton(chkFrame, text="Loja 38", variable=var38)
chk38.grid(column=4, row = 5)


chk39 = Checkbutton(chkFrame, text="Loja 39", variable=var39)
chk39.grid(column=5, row =5)


chk40 = Checkbutton(chkFrame, text="Loja 40", variable=var40)
chk40.grid(column=6, row = 5)


chk41 = Checkbutton(chkFrame, text="Loja 41", variable=var41)
chk41.grid(column=7, row =5)


chk42 = Checkbutton(chkFrame, text="Loja 42", variable=var42)
chk42.grid(column=0, row = 6)


chk43 = Checkbutton(chkFrame, text="Loja 43", variable=var43)
chk43.grid(column=1, row =6)


chk44 = Checkbutton(chkFrame, text="Loja 44", variable=var44)
chk44.grid(column=2, row = 6)


chk45 = Checkbutton(chkFrame, text="Loja 45", variable=var45)
chk45.grid(column=3, row = 6)


chk46 = Checkbutton(chkFrame, text="Loja 46", variable=var46)
chk46.grid(column=4, row = 6)


chk47 = Checkbutton(chkFrame, text="Loja 47", variable=var47)
chk47.grid(column=5, row =6)


chk48 = Checkbutton(chkFrame, text="Loja 48", variable=var48)
chk48.grid(column=6, row = 6)


chk49 = Checkbutton(chkFrame, text="Loja 49", variable=var49)
chk49.grid(column=7, row = 6)

btnLimpar = Button(bottom, text='Limpar', bg="grey", fg="black", width=7, height=1, font="Arial 10", command=limpar)
btnLimpar.bind('<Button-1>', Aguarde)
btnLimpar.grid()

btnExecutar = Button(bottom, text='Executar', bg="yellow", fg="red", width=7, height=1, font="Arial 10", command=var_states)
btnExecutar.bind('<Button-1>', Aguarde)
btnExecutar.grid()

btnSair = Button(bottom, text='Sair', bg="red", fg="yellow", width=7, height=1, font="Arial 10", command=gui.quit)
btnSair.bind('<Button-1>', Aguarde)
btnSair.grid()


#btn1 = Button(bottomFrame, text="Loja 01", bg="white", fg="black", command=Loja01)
#btn1.pack(side=LEFT, anchor=W, expand=0)
#btn1.bind('<Button-1>', Aguarde)
#btn1.grid(column=0, row = 1)

#btnSair = Button(bottomSair, text="SAIR", bg="red", fg="yellow", font="Arial 10", command=gui.quit)
#btnSair.pack(anchor=S, expand=0)
#btnSair.grid()

Ex = Label(gui, text= "Exemplo PRINI:\n[IMPRESSORA]\nCAIXA=999\n\nDigitar: IMPRESSORA;CAIXA;999\n", height=6, width=50, bg='red', fg='yellow', font='Arial 12').place(x=1, y=170)

#T = Text(gui, height=5, width=50)
#T.place(x = 1, y=170 )
quote = """Exemplo PRINI:\n[IMPRESSORA]\nCAIXA=999\n\nDigitar: IMPRESSORA;CAIXA;999\n"""

gui.mainloop()