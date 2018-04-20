# data-digester

Repositório dedicado ao aprendizado com os dados coletados pelo biodigestor

# Configurando o ambiente

1. Clonando o repositório:
```
git clone https://github.com/jarvis-fga/Projetos.git
```
2. Construindo a imagem:
```
sudo docker build -t bio-digester .
```
3. Executando o container:
```
sudo docker run -it --name data-digester -p 8888:8888 -v $PWD:/code bio-digester:latest bash
```
