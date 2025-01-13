class Worker:
    def __init__(self,name,surname,age,email):
        self.name = name
        self.surname = surname
        self.age = age
        self.email = email
    def giveNameSurname(self):
        return self.name + " " + self.surname    

worker=Worker("İlhan","danis","23","enes123@gmail.com")
print(worker.giveNameSurname())