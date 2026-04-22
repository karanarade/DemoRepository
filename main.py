## write a python fuction which will take user input as a num and will print table of that num

def generate_table():
    x= int(input("Enter a num: "))

    for i in range(1,11):
        print(f"{x}*{i} = {x*i}")
generate_table()
        
        