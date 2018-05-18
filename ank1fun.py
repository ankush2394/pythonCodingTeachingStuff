from operator import itemgetter

def func(x):

    if x<7:
        return x
    else: return 9

y=func(90)
print(y)

#name = input("whts ur name: ")#raw input renameed to input http://docs.python.org/dev/py3k/whatsnew/3.0.html
#age = input("how old r u: ")
#hobbies = input("tell me some of your hobbies: ")

#print(type(name), type(age), type(hobbies))

#list = hobbies.split(',')
#print (list)

pairs = [(1, 'one'), (2, 'two'), (3, 'three'), (4, 'four')]
pairs.sort(key= itemgetter(1))
print(pairs)


dict={}
print(len(dict))


#import operator
x = {1: 2, 3: 4, 4: 3, 2: 1, 0: 0}
sorted_x = sorted(x.items(), key=itemgetter(1))
print(sorted_x) #u cant sort a dictionary it will be sorted oly to give us a list of tuples

for x in sorted_x:
    print(x[0],x[1])

