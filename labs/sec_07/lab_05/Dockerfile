FROM ubuntu:latest

RUN apt-get update
RUN apt-get install -y wget unzip

RUN wget -O /tmp/sample.zip https://getsamplefiles.com/download/zip/sample-2.zip && unzip /tmp/sample.zip -d /app && rm /tmp/sample.zip
# Tốn 5.0s để build

#RUN wget -O /tmp/sample.zip https://getsamplefiles.com/download/zip/sample-2.zip
#RUN unzip /tmp/sample.zip -d /app
#RUN rm /tmp/sample.zip
# Tốn 20.1s để build

CMD ["ls", "/app"]