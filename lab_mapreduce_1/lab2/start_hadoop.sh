#!/usr/bin/env bash

hadoop fs -rm -r output/lab2/*



hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -cacheFile output/lab2/allDocCount#AllDocCount
    -input input/lab_mapreduce_1/* \
    -output output/lab2/result \
    -mapper ~/projects/lab_mapreduce_1/lab2/mapper2.py \
    -reducer ~/projects/lab_mapreduce_1/lab2/mapper2.py \

hadoop fs -cat output/lab2/result/* | head > head_result.dat
