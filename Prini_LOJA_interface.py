import os
import os.path
import shutil
import sys
from tkinter import messagebox
from tkinter import *
from pathlib import Path

tk = Tk()
tk.title("Configuracao PRINI POR LOJA")
tk.geometry("800x600")
tk.resizable(0,0)

def loja1():
#			arq = open("PRINI.001".format(msg.get()), "w")
#			print(msg.get())
#			arq.close()

		fileName = asksaveasfilename()
		file = open(fileName, 'w')
		textoutput = msg.get(0.0, END)
		file.write(textoutput)
		file.close()


msg = StringVar()
msg1 = StringVar()

lbl = Label(tk, text="Digite os parametros separados por ponto e virgula: ", font="Arial 10")
lbl.place(x=10, y=30)

mEntry = Entry(tk, width= 68, textvariable=msg, font="Arial 10")
mEntry.place(x=310, y=31)

lbl1 = Label(tk, text="Digite o nome da loja que deseja copiar: ", font="Arial 10")
lbl1.place(x=10, y=60)

mEntry1 = Entry(tk, width= 68, textvariable=msg1, font="Arial 10")
mEntry1.place(x=310, y=61)

btn = Button(tk, text="OK", bg="white", fg="black", command= loja1)
btn.pack(side="left", expand=2)

