1. Spark clusters in Docker

1.1 Setup of Spark image - locally

Based on the towardsdatascience article
https://towardsdatascience.com/a-journey-into-big-data-with-apache-spark-part-1-5dfcc2bccdd2

Uses : spark-2.4.4-bin-hadoop2.7
openjdk:8-alpine

Created a docker image from docker file :
$USER/spark:latest (mani/spark:latest)

Dockerfile : /home/mani/workspace/spark/Dockerfile
Docker Image : mani/spark:latest
Docker Compose : /home/mani/workspace/spark/docker-compose.yml

Masternode and Workernodes are created by running:
docker-compose up --scale spark-worker=3

which creates 3 worker nodes in a local cluster.

WebUI location: http://localhost:8080 


Commands to start master and worker within container:

master : /spark/bin/spark-class org.apache.spark.deploy.master.Master --ip `hostname` --port 7077 --webui-port 8080

worker :  /spark/bin/spark-class org.apache.spark.deploy.worker.Worker \
    --webui-port 8080 spark://spark-master:7077


2. Live data analytics using MongoDB

https://github.com/colaberry/ai-poc/blob/master/spark/Regression_Model_MongoDB.ipynb

