class Student():

    def __init__ (self, name, surname, studentnumber, course):
        self.name = name
        self.surname = surname
        self.studentnumber = studentnumber
        self.course = course

    def printDetails(self):
        print("My name is "+self.name)
        print("My surname is "+self.surname)
        print("My student number is "+self.studentnumber)
        print("My course is "+self.course)



    def getName(self):
        return self.name

    def getSurname(self):
        return self.surname


    def getStudentnumber(self):
        return self.studentnumber


    def getCourse(self):
        return self.course


                
    def setName(self, nameinput):
        self.name = nameinput   

     
    def setSurame(self, surnameinput):
        self.surname = surnameinput   

        
    def setStudentnumber(self, studentnumberinput):
        self.studentnumber = studentnumberinput  
               
        
    def setCourse(self, courseinput):
        self.course = courseinput
