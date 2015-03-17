#!/usr/bin/env bash

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar -input input/lab1/* -output output/lab1 -mapper ~/projects/lab_mapreduce_1/lab1/mapper.py -reducer ~/projects/lab_mapreduce_1/lab1/reducer.sh
hadoop fs -cat output/lab1/* | head > head_result.dat
