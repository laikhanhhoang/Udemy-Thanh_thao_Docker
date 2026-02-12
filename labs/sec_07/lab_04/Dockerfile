FROM ubuntu:latest

RUN apt-get update

RUN apt-get install -y wget

# RUN echo "Hello Docker layers!" > /message.txt
RUN echo "Hello Docker layers - CACHE!" > /message.txt

CMD ["cat", "/message.txt"]