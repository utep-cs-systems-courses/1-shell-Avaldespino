#! /usr/bin/python3
import os, sys, time, re


def main():
    pid = os.getpid()
    fdOut = os.open("shell-output.txt", os.O_CREAT | os.O_WRONLY)
    fdIn = os.read(0,10000)
        
    while True:
        os.write(1,(os.getcwd()).encode())
        os.write(1,(">>").encode())
        userInput = os.read(fdIn,10000)

        if userInput.lower() == "exit":
            sys.exit(1)
        os.write(1,(userInput).encode())
        os.write(1,("\n").encode())
        if sys.argv[0] == "cd":
            change_Dir(sys.argv[1])
        else:
            execute_Command(userInput)


    
def execute_Command(command):
    rc = os.fork()

    if rc < 0 :
        os.write(2,("Fork failed").encode())
        sys.exit(1)
    elif rc == 0:
        args = command.split()
        for dir in re.split(":", os.environ['PATH']):
            program = "%s/%s" % (dir,args[0])
            
            try:
                os.execve(program,args,os.environ)
            except FileNotFoundError:
                pass
        os.write(1,("Program Not found").encode())
        print("\n")
        sys.exit(1)
    else:

        waitForChild = os.wait()
        #os.write(1,("Done waiting\n").encode())



def change_Dir(directory):
    os.chdir(directory)

if '__main__' == __name__:
    main()
