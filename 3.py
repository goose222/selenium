import json
import re
import flask
dic = {"results":[]}
with open("data.txt",encoding="utf-8") as fr:
    lines = fr.readlines()
    i=0
    n=len(lines)
    while i<n:
        if not lines[i][0].isdigit():
            i+=1
            continue
        tmp={}
        n=0
        while(lines[i][n].isdigit()):
            n=n+1
        tmp["名称"]=lines[i][n+2:-1]
        tmp["批准号"]=lines[i+1][4:-1]
        tmp["项目类别"]=lines[i+2][5:-1]
        tmp["项目负责人"]=lines[i+3][6:-1]
        tmp["批准年度"]=lines[i+4][5:-1]
        tmp["资助经费"]=lines[i+5][5:-1]
        tmp["依托单位"]=lines[i+6][5:-1]
        tmp["起止年月"]=lines[i+7][5:-1]
        tmp["申请代码"]=lines[i+8][5:-1]
        tmp["关键词"]=""
        tmp["研究成果"]=""
        tmp["结题项目"]=""
        i=i+9
        dic["results"].append(tmp)
#print(dic)
with open("data.json",'w',encoding='utf-8') as f:
    json.dump(dic,f,ensure_ascii=False,indent = 2)
