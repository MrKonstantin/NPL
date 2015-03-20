#!/usr/bin/env bash

hadoop fs -rm -r output/lab2/*

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -Dmapreduce.job.reduces=1 \
    -input input/lab_mapreduce_1/* \
    -output output/lab2/allDocCount \
    -mapper ~/projects/lab_mapreduce_1/lab2/mapper1.py \
    -reducer ~/projects/lab_mapreduce_1/lab2/reducer1.py \

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -files hdfs://127.0.0.1:8020/user/cloudera/output/lab2/allDocCount#AllDocCount \
    -input input/lab_mapreduce_1/* \
    -output output/lab2/result \
    -mapper ~/projects/lab_mapreduce_1/lab2/mapper2.py \
    -reducer ~/projects/lab_mapreduce_1/lab2/mapper2.py \

hadoop fs -cat output/lab2/result/* | head > head_result.dat
