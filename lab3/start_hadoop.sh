hadoop fs -rm -r output/lab3
hadoop fs -mkdir output/lab3

hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -files mapper.py,reducer.py,user_categories.dat \
        -input s3n://newprolab/lab3data/* \
        -output output/lab3/lab3_users.txt \
        -mapper "python mapper.py" \
        -reducer "python reducer.py"\
&& hadoop fs -cat output/lab3/lab3_users.txt/* | sort -nk1 > lab3_users.txt
