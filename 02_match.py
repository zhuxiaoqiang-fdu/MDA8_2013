#!/public/software/nodes/python361/bin/python3
import pandas as pd
import os
import numpy as np

sta_mat = pd.read_csv('city_sites.txt.bk.modified',header=None,delim_whitespace=True)
sta_xy = pd.read_csv('/data1/zhusq/long_trend_O3/post_cmaq/03_extract_1layer/36km.xy.China_2019jl.txt',header=None,delim_whitespace=True)
sta_con_name='result_2013070201'
sta_con = pd.read_csv(sta_con_name,index_col=0,header=None,delim_whitespace=True)

df = pd.DataFrame(columns=['x','y','con'])
df[['x','y']] = df[['x','y']].astype(np.int8)
df.dtypes
sta_name = sta_con.index
for i in range(len(sta_name)):
    sta = sta_name[i]
    temp = sta_mat.loc[sta_mat[1] == sta]
    temp_xy = temp[0].tolist()
    if len(temp_xy) == 0:
        continue
    avg_x = 0
    avg_y = 0
    for xy in temp_xy:
        txy = sta_xy.loc[sta_xy[0] == xy]
        avg_x = avg_x + txy.iloc[0,1]
        avg_y = avg_y + txy.iloc[0,2]
    df.loc[i] = [str(round(avg_x/len(temp_xy))), str(round(avg_y/len(temp_xy))), sta_con[1][sta]]
    
df.to_csv(sta_con_name+'_for_plot',header=0,index=0,sep='\t')


















