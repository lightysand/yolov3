train_path="YOLO-V3-IOU/dataset/imageset/train.txt"


with open(train_path,) as f:
    train = f.readlines()
    new_train=[]
    file=""
    cache=[]
    for i in range(0,len(train)):
        s=train[i].split("jpg,")
        s[0]="dataset/images/"+s[0]+"jpg "
        s[1]=s[1][0:len(s[1])-1]
        s[1]=s[1]+",0"
        #print(s)
        if len(cache)>0:
            if cache[0]==s[0]:
                cache[1]=cache[1]+" "+s[1]
            else:
                cache[1]=cache[1]+"\n"
                new_train.append(cache[0]+cache[1])

                cache=s
        else:
            cache=s

    new_train.append(cache[0]+cache[1]+"\n")
    str=""
    for i in new_train:
        str=str+i
    print(new_train)

with open("YOLO-V3-IOU/infos/train.txt","w") as a:
    a.write(str)
    a.flush()
    a.close()
    #f.write(train)
#print(train)



