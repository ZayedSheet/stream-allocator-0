## @file testCalc.py
#  @author Zayed Sheet
#  @brief This file tests the functions in the CalcModule.py file.
#  @date 2019-01-18
from CalcModule import *

emptyList = [] #this represents an empty list (empty student list, empty free choice list etc)
emptyDictionary = {}
noFreeChoice = []
unlimitedCapacity = {'engphys': 999, 'civil': 999, 'chemical': 999, 'materials': 999, 'electrical': 999, 'mechanical': 999, 'software': 999}
controlledFreeChoice = ['sheetz', 'dominikb']
randomList = [
  {'gender': 'male', 'gpa': 10.5, 'choices': ['engphys', 'electrical', 'materials'], 'lname': 'sheet', 'fname': 'zayed', 'macid': 'sheetz'}, 
  {'gender': 'male', 'gpa': 10.8, 'choices': ['software', 'electrical', 'civil'], 'lname': 'yazdinia', 'fname': 'pedram', 'macid': 'yazdinip'}, 
  {'gender': 'male', 'gpa': 11.5, 'choices': ['software', 'chemical', 'electrical'], 'lname': 'buszowiecki', 'fname': 'dominik', 'macid': 'dominikb'}, 
  {'gender': 'male', 'gpa': 3.2, 'choices': ['mechanical', 'electrical', 'software'], 'lname': 'valkir', 'fname': 'farzad', 'macid': 'valkirf'}, 
  {'gender': 'female', 'gpa': 6.0, 'choices': ['mechanical', 'electrical', 'materials'], 'lname': 'gonzal', 'fname': 'cat', 'macid': 'gonzalc'}, 
  {'gender': 'male', 'gpa': 10.9, 'choices': ['software', 'civil', 'materials'], 'lname': 'hula', 'fname': 'mustafa', 'macid': 'mustafah'}, 
  {'gender': 'male', 'gpa': 10.5, 'choices': ['civil', 'electrical', 'software'], 'lname': 'samson', 'fname': 'jordan', 'macid': 'jordans'}
]

def sortList():
  #tests the sortlist function's correctness
  #also tests if it still works when two students have the same GPA
  expectedOutput = [
    {'gender': 'male', 'gpa': 11.5, 'macid': 'dominikb', 'lname': 'buszowiecki', 'fname': 'dominik', 'choices': ['software', 'chemical', 'electrical']}, 
    {'gender': 'male', 'gpa': 10.9, 'macid': 'mustafah', 'lname': 'hula', 'fname': 'mustafa', 'choices': ['software', 'civil', 'materials']}, 
    {'gender': 'male', 'gpa': 10.8, 'macid': 'yazdinip', 'lname': 'yazdinia', 'fname': 'pedram', 'choices': ['software', 'electrical', 'civil']},
    {'gender': 'male', 'gpa': 10.5, 'macid': 'sheetz', 'lname': 'sheet', 'fname': 'zayed', 'choices': ['engphys', 'electrical', 'materials']},
    {'gender': 'male', 'gpa': 10.5, 'macid': 'jordans', 'lname': 'samson', 'fname': 'jordan', 'choices': ['civil', 'electrical', 'software']},
    {'gender': 'female', 'gpa': 6.0, 'macid': 'gonzalc', 'lname': 'gonzal', 'fname': 'cat', 'choices': ['mechanical', 'electrical', 'materials']},
    {'gender': 'male', 'gpa': 3.2, 'macid': 'valkirf', 'lname': 'valkir', 'fname': 'farzad', 'choices': ['mechanical', 'electrical', 'software']}
  ]
  if (sort(randomList) == expectedOutput):
    print("Sort List Passed!")
  else:
    print("Sort List Failed :(")

def emptySortAllocate():
  #if an empty list is passed into the alllocate function
  #first sort is checked because if sort doesnt work allocate wont work anyways
  #if sort works then it checks allocate with an empty list in several different cases
  emptyCapacityDictionary = {'engphys': [], 'civil': [], 'chemical': [], 'materials': [], 'electrical': [], 'mechanical': [], 'software': []}

  if (sort(emptyList) == []):
    print("Empty Sort Passed!")
    if ((allocate(emptyList,emptyList,emptyDictionary) == emptyCapacityDictionary) & (allocate(emptyList,emptyList,unlimitedCapacity) == emptyCapacityDictionary) & (allocate(emptyList,controlledFreeChoice,emptyDictionary) == emptyCapacityDictionary)):
      print("Empty Allocation Passed!")
    else:
      print("Empty Allocation Failed :(")
  else:
    print("Empty Sort Failed :(")

