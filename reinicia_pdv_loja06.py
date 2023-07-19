# encoding: iso-8859-1
import logging
import subprocess
import time
from tkinter import *
from tkinter import messagebox, StringVar

from PIL import Image, ImageTk

logging.basicConfig(filename="reinicia.log", format="%(asctime)s %(message)s", datefmt='%d-%m-%y %H:%M:%S',
                    level=logging.INFO)
logging.info("Iniciando programa vers�o 3.0")

gui = Tk()

bottomFrame = Frame(gui)
bottomFrame.pack(side=BOTTOM, anchor=W)


def disable_event():
    pass


gui.title("PDVCORAL_REMARCA - NAGUMO **(LOJA 06)**")
gui.geometry("630x320")
gui.resizable(0,0)
gui.attributes("-toolwindow", 1)
gui.protocol("WM_DELETE_WINDOW", disable_event)
load = Image.open("logo-remarca.png")
render = ImageTk.PhotoImage(load)
img = Label(gui, image=render)
img.image = render
img.place(x=370, y=0)


def sel():
    selection = "ESCOLHIDA OP��O: " + str(var.get()) + " DO MENU!!!"
    label.config(text=selection, bg="red", fg="yellow", font="Terminal 12")
    label.place(x=10, y=50)
    logging.info("Escolheu a op��o: " + str(var.get()) + " do menu")


var = IntVar()

R1 = Radiobutton(gui, text="1 - Reiniciar PDVCORAL", variable=var, value=1, font="Arial 10", command=sel)
R1.pack(anchor=NW)

R2 = Radiobutton(gui, text="2 - Reiniciar CPU", variable=var, value=2, font="Arial 10", command=sel)
R2.pack(anchor=NW)

msg = StringVar()
lbl = Label(gui, text="Remarca - telefone: (11)2755-7911 ", fg="red", font="Arial 15")
lbl.place(x=140, y=225)

msg = StringVar()
lbl = Label(gui, text="Vers�o 3.0", fg="black", font="Arial 8")
lbl.place(x=1, y=300)
# vers�o 2.0 - Altera��o - tirado pdvcoral.exe e colocado inicia_pdv.bat
# vers�o 3.0 - Inclus�o do log - reinicia.log

label = Label(gui)
label.pack()

res = " "

lblaguarde = Label(gui, text=res, font="Arial 20", fg="red")
lblaguarde.place(x=180, y=100)


def Aguarde(event):
    res = "Aguarde..."
    res_texto(res)


def res_texto(res):
    lblaguarde.config(text=res)


nvar = IntVar()


def telamotivo():
    ws = Toplevel(gui)
    ws.title(string='')
    ws.geometry('400x300')
    ws.attributes("-toolwindow", 1)
    ws.transient(gui)
    ws.focus_force()
    ws.grab_set()

    frame = LabelFrame(
        ws,
        text='Escolha o motivo do travamento:',
        bg='#f0f0f0',
        font=(20)
    )
    frame.pack(expand=True, fill=BOTH)

    def disable_event():
        pass

    def close_window():

        if nvar.get() == 1 or nvar.get() == 2 or nvar.get() == 3 or nvar.get() == 4 or nvar.get() == 5 or nvar.get() == 6 or nvar.get() == 7 or nvar.get() == 8:
            resp = messagebox.showinfo("Informacao", "REINICIADO O CAIXA")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)

            ws.destroy()

        else:
            resp = messagebox.showwarning("Alerta", "Escolha uma motivo!!!")
            logging.info("Escolha um motivo!!!")

    nvar.set(False)

    R3 = Radiobutton(frame, text="Tela travada (PESAGEM)", variable=nvar, value=1, font='Arial 10', command=execute)
    R3.pack(anchor=NW)
    R4 = Radiobutton(frame, text="Tela travada (LENDO OU DIGITANDO ITEM)", variable=nvar, value=2, font='Arial 10',
                     command=execute)
    R4.pack(anchor=NW)
    R5 = Radiobutton(frame, text="Iniciando venda (CPF)", variable=nvar, value=3, font='Arial 10', command=execute)
    R5.pack(anchor=NW)
    R6 = Radiobutton(frame, text="Finalizando venda (SUBTOTAL)", variable=nvar, value=4, font='Arial 10',
                     command=execute)
    R6.pack(anchor=NW)
    R7 = Radiobutton(frame, text="Pinpad travado ou desligado", variable=nvar, value=5, font='Arial 10',
                     command=execute)
    R7.pack(anchor=NW)
    R8 = Radiobutton(frame, text="Impressora desligada ou desconectada", variable=nvar, value=6, font='Arial 10',
                     command=execute)
    R8.pack(anchor=NW)
    R9 = Radiobutton(frame, text="Scanner desligado ou desconectado", variable=nvar, value=7, font='Arial 10',
                     command=execute)
    R9.pack(anchor=NW)
    R10 = Radiobutton(frame, text="SAT desligado ou desconectado", variable=nvar, value=8, font='Arial 10',
                      command=execute)
    R10.pack(anchor=NW)
    button = Button(frame, text="Fechar", bg="cyan", fg="red", font="Arial 12", command=close_window)
    button.pack(anchor=SE, expand=1)
    ws.protocol("WM_DELETE_WINDOW", disable_event)


