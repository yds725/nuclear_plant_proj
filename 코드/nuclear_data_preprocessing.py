# train data 만 다 불러서 dictionary에다 넣어놓기

import glob
import pandas as pd
from pprint import pprint

# glob glob
train_csv_files = [file for file in glob.glob("./data/train-002/*.csv")]

train_dic = {}

dic_idx = -1
# 각 csv 파일
for file_name in train_csv_files:
    # csv 파일
    dic_idx += 1
    train_csv = pd.read_csv(file_name)

    # dictionary 만들기
    train_dic[dic_idx] = train_csv

pprint(train_dic)









































