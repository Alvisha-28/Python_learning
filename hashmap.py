m1 = {'name': "Alvisha","sem":6,"branch":"EEE"}
print(m1)
print(m1['name'])
m1['name'] = "Alvisha S"
print(m1)
m1 = {'name': "Alvisha","sem":6,"branch":"EEE","subjects":['DS','OS','DBMS'], 101:"hardware engineering"
      }
print(m1)
'''time
 insert:0(1)
 search:0(1)
 delete:0(1)    '''
for key, value in m1.items():
    print(key, ":", value)
print(m1.keys())
# print(m1.values())
# pop = m1.pop(101)
# print(pop)
# print(m1)
# m1.pop("subjects")
# print(m1)
# topper ={"alvisha": 9.5, "sneha": 9.6, "priya": 9.4}
# print(topper)
# print(topper["alvisha"])
# topper[1]="keerthana"
# print(topper)
a ={}
a.add(1)
print(a)
if 1 in a:
    print("present")
    