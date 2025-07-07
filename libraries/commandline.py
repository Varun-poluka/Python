import sys # gives access to argv and exit 

if len(sys.argv) != 2: #checking if any command line arguement was given
    print("ERROR no command line arguement given")
    sys.exit(1) # exits the code by return 1 to signify error

print(f"Hello, {sys.argv[1]}") 
sys.exit(0) # exits the code with no error message returning 0 to signify success