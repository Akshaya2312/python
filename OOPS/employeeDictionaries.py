def main ():
    employee = get_employee()   
    print(f"{employee['name']} work in {employee['c']}")

def get_employee():
    # employee = {} #syntax of defining dictionary  with curly brackets
    # employee["name"] = input("Name: ")
    # employee["house"] = input("HOuse: ") 
    # return employee
    # Instead of creating un ncessary variables we  do not need to create discornay in starting

    name= input("Name: ")
    company = input ("Company: ")
    return {"name": name, "house":company} #creating dictionaries ont thr file . it am not look like readable as compared to first approach but this could also be the way.

if __name__ == "__main__":
    main()
    
  

## Dictioary is a collection of keys and values. You do not need to remember the loaction of house , name etc.