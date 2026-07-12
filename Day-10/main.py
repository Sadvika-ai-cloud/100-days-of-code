import art
def add(n1, n2):
    return n1 + n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
my_dict={"+":add,"-":sub,"*":mul,"/":div,
}

print(my_dict["*"](4,6))
#print(add(3,(sub(5,(mul(3,(div(8,2))))))))
def calculator():
    print(art.logo)
    should_accumulate = True
    num1 = float(input("What is the first number?: "))

    while should_accumulate:
        for symbol in my_dict:
            print(symbol)
        operation_symbol = input("Pick an operation: ")
        num2 = float(input("What is the next number?: "))
        answer = my_dict[operation_symbol](num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        choice = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ")

        if choice == "y":
            num1 = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

