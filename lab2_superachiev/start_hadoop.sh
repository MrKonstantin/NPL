hadoop fs -rm -r output/lab2_sa
hadoop fs -mkdir output/lab2_sa

# Расчет количества посещений для каждого сайта
# && Выборка ТОП350
# && Вывод первых строк результата в файл
hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -files mapper1.py,reducer1.py \
        -input s3n://newprolab/facetz_2015_02_01/part-00006 \
        -output output/lab2_sa/mapreduce1 \
        -mapper "python mapper1.py" \
        -reducer "python reducer1.py"\
&& hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -Dmapreduce.job.reduces=1 \
        -files mapper2.py,reducer2.py \
        -input output/lab2_sa/mapreduce1/* \
        -output output/lab2_sa/top350.txt \
        -mapper "python mapper2.py" \
        -reducer "python reducer2.py" \
&& hadoop fs -cat output/lab2_sa/top350.txt/* > head_top350.txt
