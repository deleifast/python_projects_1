# -*- coding: iso-8859-1 -*-
"""Autor: César T. Silva <cesarts25@gmail.com> <magodoschatsbh@gmail.com>
   Data: 05/04/2012
   Copyrigth: Este software pode ser usado, alterado e distribuido de mandeira livre, desde que se mantenha a nota de autoria.
   Descrição: Leia todos os valores (nodeValue) de todos os nodos do xml atraves de recurssao em nodos populados (+1 filho)
"""
import hashlib , sys, md5,time
import xml.dom.minidom
class ReadXml():
    """INSTANCIA XML PARA INICIO DA LEITURA"""
    def __init__(self,arquivo):
        try:
            print ("INICIANDO LEITURA DOS VALORES DO XML...""")
            self.arvore=input("DESEJA IMPRIMIR A ESTRUTURA DO ARQUIVO XML? 1(SIM)-0(NAO): ")
            if self.arvore != 1 and self.arvore !=0:
                self.arvore=0
            log=input("DESEJA CRIAR ARQUIVO COM VALORES DO XML? 1(SIM)-0(NAO): ")
            if log !=1 and log!=0:
                log=0
            timea=time.clock()
            self.limite=0
            self.arquivo=arquivo
            self.concat=""
            self.hash=""
            if self.arquivo==1:
                print (5*"*"+"ESTRUTURA XML ABAIXO"+5*"*")
            self.xmls = xml.dom.minidom.parse(arquivo+".xml")
            base = self.xmls.childNodes[0].childNodes
            self.readChild(base)
            self.setHash()
            print (60*'-')
            print ("Nome Arquivo: " + arquivo + ".xml")
            print ("Hash: " + self.hash)
            timeb=time.clock()
            print ("Tempo de Processamento: %f segundo(s)" % (timeb-timea))
            print (60*'-')
            if log:
                self.createLog()
            
        except:
            print (sys.exc_info())
    def readChild(self,base):
        try:
            for node in base:
                if node.localName:
                    if self.arvore:
                        print (self.limite*"-"+"> "+node.localName)
                    if node.localName == "epilogo":
                        continue
                    if len(node.childNodes)>1:
                                    self.limite+=2
                                    self.readChild(nodo for nodo in node.childNodes)
                                    self.limite-=2
                    else:
                                    self.concat+= (node.childNodes[0].nodeValue).strip()
        except:
            print (sys.exc_info())
    
    def setHash(self):
        cod=hashlib.md5()
        cod.update(self.concat.encode('iso-8859-1'))
        self.hash = cod.hexdigest()
        return

    def createLog(self):
        try:
            arq=file(self.arquivo+"_Texto.txt","w")
            arq.write(self.concat.encode('iso-8859-1'))
            arq.close()
        except:
            print ("Erro ao salvar arquivo log: " +  sys.exc_info())

concat = ReadXml("NOME-DO-ARQUIVO-SEM-EXTENSAO")
