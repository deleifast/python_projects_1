#encoding: iso-8859-1
import os, time, subprocess
from tkinter import messagebox
from tkinter import *
from PIL import Image, ImageTk


gui = Tk()

bottomFrame = Frame(gui)
bottomFrame.pack(side=BOTTOM, anchor = W)

gui.title("PDVCORAL_REMARCA - NAGUMO **(LOJA 01)**")
gui.geometry("600x370")
gui.resizable(0,0)


def Caixa1():
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

				print("PDV e IP {} : {}".format(hostName,ipAddress))

				with open('pdv.txt', 'a') as caixa:
					caixa.write(str("PDV e IP {} : {}".format(hostName,ipAddress)))
					caixa.close()

btn1 = Button(bottomFrame, text="Caixa 01", bg="white", fg="black", command=Caixa1)
#btn1.pack(side=LEFT, anchor=W, expand=0)
btn1.bind('<Button-1>')
btn1.grid(column=0, row = 1)

btnSair = Button(bottomFrame, text="SAIR", bg="red", fg="yellow", font="Arial 12", command=gui.quit)
#btnSair.pack(anchor=SE, expand=1)
btnSair.grid(column=11, row = 5)


gui.mainloop()