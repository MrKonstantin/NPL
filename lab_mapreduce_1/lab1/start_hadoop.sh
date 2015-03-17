#!/usr/bin/env bash

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -input /user/cloudera/input/lab1/* -output /user/cloudera/output/lab2 -mapper /home/cloudera/projects/lab1/mapper.py -reducer /home/cloudera/projects/lab1/reducer.sh
