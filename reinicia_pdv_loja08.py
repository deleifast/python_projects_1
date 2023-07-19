# encoding: iso-8859-1
import logging
import subprocess
import time
from tkinter import *
from tkinter import messagebox, StringVar

from PIL import Image, ImageTk

logging.basicConfig(filename="reinicia.log", format="%(asctime)s %(message)s", datefmt='%d-%m-%y %H:%M:%S',
                    level=logging.INFO)
logging.info("Iniciando programa versão 3.0")

gui = Tk()

bottomFrame = Frame(gui)
bottomFrame.pack(side=BOTTOM, anchor=W)


def disable_event():
    pass


gui.title("PDVCORAL_REMARCA - NAGUMO **(LOJA 08)**")
gui.geometry("620x420")
gui.resizable(0,0)
gui.attributes("-toolwindow", 1)
gui.protocol("WM_DELETE_WINDOW", disable_event)
load = Image.open("logo-remarca.png")
render = ImageTk.PhotoImage(load)
img = Label(gui, image=render)
img.image = render
img.place(x=370, y=0)


def sel():
    selection = "ESCOLHIDA OPÇÃO: " + str(var.get()) + " DO MENU!!!"
    label.config(text=selection, bg="red", fg="yellow", font="Terminal 12")
    label.place(x=10, y=50)
    logging.info("Escolheu a opção: " + str(var.get()) + " do menu")


var = IntVar()

R1 = Radiobutton(gui, text="1 - Reiniciar PDVCORAL", variable=var, value=1, font="Arial 10", command=sel)
R1.pack(anchor=NW)

R2 = Radiobutton(gui, text="2 - Reiniciar CPU", variable=var, value=2, font="Arial 10", command=sel)
R2.pack(anchor=NW)

msg = StringVar()
lbl = Label(gui, text="Remarca - telefone: (11)2755-7911 ", fg="red", font="Arial 15")
lbl.place(x=140, y=225)

msg = StringVar()
lbl = Label(gui, text="Versão 3.0", fg="black", font="Arial 8")
lbl.place(x=1, y=400)
# versão 2.0 - Alteração - tirado pdvcoral.exe e colocado inicia_pdv.bat
# versão 3.0 - Inclusão do log - reinicia.log

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
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.1 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 01 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 01 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 01")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.1 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 01 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 01 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
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
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa2():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.2 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 02 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 02 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 02")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.2 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 02 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 02 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
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
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa3():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.3 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 03 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 03 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 03")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.3 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 03 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 03 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
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
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa4():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.4 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 04 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 04 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 04")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.4 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 04 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 04 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
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
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa5():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.5 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 05 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 05 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 05")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.5 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 05 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 05 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
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
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa6():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.6 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 06 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 06 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 06")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.6 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 06 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 06 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
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
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa7():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.7 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 07 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 07 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 07")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.7 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 07 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 07 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
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
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa8():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.8 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 08 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 08 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 08")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.8 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 08 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 08 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
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
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa9():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.9 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 09 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 09 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 09")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.9 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 09 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 09 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
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
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa10():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.10 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 10 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 10 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 10")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.10 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 10 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 10 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
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
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa11():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.11 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 11 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 11 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 11")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.11 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 11 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 11 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 11 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 11 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 11 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa12():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.12 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 12 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 12 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 12")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.12 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 12 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 12 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 12 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 12 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 12 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa13():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.13 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 13 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 13 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 13")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.13 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 13 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 13 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 13 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 13 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 13 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa14():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.14 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 14 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 14 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 14")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.14 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 14 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 14 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 14 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 14 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 14 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa15():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.15 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 15 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 15 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 15")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.15 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA15 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 15 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 15 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 15 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA15 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa16():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.16 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA16 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 16 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 16")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.16 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA16 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 16 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 16 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 16 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA16 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa17():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.17 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 17 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 17 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 17")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.17 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 17 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 17 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 17 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 17 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 17 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa18():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.18 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 18 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 18 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 18")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.18 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 18 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 18 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 18 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 18 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 18 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa19():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.19 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 19 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 19 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 19")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.19 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 19 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 19 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 19 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 19 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 19 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ãƒo 1 ou 2!!!"
            res_texto(res)


