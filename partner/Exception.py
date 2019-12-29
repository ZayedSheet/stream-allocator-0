## @file Exception.py
#  @author Jack Buckley
#  @brief A module containing custom exceptions for CalcModule.
#  @date 18 January 2019

class GenderNotGiven(Exception):
    pass

class NoDepartmentsHaveCapacity(Exception):
    pass

class FreeChoiceStudentNotAccountedFor(Exception):
    pass

class EmptyStudentDictionaryList(Exception):
    pass

class EmptyDepartmentCapacityDict(Exception):
    pass