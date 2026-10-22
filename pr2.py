""". Write a Python program to create a list containing the names of five students

(list1)and a nested list containing the names and marks of at least five students(list2)."""

# list1=["Raj","Parth","Ketan","Nayan","Shrey"]
# print("List1 - student  Names : ")
# print(list1)
#
#
# # Nested list containing student names and marks
#
# list2=[["Karan",85],
#        ["Het",95],
#        ["Ankit",74],
#        ["Manish",83],
#        ["Rahul",63]
#        ]
#
# print("List 2 -Student names and marks : ")
# print(list2)
#

"""a) Accept a student name from the user and search for it in the student list. 
Display its index if found; otherwise, display an appropriate message."""
#
# list1=["Karan","Het","Raj","Rohit","Virat"]
# name=input("Enter a student name :")
#
# if name in list1:
#     print("Index : ",list1.index(name))
#
# else:
#     print("Student not found")



"""b.  Sort student names in ascending and descending alphabetical order using sort() and sorted()."""

name=["jay","zara","Ketan","Nayan","Virat"]

# Ascending order using sort()
#
# name.sort()
# print(name)
#
# # Descending order using sort()
#
# name.sort(reverse=True)
# print(name)


# # Ascending order using sorted()
#
# print("Ascending using sorted :",sorted(name))
# print("Descending using sorted :",sorted(name,reverse=True))

"""c. Add a new student name, insert a name at a specified position, and remove a student name."""
#
# list1=["Karan","Zara","Navin","Shrey"]
# list1.append("Raj")
# print(list1)
# list1.insert(1,"Amit")
# print(list1)
# list1.remove("Raj")
# print(list1)


"""d. Display all student records using a loop(list2)."""
#
# list1=["Karan","Rahul","Priya","Amit"]
#
# for i in list1:
#     print(i)

"""e.) Find the student who obtained the highest marks and calculate the average marks(list2)."""
#
# list=[("kran",94),("Raj",84),("Krish",74),("Manish",46),("Kavya",84)]
#
# highest_marks=max(list,key=lambda x:x[1])
# print("Student with highest marks:",highest_marks[0])
# print("highest marks:",highest_marks[1])
#
# total=sum(student[1] for  student in list)
# average=total/len(list)
#
# print("Average marks:",average)




"""f. Display the number of student records using len()(list2)."""
#
# list2=[("Karan",84),("navin",48),("ketan",84)]
# print(len(list2))


















"""f) Display the number of student records using len()(list2)."""
