#!/usr/bin/env bash

hadoop fs -rm -r output/lab_mapreduce_1/TFIDF/*

# Расчет количества документов
# && Расчет IDF
# && Вывод первых строк результата в файл
hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -input input/lab_mapreduce_1/data.json \
    -input output/lab_mapreduce_1/IDF/result/* \
    -output output/lab_mapreduce_1/TFIDF/mapreduce1 \
    -mapper "python3 mapper.py" \
    -reducer "python3 reducer.py" \
&& hadoop jar /usr/lib/hadoop-mapreduce/hadoop-streaming.jar \
    -input output/lab_mapreduce_1/TFIDF/mapreduce1/* \
    -output output/lab_mapreduce_1/TFIDF/result \
    -mapper "python3 mapper2.py" \
    -reducer "python3 reducer2.py" \
&& hadoop fs -cat output/lab_mapreduce_1/TFIDF/result/* | head > head_result.dat
