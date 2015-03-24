#!/usr/bin/env bash

hadoop fs -rm -r output/lab_mapreduce_1/IDF
hadoop fs -rm -r output/lab_mapreduce_1/allDocCount

# Расчет количества документов
# && Расчет IDF
# && Вывод первых строк результата в файл
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -Dmapreduce.job.reduces=1 \
    -input input/lab_mapreduce_1/data.json \
    -output output/lab_mapreduce_1/allDocCount \
    -mapper ~/projects/lab_mapreduce_1/IDF/mapper1.py \
    -reducer ~/projects/lab_mapreduce_1/IDF/reducer1.py \
&& hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -files hdfs://127.0.0.1:8020/user/cloudera/output/IDF/allDocCount/part-00000#totalDoc \
    -input input/lab_mapreduce_1/data.json \
    -output output/lab_mapreduce_1/IDF \
    -mapper ~/projects/lab_mapreduce_1/IDF/mapper2.py \
    -reducer ~/projects/lab_mapreduce_1/IDF/reducer2.py \
&& hadoop fs -cat output/lab_mapreduce_1/IDF/* | head > head_result.dat
