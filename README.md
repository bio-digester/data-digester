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

Exemplo resposta:
```json
[
    {
        "water_flow": 1.0,
        "temperature": 25.0,
        "internal_pressure": 123.0,
        "ph": 6.0,
        "volume": 15.0,
        "gas_production": 56.0
    }
]
```


__post__: enviar uma lista de amostras

Exemplo envio:
```json
[
    {
        "water_flow": 1.0,
        "temperature": 25.0,
        "internal_pressure": 123.0,
        "ph": 6.0,
        "volume": 15.0,
        "gas_production": 56.0
    }
]
```
Exemplo resposta: confirmação de recebimento com mesmos dados enviados.

## Optimize
```
http://localhost:8000/api/optimize/
```
__get__ : recebe combinação de parâmetros com a respectiva predição da produção de gás

Exemplo resposta:
```json
[
    {
        "temperature": 30,
        "internal_pressure": 0.5,
        "ph": 6.5,
        "volume": 0.3,
        "prediction": 14.502904695609919
    },
    {
        "temperature": 30,
        "internal_pressure": 0.5,
        "ph": 6.5,
        "volume": 0.4,
        "prediction": 14.526243513481074
    }
]
```
