import os

newDir = 'char'
fileName='newCharList.txt'
c = os.getcwd()

count = 0
count1 = 0
c = os.getcwd()

for i in range(6):
    foldName = "{}{:02d}-{:02d}".format(newDir,count+1, count+5)
    if os.path.exists(foldName):
        pass
        #print("{} fold is existed!".format(foldName))
    else:
        os.mkdir(foldName)
    count+=5
    zero = 0
    for i in range(5):
        zero += 1   
        file = open(f"{c}\\{foldName}\\{newDir}_{count1+zero :02d}.txt" ,'w')
        file.close()
    count1+=5
    

with open(fileName,'r',encoding='utf-8') as file_obj:
    j=file_obj.readlines()

count = 0
name = list(input(''))
namelist = []

while count<3315:   
    b = j[count]
    a = list(b)
    
    if a[5] == ',':
        if a[4] <='5':
            f = open(f"{c}\\{newDir}01-05\\{newDir}_{int(a[4]) :02d}.txt" ,'a',encoding='UTf-8')
            f.write(b)
       
          
        else:
            f = open(f"{c}\\{newDir}06-10\\{newDir}_0{a[4]}.txt" ,'a',encoding='UTf-8')
            f.write(b)
    
                 
    else:
        if  a[4]+a[5] == '10':
            f = open(f"{c}\\{newDir}06-10\\{newDir}_{10 :02d}.txt" ,'a',encoding='UTf-8')
            f.write(b)
           

        elif  '10'< a[4]+a[5]<='15':          
            f = open(f"{c}\\{newDir}11-15\\{newDir}_{a[4]+a[5]}.txt" ,'a',encoding='UTf-8')    
            f.write(b)
                    

        elif '15'<a[4]+a[5]<='20':
            f = open(f"{c}\\{newDir}16-20\\{newDir}_{a[4]+a[5] }.txt" ,'a',encoding='UTf-8')    
            f.write(b)
          

        elif '20'<a[4]+a[5]<='25':
            f = open(f"{c}\\{newDir}21-25\\{newDir}_{a[4]+a[5]}.txt" ,'a',encoding='UTf-8')    
            f.write(b)
           
           
        else:
            f = open(f"{c}\\{newDir}26-30\\{newDir}_{a[4]+a[5] }.txt" ,'a',encoding='UTf-8')    
            f.write(b)
            

    if a[1] in name:
        if a[5] == ',':
            namelist.append(f"{a[1]}的筆劃為:{a[4]}")
            #print(f"{a[1]}的筆劃為:{a[4]}")
        else:
            namelist.append(f"{a[1]}的筆劃為:{a[4]+a[5]}")
            #print(f"{a[1]}的筆劃為:{a[4]+a[5]}")
            
    count+=1

set_namelist = list(set(namelist))
print(set_namelist)
for i in set_namelist:
    print(i)

#f len(name) != len(namelist):
    #namelist.pop()

#for i in namelist:
    #print(i)i

