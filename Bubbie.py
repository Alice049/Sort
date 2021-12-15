data=[4,1,3,5,2]
data_count=len(data)
for i in range(data_count-1):
    for j in range(data_count-1-i):
        if data[j]>data[j+1]:
            temp=data[j]
            data[j+1]=temp
    print("第",i,'回合結果:',data)
print("泡泡排序結束")
