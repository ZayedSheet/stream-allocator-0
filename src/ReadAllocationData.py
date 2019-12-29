## @file ReadAllocationData.py
#  @author Zayed Sheet
#  @brief This file contains functions that extracts student/department data from text files.
#  @date 2019-01-18


## @brief Uses the data from a text file to create a list of dictionaries.
#  @details Reads from a text file and uses the data to create a list of dictionaries where each dictionary represents a student. 
#           \nSome of the code for this function was referenced from:\n 
#           https://stackoverflow.com/questions/4842057/easiest-way-to-ignore-blank-lines-when-reading-a-file-in-python
#  @param s This parameter is a text file that contains a student on each line. Each line should contain the student's macid
#           firstname, lastname, gender, gpa and top 3 engineering stream choices. \nEach line in the textfile should be
#           formatted as such: 'macid, firstname, lastname, gender(male/female), gpa, firstchoice, secondchoice, thirdchoice'.
#  @return  This function returns a list of dictionaries where each dictionary represents a student with their macid, fname,
#           lname, gpa, choices as keys. The choices key contains a list with their top 3 engineering stream choices.  
def readStdnts(s):
  with open(s, "r") as f:
    #the line below creates a list of each line in the text file, ignoring empty lines
    student = [line.strip() for line in f if line.strip()] #https://stackoverflow.com/questions/4842057/easiest-way-to-ignore-blank-lines-when-reading-a-file-in-python
    dictionaries = []
    for i in range(len(student)):
      attributes = student[i].split(', ')
      try:
        if ((attributes[3] == 'male') | (attributes[3] == 'female')): #this ensures that the inputted gender is either male or female to prevent errors in average function
          dictionaries.append({
            'macid':attributes[0],
            'fname':attributes[1],
            'lname':attributes[2],
            'gender':attributes[3],
            'gpa':float(attributes[4]),
            'choices':[attributes[5],attributes[6],attributes[7]]
          })
        else:
          print("Student with macid ", attributes[0], " has been ignored due to invalid gender input")
      except IndexError:
        print("Error while processing macid ", attributes[0], " check file for missing information!")
  f.close()
  return(dictionaries)


## @brief Obtains the macids of everyone that has free choice from a text file.
#  @param s This parameter is a text file that has the macids of everyone with free choice. Each line should be an individual macid in the text file.
#  @return Returns a list of macids for students that have free choice.
def readFreeChoice(s):
  with open(s, "r") as f:
    macids = [line.strip() for line in f if line.strip()]
    return(macids)
  f.close()


## @brief  Obtains information on the engineering streams and their respective capacities.
#  @param s This parameter is a text file that contains the engineering streams and their respective capacities.
#           \nEach line in the text file should be formatted as such: 'program: capacity'
#  @return Returns a dictionary where each key is an engineering stream and the value is its' respective capacity. 
def readDeptCapacity(s):
  departmentOptions = ['software','electrical','mechanical','engphys','chemical','civil','materials']
  with open(s, "r") as f:
    lines = [line.strip() for line in f if line.strip()]
    dictionary = {}
    for i in range(len(lines)): #for every line
      dept = lines[i].split(': ') #creates a list with department and capacity
      if ((dept[1].isdigit() == True) & (dept[0] in departmentOptions)):
        dictionary[dept[0]] = int(dept[1]) #adds onto dictionary with department as the key and capacity as the value
      else:
        print("Error with one of the program capacities or name!")
  f.close()
  return dictionary
  
# print(readStdnts("test.txt"))
# print(readFreeChoice("free.txt"))
# print(readDeptCapacity("dept.txt"))