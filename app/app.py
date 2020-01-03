#USER DEFINITIONS
from user_definition import *

# this should be file_roots = ['../data/A/', '../data/B/'] for original subset where data dir
# is at one level high in hierarchy and where data/A and data/B have all the subdirs that eventually
# contain song .h5 files
# I've here used a dummy root for sanity check with a sample data
file_roots = ['/data/A/C/A']

#PYTHON
#import h5py
#import json
from collections import defaultdict
#import numpy as np
import os

#SPARK
from pyspark import SparkContext, SparkConf
from pyspark.sql import SQLContext
from pyspark.sql.types import *
from pyspark.sql import Row

#SPARK CONFIGS
conf = SparkConf().setAppName("App")
conf = (conf.setMaster('local[*]')
        .set('spark.executor.memory', executor_mem)
        .set('spark.driver.memory', driver_mem)
        .set('spark.driver.maxResultSize', max_result)
        .set('spark.yarn.executor.memoryOverhead', overhead))
sc = SparkContext(conf = conf)
sqlContext = SQLContext(sc)

#PYMONGO
#from pymongo import MongoClient

print('Imports Ready')
print('Driver Memory', sc._conf.get('spark.driver.memory'))
print('Executor Memory', sc._conf.get('spark.executor.memory'))
print('Max Result Size', sc._conf.get('spark.driver.maxResultSize'))
print('\n')
#########################################################
                ###FUNCTIONS###


print('{} songs are inserted to collection: "{}" (MONGODB)'.format(1,2))












