def add_two_numbers(num1,num2):
    return num1+num2


#-----------Main_Handler------------#

def my_handler():
    try:
        temp = input("Hello")
        number1 = int(input("Enter the first number"))
        number2 = int(input("Enter the second number"))
        result = add_two_numbers(number1,number2)
        print(f"Sum of the two numbers is {result}")
    
    except Exception as e:
        print("Error: Exception in main handler",e)

my_handler()