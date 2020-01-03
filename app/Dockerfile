FROM mani/spark-submit:1.0

LABEL maintainer="Mani"

COPY template.sh /

ENV SPARK_MASTER_NAME spark-master
ENV SPARK_MASTER_PORT 7077
ENV SPARK_APPLICATION_PYTHON_LOCATION /app/app.py
ENV SPARK_APPLICATION_ARGS ""

# Copy the requirements.txt first, for separate dependency resolving and downloading
RUN apt-get update \
  && apt-get upgrade -y \
  && apt-get install -y \
    python3.7 python3-pip

COPY requirements.txt /app/
RUN cd /app \
      && python3.7 -m pip install pip \
      && pip3 install -r requirements.txt

# Copy the source code
COPY . /app