'''
if os.path.exists("C:\PDV\PRINI\loja1"):
	print ('existe')
else:
	dir = './loja1'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja2"):
	print ('existe')
else:
	dir = './loja2'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja3"):
	print ('existe')
else:
	dir = './loja3'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja4"):
	print ('existe')
else:
	dir = './loja4'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja6"):
	print ('existe')
else:
	dir = './loja6'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja7"):
	print ('existe')
else:
	dir = './loja7'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja8"):
	print ('existe')
else:
	dir = './loja8'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja9"):
	print ('existe')
else:
	dir = './loja9'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja10"):
	print ('existe')
else:
	dir = './loja10'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja11"):
	print ('existe')
else:
	dir = './loja11'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja12"):
	print ('existe')
else:
	dir = './loja12'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja13"):
	print ('existe')
else:
	dir = './loja13'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja14"):
	print ('existe')
else:
	dir = './loja14'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja15"):
	print ('existe')
else:
	dir = './loja15'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja16"):
	print ('existe')
else:
	dir = './loja16'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja17"):
	print ('existe')
else:
	dir = './loja17'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja18"):
	print ('existe')
else:
	dir = './loja18'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja19"):
	print ('existe')
else:
	dir = './loja19'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja20"):
	print ('existe')
else:
	dir = './loja20'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja21"):
	print ('existe')
else:
	dir = './loja21'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja22"):
	print ('existe')
else:
	dir = './loja22'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja23"):
	print ('existe')
else:
	dir = './loja23'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja24"):
	print ('existe')
else:
	dir = './loja24'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja25"):
	print ('existe')
else:
	dir = './loja25'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja26"):
	print ('existe')
else:
	dir = './loja26'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja27"):
	print ('existe')
else:
	dir = './loja27'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja28"):
	print ('existe')
else:
	dir = './loja28'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja29"):
	print ('existe')
else:
	dir = './loja29'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja30"):
	print ('existe')
else:
	dir = './loja30'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja31"):
	print ('existe')
else:
	dir = './loja31'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja32"):
	print ('existe')
else:
	dir = './loja32'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja33"):
	print ('existe')
else:
	dir = './loja33'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja34"):
	print ('existe')
else:
	dir = './loja34'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja35"):
	print ('existe')
else:
	dir = './loja35'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja36"):
	print ('existe')
else:
	dir = './loja36'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja37"):
	print ('existe')
else:
	dir = './loja37'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja38"):
	print ('existe')
else:
	dir = './loja38'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja39"):
	print ('existe')
else:
	dir = './loja39'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja40"):
	print ('existe')
else:
	dir = './loja40'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja41"):
	print ('existe')
else:
	dir = './loja41'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja42"):
	print ('existe')
else:
	dir = './loja42'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja43"):
	print ('existe')
else:
	dir = './loja43'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja44"):
	print ('existe')
else:
	dir = './loja44'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja45"):
	print ('existe')
else:
	dir = './loja45'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja46"):
	print ('existe')
else:
	dir = './loja46'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja47"):
	print ('existe')
else:
	dir = './loja47'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja48"):
	print ('existe')
else:
	dir = './loja48'
	os.makedirs(dir)

if os.path.exists("C:\PDV\PRINI\loja49"):
	print ('existe')
else:
	dir = './loja49'
	os.makedirs(dir)


with open("PRINI.001","a") as PRINI:
	item = input("Digite os parametros separados por ponto e virgula:")
	PRINI.write("%s \n" % item)
	
with open ('PRINI.001', 'r') as arquivo_existente, open('PRINI.BAK', 'w') as novo_arquivo:
	for linha in arquivo_existente.readlines():
		novo_arquivo.write(linha)
		print(linha)
		

pasta_ori = 'C://PDV/PRINI'
arquivo = 'C://PDV/PRINI/PRINI.001'
diretorio = os.listdir(pasta_ori)
pasta_dest = str(input('digite o nome da pasta que deseja copiar: '))

if pasta_dest == 'loja1':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja1')
	for el in range(101, 125):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja2':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja2')
	for el in range(101, 121):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja3':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja3')
	for el in range(101, 121):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja4':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja4')
	for el in range(101, 110):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja6':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja6')
	for el in range(101, 110):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja7':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja7')
	for el in range(101, 132):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja8':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja8')
	for el in range(101, 141):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja9':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja9')
	for el in range(101, 119):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja10':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja10')
	for el in range(101, 110):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja11':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja11')
	for el in range(101, 132):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja12':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja12')
	for el in range(101, 119):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja13':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja13')
	for el in range(101, 121):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja14':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja14')
	shutil.copy ('PRINI.001' , 'PRINI.101')
	shutil.copy ('PRINI.001' , 'PRINI.102')
	shutil.copy ('PRINI.001' , 'PRINI.105')
	shutil.copy ('PRINI.001' , 'PRINI.107')
	shutil.copy ('PRINI.001' , 'PRINI.110')
	shutil.copy ('PRINI.001' , 'PRINI.111')
	shutil.copy ('PRINI.001' , 'PRINI.112')
	shutil.copy ('PRINI.001' , 'PRINI.114')
	shutil.copy ('PRINI.001' , 'PRINI.115')
	shutil.copy ('PRINI.001' , 'PRINI.117')
	shutil.copy ('PRINI.001' , 'PRINI.118')
	shutil.copy ('PRINI.001' , 'PRINI.119')
	shutil.copy ('PRINI.001' , 'PRINI.120')
	shutil.copy ('PRINI.001' , 'PRINI.121')
	shutil.copy ('PRINI.001' , 'PRINI.122')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja15':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja15')
	for el in range(101, 121):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja16':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja16')
	for el in range(101, 117):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja17':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja17')
	for el in range(101, 124):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja18':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja18')
	for el in range(101, 117):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja19':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja19')
	for el in range(101, 110):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja20':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja20')
	shutil.copy ('PRINI.001' , 'PRINI.101')
	shutil.copy ('PRINI.001' , 'PRINI.102')
	shutil.copy ('PRINI.001' , 'PRINI.103')
	shutil.copy ('PRINI.001' , 'PRINI.104')
	shutil.copy ('PRINI.001' , 'PRINI.106')
	shutil.copy ('PRINI.001' , 'PRINI.107')
	shutil.copy ('PRINI.001' , 'PRINI.108')
	shutil.copy ('PRINI.001' , 'PRINI.109')
	shutil.copy ('PRINI.001' , 'PRINI.110')
	shutil.copy ('PRINI.001' , 'PRINI.111')
	shutil.copy ('PRINI.001' , 'PRINI.112')
	shutil.copy ('PRINI.001' , 'PRINI.113')
	shutil.copy ('PRINI.001' , 'PRINI.114')
	shutil.copy ('PRINI.001' , 'PRINI.115')
	shutil.copy ('PRINI.001' , 'PRINI.118')
	sys.exit()

if pasta_dest == 'loja21':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja21')
	for el in range(101, 123):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja22':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja22')
	for el in range(23, 44):
		shutil.copy('PRINI.001',f'PRINI.0{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja23':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja23')
	for el in range(101, 126):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja24':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja24')
	for el in range(101, 122):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja25':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja25')
	for el in range(101, 116):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja26':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja26')
	for el in range(101, 132):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja27':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja27')
	shutil.copy ('PRINI.001' , 'PRINI.002')
	shutil.copy ('PRINI.001' , 'PRINI.003')
	shutil.copy ('PRINI.001' , 'PRINI.004')
	shutil.copy ('PRINI.001' , 'PRINI.005')
	shutil.copy ('PRINI.001' , 'PRINI.006')
	shutil.copy ('PRINI.001' , 'PRINI.007')
	shutil.copy ('PRINI.001' , 'PRINI.008')
	shutil.copy ('PRINI.001' , 'PRINI.009')
	shutil.copy ('PRINI.001' , 'PRINI.010')
	shutil.copy ('PRINI.001' , 'PRINI.011')
	shutil.copy ('PRINI.001' , 'PRINI.012')
	shutil.copy ('PRINI.001' , 'PRINI.013')
	shutil.copy ('PRINI.001' , 'PRINI.014')
	shutil.copy ('PRINI.001' , 'PRINI.015')
	shutil.copy ('PRINI.001' , 'PRINI.016')
	shutil.copy ('PRINI.001' , 'PRINI.017')
	shutil.copy ('PRINI.001' , 'PRINI.018')
	shutil.copy ('PRINI.001' , 'PRINI.019')
	shutil.copy ('PRINI.001' , 'PRINI.020')
	shutil.copy ('PRINI.001' , 'PRINI.021')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja28':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja28')
	for el in range(101, 116):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja29':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja29')
	for el in range(101, 116):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja30':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja30')
	shutil.copy ('PRINI.001' , 'PRINI.002')
	shutil.copy ('PRINI.001' , 'PRINI.003')
	shutil.copy ('PRINI.001' , 'PRINI.004')
	shutil.copy ('PRINI.001' , 'PRINI.005')
	shutil.copy ('PRINI.001' , 'PRINI.006')
	shutil.copy ('PRINI.001' , 'PRINI.007')
	shutil.copy ('PRINI.001' , 'PRINI.008')
	shutil.copy ('PRINI.001' , 'PRINI.009')
	shutil.copy ('PRINI.001' , 'PRINI.010')
	shutil.copy ('PRINI.001' , 'PRINI.011')
	shutil.copy ('PRINI.001' , 'PRINI.012')
	shutil.copy ('PRINI.001' , 'PRINI.013')
	shutil.copy ('PRINI.001' , 'PRINI.014')
	shutil.copy ('PRINI.001' , 'PRINI.015')
	shutil.copy ('PRINI.001' , 'PRINI.016')
	shutil.copy ('PRINI.001' , 'PRINI.017')
	shutil.copy ('PRINI.001' , 'PRINI.018')
	shutil.copy ('PRINI.001' , 'PRINI.019')
	shutil.copy ('PRINI.001' , 'PRINI.020')
	shutil.copy ('PRINI.001' , 'PRINI.021')
	shutil.copy ('PRINI.001' , 'PRINI.022')
	shutil.copy ('PRINI.001' , 'PRINI.023')
	shutil.copy ('PRINI.001' , 'PRINI.024')
	shutil.copy ('PRINI.001' , 'PRINI.025')
	shutil.copy ('PRINI.001' , 'PRINI.026')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja31':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja31')
	shutil.copy ('PRINI.001' , 'PRINI.101')
	shutil.copy ('PRINI.001' , 'PRINI.102')
	shutil.copy ('PRINI.001' , 'PRINI.104')
	shutil.copy ('PRINI.001' , 'PRINI.106')
	shutil.copy ('PRINI.001' , 'PRINI.108')	
	shutil.copy ('PRINI.001' , 'PRINI.109')
	shutil.copy ('PRINI.001' , 'PRINI.110')
	shutil.copy ('PRINI.001' , 'PRINI.112')
	shutil.copy ('PRINI.001' , 'PRINI.114')
	shutil.copy ('PRINI.001' , 'PRINI.115')
	shutil.copy ('PRINI.001' , 'PRINI.116')
	shutil.copy ('PRINI.001' , 'PRINI.117')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja32':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja32')
	shutil.copy ('PRINI.001' , 'PRINI.102')
	shutil.copy ('PRINI.001' , 'PRINI.104')
	shutil.copy ('PRINI.001' , 'PRINI.105')
	shutil.copy ('PRINI.001' , 'PRINI.106')
	shutil.copy ('PRINI.001' , 'PRINI.108')
	shutil.copy ('PRINI.001' , 'PRINI.110')
	shutil.copy ('PRINI.001' , 'PRINI.111')
	shutil.copy ('PRINI.001' , 'PRINI.112')
	shutil.copy ('PRINI.001' , 'PRINI.113')
	shutil.copy ('PRINI.001' , 'PRINI.114')
	shutil.copy ('PRINI.001' , 'PRINI.115')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja33':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja33')
	shutil.copy ('PRINI.001' , 'PRINI.101')
	shutil.copy ('PRINI.001' , 'PRINI.104')
	shutil.copy ('PRINI.001' , 'PRINI.105')
	shutil.copy ('PRINI.001' , 'PRINI.107')
	shutil.copy ('PRINI.001' , 'PRINI.108')
	shutil.copy ('PRINI.001' , 'PRINI.109')
	shutil.copy ('PRINI.001' , 'PRINI.110')
	shutil.copy ('PRINI.001' , 'PRINI.111')
	shutil.copy ('PRINI.001' , 'PRINI.112')
	shutil.copy ('PRINI.001' , 'PRINI.113')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja34':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja34')
	shutil.copy ('PRINI.001' , 'PRINI.101')
	shutil.copy ('PRINI.001' , 'PRINI.102')
	shutil.copy ('PRINI.001' , 'PRINI.104')
	shutil.copy ('PRINI.001' , 'PRINI.105')
	shutil.copy ('PRINI.001' , 'PRINI.106')
	shutil.copy ('PRINI.001' , 'PRINI.107')
	shutil.copy ('PRINI.001' , 'PRINI.108')
	shutil.copy ('PRINI.001' , 'PRINI.110')
	shutil.copy ('PRINI.001' , 'PRINI.111')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja35':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja35')
	shutil.copy ('PRINI.001' , 'PRINI.101')
	shutil.copy ('PRINI.001' , 'PRINI.102')
	shutil.copy ('PRINI.001' , 'PRINI.103')
	shutil.copy ('PRINI.001' , 'PRINI.104')
	shutil.copy ('PRINI.001' , 'PRINI.105')
	shutil.copy ('PRINI.001' , 'PRINI.106')
	shutil.copy ('PRINI.001' , 'PRINI.110')
	shutil.copy ('PRINI.001' , 'PRINI.111')
	shutil.copy ('PRINI.001' , 'PRINI.112')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja36':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja36')
	for el in range(101, 119):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja37':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja37')
	for el in range(101, 119):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja38':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja38')
	shutil.copy ('PRINI.001' , 'PRINI.005')
	shutil.copy ('PRINI.001' , 'PRINI.101')
	shutil.copy ('PRINI.001' , 'PRINI.102')
	shutil.copy ('PRINI.001' , 'PRINI.103')
	shutil.copy ('PRINI.001' , 'PRINI.104')
	shutil.copy ('PRINI.001' , 'PRINI.106')
	shutil.copy ('PRINI.001' , 'PRINI.107')
	shutil.copy ('PRINI.001' , 'PRINI.108')
	shutil.copy ('PRINI.001' , 'PRINI.109')
	shutil.copy ('PRINI.001' , 'PRINI.110')
	shutil.copy ('PRINI.001' , 'PRINI.111')
	shutil.copy ('PRINI.001' , 'PRINI.112')
	shutil.copy ('PRINI.001' , 'PRINI.113')
	shutil.copy ('PRINI.001' , 'PRINI.114')
	shutil.copy ('PRINI.001' , 'PRINI.115')
	shutil.copy ('PRINI.001' , 'PRINI.116')
	shutil.copy ('PRINI.001' , 'PRINI.117')
	shutil.copy ('PRINI.001' , 'PRINI.118')
	shutil.copy ('PRINI.001' , 'PRINI.119')
	shutil.copy ('PRINI.001' , 'PRINI.120')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja39':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja39')
	for el in range(101, 122):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja40':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja40')
	for el in range(101, 117):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja41':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja41')
	shutil.copy ('PRINI.001' , 'PRINI.002')
	shutil.copy ('PRINI.001' , 'PRINI.003')
	shutil.copy ('PRINI.001' , 'PRINI.004')
	shutil.copy ('PRINI.001' , 'PRINI.005')
	shutil.copy ('PRINI.001' , 'PRINI.006')
	shutil.copy ('PRINI.001' , 'PRINI.007')
	shutil.copy ('PRINI.001' , 'PRINI.008')
	shutil.copy ('PRINI.001' , 'PRINI.009')
	shutil.copy ('PRINI.001' , 'PRINI.010')
	shutil.copy ('PRINI.001' , 'PRINI.011')
	shutil.copy ('PRINI.001' , 'PRINI.012')
	shutil.copy ('PRINI.001' , 'PRINI.013')
	shutil.copy ('PRINI.001' , 'PRINI.014')
	shutil.copy ('PRINI.001' , 'PRINI.015')
	shutil.copy ('PRINI.001' , 'PRINI.016')
	shutil.copy ('PRINI.001' , 'PRINI.017')
	shutil.copy ('PRINI.001' , 'PRINI.018')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja42':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja42')
	shutil.copy ('PRINI.001' , 'PRINI.002')
	shutil.copy ('PRINI.001' , 'PRINI.003')
	shutil.copy ('PRINI.001' , 'PRINI.004')
	shutil.copy ('PRINI.001' , 'PRINI.005')
	shutil.copy ('PRINI.001' , 'PRINI.006')
	shutil.copy ('PRINI.001' , 'PRINI.007')
	shutil.copy ('PRINI.001' , 'PRINI.008')
	shutil.copy ('PRINI.001' , 'PRINI.009')
	shutil.copy ('PRINI.001' , 'PRINI.010')
	shutil.copy ('PRINI.001' , 'PRINI.011')
	shutil.copy ('PRINI.001' , 'PRINI.012')
	shutil.copy ('PRINI.001' , 'PRINI.013')
	shutil.copy ('PRINI.001' , 'PRINI.014')
	shutil.copy ('PRINI.001' , 'PRINI.015')
	shutil.copy ('PRINI.001' , 'PRINI.016')
	shutil.copy ('PRINI.001' , 'PRINI.017')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja43':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja43')
	shutil.copy ('PRINI.001' , 'PRINI.002')
	shutil.copy ('PRINI.001' , 'PRINI.003')
	shutil.copy ('PRINI.001' , 'PRINI.004')
	shutil.copy ('PRINI.001' , 'PRINI.005')
	shutil.copy ('PRINI.001' , 'PRINI.006')
	shutil.copy ('PRINI.001' , 'PRINI.007')
	shutil.copy ('PRINI.001' , 'PRINI.008')
	shutil.copy ('PRINI.001' , 'PRINI.009')
	shutil.copy ('PRINI.001' , 'PRINI.010')
	shutil.copy ('PRINI.001' , 'PRINI.011')
	shutil.copy ('PRINI.001' , 'PRINI.012')
	shutil.copy ('PRINI.001' , 'PRINI.013')
	shutil.copy ('PRINI.001' , 'PRINI.014')
	shutil.copy ('PRINI.001' , 'PRINI.015')
	shutil.copy ('PRINI.001' , 'PRINI.016')
	shutil.copy ('PRINI.001' , 'PRINI.017')
	shutil.copy ('PRINI.001' , 'PRINI.018')
	shutil.copy ('PRINI.001' , 'PRINI.019')
	shutil.copy ('PRINI.001' , 'PRINI.020')
	shutil.copy ('PRINI.001' , 'PRINI.021')
	shutil.copy ('PRINI.001' , 'PRINI.022')
	shutil.copy ('PRINI.001' , 'PRINI.023')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja44':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja44')
	shutil.copy ('PRINI.001' , 'PRINI.002')
	shutil.copy ('PRINI.001' , 'PRINI.003')
	shutil.copy ('PRINI.001' , 'PRINI.004')
	shutil.copy ('PRINI.001' , 'PRINI.005')
	shutil.copy ('PRINI.001' , 'PRINI.006')
	shutil.copy ('PRINI.001' , 'PRINI.007')
	shutil.copy ('PRINI.001' , 'PRINI.008')
	shutil.copy ('PRINI.001' , 'PRINI.009')
	shutil.copy ('PRINI.001' , 'PRINI.010')
	shutil.copy ('PRINI.001' , 'PRINI.011')
	shutil.copy ('PRINI.001' , 'PRINI.012')
	shutil.copy ('PRINI.001' , 'PRINI.013')
	shutil.copy ('PRINI.001' , 'PRINI.014')
	shutil.copy ('PRINI.001' , 'PRINI.015')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja45':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja45')
	for el in range(69, 99):
		shutil.copy('PRINI.001',f'PRINI.0{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja46':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja46')
	shutil.copy ('PRINI.001' , 'PRINI.002')
	shutil.copy ('PRINI.001' , 'PRINI.003')
	shutil.copy ('PRINI.001' , 'PRINI.004')
	shutil.copy ('PRINI.001' , 'PRINI.005')
	shutil.copy ('PRINI.001' , 'PRINI.006')
	shutil.copy ('PRINI.001' , 'PRINI.007')
	shutil.copy ('PRINI.001' , 'PRINI.008')
	shutil.copy ('PRINI.001' , 'PRINI.009')
	shutil.copy ('PRINI.001' , 'PRINI.010')
	shutil.copy ('PRINI.001' , 'PRINI.011')
	shutil.copy ('PRINI.001' , 'PRINI.012')
	shutil.copy ('PRINI.001' , 'PRINI.013')
	shutil.copy ('PRINI.001' , 'PRINI.014')
	shutil.copy ('PRINI.001' , 'PRINI.015')
	shutil.copy ('PRINI.001' , 'PRINI.016')
	shutil.copy ('PRINI.001' , 'PRINI.017')
	shutil.copy ('PRINI.001' , 'PRINI.018')
	shutil.copy ('PRINI.001' , 'PRINI.019')
	shutil.copy ('PRINI.001' , 'PRINI.020')
	shutil.copy ('PRINI.001' , 'PRINI.021')
	shutil.copy ('PRINI.001' , 'PRINI.022')
	shutil.copy ('PRINI.001' , 'PRINI.023')	
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja47':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja47')
	for el in range(101, 119):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja48':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja48')
	for el in range(101, 122):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()

if pasta_dest == 'loja49':
	loja1 = pasta_dest
	shutil.copy(arquivo, pasta_dest)  
	os.chdir('c:\pdv\prini\loja49')
	for el in range(101, 128):
		shutil.copy('PRINI.001',f'PRINI.{el}')
	print('%s copiado para pasta %s' % (arquivo, pasta_dest))
	sys.exit()
	
else:
	print("Loja nao cadastrada!")
	sys.exit()'''

tk.mainloop()