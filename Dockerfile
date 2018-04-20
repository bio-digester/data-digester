from python:latest

run mkdir /code
workdir /code

add . /code/
run pip install -r requirements.txt

expose 8888
cmd jupyter notebook --ip=0.0.0.0 --allow-root
