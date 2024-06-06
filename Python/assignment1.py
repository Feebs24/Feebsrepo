#Assignment - 2024-06-03
#1
greeting = "Welcome to python"
#print(greeting.index("python"))
print(greeting[11:])

#2
data = "1:A, 2:B, 3:C, 4:D, 5:E, 6:F, 7:G, 8:H"
#print(data.index("B"))
print(data[0::5])

#3
sample = 'My Name is Wale'
name = sample.split(" ")[-1]
#print(name)
print(name[::-1])


#4
#I have 1000 dollars so I can buy 3 football for 450 dollars.
totalMoney = str(1000)
quantity = str(3)
price = str(450)
concat = "I have " + totalMoney + " dollars so I can buy " + quantity + " football for " + price + " dollars." 
print(concat)

#5 mention 4 rules for naming a variable
# 1. Variables bust not contain reserved words
# 2. Variables names should not be ambigous, they should be descriptive and  easy to understand.
# 3 Variables should not start with an integer
# 4. Variable names are casesensitive and hence should have uniform casing with snake case the recommended case.    
# 5. Variable names cannot contain spaces

#6
#My name is wale. I am 18 years old.
name = "Wale"
age = str(18)
sentence = "My name is " + name+ "." + " I am " + age + " years old."
print(sentence)

#7
student_score = [1,2,3,[4,5,[6,7]]]
del student_score[3][2][1]
student_score[3][2].append(8)
print(student_score)

#8
record ={'k1':[{'nest_key':['this is deep',['tech365']]}]}
# print(record["k1"][0])
# record2 = record["k1"]
# print(record2)
# print(record2['nest_key'])
# # print(record2[])
print(record['k1'][0]['nest_key'][1])

#9
record2 = {'k1':[1,2,{'k2':['this is tricky',{'tough':[1,2,['python']]}]}]}
print(record2['k1'][2]['k2'][1]['tough'][2])

#10
message = ["Welcome", "to", "training"]
message.pop(2)
message.append("python")
message.append("training")
print(message)