def execute():
    if nvar.get() == 1:
        logging.info("Motivo - Tela travada (PESAGEM)")

    if nvar.get() == 2:
        logging.info("Motivo - Tela travada (LENDO OU DIGITANDO ITEM)")

    if nvar.get() == 3:
        logging.info("Motivo - Iniciando venda (CPF)")

    if nvar.get() == 4:
        logging.info("Motivo - Finalizando venda (SUBTOTAL)")

    if nvar.get() == 5:
        logging.info("Motivo - Pinpad travado ou desligado")

    if nvar.get() == 6:
        logging.info("Motivo - Impressora desligada ou desconectada")

    if nvar.get() == 7:
        logging.info("Motivo - Scanner desligado ou desconectado")

    if nvar.get() == 8:
        logging.info("Motivo - SAT desligado ou desconectado")


def sair():
    gui.quit()
    logging.info("Clicou sair do programa")


def Caixa1():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Administrator -p pdv \\\\192.168.6.1 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 01 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 01 - SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 01")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Administrator -p pdv \\\\192.168.6.1 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 01 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 01 - SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 01 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 01 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 01 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na op��o 1 ou 2!!!"
            res_texto(res)


def Caixa2():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Administrator -p pdv \\\\192.168.6.2 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 02 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 02 - SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 02")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Administrator -p pdv \\\\192.168.6.2 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 02 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 02 - SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 02 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 02 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 02 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na op��o 1 ou 2!!!"
            res_texto(res)


def Caixa3():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Administrator -p pdv \\\\192.168.6.3 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 03 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 03 - SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 03")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Administrator -p pdv \\\\192.168.6.3 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 03 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 03 - SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 03 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 03 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 03 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na op��o 1 ou 2!!!"
            res_texto(res)


def Caixa4():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Administrator -p pdv \\\\192.168.6.4 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 04 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 04 - SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 04")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Administrator -p pdv \\\\192.168.6.4 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 04 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 04 - SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 04 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 04 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 04 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na op��o 1 ou 2!!!"
            res_texto(res)


def Caixa5():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Administrator -p pdv \\\\192.168.6.5 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 05 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 05 - SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 05")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Administrator -p pdv \\\\192.168.6.5 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 05 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 05 - SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 05 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 05 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 05 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na op��o 1 ou 2!!!"
            res_texto(res)


def Caixa6():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Administrator -p pdv \\\\192.168.6.6 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 06 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 06 - SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 06")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Administrator -p pdv \\\\192.168.6.6 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 06 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 06 - SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 06 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 06 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 06 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na op��o 1 ou 2!!!"
            res_texto(res)


