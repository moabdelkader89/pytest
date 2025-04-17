class bank_account:
  def __init__(self,name,salary,age,dep):
      self.name=name
      self.salary=salary
      self.age=age
      self.dep=dep
      
      
  def salary_rise(self): 
      if self.salary<100:
          new_salary=self.salary+500
          return new_salary
      else:
          print("salary is th same",self.salary)
          
          
  def cut_salary(self):
      if self.salary<=100:
          new_salary=self.salary+200
          print(new_salary)
      else:
          print("no need",self.salary) 
          
          
  def dep_rise(self):
       if self.name=="ahmed":
           newreise=self.salary+1000
           print(newreise)
       else:
           print("no rise")   