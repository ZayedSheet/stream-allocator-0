## @file CalcModule.py
#  @author Zayed Sheet
#  @brief This file contains functions that manipulates data provided by the ReadAllocationData file.
#  @date 2019-01-18
from ReadAllocationData import *

## @brief Sorts a list of dictionaries by their 'gpa' in descending order.
#  @details This function sorts a list of dictionaries by the value of their 'gpa' key. \nSome of this code is referenced from
#           \n'https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary'
#  @param S The single parameter this function takes is a list of dictionaries, each containing a 'gpa' key.
#  @return The returned value is a new list of dictionaries, sorted in descending order by the value of thier 'gpa' keys.
def sort(S):
  newlist = sorted(S, key=lambda g: g['gpa'], reverse=True) #https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary
  return newlist
 
## @brief Calculates the average GPA of a specified gender.
#  @details The function adds together the floating point values for all dictionaries that have the specified 'gender' value that 
#           was passed into the function. While doing this it also counts how many dictionaries
#           from the list have that gender value. It then divides the total gpa by the counter to find the average.
#  @param L This parameter is a list of dictionaries that have a 'gpa' and 'gender' key.
#  @param g This parameter is a string for the gender you want to find the average for.
#  @return The returned value is a value rounded to two decimal places for the average GPA of a specified gender.
def average(L,g):
  total = 0
  count = 0 #total number of students
  for i in L: #for every dictionary in list
   if (i['gender'] == g): #if the gender of the person is equal to given gender
      count = count + 1 
      total = total + i['gpa']
  if total <= 0:
    print("Error with function input! Please check that gender is either male/female and or input is not empty.")
    return -1
  return(round(total/count, 2)) #return the gpa average

## @breif Allocates students into an engineering stream.
#  @details The function sorts a list of students by their GPA in descending order. It then adds everyone with a GPA below 4.0 
#           into a text file and allocates everyone with free choice into their first choice. The program then allocates everyone 
#           else from highest to lowest gpa into their first, second or third choice in that order depending on which one has 
#           available capacity first. Anyone that isn't allocated into a program (because all three capacities are full) gets 
#           placed into a text file.
#  @param S This parameter is a list of dictionaries where each dictionary represents a student with several attributes (such as)
#           name, macid, program choices, etc.)
#  @param F This parameter is a list of students that have free choice. Each student is represented by their macid.
#  @param C This parameter is a dictionary with engineering departments as keys and their respective capacity as the key's value. 
#  @return This function returns a dictionary that contains the engineering streams as keys and a list of dictionaries as values.
#          Each dictionary represents a student that is allocated into that engineering stream.
def allocate(S, F, C):
  S = sort(S)
  dictionary = {'civil':[], 'chemical':[], 'electrical':[], 'mechanical':[], 'software':[], 'materials':[], 'engphys':[]}
  failFile = open("FailList.txt", 'w') #file for everyone that failed

  i = 0
  while(i != len(S)):
    if S[i]['gpa'] < 4.0: #if students gpa is below 4
      print("student has failed: ", S[i]['macid'])
      failFile.write( #writes their student information into a text file
        "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}\r\n".format(S[i]['macid'],S[i]['fname'],S[i]['lname'],S[i]['gender'],S[i]['gpa'],S[i]['choices'][0],S[i]['choices'][1],S[i]['choices'][2])
      )
      del S[i] #removes that student from the list
    elif S[i]['macid'] in F: #if the student has free choice
      print("student has free choice: ", S[i]['macid'])
      dictionary[S[i]['choices'][0]].append(S[i]) #places the user into their first choice program
      C[S[i]['choices'][0]] = C[S[i]['choices'][0]] - 1 #reduces the capacity of the first choice program by one 
      del S[i] #removes that student from the list
    else:
      i = i + 1
  failFile.close()

  unallocatedFile = open("Unallocated.txt", 'w')
  for i in range(len(S)): #loop will run for every remaining student in the list
    firstchoice = S[0]['choices'][0] #selected users first choice
    secondchoice = S[0]['choices'][1]
    thirdchoice = S[0]['choices'][2]

    if C[firstchoice] > 0: #if their first choice still has capacity (more than 0)
      dictionary[firstchoice].append(S[0]) #puts the user into their first choice program
      C[firstchoice] = C[firstchoice] - 1 #reduce the capacity by 1
      del S[0] #removes the user from the list
    elif C[secondchoice] > 0:
      dictionary[secondchoice].append(S[0])
      C[secondchoice] = C[secondchoice] - 1
      del S[0]
    elif C[thirdchoice] > 0:
      dictionary[thirdchoice].append(S[0])
      C[thirdchoice] = C[thirdchoice] - 1
      del S[0]
    else: #if the user hasnt been placed into any program because their first 3 choices were full
      print(S[0]['macid']," not allocated")
      unallocatedFile.write( #adds them into the unallocated students text file
        "{0}, {1}, {2}, {3}, {4}, {5}, {6}, {7}\r\n".format(S[0]['macid'],S[0]['fname'],S[0]['lname'],S[0]['gender'],S[0]['gpa'],S[0]['choices'][0],S[0]['choices'][1],S[0]['choices'][2])
      )
      del S[0] 
  unallocatedFile.close() 
  print(len(S), " students left in the list")
  return dictionary
    

# test = (readStdnts("test.txt"))
# print(sort(test))
# print(average(readStdnts("test.txt"),'male'))
# print(allocate(readStdnts("test.txt"),readFreeChoice("free.txt"),readDeptCapacity("dept.txt")))
