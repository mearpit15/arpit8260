# count the number of occurence of words in Inputfile.txt
def word_count(str):
words=str.lower().split()
d=dict()
for word in words:
if word in d:
d[word]=d[word]+1
else:
d[word]=1
return d
with open('Inputfile.txt','r') as f:
contents=f.read()
output=word_count(contents)
with open('Outputfile.txt','w') as w:
for key in list(sorted(output.keys())):
w.write(str(key+':'+str(output[key])))
w.write('\n')
