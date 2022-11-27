#Class is like a blueprint for pieces of data objects. 
# It is like structure of car with attributes and functions like seats , brakes wheel with taht you can crate multiple objects like Honda city, Maruti with differnt color sizes and functinallity 
#Class will alow to invent your data types in python

class Employee:
    ...
# Here we created an empty class 
def main ():
    employee = get_employee()   
    print(f"{employee.name} work in {employee.company}")

def get_employee():
    employee = Employee () #Creating a funtion same as class name
    employee.name= input("Name: ")
    employee.company= input("Employee:")
    return employee

if __name__ == "__main__":
    main()