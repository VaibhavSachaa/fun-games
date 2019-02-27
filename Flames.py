import string

p1 = input("Enter first person name:")
p1 = p1.lower()
p1=  p1.replace(" ","")

p2 = input("Enter Second person name:")
p2 = p2.lower()
p2 =  p2.replace(" ","")

l1 = list(p1)
l2 = list(p2)

proceed = True
while proceed:
   for i in l1:
        if i in l2:
            c=i
            l1.remove(c)
            l2.remove(c)
            proceed=True
            break
        else:
            proceed=False
    
count = len(l1) + len(l2)
result = ['Friends','Love','Affection','Marriage','Enemy','Sibling']

while len(result) > 1 :
    split_index = (count%len(result)) -1
    if split_index >= 0 :
        right = result[split_index + 1 :]
        left = result[:split_index]
        result = right + left
    else :
        result = result[:len(result) -1]
print(result[0])