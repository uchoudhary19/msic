class Employee:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.__dict__[location] = location
    
    def increase_salary(self, percentage):
        self.salary += 100 * (percentage/100)

    def info(self):
        return(f"{self.name}")

    def __str__(self):
        return self.info()

class Developer(Employee):
    def increase_salary(self, percentage):
        return super().increase_salary(percentage)


developer = Developer("Usman", 21, "Mancester")
print(developer.increase_salary(10))