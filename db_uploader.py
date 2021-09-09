import pandas as pd
from pandas import DataFrame as Df
from collections import Counter
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")
import django
django.setup()
from algorithm.models import Keyword

df = Df(pd.read_csv('키워드_Column_추출.csv'))
df = df.dropna()
listkey = []
keyword = []

def keylog():
    for i in range(7):
        keyword = df.loc[i, '키워드'].split(',')
        for j in range(0, len(keyword)):
            listkey.append(keyword[j])

    return listkey

def frequency_sort(data):
    rt_data = []
    for d, c in Counter(data).most_common():
        for i in range(c):
            rt_data.append(d)
    return rt_data

def overlap(a,b):
    for i in a:
        if i not in b:
            b.append(i)
    return b

keylog()
listkey = frequency_sort(listkey)
overlap(listkey,keyword)
if __name__ == '__main__':
    for t in keyword:
        Keyword(keyword=t).save()
# print(keyword)
