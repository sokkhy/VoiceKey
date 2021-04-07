from math import sqrt

def findName(age,fname, lName="elon"):
    fullName = fname + lName + age
    
    return fullName


print("positional arguments :  " ,findName("18", "musk"))   #positional arguments

print("keyword arguments : ",findName(age = "18",fname="musk"))#keyword arguments