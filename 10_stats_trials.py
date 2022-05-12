

# find the lowest number

#declaring a list
list0 = [4, 10, 5, 4, 1, 6]
print ("list = ", list0)
 
#finding smallest number
s_num = min(list0)
s_num_max = max(list0)
average = sum(list0) / len(list0)
print ("The smallest number of gueeses in any given round was: ", s_num)
print ("The largest number of gueeses in any given round was: ", s_num_max)
print("Average: {}".format(average))






# find the highest


# Python program to find largest
# number in a list
  

  
  
# Driver code
list1 = [10, 20, 4, 45, 99]
print("Largest amount of guesses made per round :", myMax(list1))


average = sum(list1) / len(list1)
print("Length of list", len(list1))
print("Average: {}".format(average))

def myMax(list1):
  
    # Assume first number in list is largest
    # initially and assign it to variable "max"
    max = list1[0]
   
    # Now traverse through the list and compare 
    # each number with "max" value. Whichever is 
    # largest assign that value to "max'.
    for x in list1:
        if x > max :
             max = x
      
    # after complete traversing the list 
    # return the "max" value
    return max

guess_stats = [2, 10, 8, 3, 1, 5]