import socket

ip_local = socket.gethostbyname(socket.gethostname())
print(f'IP Local: {ip_local}')

dic = { 'ip maquina' : ip_local,
       'dsfdsf' : 'sdasdadsa'}

print(dic)