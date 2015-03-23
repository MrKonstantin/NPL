#!/usr/bin/env bash

hadoop fs -rm -r output/lab_mapreduce_1/TFIDF/*

# Расчет количества документов
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -input input/lab_mapreduce_1/* \
    -input output/lab_mapreduce_1/IDF/* \
    -output output/lab_mapreduce_1/TFIDF/mapreduce1 \
    -mapper ~/projects/lab_mapreduce_1/TFIDF/mapper.py \
    -reducer ~/projects/lab_mapreduce_1/TFIDF/reducer.py

# Расчет IDF
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -input output/lab_mapreduce_1/TFIDF/mapreduce1/* \
    -output output/lab_mapreduce_1/TFIDF/result \
    -mapper ~/projects/lab_mapreduce_1/TFIDF/mapper2.py \
    -reducer ~/projects/lab_mapreduce_1/TFIDF/reducer2.py

# Вывод первых строк результата в файл
hadoop fs -cat output/lab_mapreduce_1/TFIDF/result/* | head > head_result.dat
