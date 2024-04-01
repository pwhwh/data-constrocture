from queue_1 import Listqueue 



def check(input_str):
    queue=Listqueue()
    for char in input_str:
        queue.enqueue(char)
    
    str1=""
    while queue.front() != '$':
        str1+=queue.dequeue()
    queue.dequeue()
    
    str2=""
    while not queue.isEmpty():
        str2+=queue.dequeue()
        
    return str1 == str2
    
input_str=input("입력을 받으세요")
result=check(input_str)
print(result)
        
        
        
    
        
        
        
        
        



            
    
        
    

