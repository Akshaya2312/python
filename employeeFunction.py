def main ():
    name = get_name()
    company = get_company()
    print(f"{name} work in {company}")


def get_name():
    name = input("Name:")
    return name 

##Another way to return 
## return input ("Name:")

def get_company():
    company = input("Company:")
    return company

if __name__ == "__main__":
    main()


##  It is  super simple funtion but its an bstaraction  We have function called get_name() but we odnt care about the abstraction.
## We just know its a function which will return name and dont care about implimentation