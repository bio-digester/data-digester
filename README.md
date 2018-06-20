# data-digester

Repositório dedicado ao aprendizado com os dados coletados pelo biodigestor

# Configurando o ambiente

1. Clonando o repositório:
```
git clone https://github.com/jarvis-fga/Projetos.git
```
2. Executando os serviços:
```
sudo docker-compose up
```

# Endpoints
## Samples
```
http://localhost:8000/api/samples/
```
__get__ : recebe a lista de todas as amostras armazenadas

__post__: enviar uma lista de amostras

## Optimize
```
http://localhost:8000/api/optimize/
```
__get__ : recebe combinação de parâmetros com a respectiva predição da produção de gás
