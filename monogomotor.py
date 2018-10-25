# -*- coding: utf-8 -*-

# A função connect é usada para connectar a um banco de dados
from mongomotor import connect

# Conectamos uma vez quando nosso programa começa e está feita a conexão.

# Usando connect() sem parâmetros, o mongomotor vai tentar se conectar ao
# mongo em localhost na porta 27017, o padrão para a instalação.
connect()

# Se necessário é possível passar outros parâmetros, além dos parâmetros de
# autenticação
connect(host='my.mongo.host', port=1234,
        username='myself', password='my-password')
