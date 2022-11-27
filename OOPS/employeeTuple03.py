def main ():
    
    # name,company = get_student() ## we don tneed to unpack the value just get the whole tuple and get using its index.
    student = get_student()
    # if student[0]== "Deepak": So this is an example of tuple immutability. Here you cant not change the value of company.
    #     student[1] = "Amazon"    
     
    print(f"{student[0]} work in {student[1]}")

def get_student():
    name = input("Name:")
    company = input("Company:")

    return (name, company) ## Here its not two  values but tuple with two values.

    # return name, company (this is return values without parenthesiis and its tuple)


if __name__ == "__main__":
    main()
    
  

## In python you return two value in a single  return like name, company. This is not returning a single value but its a tuple.
## return (name, company)  this is Tuple 
## So tuple is collection of value (x,y) or (x,y,z). Tupels are immutable . If you want return list but do not want to change it then tuple is best
##