def emptyGender():
  #if an empty list is passed into the average function
  if (average(emptyList, 'male') == -1):
    print("Empty Gender Passed!")
  else:
    print("Empty Gender Failed :(")

def wrongGender(): 
  #if the programer does not enter either male or female as a parameter
  if (average(randomList, 'test') == -1):
    print("Wrong Gender Passed!")
  else:
    print("Wrong Gender Failed :(")

def zeroGender():
  #if the programer enters a list with zero males or zero females as a parameter
  zeroMaleList = [
    {'gender': 'female', 'gpa': 10.5, 'choices': ['engphys', 'electrical', 'materials'], 'lname': 'sheet', 'fname': 'zayed', 'macid': 'sheetz'}, 
    {'gender': 'female', 'gpa': 10.8, 'choices': ['software', 'electrical', 'civil'], 'lname': 'yazdinia', 'fname': 'pedram', 'macid': 'yazdinip'}
  ]
  if ((average(zeroMaleList, 'male') == -1)):
    print("Zero Gender Passed!")
  else:
    print("Zero Gender Failed :(")
  

def allPassAllocate():
  #In this test case everyone passes, theres unlimited capacity, no free choice students and everyone gets their first choice
  allPassList = [
    {'gender': 'male', 'gpa': 10.5, 'choices': ['software', 'electrical', 'materials'], 'lname': 'sheet', 'fname': 'zayed', 'macid': 'sheetz'},
    {'gender': 'male', 'gpa': 10.8, 'choices': ['chemical', 'electrical', 'civil'], 'lname': 'yazdinia', 'fname': 'pedram', 'macid': 'yazdinip'},
    {'gender': 'male', 'gpa': 11.5, 'choices': ['software', 'chemical', 'electrical'], 'lname': 'buszowiecki', 'fname': 'dominik', 'macid': 'dominikb'},
    {'gender': 'male', 'gpa': 7.2, 'choices': ['materials', 'electrical', 'software'], 'lname': 'valkir', 'fname': 'farzad', 'macid': 'valkirf'},
    {'gender': 'female', 'gpa': 6.0, 'choices': ['mechanical', 'electrical', 'materials'], 'lname': 'gonzal', 'fname': 'cat', 'macid': 'gonzalc'},
    {'gender': 'male', 'gpa': 10.9, 'choices': ['civil', 'mechanical', 'materials'], 'lname': 'hula', 'fname': 'mustafa', 'macid': 'mustafah'},
    {'gender': 'male', 'gpa': 10.2, 'choices': ['engphys', 'electrical', 'software'], 'lname': 'samson', 'fname': 'jordan', 'macid': 'jordans'}
  ]
  expectedOutput = {
    'engphys': [{'gender': 'male', 'gpa': 10.2, 'choices': ['engphys', 'electrical', 'software'], 'lname': 'samson', 'fname': 'jordan', 'macid': 'jordans'}],
    'civil': [{'gender': 'male', 'gpa': 10.9, 'choices': ['civil', 'mechanical', 'materials'],'lname': 'hula', 'fname': 'mustafa', 'macid': 'mustafah'}], 
    'chemical': [{'gender': 'male', 'gpa': 10.8, 'choices': ['chemical', 'electrical', 'civil'], 'lname': 'yazdinia', 'fname': 'pedram', 'macid': 'yazdinip'}],
    'materials': [{'gender': 'male', 'gpa': 7.2, 'choices': ['materials', 'electrical', 'software'], 'lname': 'valkir', 'fname': 'farzad', 'macid': 'valkirf'}],
    'electrical': [],
    'mechanical': [{'gender': 'female', 'gpa': 6.0, 'choices': ['mechanical', 'electrical', 'materials'], 'lname': 'gonzal', 'fname': 'cat', 'macid': 'gonzalc'}],
    'software': [{'gender': 'male', 'gpa': 11.5, 'choices': ['software', 'chemical', 'electrical'], 'lname': 'buszowiecki', 'fname': 'dominik', 'macid': 'dominikb'},{'gender': 'male', 'gpa': 10.5, 'choices': ['software', 'electrical', 'materials'], 'lname': 'sheet', 'fname': 'zayed', 'macid': 'sheetz'}]
  }
  if (allocate(allPassList,noFreeChoice,unlimitedCapacity) == expectedOutput):
    print("All Pass Allocate Passed!")
  else:
    print("All Pass Allocate Failed :(")

