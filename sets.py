numbers = {5,13,7,3,5,86,47,35,64,7,3}
print(numbers)
#Numbers cant repeat
# numbers dont have a fixed postion

#print(numbers[2])
#Don't have index postitions

numbers.add(42)
print(numbers)
#to add a value

numbers.remove(86)
print(numbers)
#to remove a value 

set_1 = {1,4,3,5,7}
set_2 = {1,4,8,9,6}

print(set_1.union(set_2))
# joins both sets tougether

print(set_1.intersection(set_2))
#gives the common values from each set

print(set_1.difference(set_2))
#remove all the elements of set2 from set 1

print(set_2.difference(set_1))
#remove all the elements of set1 from set 2

print(set_2.symmetric_difference(set_1))