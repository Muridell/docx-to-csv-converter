#Import Packages
import pandas as pd
import docx2txt
import json, collections
from pandas.io.json import json_normalize

#Extract Text from Docx File.
text = docx2txt.process("file directory")

#Create a Dictionary for wach line
dic = {x for x in text.split('\n')}

#Remove the Empty Spaces in dictionary
dic.remove('') if '' in dic else dic

#Create JSON format from Dictionary
json_dic = {}
for x in dic:
    #split each question by space (depends on the content of the file) and tranform it into a json format
    y = x.split(' ')
    for m in y:
        json_dic.update({y[0]:y[1]})
        
data = json.loads(json.dumps(json_dic, indent=4))
temp = pd.DataFrame.from_dict(json_normalize(data),orient='columns')

#Transpose temp Dataframe and sort by index
trans_temp = temp.transpose().sort_index()

#Convert and export Dataframe to csv file
trans_temp.to_csv("filename.csv")

#Display Transposed Dataframe
trans_temp