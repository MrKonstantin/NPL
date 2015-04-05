hadoop fs -rm -r output/lab2_sa
hadoop fs -mkdir output/lab2_sa

hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -files mapper1.py,reducer1.py \
        -input s3n://newprolab/facetz_2015_02_03/* \
        -output output/lab2_sa/mapreduce1 \
        -mapper "python mapper1.py" \
        -reducer "python reducer1.py" \
&& hadoop  fs -cat ouput/lab2_sa/mapreduce1/* | sort -rnk2 | head -n350 > top350.txt
