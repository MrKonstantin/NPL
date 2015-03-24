#!/usr/bin/env bash

hadoop fs -rm -r output/lab_mapreduce_1/Centroid

# Расчет количества документов
# && Расчет IDF
# && Вывод первых строк результата в файл
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -input output/lab_mapreduce_1/TFIDF/result/* \
    -output output/lab_mapreduce_1/Centroid \
    -mapper ~/projects/lab_mapreduce_1/Centroid/mapper1.py \
    -reducer ~/projects/lab_mapreduce_1/Centroid/reducer1.py \
&& hadoop fs -cat output/lab_mapreduce_1/Centroid/* | head > head_result.dat
