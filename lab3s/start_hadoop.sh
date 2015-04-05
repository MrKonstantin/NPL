hadoop fs -rm -r output/lab3s
hadoop fs -mkdir output/lab3s
rm auto_number.txt

hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -files mapper1.py,count_auto.py,autousers_lab3s.txt \
        -input s3n://newprolab/lab3data/part-0000[0-18] \
        -output output/lab3s/count_auto.txt \
        -mapper "python mapper1.py" \
        -reducer "python count_auto.py"\
&& hadoop fs -cat output/lab3s/count_auto.txt/* > auto_number.txt\
&& hadoop jar /opt/cloudera/parcels/CDH/lib/hadoop-mapreduce/hadoop-streaming.jar \
        -files mapper1.py,reducer1.py,autousers_lab3s.txt,auto_number.txt \
        -input s3n://newprolab/lab3data/part-0000[0-18] \
        -output output/lab3s/lab3Sdomains.txt \
        -mapper "python mapper1.py" \
        -reducer "python reducer1.py"\
&& hadoop fs -cat output/lab3s/lab3Sdomains.txt/* | python count.py > lab3Sdomains.txt

rm ../lab3Sdomains.txt
mv lab3Sdomains.txt ../.
