import os

files=[]
ans=[]
final=[]

dir = '/home/sun/batch/'   # give folder path in which files are residing
search="docker"            # give word for search in files
extension=".txt"           # give extension of files in which search has to be happen


for i in os.listdir(dir):
    if i.endswith(extension):
        with open (dir + i,'r') as f:
            for line in f:
                for word in line.split():
                    for j in range(len(search.lower().split(" "))):
                        if word==search.lower().split(" ")[j]:
                            ans.append(i)

for num in ans :
    if num not in final:
        final.append(num)

print(final)

