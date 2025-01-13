class Worker:
    raise_rate=1.8
    
    def __init__(self,name,surname,age,email,salary):#constructor
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
        self.salary = salary
    def giveNameSurname(self):
        return self.name + " " + self.surname
    def calculateSalary(self):
        self.salary=self.salary+ self.salary * self.raise_rate

worker=Worker("İlhan","danis","23","enes123@gmail.com",10000)
print(worker.giveNameSurname())

# class variable

person = Worker("Enes","Daniş","23","enes123@gmail.com",20000)


person.calculateSalary()

print(person.salary)