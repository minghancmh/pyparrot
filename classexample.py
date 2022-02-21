class Employee:
   'Common base class for all employees'
   empCount = 0

   def __init__(self, name, salary):
      self.name = name
      self.salary = salary
      Employee.empCount += 1
   
   def displayCount(self):
     print ("Total Employee %d" % Employee.empCount)

   def displayEmployee(self):
      print ("Name : ", self.name,  ", Salary: ", self.salary, "age: ", self.age)


emp1 = Employee('harry','2000')
emp2 = Employee('charles', '2')

emp1.age = 5
emp2.age = 70

emp2.displayEmployee()
