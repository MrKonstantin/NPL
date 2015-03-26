#!/usr/bin/env bash

hadoop fs -rm -r output/lab_mapreduce_1/Centroid

# Расчет количества посещений для каждого сайта
# && Выборка ТОП350
# && Вывод первых строк результата в файл
hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -file mapper.py \
        -input s3n://newprolab/facetz_2015_02_0[1-5]\
        -output user/mapreduce1 \
        -mapper "python mapper1.py"
        -reducer "python reducer1.py"\
&& hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -file mapper.py \
        -input s3n://newprolab/facetz_2015_02_0[1-5]\
        -output user/top350.txt \
        -mapper "python mapper2.py"
        -reducer "python reducer2.py"
