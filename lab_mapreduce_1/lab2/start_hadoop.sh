#!/usr/bin/env bash

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar
    -input input/lab_mapreduce_1/*
    -output output/lab2/allDocCount
    -mapper ~/projects/lab_mapreduce_1/lab2/mapper.py
    -reducer ~/projects/lab_mapreduce_1/lab2/mapper.py
    -Dmapreduce.job.reduces=1

hadoop fs -cat output/lab2/result/* | head > head_result.dat
