''' 1.List Operations '''
# create a list of ten integers using range()

#
# list1=list(range(1,11))
# print("Original list:",list1)


'''a. Display the list and access its elements using positive indexing,negative indexing,and slicing.'''

# list2=[10,20,30,40,50]
#
# print("Positive Indexing :",list2[1])  # Positive indexing
# print("Negative Indexing :",list2[-1]) # Negative indexing
# print("Slicing :",list2[1:4])  # Slicing

'''b. Update an elements at a specified index entered by user.'''

# num=list(range(1,11))
# index=int(input("Enter a index to update : "))
# value=int(input("Enter a new value : "))
#
# num[index]=value
# print(num)

'''c. Perform List concatenation using + and repitition using *. '''
#
# List1=[1,2,3]
# List2=[4,5,6]
#
# # List Concatenation using +
# print("Concatenation:",List1+List2)
#
# # List repetation using *
# print("Repetition :",List1 * 3)


'''d.Check whether a number exists in the list using in and n and not in. '''

# a=[1,2,3,4,5]
#
# n=3
# print(n in a)
# print(n not in a)

'''e. Perform the following list methods: append(), insert(), remove(), pop(), reverse(), and count()'''

# a=[10,20,30,40,50,20,20]
#
# a.append(70)
# print(a)
# a.insert(2,40)
# print(a)
# a.remove(30)
# print(a)
# a.pop()
# print(a)
# a.reverse()
# print(a)
# print(a.count(20))
# a.sort()
# print("Sorted list:",a)

'''f. Display the list in ascending and descending order using sort() and sorted().'''

# list=[10,30,20,40,50]
# list.sort()
# print("Ascending oreder using sort():",list)
# list.sort(reverse=True)
# print("Descending order using sort():",list)

# # Using sorted() in ascending order
# a=[10,20,40,50,30]
# print("Ascending order using sorted():", sorted(a))
# print("Descending order using sorted():",sorted(a,reverse=True))

'''g. Create an alias and a clone of the list, modify one element, 
and demonstrate the difference between aliasing and cloning.'''

# a=[10,20,30,40]
#
# alias =a
# clone =a.copy()

# a[0]=80
#
# print("Original List: ",a)
# print("Alias List :",alias)
# print("Clone List :",clone)

'''h. Display the maximum, minimum, and length of the list using max(), min(), and len().'''

# lst_2=[10,20,30,40,50]
# print("Maximum :",max(lst_2))
# print("Minimum :",min(lst_2))
# print("Length :",len(lst_2))
