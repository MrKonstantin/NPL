
hadoop fs -rm -r output/TFIDF
hadoop fs -mkdir output/TFIDF
chmod +x mapper.py
chmod +x mapper2.py
chmod +x reducer.py
chmod +x reducer2.py
chmod +x start_hadoop.sh