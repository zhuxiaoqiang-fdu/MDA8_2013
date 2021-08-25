#!/public/software/nodes/python361/bin/python3
import pandas as pd
import os
import numpy as np

sthr = 2013070201
nday = 30
stationfile = './city_sites.txt.bk.modified'
obsdir = '/public/home/data/zhusq/post_cmaq/obs_2013_china/o3'

def findfiles(fpath,wd):
    files=os.listdir(fpath)
    result=[]
    for s in files:
        s_path=os.path.join(fpath,s)
        if os.path.isdir(s_path):
            findfiles(s_path,files_list)
        elif os.path.isfile(s_path) and wd in s:
            result.append(s_path)
    return result

station=pd.read_csv(stationfile,header=None,delim_whitespace=True)
lenst=len(station)
st = 0

def get_mda8(data):
    s = (data <= 0).astype(int).sum(axis=0)
    data.index = range(24)
    if s[1] > 6 :
        return -999
    else:
        avg_list = []
        for i in range(16):
            avg = 0
            num = 0
            for j in range(8):
                if data[1][i+j] > 0:
                    avg = avg + data[1][i+j]
                    num = num + 1
            avg_list.append(avg/num)
        mda8 = max(avg_list)
        return mda8        

df = pd.DataFrame(columns = ['station', 'val'])
sn = 0
while st < lenst:
    obsf = findfiles(obsdir, station[1][st])
    print(obsf)
    mda = []
    for i in range(len(obsf)):
        temp = pd.read_csv(obsf[i], header=None, sep=',')
        a = temp.loc[temp[0] == sthr].index.tolist()
        for dy in range(nday):
            temp_day = temp.iloc[range((a[0]+dy*24),(a[0]+dy*24+24))]
            mda8 = get_mda8(temp_day)
            if mda8 > 0:
                mda.append(mda8)
    df.loc[sn] = [station[1][st], np.mean(mda)]
    sn = sn + 1
    st = st + len(obsf)

df.to_csv('result_'+str(sthr),header=0,index=0,sep='\t')







