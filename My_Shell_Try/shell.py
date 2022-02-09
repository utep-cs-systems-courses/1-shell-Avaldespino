import os, sys, time, re


def main():
    pid = os.getpid()
    userName = "Malcom"
    password = "ChaosTheory"
    os.write(1,("Welcome to Jurassic park>>>\n").encode())
    while True:
        os.write(1,("Please enter User: ").encode())
        name = input();
        if name == userName:
            os.write(1,("Please enter password: ").encode())
            userPass = input();
            if userPass == password:
                break;
            else:
                os.write(1,("Wrong password\n").encode())
        else:
            os.write(1,("Wrong username\n").encode())
    
    while(1):
        userInput = input(">>")

        if userInput.lower() == "exit":
            sys.exit(1)
        os.write(1,(userInput).encode())
        os.write(1,("\n").encode())
    
    
def execute_Command(command):
    rc = os.fork()

    if rc < 0 :
        os.write(2,("Fork failed").encode())
        sys.exit(1)
    elif rc == 0:

        os.write(1,("Fork worked").encode())
    else:

        waitForChild = os.wait()
        os.write(1,("Done waiting\n").encode())



if '__main__' == __name__:
    main()
