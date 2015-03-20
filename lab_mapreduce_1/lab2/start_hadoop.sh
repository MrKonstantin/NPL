#!/usr/bin/env bash

hadoop fs -rm -R output/lab2/*

hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -Dmapreduce.job.reduces=1
    -input input/lab_mapreduce_1/* \
    -output output/lab2/allDocCount \
    -mapper ~/projects/lab_mapreduce_1/lab2/mapper.py \
    -reducer ~/projects/lab_mapreduce_1/lab2/mapper.py \
<<<<<<< HEAD
    -D mapreduce.job.reduces=1
=======
>>>>>>> b25cc6d9e56a9f7717a1e1470087acf34b4be651

hadoop fs -cat output/lab2/result/* | head > head_result.dat
