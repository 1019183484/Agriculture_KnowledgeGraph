# -*- coding: utf-8 -*-
import thulac
import csv
import sys
sys.path.append("..")
from Model.neo_models import Neo4j 
from toolkit.vec_API import word_vector_model
	
pre_load_thu = thulac.thulac()  #默认模式
print('thulac open!')

neo_con = Neo4j()   #预加载neo4j
neo_con.connectDB()
print('neo4j connected!')

predict_labels = {}   # 预加载实体到标注的映射字典
with open('toolkit/predict_labels.txt','r') as csvfile:
	reader = csv.reader(csvfile, delimiter=' ')
	for row in reader:
		predict_labels[str(row[0])] = int(row[1])
print('predicted labels load over!')
		
# 读取word vector
wv_model = word_vector_model()
#wv_model.read_vec('toolkit/curvector.txt') # 测试用，节约读取时间
wv_model.read_vec('toolkit/vector.txt')	 