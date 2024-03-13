a=[]

for i in range(1,11):
    x=int(input("데이터를 입력하시오"))
    a.append(x)
    
def find_max_recursive(list):
    if len(list) ==0:
        return None
    elif len(list) ==1:
        return list[0]
    else:
        return max(list[0], find_max_recursive(list[1:]))
def find_max_iterative(list):
    if not list:
        return None
    
    max=list[0]
    for num in list[1:]:
        if num>max:
            max=num
    
    return max

recursive=find_max_recursive(a)
iterative=find_max_iterative(a)
print(recursive)
print(iterative)
    


    