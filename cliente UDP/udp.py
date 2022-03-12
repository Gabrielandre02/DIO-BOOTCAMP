import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente Socket Criado com sucesso')

host = 'localhost'
port = 5433
mensagem = 'Olá Beleza?'

try:
    print('Cliente:' + mensagem)
    s.sendto(mensagem.encode(), (host, 5432))

    
    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print("Cliente: {}".format(dados))\

finally:
    print('Cliente: Fechando a conexão')
    s.close()