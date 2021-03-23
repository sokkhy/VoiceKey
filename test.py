x = (1 + 2 + 3 + 4 + 
    5 + 6 + 7 + 8) # continue statement to the next line using parentheses ()
x1 = 1 + 2 + 3 + 4 +\
5 + 6 + 7 + 8 # continue statement to the next line using "\" marker



# set the midpoint

mid_point = 5 #End-of-Line Terminates a Statement


# make two empty lists
lower = []; upper = [] # two statement in one line using ;

# split the numbers into lower and upper
for i in range(10): 
    if (i < mid_point):   
        # indentation indicates code block
        # indented code blocks are always preceded by a colon (:) on the previous line.
        lower.append(i)
    else:
        upper.append(i)

print("lower:", lower)
print("upper:", upper)


z = 10
if z < 4:         
    y = x * 2    
print(z)   # show  10 regardless of z value

if z < 5:         
    y = z * 2    
    print(z)      # no result;  execute only when z < 5 



x = 1+2
x = 1 + 2
x             =        1    +                2  #Whitespace Within Lines Does Not Matter

a = 10 ** -2
print(a)



#Parentheses Are for Grouping or Calling
2 * (3 + 4)

print('first value:', 1) #print () function is called



