
class Employee:
    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "." + last + "@company.com"
    def fullname(self):
        return self.first + " " + self.last

empl_1 = Employee("Josh", "Bupper", 10000)
empl_2 = Employee("Jogger", "Roud", 200)

print(empl_1)



print('{} "test"  {}'.format(empl_1.email, empl_1.fullname()))
