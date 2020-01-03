#FROM python:3.8.1-alpine3.11
FROM ubuntu:18.04

RUN apt-get update

RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y \
    wget \
    python3 \
    python3-dev \
  && apt-get clean

RUN wget http://mirrors.estointernet.in/apache/spark/spark-2.4.4/spark-2.4.4-bin-hadoop2.7.tgz

RUN tar -xzf spark-2.4.4-bin-hadoop2.7.tgz && \
    mv spark-2.4.4-bin-hadoop2.7 /spark && \
    rm spark-2.4.4-bin-hadoop2.7.tgz

COPY wait-for-step.sh /
COPY execute-step.sh /
COPY finish-step.sh /
#COPY master.sh /
#COPY worker.sh /
#COPY submit.sh /

RUN apt-get install -y curl bash default-jre python-nss 
      #&& cd /css \
      #&& jar uf /spark/jars/spark-core_2.11-${SPARK_VERSION}.jar org/apache/spark/ui/static/timeline-view.css \
      

RUN chmod +x /wait-for-step.sh && chmod +x /execute-step.sh && chmod +x /finish-step.sh

