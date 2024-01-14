def calculator
    def add(x,y):
        return x+y
    def subtract(x-y):
        return x-y
    def multiply(x*y):
        return x*y
    def divide(x/y):
        return x/y
    print("select opration.")
    print("1.add")
    print("2.subtract")
    print("3.multiply")
    print("4.divide")
    while True:
        choice = input("Enter your choice(1,2,3,4)")
        if choice in('1', '2', '3', '4'):
            number1 = float(input("Enter first number:"))
            number2 = float(input("Enter second number:"))
            if choice == '1':
                print(number1, "+", number2, "=", (add number1, number2))
            if choice == '2':
                print(number1, "-", number2, "=", (subtract number1, number2))
            if choice == "3":
                print(number1, "*", number2, "=", (mutiply number1, number2))
            if choice == "4":
                print(number1, "/", number2, "=", (divide number1, number2))
                break
            else
            print("Enter input is invaid")
    
                
            
        
    
