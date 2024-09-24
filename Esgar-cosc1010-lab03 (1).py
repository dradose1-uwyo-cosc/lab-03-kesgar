# Kaylee Esgar
# UWYO COSC 1010
# 9-24-24
# Lab 03 
# Lab Section: 10
# Sources, people worked with, help given to: Ashley Criger, TA (Austin Barner)




# This is your second lab section. It will primarily be based on the Introducing Lists lecture, reference it if you need
# Complete all sections of this assignment 


print("Part One------------------------------------------------------------------------")
#We are going to start with the basics. Declare a list  states that contains the elements: Wyoming, Colorado, Montana in that order 
#Note this is the ONLY point where you need to declare the states list
states = ['Wyoming', 'Colorado', 'Montana'] #simple list named states to hold terms given in the problem.


#print the entire list
print(states) #prints entire list with no changes

#now print the first element in the list
print(states[0]) #printing first term, indexed (0)

#Print the last element using the syntax shown in class to access the final element (hint, think negatives)
print(states[-1]) #printing the last term of the list using the -1 shortcut

#Using an F-string to access the first and second element print the string "COLORADO is south of WYOMING", matching the casing provided
print(f"{states[1].upper()} is south of {states[0].upper()}") #using .upper to capitalize list elements and a f string to print a statement



print("Part Two------------------------------------------------------------------------")
#Append the following states to your list: Washington, Oregon, California and print your list
states.append("Washington") #appending a state to the end of the list
states.append("Oregon") #appending another state to the end of the list
states.append("California") #appending another state to the end of the list
print(states) #prints list with new states appended.

#Again using the specific syntax mentioned in class overwrite the second to last element to be Maine, printing the list 
states[-2] = "Maine" #adding Maine to the list in a specific index area.
print(states) #printing new list with Maine in the second to last spot on the list.

#Insert the state Texas to be the third element in the list, again printing your list
states.insert(2,"Texas") #using the insert feature to insert Texas as the third element.
print(states) #printing list with updated Texas replacement. 

#Using the `del` statement remove the fourth item from the list, print your list 

del states[3] #using del to remove the 4th element in the list.
print(states) #prints list with 4th element removed. 
#Remove Texas using its value, print the list
states.remove("Texas") #using a specific value (Texas) to remove it.
print(states) #new states list printed with Texas removed.

print("Part Three----------------------------------------------------------------------")
#Temporarily sort your list, print it both sorted and unsorted 
print(states) #prints current states list
print(sorted(states)) #temporarly sorts the states list alphabetically

#Permanently sort your list in reverse order, printing it out
states.sort(reverse=True) #permanetley sorts the states list in reverse alphabetical order.
print(states) #prints list in reverse order, will keep list in this order since it was permanetely sorted.

#Using the reverse method reverse the list and print it
states.reverse() #reverses the list using a different method than before.
print(states) #prints new states list.