def failAllocate():
  #In this test case a few students fail, they should not be on the expectedOutput
  failList = [
    {'gender': 'male', 'gpa': 10.5, 'choices': ['software', 'electrical', 'materials'], 'lname': 'sheet', 'fname': 'zayed', 'macid': 'sheetz'},
    {'gender': 'male', 'gpa': 10.8, 'choices': ['chemical', 'electrical', 'civil'], 'lname': 'yazdinia', 'fname': 'pedram', 'macid': 'yazdinip'},
    {'gender': 'male', 'gpa': 11.5, 'choices': ['software', 'chemical', 'electrical'], 'lname': 'buszowiecki', 'fname': 'dominik', 'macid': 'dominikb'},
    {'gender': 'male', 'gpa': 2.2, 'choices': ['materials', 'electrical', 'software'], 'lname': 'valkir', 'fname': 'farzad', 'macid': 'valkirf'},
    {'gender': 'female', 'gpa': 6.0, 'choices': ['mechanical', 'electrical', 'materials'], 'lname': 'gonzal', 'fname': 'cat', 'macid': 'gonzalc'},
    {'gender': 'male', 'gpa': 0, 'choices': ['civil', 'mechanical', 'materials'], 'lname': 'hula', 'fname': 'mustafa', 'macid': 'mustafah'},
    {'gender': 'male', 'gpa': 10.2, 'choices': ['civil', 'engphys', 'software'], 'lname': 'samson', 'fname': 'jordan', 'macid': 'jordans'}
  ]
  expectedOutput = {
    'engphys': [],
    'civil': [{'gender': 'male', 'gpa': 10.2, 'choices': ['civil', 'engphys', 'software'], 'lname': 'samson', 'fname': 'jordan', 'macid': 'jordans'}], 
    'chemical': [{'gender': 'male', 'gpa': 10.8, 'choices': ['chemical', 'electrical', 'civil'], 'lname': 'yazdinia', 'fname': 'pedram', 'macid': 'yazdinip'}],
    'materials': [],
    'electrical': [],
    'mechanical': [{'gender': 'female', 'gpa': 6.0, 'choices': ['mechanical', 'electrical', 'materials'], 'lname': 'gonzal', 'fname': 'cat', 'macid': 'gonzalc'}],
    'software': [{'gender': 'male', 'gpa': 11.5, 'choices': ['software', 'chemical', 'electrical'], 'lname': 'buszowiecki', 'fname': 'dominik', 'macid': 'dominikb'},{'gender': 'male', 'gpa': 10.5, 'choices': ['software', 'electrical', 'materials'], 'lname': 'sheet', 'fname': 'zayed', 'macid': 'sheetz'}]
  }
  if (allocate(failList,controlledFreeChoice,unlimitedCapacity) == expectedOutput):
    print("Fail Allocate Passed!")
  else:
    print("Fail Allocate Failed :(")



def freeChoiceAllocate():
  #In this test case  capacity is limited to ensure free choice students get the program they desire first. 
  #In turn it also technically checks what happens if a student's choice is full.
  freeChoiceList = [
    {'gender': 'male', 'gpa': 10.5, 'choices': ['software', 'electrical', 'materials'], 'lname': 'sheet', 'fname': 'zayed', 'macid': 'sheetz'},
    {'gender': 'male', 'gpa': 10.8, 'choices': ['chemical', 'electrical', 'civil'], 'lname': 'yazdinia', 'fname': 'pedram', 'macid': 'yazdinip'},
    {'gender': 'male', 'gpa': 11.5, 'choices': ['software', 'chemical', 'electrical'], 'lname': 'buszowiecki', 'fname': 'dominik', 'macid': 'dominikb'},
    {'gender': 'male', 'gpa': 4.2, 'choices': ['electrical', 'materials', 'software'], 'lname': 'valkir', 'fname': 'farzad', 'macid': 'valkirf'},
    {'gender': 'female', 'gpa': 6.0, 'choices': ['mechanical', 'electrical', 'materials'], 'lname': 'gonzal', 'fname': 'cat', 'macid': 'gonzalc'},
    {'gender': 'male', 'gpa': 4.0, 'choices': ['civil', 'mechanical', 'materials'], 'lname': 'hula', 'fname': 'mustafa', 'macid': 'mustafah'},
    {'gender': 'male', 'gpa': 10.2, 'choices': ['software', 'engphys', 'electrical'], 'lname': 'samson', 'fname': 'jordan', 'macid': 'jordans'}
  ]
  freeCapacity = {'engphys': 0, 'civil': 999, 'chemical': 999, 'materials': 999, 'electrical': 1, 'mechanical': 999, 'software': 2}
  expectedOutput = {
    'engphys': [],
    'civil': [{'gender': 'male', 'gpa': 4.0, 'choices': ['civil', 'mechanical', 'materials'], 'lname': 'hula', 'fname': 'mustafa', 'macid': 'mustafah'}], 
    'chemical': [{'gender': 'male', 'gpa': 10.8, 'choices': ['chemical', 'electrical', 'civil'], 'lname': 'yazdinia', 'fname': 'pedram', 'macid': 'yazdinip'}],
    'materials': [{'gender': 'male', 'gpa': 4.2, 'choices': ['electrical', 'materials', 'software'], 'lname': 'valkir', 'fname': 'farzad', 'macid': 'valkirf'}],
    'electrical': [{'gender': 'male', 'gpa': 10.2, 'choices': ['software', 'engphys', 'electrical'], 'lname': 'samson', 'fname': 'jordan', 'macid': 'jordans'}],
    'mechanical': [{'gender': 'female', 'gpa': 6.0, 'choices': ['mechanical', 'electrical', 'materials'], 'lname': 'gonzal', 'fname': 'cat', 'macid': 'gonzalc'}],
    'software': [{'gender': 'male', 'gpa': 11.5, 'choices': ['software', 'chemical', 'electrical'], 'lname': 'buszowiecki', 'fname': 'dominik', 'macid': 'dominikb'},{'gender': 'male', 'gpa': 10.5, 'choices': ['software', 'electrical', 'materials'], 'lname': 'sheet', 'fname': 'zayed', 'macid': 'sheetz'}]
  }
  if (allocate(freeChoiceList,controlledFreeChoice,freeCapacity) == expectedOutput):
    print("Free Choice Allocate Passed!")
  else:
    print("Free Choice Allocate Failed :(")  

