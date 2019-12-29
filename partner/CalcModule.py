## @file CalcModule.py
#  @author Jack Buckley
#  @brief A module containing the core functions used for allocating a student to their program.
#  @date 18 January 2019

from statistics import mean
from random import shuffle
import Exceptions

## @brief Sorts a list of student dictionaries by GPA.  
#  @details The student dictionaries are sorted in descending order in terms of GPA. It is assumed that
#           the dictionary for each student will not be changed (won't cause aliasing issues).
#  @param S Takes in list of student dictionaries of the form generated by readStdnts(s)
#  @return A list of student dictionaries sorted by GPA.

# Credit on how to sort lists in Python using a key function:
# https://www.geeksforgeeks.org/python-list-sort/

def sort(S):
    # Make a copy of S (otherwise side effects will arise using list.sort())
    D = S.copy()
    # A lambda function which returns the value of a dictionary at the key 'gpa'
    sortByGPA = lambda diction : diction['gpa']

    # Sort the list of dictionary S by the GPA of each student in descending orders
    D.sort(key = sortByGPA, reverse = True)
    return D

## @brief Finds the average GPA of all males or females.
#  @param L Takes in list of student dictionaries of the form generated by readStdnts(s)
#  @param g Takes in string of gender to find the average of: "male" or "female"
#  @exception GenderNotGiven raised if g is not "male" or "female"
#  @return A float representing the average GPA of the specified gender

def average(L, g):
    # A list where male GPAs will go
    maleGPAs = []
    # A list where female GPAs will go
    femaleGPAs = []

    # Iterate through each student dictionary
    for studentDict in L:
        # Get the gender of the current student
        gender = studentDict['gender']

        # If the current student is male, add his GPA to the male GPA list
        if(gender == 'male'):
            maleGPAs += [studentDict['gpa']]

        # If the current student is female, add her GPA to the male GPA list
        elif(gender == 'female'):
            femaleGPAs += [studentDict['gpa']]

    # If the user wants to know the male GPA, find the mean of the male GPA list
    if(g == 'male'):
        return mean(maleGPAs)

    # If the user wants to know the female GPA, find the mean of the male GPA list
    elif(g == 'female'):
        return mean(femaleGPAs)
    else:
        raise Exceptions.GenderNotGiven('g is not "male" or "female"')

## @brief Allocates students to their programs.
#  @details Students who have free choice get first pick, followed by the remaining students according to their GPA
#           with those with higher GPAs getting higher priority. Those eligible will be also shuffled in a lottery 
#           according to their eligibility. That is to say all students with free choice will be shuffled among
#           themselves and all students with the same GPA will be shuffled among themselves as well. Any student,
#           regardless of if they have free choice, who has a GPA of less than 4.0 will not be allocated to a program.
#           While students are allocated in the aforementioned order, if a department no longer has capacity for additional
#           students, students will allocated to their second/third preferences. If it arises that all three of a student's
#           choices are at full capacity, the student will be assigned to a random department with room. 
#      
#  @param S Takes in list of student dictionaries of the form generated by readStdnts(s)
#  @param F Takes in list of students' MacID strings for those who have free choice in the form generated by readFreeChoice(s)
#  @param C Takes in dictionary of department capacities of the form generated by readDeptCapacity(s)
#  @return A dictionary where the department names are the keys and their respective values are lists of student dictonaries of
#          students who have been allocated to them.
#  @exception Exceptions.FreeChoiceStudentNotAccountedFor when a student in the free choice list cannot be allocated to a program
#               because their student dictionary is not in the dictionary list.
#  @exception Exceptions.NoDepartmentsHaveCapacity when no departments have capacity but there still exist students to be allocated
#               to programs.
#  @exception Exceptions.EmptyStudentDictionaryList when parameter S containing a list of student dictionaries is empty.
#  @exception Exceptions.EmptyDepartmentCapacityDict when parameter C containing a dictionary of department capacities is empty.

def allocate(S, F, C):
    # Do not want to mutate inputs, so copying them to prevent side effects
    SLocal = S.copy()
    FLocal = F.copy()
    CLocal = C.copy()


    # We should not allocate any students if the student dictionary list or department 
    # capacity dictionary are empty (It's OK if free choice is empty, however)
    if SLocal == []:
        raise Exceptions.EmptyStudentDictionaryList

    elif CLocal == {}:
        raise Exceptions.EmptyDepartmentCapacityDict

    
    # The allocation dictionary
    allocation = {'civil': [], 'chemical': [], 'electrical': [], 'mechanical': [], 'software': [], 'materials': [], 'engphys': []}


    # Get the student dictonaries for those with free choice from the list SLocal and remove them from SLocal
    freeChoiceDicts = []
    for freeChoiceStudent in FLocal:
        # Try to get the student's information from the list of dictionaries SLocal by matching against their MacID
        try:
            stdntInfo = list(filter(lambda diction : diction["macid"] == freeChoiceStudent, SLocal))[0]
        except:
            raise Exceptions.FreeChoiceStudentNotAccountedFor("A student on the free choice list is not" +
            "in the list of student dictionaries and thus cannot be allocated.")
        
        # Remove free choice student from the list of student dictionaries
        SLocal.remove(stdntInfo)

        # Place their dictionary in the list of dictionaries of those with free choice
        freeChoiceDicts += [stdntInfo]
    
    # Shuffle those with free choice
    shuffle(freeChoiceDicts)
    # Shuffle everyone else
    shuffle(SLocal)
 

    # Sort everyone else by GPA
    SLocal = sort(SLocal)
    # print(SLocal)
    # print("\n")

    # Combine the student dictonaries so first the students with free choice get first pick
    # Then, everyone else gets to pick starting with those with the highest GPA 
    SLocal = freeChoiceDicts + SLocal

    # Iterate through each student's dictonary in the list.
    # The list now has the students with the highest priority at the beginning of the list and
    # accounts for those with free choice
    for student in SLocal:
        gpa = student["gpa"]
        # If the student has less than a 4.0 GPA, they will not be allocated
        if (gpa < 4.0):
            continue

        # Extract the student's choices from their dictionary 
        choices = student["choices"]
        fstChoice = choices[0]
        sndChoice = choices[1]
        thrdChoice = choices[2]

        # If the first choice department has spots available, put the student in that program
        if(CLocal[fstChoice] != 0):
            allocation[fstChoice] += [student]

            # Decrease capacity by 1
            CLocal[fstChoice] -= 1

        # If not, check if there are spots in the student's second preference and place them there if there is
        elif(CLocal[sndChoice] != 0):
            allocation[sndChoice] += [student]

            # Decrease capacity by 1
            CLocal[sndChoice] -= 1

        # If not, check if there are spots in the student's third preference and place them there if there is
        elif(CLocal[thrdChoice] != 0):
            allocation[thrdChoice] += [student]

            # Decrease capacity by 1
            CLocal[thrdChoice] -= 1

        # Otherwise, put the student in a random department that still has capacity
        else:
            # Get all the departments
            depts = list(CLocal.keys())
            deptsWithRoom = []
        
            # Add to the departments with room list
            for dept in depts:
                if CLocal[dept] != 0:
                    deptsWithRoom += [dept]
            
            # If deptsWithRoom is still empty, there is not enough room for students
            if deptsWithRoom == []:
                raise Exceptions.NoDepartmentsHaveCapacity

            # Shuffle the departments with room
            shuffle(deptsWithRoom)

            # The student is assigned a random department with room
            assignedDept = deptsWithRoom[0]
            allocation[assignedDept] += [student]
            
            # Decrease capacity by 1
            CLocal[assignedDept] -= 1
    print(allocation)
    return allocation
