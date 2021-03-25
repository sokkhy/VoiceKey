
# counter = 100          # An integer assignment
# miles   = 1000.0       # A floating point
# name    = "John"       # A string
# list    = ['1','2']    # A list

# String_to_List  = name.strip('][').split(', ') 
# List_to_String  = str(list)
# Int_to_String   = str(counter)
# Float_to_Int    = int(miles)

# print ("counter " , type(Int_to_String))         # number to string 
# print ("miles ",    type(Float_to_Int))           # float to int 
# print ("String_To_List ",  type(String_to_List)) # String to List
# print ("List_To_String ",  type(List_to_String)) # List to String










_getList = ["key",26,"IT"] #List 

print("employee age " , _getList[1]) # get list item by index 


my_tuple = ('a', 'b', 'c')  # literal notation to create a new tuple
my_list = list(my_tuple) 


print(type(my_list))


nuts = list(("pecan nut", "walnut", "cashew nut", "macadamia nut"))

forrests_favorites = list(nuts) # makes a new list with the same content


#print(forrests_favorites)



set_new_fruit = {"apple", "banana", "cherry"}
set_exsit_fruit = {"mango", "cherry"}
set_price = {1, 5, 7, 9, 3}


#set_new_fruit.update(set_price)

#set_fruit = set_new_fruit.difference(set_exsit_fruit)
#set_fruit = set_new_fruit.intersection(set_exsit_fruit)
set_fruit = set_new_fruit.symmetric_difference(set_exsit_fruit)
print("Update fruit ", set_fruit)