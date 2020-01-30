1. Spark clusters in Docker

This POC is for demonstrating the technology stack to be used for processing large dataset and using predictive analytics on the same.

The dataset used in this POC is about 2GB in size. However, this same process can be used to process data of virtually any size.

Goals:

We have two broad goals for this POC:

1. To create the tech stack for processing large dataset, such as updating data columns in say million records etc.
2. To process the analytics for the large dataset.

Approach:

The approach used in this POC is of 3 steps:

a. Use a local spark cluster

b. Use Spark on AWS using EMR instances

c. Deploy the spark docker images on kubernetes to scale the cluster.

 
1.1 Setup of Spark image - locally

First let us create the spark docker images. For this we have followed couple of references.

1. Based on the towardsdatascience article
https://towardsdatascience.com/a-journey-into-big-data-with-apache-spark-part-1-5dfcc2bccdd2

2. Dockerfiles for Spark cluster using python app based on Big data Europe's repository https://github.com/big-data-europe/docker-spark

Both the approach use spark version 2.4.x
We use a hybrid approach to create a structure of docker images to be created for Spark Master and Workers.


Here are some docker details:

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

The initial POC is for simply processing the data from mongodb cluster into a notebook. The working notebook is available in the below jupyter notebook.

https://github.com/colaberry/ai-poc/blob/master/spark/Regression_Model_MongoDB.ipynb

