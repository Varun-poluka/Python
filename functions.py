def main(): #defining the main function
    lang = input("Enter the first two letters of the language:")
    greeting = greet(lang) #calling the greet function
    print(f"{greeting},Varun")

def greet(lang): # defining thr greet function and returning the appropriate greeting
    if lang == "en":
        return "Hello"
    elif lang == "es":
        return "Hola"
    else:
        return "Bonjour"

main() # calling main to execute the code