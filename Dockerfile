from python:latest

run mkdir /code
workdir /code

add . /code/
run pip install -r requirements.txt

expose 8888
expose 8000

cmd python3 manage.py runserver 0.0.0.0:8000
