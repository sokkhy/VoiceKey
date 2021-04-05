


# # no duplicate is allowed
# animal = {"dog","cat","horse","horse"}
# print ("no duplicate ", animal)

# # item cannot update 
# # but set can update
# animal.add("rat") # add a item to set
# animal.update (animal ,["rat","chicken"])  # add multi items to set
# print ("animal add rat : ", animal)

# animal.discard("dog") # remove a item from set
# print ("animal remove dog : ", animal)

# new_animal = {"tiger","duck","dragon","chicken"}
# # Intersection of new_animal and animal is a set of elements that are common in both the sets.
# print ("intersection of new_animal and animal is ", new_animal.intersection(animal)) 

# #Union of new_animal and animal is a set of all elements from both sets.
# print ("union of new_animal and animal are ", new_animal.union(animal)) 


# # tuple of vowels
# vowels = ('a', 'e', 'i', 'o', 'u')

# fSet = frozenset(vowels)
# print('The frozen set is:', fSet)
# print('The empty frozen set is:', frozenset())

# # frozensets are immutable
# fSet.add('v')



# random dictionary
person = {"name": "John", "age": 23, "sex": "male"}

fSet = frozenset(person)
print('The frozen set is:', fSet)