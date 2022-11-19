def main ():
    
 
    student = get_student()
    if student[0]== "Deepak": 
        student[1] = "Amazon"    
    print(f"{student[0]} work in {student[1]}")

def get_student():
    name = input("Name:")
    company = input("Company:")

    return [name, company] ## This is syntax  of list with square brackets


if __name__ == "__main__":
    main()
    
  

## So list is collection of value (x,y) or (x,y,z). They are immutable.