def Caixa7():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Administrator -p pdv \\\\192.168.6.7 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 07 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 07 - SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 07")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Administrator -p pdv \\\\192.168.6.7 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 07 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 07 - SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 07 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 07 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 07 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na op��o 1 ou 2!!!"
            res_texto(res)


def Caixa8():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Administrator -p pdv \\\\192.168.6.8 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 08 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 08 - SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 08")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Administrator -p pdv \\\\192.168.6.8 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 08 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 08 - SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 08 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 08 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 08 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na op��o 1 ou 2!!!"
            res_texto(res)


def Caixa9():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Administrator -p pdv \\\\192.168.6.9 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 09 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 09 - SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 09")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Administrator -p pdv \\\\192.168.6.9 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 09 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 09 - SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 09 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 09 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 09 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na op��o 1 ou 2!!!"
            res_texto(res)


def Caixa10():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Administrator -p pdv \\\\192.168.6.10 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 10 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 10 - SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 10")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Administrator -p pdv \\\\192.168.6.10 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 10 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 10 - SEM USU�RIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 10 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 10 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 10 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na op��o 1 ou 2!!!"
            res_texto(res)




btn1 = Button(bottomFrame, text="Caixa 01", bg="white", fg="black", command=Caixa1)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn1.bind('<Button-1>', Aguarde)
btn1.grid(column=0, row=1)

btn2 = Button(bottomFrame, text="Caixa 02", bg="white", fg="black", command=Caixa2)
# btn2.pack(side=LEFT, anchor=W, fill=X, expand=0)
btn2.bind('<Button-1>', Aguarde)
btn2.grid(column=1, row=1)

btn3 = Button(bottomFrame, text="Caixa 03", bg="white", fg="black", command=Caixa3)
# btn3.pack(side=LEFT, anchor=W, expand=0)
btn3.bind('<Button-1>', Aguarde)
btn3.grid(column=2, row=1)

btn4 = Button(bottomFrame, text="Caixa 04", bg="white", fg="black", command=Caixa4)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn4.bind('<Button-1>', Aguarde)
btn4.grid(column=3, row=1)

btn5 = Button(bottomFrame, text="Caixa 05", bg="white", fg="black", command=Caixa5)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn5.bind('<Button-1>', Aguarde)
btn5.grid(column=4, row=1)

btn6 = Button(bottomFrame, text="Caixa 06", bg="white", fg="black", command=Caixa6)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn6.bind('<Button-1>', Aguarde)
btn6.grid(column=5, row=1)

btn7 = Button(bottomFrame, text="Caixa 07", bg="white", fg="black", command=Caixa7)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn7.bind('<Button-1>', Aguarde)
btn7.grid(column=6, row=1)

btn8 = Button(bottomFrame, text="Caixa 08", bg="white", fg="black", command=Caixa8)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn8.bind('<Button-1>', Aguarde)
btn8.grid(column=7, row=1)

btn9 = Button(bottomFrame, text="Caixa 09", bg="white", fg="black", command=Caixa9)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn9.bind('<Button-1>', Aguarde)
btn9.grid(column=8, row=1)

btn10 = Button(bottomFrame, text="Caixa 10", bg="white", fg="black", command=Caixa10)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn10.bind('<Button-1>', Aguarde)
btn10.grid(column=9, row=1)


btnSair = Button(bottomFrame, text="SAIR", bg="red", fg="yellow", font="Arial 12", command=sair)
#btnSair.pack(anchor=SE, expand=1)
btnSair.grid(column=11, row=6)

T = Text(gui, height=5, width=80)
T.place(x=1, y=140)
T.insert(END,
         "(PARA REMARCA)Erros:\n1    - Verificar usu�rio e senha no Windows\n2    - Verificar arquivos (inicia_pdv.bat / desligar.bat) na pasta PDV\n53   - Verificar cabos de rede\n1326 - Verificar usuario e senha no Windows")

gui.mainloop()
