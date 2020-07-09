import pandas as pd

f1 = '/Users/xuweijun/Downloads/python3/user_study.json' #练手用的实验室的用户数据 json格式
id1 = 199373
user_id = 'user_id'

def count(file,id):
    times=0
    minutes=0
    df = pd.read_json(file,'r')
    user_data = df[df.user_id == id]
    times = len(user_data)
    minutes = user_data.minutes.sum()
    print("Students id: %d\nStudy times: %d\nTotal learning times: %d"%(id,times,minutes))
    return times, minutes

count(f1,id1)

df = pd.read_json(f1)
df_id = sorted(set(df.user_id))

df_id2 = [1,13,32,33]

for a in range(0,len(df_id2)):
    if df_id2[a] in df_id:
        print('ID: %d 是试验台学员。'%(df_id2[a]))
        a += 1
    else:
        print('%d 是假学员。'%(df_id2[a]))
        a += 1
print("查完了")

