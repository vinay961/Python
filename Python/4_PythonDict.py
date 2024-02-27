dic = {
    'Name':"Vinay",
    'dept':"B.tech",
    'rollNo':123
}
print(dic['dept'])
# we can also traverse the dictionary using get method
print(dic.get('rollNo'))
# Note diffenence between these two format is that in above way we write name of key wrong then it gives us error but in case of get we doesn't get any error.

for info in dic:
    print(info,dic[info])
    
# another method used for above work is,
for key,value in dic.items():
    print(key,value)
# Here we took item from dic, and than use there key and value as key and value.

print(len(dic))
dic['hobbies'] = 'fitness'
# dic.pop('rollNo')
x = dic.popitem()
print(x)



