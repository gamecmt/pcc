class Employee(object):

    def __init__(self, firstname, lastname, annual_salary):
        self.firstname = firstname
        self.lastname = lastname
        self.annual_salary = annual_salary
        self.properties = [self.firstname, self.lastname, self.annual_salary]

    def give_raise(self, raised='5000'):
        self.raised = raised
        self.properties.append(self.raised)
        print("You annual salary can be raised " + str(self.raised))

    def show_employee(self):
        print("Employee properties: ")
        for property in self.properties:
            print(' - ' + property)

flypig = Employee('fly', 'pig', '50000')
flypig.show_employee()
flypig.give_raise('333')
flypig.show_employee()
