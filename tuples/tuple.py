x , y = "varun" , "varshini" # tuples can be assigned directly with tuples
print(x,y)

if (0,1,2) > (1,0,2000): # tuples are comparable and break when operator is sattisifies first time
    print("greater")
else:
    print("lesser")

#tuples can be used to sort dictionaries
d = {'a' : 22 , 'c' : 3 , 'b' : 2}
lst = d.items()
srt = sorted(lst) #sorting based on key
print(srt)

#reversing a dictionary to value-key
tmp = list()
for k,v in lst:
    tmp.append((v,k))
print(tmp)

#sorting a dict by value in reverse order
tmp = sorted(tmp , reverse=True)
print(tmp)