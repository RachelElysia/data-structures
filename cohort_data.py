"""Functions to parse a file containing student data."""


def all_houses(filename):
    """Return a set of all house names in the given file.

    For example:
      >>> unique_houses('cohort_data.txt')
      {"Dumbledore's Army", 'Gryffindor', ..., 'Slytherin'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

  #split the lines at | vertical bar  
    opened_file = open(filename)
    #houses = set()
    house_list = []
  
    for line in opened_file:
      person_line = line.split("|")
      if person_line[2] != '':
        house_list.append(person_line[2])
      
    house_set = set(house_list)

    return house_set



def students_by_cohort(filename, cohort='All'):
    """Return a list of students' full names by cohort.

    Names are sorted in alphabetical order. If a cohort isn't
    given, return a list of all students. For example:
      >>> students_by_cohort('cohort_data.txt')
      ['Adrian Pucey', 'Alicia Spinnet', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Fall 2015')
      ['Angelina Johnson', 'Cho Chang', ..., 'Terence Higgs', 'Theodore Nott']

      >>> students_by_cohort('cohort_data.txt', cohort='Winter 2016')
      ['Adrian Pucey', 'Andrew Kirke', ..., 'Roger Davies', 'Susan Bones']

      >>> students_by_cohort('cohort_data.txt', cohort='Spring 2016')
      ['Cormac McLaggen', 'Demelza Robins', ..., 'Zacharias Smith']

      >>> students_by_cohort('cohort_data.txt', cohort='Summer 2016')
      ['Alicia Spinnet', 'Dean Thomas', ..., 'Terry Boot', 'Vincent Crabbe']

    Arguments:
      - filename (str): the path to a data file
      - cohort (str): optional, the name of a cohort

    Return:
      - list[list]: a list of lists
    """

    opened_file = open(filename)

    students = []
    cohort_list = []

    for line in opened_file:
      # unpack the list, assign names to each item
      # strip the right side of /n or spaces or whatever
      first_name, last_name, house, adviser, cohort_name = line.rstrip().split("|")  
      if cohort_name is "I":
        continue
      if cohort_name is "G":
        continue
      full_name = first_name + " " + last_name
      #cohorts first and make a set
      cohort_list.append(cohort_name)
      if cohort in ('All', cohort_name):
          students.append(full_name)

    return sorted(students)

def all_names_by_house(filename):
    """Return a list that contains rosters for all houses, ghosts, instructors.

    Rosters appear in this order:
    - Dumbledore's Army
    - Gryffindor
    - Hufflepuff
    - Ravenclaw
    - Slytherin
    - Ghosts
    - Instructors

    Each roster is a list of names sorted in alphabetical order.

    For example:
      >>> rosters = hogwarts_by_house('cohort_data.txt')
      >>> len(rosters)
      7

      >>> rosters[0]
      ['Alicia Spinnet', ..., 'Theodore Nott']
      >>> rosters[-1]
      ['Filius Flitwick', ..., 'Severus Snape']

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[list]: a list of lists
    """
    opened_file = open(filename)
    
    dumbledores_army = []
    gryffindor = []
    hufflepuff = []
    ravenclaw = []
    slytherin = []
    ghosts = []
    instructors = []

    for line in opened_file:
      # unpack the list, assign names to each item
      # strip the right side of /n or spaces or whatever
      first_name, last_name, house, adviser, cohort_name = line.rstrip().split("|")  
      full_name = first_name + " " + last_name
      if cohort_name is "I":
        instructors.append(full_name)
      if cohort_name is "G":
        ghosts.append(full_name)
      #cohorts first and make a set
      if house == "Dumbledore's Army":
        dumbledores_army.append(full_name)
      if house == "Gryffindor":
        gryffindor.append(full_name)
      if house == "Hufflepuff":
        hufflepuff.append(full_name)
      if house == "Ravenclaw":
        ravenclaw.append(full_name)
      if house == "Slytherin":
        slytherin.append(full_name)

    dumbledores_army.sort()
    gryffindor.sort()
    hufflepuff.sort()
    ravenclaw.sort()
    slytherin.sort()
    ghosts.sort()
    instructors.sort()

    houses = [dumbledores_army, gryffindor, hufflepuff, ravenclaw, slytherin, ghosts, instructors]

    # TODO: replace this with your code

    return houses


def all_data(filename):
    """Return all the data in a file.

    Each line in the file is a tuple of (full_name, house, advisor, cohort)

    Iterate over the data to create a big list of tuples that individually
    hold all the data for each person. (full_name, house, advisor, cohort)

    For example:
      >>> all_student_data('cohort_data.txt')
      [('Harry Potter', 'Gryffindor', 'McGonagall', 'Fall 2015'), ..., ]

    Arguments:
      - filename (str): the path to a data file

    Return:
      - list[tuple]: a list of tuples
    """
    opened_file = open(filename)
    all_data = []
    for line in opened_file:
      # unpack the list, assign names to each item
      # strip the right side of /n or spaces or whatever
      first_name, last_name, house, advisor, cohort_name = line.rstrip().split("|")  
      full_name = first_name + " " + last_name
      
      #create tuple for each line
      line_tuple = (full_name, house, advisor, cohort_name)
      all_data.append(line_tuple)

    return all_data


def get_cohort_for(filename, name):
    """Given someone's name, return the cohort they belong to.

    Return None if the person doesn't exist. For example:
      >>> get_cohort_for('cohort_data.txt', 'Harry Potter')
      'Fall 2015'

      >>> get_cohort_for('cohort_data.txt', 'Hannah Abbott')
      'Winter 2016'

      >>> get_cohort_for('cohort_data.txt', 'Balloonicorn')
      None

    Arguments:
      - filename (str): the path to a data file
      - name (str): a person's full name

    Return:
      - str: the person's cohort or None
    """
    opened_file = open(filename)

    for line in opened_file:
      # unpack the list, assign names to each item
      # strip the right side of /n or spaces or whatever
      first_name, last_name, house, advisor, cohort_name = line.rstrip().split("|")  
      full_name = first_name + " " + last_name

      if full_name == name:
        return cohort_name
          


def find_duped_last_names(filename):
    """Return a set of duplicated last names that exist in the data.

    For example:
      >>> find_name_duplicates('cohort_data.txt')
      {'Creevey', 'Weasley', 'Patil'}

    Arguments:
      - filename (str): the path to a data file

    Return:
      - set[str]: a set of strings
    """

    opened_file = open(filename)
    last_name_set = set()
    last_name_list = []

    for line in opened_file:
      # unpack the list, assign names to each item
      # strip the right side of /n or spaces or whatever
      first_name, last_name, house, advisor, cohort_name = line.rstrip().split("|")  

      if last_name not in last_name_list:
        last_name_list.append(last_name)
      else:
        last_name_set.add(last_name)
        
    return last_name_set



def get_housemates_for(filename, name):
    """Return a set of housemates for the given student.

    Given a student's name, return a list of their housemates. Housemates are
    students who belong to the same house and were in the same cohort as the
    given student.

    For example:
    >>> get_housemates_for('cohort_data.txt', 'Hermione Granger')
    {'Angelina Johnson', ..., 'Seamus Finnigan'}
    """
    opened_file = open(filename)

    housemates = set()


    for line in opened_file:
      # unpack the list, assign names to each item
      # strip the right side of /n or spaces or whatever
      first_name, last_name, house, advisor, cohort_name = line.rstrip().split("|")  
      full_name = first_name + " " + last_name

      if full_name == name:
        correct_cohort = cohort_name
        correct_house = house

    for line in opened_file:
      first_name, last_name, house, advisor, cohort_name = line.rstrip().split("|")  
      full_name = first_name + " " + last_name

      if correct_cohort == cohort_name and correct_house == house and full_name != name:
        housemates.add(full_name)

    #given students name, identify their house and cohort

    #from the house and cohort, find students full names who match both

    #return a list of the full_names
    
    return housemates



##############################################################################
# END OF MAIN EXERCISE.  Yay!  You did it! You Rock!
#

if __name__ == '__main__':
    import doctest

    result = doctest.testfile('doctests.py',
                              report=False,
                              optionflags=(
                                  doctest.REPORT_ONLY_FIRST_FAILURE
                              ))
    doctest.master.summarize(1)
    if result.failed == 0:
        print('ALL TESTS PASSED')
