#encoding: iso-8859-1
import os, time, subprocess, shutil, os.path, sys, glob
from tkinter import messagebox
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk


gui = Tk()

bottomLimpar = Frame(gui)
bottomLimpar.place(x=100, y=150)

bottomExecutar = Frame(gui)
bottomExecutar.place(x=300, y=150)

bottomSair = Frame(gui)
bottomSair.pack(side=BOTTOM, anchor = S)

chkFrame = Frame(gui)
chkFrame.pack(side=LEFT, anchor = S)

chkTodas = Frame(gui)
chkTodas.place(x=350, y=1)

gui.title("Reinicia SALCOMM")
gui.geometry("520x380")
gui.resizable(0,0)

load = Image.open("logo_2016.png")
render = ImageTk.PhotoImage(load)
img= Label(gui, image=render)
img.image = render
img.place(x=0, y=0)

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



def var_states():
	
	lbltodas = Label(gui, text="                                               ", font = "Arial 15").place(x=260, y=115)

	if var1.get() == 1:
		Loja01()
	if var2.get() == 1:
		Loja02()
	if var3.get() == 1:
		Loja03()
	if var4.get() == 1:
		Loja04()
	if var6.get() == 1:
		Loja06()
	if var7.get() == 1:
		Loja07()
	if var8.get() == 1:
		Loja08()
	if var9.get() == 1:
		Loja09()
	if var10.get() == 1:
		Loja10()
	if var11.get() == 1:
		Loja11()
	if var12.get() == 1:
		Loja12()
	if var13.get() == 1:
		Loja13()
	if var14.get() == 1:
		Loja14()
	if var15.get() == 1:
		Loja15()
	if var16.get() == 1:
		Loja16()
	if var17.get() == 1:
		Loja17()
	if var18.get() == 1:
		Loja18()
	if var19.get() == 1:
		Loja19()
	if var20.get() == 1:
		Loja20()
	if var21.get() == 1:
		Loja21()
	if var22.get() == 1:
		Loja22()
	if var23.get() == 1:
		Loja23()
	if var24.get() == 1:
		Loja24()
	if var25.get() == 1:
		Loja25()
	if var26.get() == 1:
		Loja26()
	if var27.get() == 1:
		Loja27()
	if var28.get() == 1:
		Loja28()
	if var29.get() == 1:
		Loja29()
	if var30.get() == 1:
		Loja30()
	if var31.get() == 1:
		Loja31()
	if var32.get() == 1:
		Loja32()
	if var33.get() == 1:
		Loja33()
	if var34.get() == 1:
		Loja34()
	if var35.get() == 1:
		Loja35()
	if var36.get() == 1:
		Loja36()
	if var37.get() == 1:
		Loja37()
	if var38.get() == 1:
		Loja38()
	if var39.get() == 1:
		Loja39()
	if var40.get() == 1:
		Loja40()
	if var41.get() == 1:
		Loja41()
	if var42.get() == 1:
		Loja42()
	if var43.get() == 1:
		Loja43()
	if var44.get() == 1:
		Loja44()
	if var45.get() == 1:
		Loja45()
	if var46.get() == 1:
		Loja46()
	if var47.get() == 1:
		Loja47()
	if var48.get() == 1:
		Loja48()
	if var49.get() == 1:
		Loja49()

	else:
		resp = messagebox.showwarning("Alerta", "SELECIONE UMA OU TODAS AS LOJAS")	
		if resp == "ok":
				res = "SELECIONE NOVAMENTE!!!"
				res_texto(res)
				

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


vartodas = IntVar()

Chk = Checkbutton(chkTodas, text="Escolher TODAS AS LOJAS", variable=vartodas, command=todas)
Chk.grid(column=1, row =1)

mensagem= StringVar()
lbl = Label(gui, text="Escolha a loja: " , fg="blue", font="Calibri 12 bold")
lbl.place(x=1, y=180)

mensagem= StringVar()
lbl = Label(gui, text="Versão 1.0" , fg="black", font="Arial 8")
lbl.place(x=1, y=550)

label = Label(gui)
label.pack()

res = " "

lblaguarde = Label(gui, text= res, font="Arial 15", fg= "red")
lblaguarde.place(x=250, y=50)

def Aguarde(event):
	res = "        Aguarde...                     "
	res_texto(res)

	
def res_texto(res):
    lblaguarde.config(text=res)




