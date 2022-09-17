#Assignment - 17 Full Stack Web Development using Python MySirG Set
#1. Write a python program to store all the programming languages known to you using Set.
set1={"c","Html","Python"}
print("This are the language which I known ",set1)
#2. Write a python program to store your own information {name, age, gender, so on..}
set2={"Soumik","17","Male"}
print("My name,age,gender:=",set2)
#3. Write a python script to get the data type of a Set
set3={3,2,1,2,3,1}
print(set3,type(set3))
#4. Write a Python script to find if “Python” is present in the set thisset = {"Java","Python", "Django"}
thisset = {"Java","Python", "Django"}
if "Python" in thisset:
    print("Yes")
else:
    print("No")    
#5. Write a python program to add items from another set to the current set. thisset ={"Java", "Python", "SQL"} secondset= {"C", "Cpp", "NoSQL"}
thisset = {"Java","Python", "Django"}
secondset= {"C", "Cpp", "NoSQL"}
print(thisset|secondset)
#6. Write a python program to add elements of list to a set thisset = {"Python", "Django", "JavaScript"} mylist = ["Java", "C"]
thisset = {"Python", "Django", "JavaScript"}
mylist = ["Java", "C"]
print(thisset|set(mylist))
#7. Write a python program to remove last item of the given set thisset = {"Python", "Django", "JavaScript", “SQL”}
thisset1 = {"Python", "Django", "JavaScript", "SQL"}
thisset1.discard("SQL")
print(thisset1)
#8. Write a python program to delete the set completely.
thisset1 = {"Python", "Django", "JavaScript", "SQL"}
thisset1.clear()
print(thisset1)
#9. Write a python program to loop through the set and print values
thisset = {"Python", "Django", "JavaScript", "SQL"}
for e in thisset:
    print(e,end=' ')
#10. Write a python program to find the maximum and minimum value in a set.
s1={1,2,3,4,5,66}
print("\nmin=",min(s1),"max=",max(s1))