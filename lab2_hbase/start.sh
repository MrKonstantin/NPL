hadoop fs -rm -R output/*

hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -file mapper.py \
        -input s3n://newprolab/facetz_2015_02_0[1-5]\
        -output output/lab2 \
        -mapper "python mapper.py"