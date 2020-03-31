import re
import os 
from tqdm import tqdm

files=os.listdir("./")

for i in tqdm(files):
    if i.endswith('.txt'):
        with open(i, 'r',encoding="utf8") as f:
            data_file=f.readlines()
        
        for num,lines in enumerate(data_file,1):
            if "standard performance" in lines:
                j=re.findall(r"\d{1,2} years",lines)
                print('File Name: '+str(i)+'  Line No: '+str(num)+'  Matched String: '+str(j))
            else:
                continue
