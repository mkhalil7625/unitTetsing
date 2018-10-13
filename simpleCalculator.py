
def main():
    menu()

def menu():
   print("Select operation.")
   print("1.Add")
   print("2.Subtract")
   print("3.Multiply")
   print("4.Divide")
   print("5.Exit")
   print()

# Take input from the user
   choice = input("Enter choice:")
   if choice.isnumeric():

        x = float(input("Enter first number: "))
        y = float(input("Enter second number: "))
        if choice == '1':
            print(x,"+",y,"=", add(x,y))

        elif choice == '2':
            print(x,"-",y,"=", subtract(x,y))

        elif choice == '3':
            print(x,"*",y,"=", multiply(x,y))

        elif choice == '4':
            try:
                print(x,"/",y,"=", divide(x,y))
            except ZeroDivisionError:
                print("Invalid input")
        elif choice == '5':
            print("See Ya!")
        else:
            print("Invalid input")

   else:
       print("Invalid input")
       print()
       menu()

# add
def add(x, y):
   return x + y

# subtract
def subtract(x, y):
   return x - y

# multiply
def multiply(x, y):
   return x * y

#divide
def divide(x, y):
   return x / y


if __name__ == '__main__':
   main()