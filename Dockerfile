##Enviroment Variables to configure things

FROM debian

##Setting Shell so pipenv shell works

ENV SHELL=/bin/bash

### Updte and install dependencies

RUN  apt update &&  \
     apt upgrade -y && \
     apt install python3-pip -y && \
     pip3 install pandas && \
     pip3 install regex && \
     pip3 install -i https://test.pypi.org/simple/ lambdata-sberniz