def Loja01():
	ret = os.system("taskkill /s 192.168.1.101 /u NAGUMO\cpd_l01 /p retag@2018 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.1.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk1.deselect()

def Loja02():
	ret = os.system("taskkill /s 192.168.2.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.2.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk2.deselect()

def Loja03():
	ret = os.system("taskkill /s 192.168.3.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.3.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk3.deselect()

def Loja04():
	ret = os.system("taskkill /s 192.168.4.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.4.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk4.deselect()

def Loja06():
	ret = os.system("taskkill /s 192.168.6.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.6.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk6.deselect()

def Loja07():
	ret = os.system("taskkill /s 192.168.7.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.7.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk7.deselect()

def Loja08():
	ret = os.system("taskkill /s 192.168.8.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.8.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk8.deselect()

def Loja09():
	ret = os.system("taskkill /s 192.168.9.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.9.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk9.deselect()

def Loja10():
	ret = os.system("taskkill /s 192.168.10.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.10.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk10.deselect()

def Loja11():
	ret = os.system("taskkill /s 192.168.11.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.11.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk11.deselect()

def Loja12():
	ret = os.system("taskkill /s 192.168.12.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.12.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk12.deselect()

def Loja13():
	ret = os.system("taskkill /s 192.168.13.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.13.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk13.deselect()

def Loja14():
	ret = os.system("taskkill /s 192.168.141.150 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.141.150 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk14.deselect()

def Loja15():
	ret = os.system("taskkill /s 192.168.15.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.15.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk15.deselect()

def Loja16():
	ret = os.system("taskkill /s 192.168.16.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.16.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk16.deselect()

def Loja17():
	ret = os.system("taskkill /s 192.168.17.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.17.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk17.deselect()

def Loja18():
	ret = os.system("taskkill /s 192.168.18.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.18.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk18.deselect()

def Loja19():
	ret = os.system("taskkill /s 192.168.19.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.19.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk19.deselect()

def Loja20():
	ret = os.system("taskkill /s 192.168.20.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.20.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk20.deselect()

def Loja21():
	ret = os.system("taskkill /s 192.168.21.100 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.21.100 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk21.deselect()

def Loja22():
	ret = os.system("taskkill /s 192.168.22.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.22.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk22.deselect()

def Loja23():
	ret = os.system("taskkill /s 192.168.23.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.23.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk23.deselect()

def Loja24():
	ret = os.system("taskkill /s 192.168.24.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.24.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk24.deselect()


def Loja25():
	ret = os.system("taskkill /s 192.168.25.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.25.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk25.deselect()

def Loja26():
	ret = os.system("taskkill /s 192.168.26.150 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.26.150 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk26.deselect()

def Loja27():
	ret = os.system("taskkill /s 192.168.27.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.27.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk27.deselect()

def Loja28():
	ret = os.system("taskkill /s 192.168.28.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.28.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk28.deselect()

def Loja29():
	ret = os.system("taskkill /s 192.168.29.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.29.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk29.deselect()

def Loja30():
	ret = os.system("taskkill /s 192.168.30.102 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.30.102 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk30.deselect()

def Loja31():
	ret = os.system("taskkill /s 192.168.31.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.31.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk31.deselect()

def Loja32():
	ret = os.system("taskkill /s 192.168.32.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.32.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk32.deselect()

def Loja33():
	ret = os.system("taskkill /s 192.168.33.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.33.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk33.deselect()

def Loja34():
	ret = os.system("taskkill /s 192.168.34.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.34.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk34.deselect()

def Loja35():
	ret = os.system("taskkill /s 192.168.35.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.35.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk35.deselect()

def Loja36():
	ret = os.system("taskkill /s 192.168.36.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.36.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk36.deselect()

def Loja37():
	ret = os.system("taskkill /s 192.168.37.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.37.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk37.deselect()

def Loja38():
	ret = os.system("taskkill /s 192.168.38.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.38.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk38.deselect()

def Loja39():
	ret = os.system("taskkill /s 192.168.39.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.39.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk39.deselect()

def Loja40():
	ret = os.system("taskkill /s 192.168.40.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.40.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk40.deselect()

def Loja41():
	ret = os.system("taskkill /s 192.168.41.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.41.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk41.deselect()

def Loja42():
	ret = os.system("taskkill /s 192.168.42.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.42.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk42.deselect()

def Loja43():
	ret = os.system("taskkill /s 192.168.43.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.43.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk43.deselect()

def Loja44():
	ret = os.system("taskkill /s 192.168.44.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.44.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk44.deselect()

def Loja45():
	ret = os.system("taskkill /s 192.168.45.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.45.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk45.deselect()

def Loja46():
	ret = os.system("taskkill /s 192.168.46.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.46.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk46.deselect()

def Loja47():
	ret = os.system("taskkill /s 192.168.47.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.47.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk47.deselect()

def Loja48():
	ret = os.system("taskkill /s 192.168.48.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\192.168.48.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk48.deselect()

def Loja49():
	ret = os.system("taskkill /s 10.132.49.101 /u compartilhar /p ruaf305 /im SALCOMM.EXE")
	if ret == 1:
		resp = messagebox.showwarning("Erro", "SEM CONEXÃO COM A LOJA, VERIFIQUE!!")
	else:
		ret = os.system("psexec.exe -d -i -u compartilhar -p ruaf305 \\\\10.132.49.101 ""c://retag/salcomm.exe")
		if ret == 53:
			resp = messagebox.showerror("Erro", "SEM CONEXÃO COM A LOJA!!")
		else:
			resp = messagebox.showinfo("Informação", "Salcomm INCICIADO")
	res = "                                                         "
	res_texto(res)
	chk49.deselect()


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

btnLimpar = Button(bottomLimpar, text='Limpar LOJAS', bg="white", fg="black", width=20, height=1, font="Arial 10", command=limpar)
btnLimpar.bind('<Button-1>', Aguarde)
btnLimpar.pack()

btnExecutar = Button(bottomExecutar, text='Reiniciar SALCOMM', bg="yellow", fg="red", width=20, height=1, font="Arial 10", command=var_states)
btnExecutar.bind('<Button-1>', Aguarde)
btnExecutar.pack()

btnSair = Button(bottomSair, text='Sair', bg="red", fg="yellow", width=10, height=1, font="Arial 10", command=gui.quit)
btnSair.bind('<Button-1>', Aguarde)
btnSair.grid()


gui.mainloop()