# Python program to find sum of all

list1 = [17,23,20,12,5,11,8]                            # creating a list
 

def sumOfList(list, size):                              # creating sum_list function
   if (size == 0):
     return 0
   else:
     return list[size - 1] + sumOfList(list, size - 1)
  
    
total = sumOfList(list1, len(list1))        
 
print("Sum of all elements in given list: ", total)