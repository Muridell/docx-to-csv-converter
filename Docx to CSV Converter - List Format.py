#Import Packages
import pandas as pd
import docx2txt

#Extract Text from Docx File.
text = docx2txt.process("file directory.docx")
text
#Split the content of the Docx file by new line
content = text.split('\n\n')


list_content = []
for item in content:
    #Split each Question/Answer/ Paragraph by "dot and space or whatever you delimiter is" and append it into the list
    sentence = item.split('. ')
    list_content.append(sentence)
list_content

#Create dataframe from list
df = pd.DataFrame(list_content)

#Convert and Export dataframe to csv file
df.to_csv("filename_of_your_choice.csv")

#Display dataframe content
df