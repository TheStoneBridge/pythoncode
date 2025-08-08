#TODO把式
#for loop  and while loop
z = [1,2,3,4,5,6]
for i in z:
    print(i)
for i in range(20):
    print(i)
    

while True:
    print("hello")
    

count = 3
while count:
    count -=1
    
s =[(1,2),(3,4),(5,6)]
for i in s:
    print(i)
    
for i,j in s:
    print(i,j)

for i in s:
    for j in i :
        print(j)
        
n = [1,2,3,4]
m = [5,6,7,8]
for i,j in zip(n,m):
    print(i,j)
    
#TODO 细则
p = [1,2,3,4,5]
for i in p :
    a=1

print(a)
print(i)


p = [1,2,3,4,5]  #循环删除
for i in p:
    print(i)
    p.remove(i)
    print(p)

p = [1,2,3,4,5]  #循环增加
for i in p:
    print(i)
    p.append(i)
    print(p)

#TODO控制
#break continue ---------------------pass
#pass  表示什么都不做
#continue 表示这次不算，继续后面的循环
#break  代表不要循环了，停止
for i in range(20):
    if i == 4:
        break
    print(i)


for i in range(20):
    if i == 4:
        continue   #符合条件的这次不算在内，继续下一次循环
    print(i) 
    
