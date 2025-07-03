def main():
#takes input of hours and rate and converts to float 
    hrs = float(input("enter the number of hours:"))
    rate = float(input("enter the rate per hour:"))
    print(f"pay {compute_pay(hrs , rate)}") #calling function to compute the pay

def compute_pay(hrs , rate): #defining the function to compute the pay
    pay = 0
    if hrs > 40:
        pay = 40 * rate
        hrs = hrs - 40
        pay = pay + (hrs * (1.5 * rate))
    else:
        pay = hrs * rate
    return pay

main() #calling the main function