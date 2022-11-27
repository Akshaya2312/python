# We can standardize what those attributes can be and define in class so that can be  use for multiple objects.

class Employee:
    def __init__(self, name, company): # this is an impliment of the initialization of an object in python
        # This is how store th values of object that just instantiated
        # Self will give access to current object just created
        self.name=name 
        self.company=company

# Here we created an empty class 
def main ():
    employee = get_employee()   
    print(f"{employee.name} work in {employee.company}")

def get_employee():
    # employee = Employee () #Technically we are object of a class. We use object build a specifc car from the blueprint  class.
    # employee.name= input("Name: ")
    # employee.company= input("Employee:")
    # return employee
    name= input("Name: ")
    company= input("Employee:")
    employee=Employee(name, company) 
    # This line also known as constructor call .It si going to construct a employee object for me
    # This will help to construct an object there is nothing initially.
    # But objects exists in computers memory. Now its upto us how to ssore name and company inside the object.
    # Python will automatically call init method for you . 
    # It is going to automatically pass in refernce to an argument that represent the current object that is just constructed in memory for you.
    # Its upto us then how to popuate value 
    # It is going to use employee class as template or basic structure . So that evey employee structure the same.
    # With this approach we can customise the objects(build car with different colors etc)
    return employee

if __name__ == "__main__":
    main()