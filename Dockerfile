FROM python:3.7-stretch

RUN apt-get -yy update && apt-get -yy upgrade

RUN mkdir /app
WORKDIR /app
COPY . /app


RUN pip3 install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python" ]

CMD [ "app.py" ]
