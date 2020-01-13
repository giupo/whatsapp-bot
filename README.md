Whatsapp bot
================

This repository contains the code taken from this blog post https://www.twilio.com/blog/build-a-whatsapp-chatbot-with-python-flask-and-twilio 
Please reference the aforementioned link for instructions and HOWTOs.

I've just added a WSGI server and a Dockerfile for convenience.

The docker container is on hub.docker.com as `giupo/whatsapp-bot`, you can run it as :
```
docker run -p 5000:5000 giupo/whatsapp-bot
```
