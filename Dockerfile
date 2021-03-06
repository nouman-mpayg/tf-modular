FROM ubuntu:18.04

RUN apt-get update

RUN apt-get install docker.io wget unzip python3-pip python3.6 zip libpq-dev -y

RUN ln -s /usr/bin/python3.6 /usr/bin/python

RUN pip3 install requests==2.22.0 --user

RUN wget https://releases.hashicorp.com/terraform/0.11.13/terraform_0.11.13_linux_amd64.zip -q

RUN unzip -o terraform_0.11.13_linux_amd64.zip -d /tmp

RUN mv /tmp/terraform /usr/local/bin/

RUN ln -s /root/.local/bin/* /usr/bin/


