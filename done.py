import os
from xml.etree.ElementTree import TreeBuilder
newDir = 'char'
j= 0
for i in range(1, 20, 5):
    j += 5
    foldName = "{}{:02d} - {:02d}".format(newDir, i, j)
    if os.path.exists(foldName):
        print("{} fold is existed!".format(foldName))
    else:
        os.mkdir(foldName)
        print("folder {} has been created!!".format(foldName))
    print('Done!')
foldName2 = "char_20up"
if os.path.exists(foldName2):
    print("{} fold is existed!".format(foldName2))
else:
    os.mkdir(foldName2)
    print("folder {} has been created!!".format(foldName2))
print('Done!')




    
name = list(input(''))
print(name)
for i in range(len(name)):
    print(name[i])

# opening the file in read mode
my_file = open("newCharList.txt", "r")
  
# reading the file
data = my_file.read()
  

# replacing end of line('/n') with ' ' and
# splitting the text it further when '.' is seen.
data_into_list = data.replace(',\n' , ' ').split(':')
  
# printing the data
print(data_into_list)
my_file.close()
done_list = []
n=-1
for i in range(len(name)):
    n+= 1
    while True:
        i+=1
        if name[n] in data_into_list[i]:
            print("ok")
            print(data_into_list[i])
            done_list.append(data_into_list[i].split())
            break
        else:
            pass
print(data_into_list[6].split()[0])
g=-1
address = os.getcwd()
for i in range():
    with open("{}//char{}-{}//{}{:02d}.txt".format(address, newDir, i), "w") as file:
    
for i in range(1, 30):
    with open("{}//char{}-{}//{}{:02d}.txt".format(address, newDir, i), "w") as file:
        
        while True:
            g+=1
            if str(i) in data_into_list[g].split()[0]:

                file.write("{}".format(data_into_list[g].split()[1]))
                
            

            elif g ==3317:
                break
            else:
                pass

                
                
            
                


print(done_list)