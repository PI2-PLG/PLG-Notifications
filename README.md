<p align="center">
  <img width="200" height="200" src="https://user-images.githubusercontent.com/18190061/65366176-f592ff00-dbf6-11e9-9b7a-8cc5c6d85ddc.png">
</p>

# Projeto Lobo-Guará - Notifications
### Sistema de monitoramento de queimadas feito por alunos da Universidade de Brasília.

Este repositório é o responsável pelo microsserviço de notificações

## Requisitos
Para executar o sistema é necessário possuir o **docker** e o **docker-compose** instalados em seu ambiente. Você pode verificar como instalar estas ferramentas nos links a seguir:

* [docker](https://docs.docker.com/install/linux/docker-ce/ubuntu/)
* [docker-compose](https://docs.docker.com/compose/install/)

## Como utilizar?

Tendo o docker e o docker-compose instalados em seu ambiente execute os passos a seguir:

```

$ docker-compose -f docker-compose.yml build

```

A imagem docker será então construída. Execute o comando a seguir para rodar o sistema:

```

$ docker-compose -f docker-compose.yml up

```

Com o processo tendo funcionado perfeitamente, será possível acessar a interface da API em:

* https:\\\\localhost:8000

## Exemplos de requisição:

* Requisição de todas as notificações

```

curl -X GET http://localhost:8001/all-notifications/

```