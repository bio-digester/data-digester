from python:latest

copy ./start.sh /start.sh
copy . /code
workdir /code

run pip install -r requirements.txt \
    && chmod +x /start.sh

expose 8000

cmd /start.sh
