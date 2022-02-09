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
    
    while True:
        userInput = input(">>")

        if userInput.lower() == "exit":
            sys.exit(1)
        os.write(1,(userInput).encode())
        os.write(1,("\n").encode())
        execute_Command(userInput)


    
def execute_Command(command):
    rc = os.fork()

    if rc < 0 :
        os.write(2,("Fork failed").encode())
        sys.exit(1)
    elif rc == 0:
        args = [command,"shell.py"]
        for dir in re.split(":", os.environ['PATH']):
            program = "%s/%s" % (dir,args[0])
            
            try:
                os.execve(program,args,os.environ)
            except FileNotFoundError:
                pass
        os.write(1,("Program Not found").encode())
        sys.exit(1)
    else:

        waitForChild = os.wait()
        #os.write(1,("Done waiting\n").encode())



if '__main__' == __name__:
    main()