def controlledAllocate():
  #in this test case there will be some students who failed, some who have free choice and some students that passed however all three of their choices will be filled up
  controlledList = [
    {'gender': 'male', 'gpa': 10.5, 'choices': ['software', 'electrical', 'materials'], 'lname': 'sheet', 'fname': 'zayed', 'macid': 'sheetz'},
    {'gender': 'male', 'gpa': 10.8, 'choices': ['software', 'electrical', 'civil'], 'lname': 'yazdinia', 'fname': 'pedram', 'macid': 'yazdinip'},
    {'gender': 'male', 'gpa': 11.5, 'choices': ['software', 'chemical', 'electrical'], 'lname': 'buszowiecki', 'fname': 'dominik', 'macid': 'dominikb'},
    {'gender': 'male', 'gpa': 3.2, 'choices': ['mechanical', 'electrical', 'software'], 'lname': 'valkir', 'fname': 'farzad', 'macid': 'valkirf'},
    {'gender': 'female', 'gpa': 6.0, 'choices': ['mechanical', 'electrical', 'materials'], 'lname': 'gonzal', 'fname': 'cat', 'macid': 'gonzalc'},
    {'gender': 'male', 'gpa': 10.9, 'choices': ['software', 'civil', 'materials'], 'lname': 'hula', 'fname': 'mustafa', 'macid': 'mustafah'},
    {'gender': 'male', 'gpa': 10.2, 'choices': ['civil', 'electrical', 'software'], 'lname': 'samson', 'fname': 'jordan', 'macid': 'jordans'}
  ]
  controlledCapacity = {'engphys': 3, 'civil': 1, 'chemical': 2, 'materials': 0, 'electrical': 0, 'mechanical': 3, 'software': 2}
  expectedOutput = {
    'engphys': [],
    'civil': [{'gender': 'male', 'gpa': 10.9, 'choices': ['software', 'civil', 'materials'],
    'lname': 'hula', 'fname': 'mustafa', 'macid': 'mustafah'}], 
    'chemical': [],
    'materials': [],
    'electrical': [],
    'mechanical': [{'gender': 'female', 'gpa': 6.0, 'choices': ['mechanical', 'electrical', 'materials'], 'lname': 'gonzal', 'fname': 'cat', 'macid': 'gonzalc'}],
    'software': [{'gender': 'male', 'gpa': 11.5, 'choices': ['software', 'chemical', 'electrical'], 'lname': 'buszowiecki', 'fname': 'dominik', 'macid': 'dominikb'},{'gender': 'male', 'gpa': 10.5, 'choices': ['software', 'electrical', 'materials'], 'lname': 'sheet', 'fname': 'zayed', 'macid': 'sheetz'}]
  }

  if (allocate(controlledList,controlledFreeChoice,controlledCapacity) == expectedOutput): 
    print("Controlled Allocate Passed!") 
  else:
    print("Controlled Allocate Failed :(")



sortList()
emptySortAllocate()
emptyGender()
wrongGender()
zeroGender()
allPassAllocate()
failAllocate()
freeChoiceAllocate()
controlledAllocate()



