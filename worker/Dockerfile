FROM mani/spark:1.0

LABEL maintainer="Mani"

COPY worker.sh /

ENV SPARK_WORKER_WEBUI_PORT 8081
ENV SPARK_WORKER_LOG /spark/logs
ENV SPARK_MASTER "spark://spark-master:7077"


COPY requirements.txt /
RUN python3.7 -m pip install pip \
  && pip3 install -r requirements.txt

EXPOSE 8081

CMD ["/bin/bash", "/worker.sh"]