def Caixa20():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.20 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 20 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 20 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 20")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.20 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 20 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 20 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 20 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 20 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 20 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa21():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u pdv -p pdv \\\\192.168.8.21 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 21 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 21 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 21")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u pdv -p pdv \\\\192.168.8.21 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 21 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 21 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 21 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 21 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 21 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa22():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.22 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 22 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 22 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 22")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.22 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 22 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 22 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 22 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 22 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 22 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa23():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.23 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 23 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 23 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 23")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.23 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 23 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 23 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 23 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 23 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 23 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa24():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.24 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 24 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 24 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 24")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.24 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 24 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 24 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 24 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 24 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 24 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa25():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.25 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 25 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 25 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 25")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.25 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 25 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 25 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 25 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 25 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 25 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa26():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.26 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 26 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 26 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 26")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.26 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 26 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 26 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 26 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 26 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 26 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa27():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.27 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 27 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 27 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 27")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.27 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 27 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 27 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 27 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 27 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 27 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa28():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.28 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 28 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 28 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 28")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.28 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 28 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 28 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 28 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 28 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 28 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa29():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.29 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 29 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 29 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 29")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.29 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 29 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 29 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 29 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 29 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 29 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa30():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u pdv -p pdv \\\\192.168.8.30 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 30 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 30 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 30")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u pdv -p pdv \\\\192.168.8.30 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 30 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 30 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 30 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 30 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 30 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa31():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.31 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 31 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 31 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 31")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.31 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 31 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 31 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 31 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 31 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 31 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa32():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.32 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 32 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 32 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 32")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.32 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 32 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 32 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 32 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 32 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 32 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa33():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.33 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 33 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 33 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 33")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.33 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 33 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 33 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 33 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 33 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 33 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa34():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.34 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 34 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 34 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 34")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.34 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 34 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 34 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 34 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 34 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 34 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa35():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.35 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 35 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 35 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 35")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.35 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 35 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 35 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 35 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 35 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 35 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa36():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u pdv -p pdv \\\\192.168.8.36 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 36 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 36 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 36")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u pdv -p pdv \\\\192.168.8.36 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 36 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 36 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 36 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 36 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 36 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa37():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.37 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 37 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 37 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 37")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.37 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 37 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 37 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 37 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 37 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA 37 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa38():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.38 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 38 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 38 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O CAIXA 38")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u Nano -p pdv \\\\192.168.8.38 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("CAIXA 38 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("CAIXA 38 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "CAIXA 38 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("CAIXA 38 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("CAIXA38 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa39():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u pdv -p pdv \\\\192.168.8.39 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("SELF_01  - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("SELF_01  - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O SELF_01")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u pdv -p pdv \\\\192.168.8.39 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("SELF_01  - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("SELF_01  - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "SELF_01 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("SELF_01 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("SELF_01 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa40():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u pdv -p pdv \\\\192.168.8.40 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("SELF_02 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("SELF_02 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O SELF_02")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u pdv -p pdv \\\\192.168.8.40 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("SELF_02 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("SELF_02 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "SELF_02 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("SELF_02 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("SELF_02 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa41():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u pdv -p pdv \\\\192.168.8.115 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("SELF_03 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("SELF_03 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O SELF_03")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u pdv -p pdv \\\\192.168.8.115 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("SELF_03 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("SELF_03 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "SELF_03 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("SELF_03 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("SELF_03 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
            res_texto(res)


def Caixa42():
    if var.get() == 1:
        ret = subprocess.call("psexec.exe -d -i -u pdv -p pdv \\\\192.168.8.117 ""c:\\pdv\inicia_pdv.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("SELF_04 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("SELF_04 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            telamotivo()
            logging.info("REINICIADO O SELF_04")

    elif var.get() == 2:
        ret = subprocess.call("psexec.exe -d -i -u pdv -p pdv \\\\192.168.8.117 ""c:\\pdv\desligar.bat", shell=True)
        if ret == 53:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "FORA DA REDE, VERIFICAR!!")
            logging.info("SELF_04 - FORA DA REDE, VERIFICAR!!")
            if resp == "ok":
                res = "Verificar Rede!!           erro:" + str(ret)
                res_texto(res)
        elif ret == 1326:
            time.sleep(5)
            resp = messagebox.showerror("Erro", "CAIXA SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            logging.info("SELF_04 - SEM USUÁRIO OU SEM REDE - LIGUE REMARCA")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
        elif ret != 2:
            time.sleep(5)
            resp = messagebox.showinfo("Informacao", "SELF_04 ESTA SENDO REINICIADO, AGUARDE...")
            logging.info("SELF_04 ESTA SENDO REINICIADO, AGUARDE...")
            if resp == "ok":
                res = "Pronto!!!"
                res_texto(res)
        else:
            resp = messagebox.showerror("Erro", "ERRO - LIGAR PARA A REMARCA!")
            logging.info("SELF_04 - ERRO - LIGAR PARA A REMARCA!")
            if resp == "ok":
                res = "LIGUE - REMARCA            erro:" + str(ret)
                res_texto(res)
    else:
        resp = messagebox.showwarning("Alerta", "ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        logging.info("ESCOLHA:  1 - Reiniciar PDVCORAL  OU  2 - REINICIAR CPU!")
        if resp == "ok":
            res = "Clique na opÃ§Ã£o 1 ou 2!!!"
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

btn11 = Button(bottomFrame, text="Caixa 11", bg="white", fg="black", command=Caixa11)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn11.bind('<Button-1>', Aguarde)
btn11.grid(column=0, row=2)

btn12 = Button(bottomFrame, text="Caixa 12", bg="white", fg="black", command=Caixa12)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn12.bind('<Button-1>', Aguarde)
btn12.grid(column=1, row=2)

btn13 = Button(bottomFrame, text="Caixa 13", bg="white", fg="black", command=Caixa13)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn13.bind('<Button-1>', Aguarde)
btn13.grid(column=2, row=2)

btn14 = Button(bottomFrame, text="Caixa 14", bg="white", fg="black", command=Caixa14)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn14.bind('<Button-1>', Aguarde)
btn14.grid(column=3, row=2)

btn15 = Button(bottomFrame, text="Caixa 15", bg="white", fg="black", command=Caixa15)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn15.bind('<Button-1>', Aguarde)
btn15.grid(column=4, row=2)

btn16 = Button(bottomFrame, text="Caixa 16", bg="white", fg="black", command=Caixa16)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn16.bind('<Button-1>', Aguarde)
btn16.grid(column=5, row=2)

btn17 = Button(bottomFrame, text="Caixa 17", bg="white", fg="black", command=Caixa17)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn17.bind('<Button-1>', Aguarde)
btn17.grid(column=6, row=2)

btn18 = Button(bottomFrame, text="Caixa 18", bg="white", fg="black", command=Caixa18)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn18.bind('<Button-1>', Aguarde)
btn18.grid(column=7, row=2)

btn19 = Button(bottomFrame, text="Caixa 19", bg="white", fg="black", command=Caixa19)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn19.bind('<Button-1>', Aguarde)
btn19.grid(column=8, row=2)

btn20 = Button(bottomFrame, text="Caixa 20", bg="white", fg="black", command=Caixa20)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn20.bind('<Button-1>', Aguarde)
btn20.grid(column=9, row=2)

btn21 = Button(bottomFrame, text="Caixa 21", bg="white", fg="black", command=Caixa21)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn21.bind('<Button-1>', Aguarde)
btn21.grid(column=0, row=3)

btn22 = Button(bottomFrame, text="Caixa 22", bg="white", fg="black", command=Caixa22)
# btn2.pack(side=LEFT, anchor=W, fill=X, expand=0)
btn22.bind('<Button-1>', Aguarde)
btn22.grid(column=1, row=3)

btn23 = Button(bottomFrame, text="Caixa 23", bg="white", fg="black", command=Caixa23)
# btn3.pack(side=LEFT, anchor=W, expand=0)
btn23.bind('<Button-1>', Aguarde)
btn23.grid(column=2, row=3)

btn24 = Button(bottomFrame, text="Caixa 24", bg="white", fg="black", command=Caixa24)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn24.bind('<Button-1>', Aguarde)
btn24.grid(column=3, row=3)

btn25 = Button(bottomFrame, text="Caixa 25", bg="white", fg="black", command=Caixa25)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn25.bind('<Button-1>', Aguarde)
btn25.grid(column=4, row=3)

btn26 = Button(bottomFrame, text="Caixa 26", bg="white", fg="black", command=Caixa26)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn26.bind('<Button-1>', Aguarde)
btn26.grid(column=5, row=3)

btn27 = Button(bottomFrame, text="Caixa 27", bg="white", fg="black", command=Caixa27)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn27.bind('<Button-1>', Aguarde)
btn27.grid(column=6, row=3)

btn28 = Button(bottomFrame, text="Caixa 28", bg="white", fg="black", command=Caixa28)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn28.bind('<Button-1>', Aguarde)
btn28.grid(column=7, row=3)

btn29 = Button(bottomFrame, text="Caixa 29", bg="white", fg="black", command=Caixa29)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn29.bind('<Button-1>', Aguarde)
btn29.grid(column=8, row=3)

btn30 = Button(bottomFrame, text="Caixa 30", bg="white", fg="black", command=Caixa30)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn30.bind('<Button-1>', Aguarde)
btn30.grid(column=9, row=3)

btn31 = Button(bottomFrame, text="Caixa 31", bg="white", fg="black", command=Caixa31)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn31.bind('<Button-1>', Aguarde)
btn31.grid(column=0, row=4)

btn32 = Button(bottomFrame, text="Caixa 32", bg="white", fg="black", command=Caixa32)
# btn2.pack(side=LEFT, anchor=W, fill=X, expand=0)
btn32.bind('<Button-1>', Aguarde)
btn32.grid(column=1, row=4)

btn33 = Button(bottomFrame, text="Caixa 33", bg="white", fg="black", command=Caixa33)
# btn3.pack(side=LEFT, anchor=W, expand=0)
btn33.bind('<Button-1>', Aguarde)
btn33.grid(column=2, row=4)

btn34 = Button(bottomFrame, text="Caixa 34", bg="white", fg="black", command=Caixa34)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn34.bind('<Button-1>', Aguarde)
btn34.grid(column=3, row=4)

btn35 = Button(bottomFrame, text="Caixa 35", bg="white", fg="black", command=Caixa35)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn35.bind('<Button-1>', Aguarde)
btn35.grid(column=4, row=4)

btn36 = Button(bottomFrame, text="Caixa 36", bg="white", fg="black", command=Caixa36)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn36.bind('<Button-1>', Aguarde)
btn36.grid(column=5, row=4)

btn37 = Button(bottomFrame, text="Caixa 37", bg="white", fg="black", command=Caixa37)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn37.bind('<Button-1>', Aguarde)
btn37.grid(column=6, row=4)

btn38 = Button(bottomFrame, text="Caixa 38", bg="white", fg="black", command=Caixa38)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn38.bind('<Button-1>', Aguarde)
btn38.grid(column=7, row=4)

btn39 = Button(bottomFrame, text="SELF  01", bg="red", fg="yellow", command=Caixa39)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn39.bind('<Button-1>', Aguarde)
btn39.grid(column=0, row=5)

btn40 = Button(bottomFrame, text="SELF  02", bg="red", fg="yellow", command=Caixa40)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn40.bind('<Button-1>', Aguarde)
btn40.grid(column=1, row=5)

btn41 = Button(bottomFrame, text="SELF  03", bg="red", fg="yellow", command=Caixa41)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn41.bind('<Button-1>', Aguarde)
btn41.grid(column=2, row=5)

btn42 = Button(bottomFrame, text="SELF  04", bg="red", fg="yellow", command=Caixa42)
# btn1.pack(side=LEFT, anchor=W, expand=0)
btn42.bind('<Button-1>', Aguarde)
btn42.grid(column=3, row=5)

btnSair = Button(bottomFrame, text="SAIR", bg="red", fg="yellow", font="Arial 12", command=sair)
# btnSair.pack(anchor=SE, expand=1)
btnSair.grid(column=11, row=6)

T = Text(gui, height=5, width=80)
T.place(x=1, y=140)
T.insert(END,
         "(PARA REMARCA)Erros:\n1    - Verificar usuário e senha no Windows\n2    - Verificar arquivos (inicia_pdv.bat / desligar.bat) na pasta PDV\n53   - Verificar cabos de rede\n1326 - Verificar usuario e senha no Windows")

gui.mainloop()
