#!/usr/bin/env bash

hadoop fs -rm -r output/lab2/*

# Расчет количества документов
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -Dmapreduce.job.reduces=1 \
    -input input/lab_mapreduce_1/* \
    -output output/IDF/allDocCount \
    -mapper ~/projects/lab_mapreduce_1/IDF/mapper1.py \
    -reducer ~/projects/lab_mapreduce_1/IDF/reducer1.py \

# Расчет IDF
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -files hdfs://127.0.0.1:8020/user/cloudera/output/IDF/allDocCount/part-00000#totalDoc \
    -input input/lab_mapreduce_1/* \
    -output output/lab2/result \
    -mapper ~/projects/lab_mapreduce_1/IDF/mapper2.py \
    -reducer ~/projects/lab_mapreduce_1/IDF/reducer2.py \

# Вывод первых строк результата в файл
hadoop fs -cat output/lab2/result/* | head > head_result.dat
