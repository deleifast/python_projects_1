import socket

hostName    = ""

ipAddress   = socket.gethostbyname_ex(socket.gethostname())

print("Nome e ip {} : {}".format(hostName,ipAddress))

with open('caixa.txt', 'a') as caixa:
			caixa.write(str("Nome e ip {} : {}".format(hostName,ipAddress)))
			caixa.close()
		