#FROM bde2020/spark-python-template:2.4.0-hadoop2.7
#MAINTAINER Srinivasa Chittaluru <cavbtech@gmail.com>
#
##ENV SPARK_MASTER_NAME
##ENV SPARK_MASTER_PORT
#ENV SPARK_APPLICATION_PYTHON_LOCATION /app/SimplePySpark.py
##ENV SPARK_APPLICATION_ARGS "foo bar baz"
FROM openjdk:8-jre-alpine

RUN apk add --update \
    curl \
    && rm -rf /var/cache/apk/*

RUN apk update && apk add wget

RUN apk update && apk add bash

ENV PYTHONUNBUFFERED=1
RUN apk add --update --no-cache python3 && ln -sf python3 /usr/bin/python
RUN python3 -m ensurepip
RUN pip3 install --no-cache --upgrade pip setuptools

#ENV JAVA_HOME /usr/bin
#
#ENV PATH $PATH:$JAVA_HOME/bin
# RUN curl -s --insecure \
#  --header "Cookie: oraclelicense=accept-securebackup-cookie;" ${JAVA_ARCHIVE} \
#  | tar -xz -C /usr/local/ && ln -s $JAVA_HOME /usr/local/java

# SPARK
ARG SPARK_ARCHIVE=https://archive.apache.org/dist/spark/spark-2.4.0/spark-2.4.0-bin-hadoop2.7.tgz
ENV SPARK_HOME /usr/local/spark-2.4.0-bin-hadoop2.7

ENV PATH $PATH:${SPARK_HOME}/bin
RUN curl -s ${SPARK_ARCHIVE} | tar -xz -C /usr/local/

WORKDIR $SPARK_HOME

## first build the docker by using the following command
##docker build --tag spark-client .
## how to run? run the followign commands
## docker run -it -p 8088:8088 \
   #  -p 8042:8042 \
   #  -p 4041:4040 \
   #  -v c://Users/srinivasa/PycharmProjects/CapstoneProject2/sparkclient/dockervolume:/myvol \
   #  --net capstoneproject2_net_pet \
   #  --name driver \
   #  -h driver \
   #  spark-client:latest
##spark-shell --master spark://172.27.1.10:7077 for spark-shell
##to run pyspark use
##