#! /usr/bin/python3
import os, sys, time, re
def get_Input():
    os.write(1,(os.getcwd()).encode())
    os.write(1,(">>").encode())

    fdIn = os.read(0,100).decode()
    
   

   
    while True:
    
        if fdIn.encode() == "exit\n".encode():
            sys.exit(1)
        os.write(1,(fdIn).encode())
        os.write(1,("\n").encode())
        #fdIn = fdIn.replace("\n","")
        #fdIn = re.split(' ',fdIn)
        change = fdIn.split()
        if change[0] == "cd":
            change_Dir(change[1])
        else:
            execute_Command(fdIn)


def main():
    pid = os.getpid()
    
    get_Input()

  

    
def execute_Command(command):
    rc = os.fork()

    if rc < 0 :
        os.write(2,("Fork failed").encode())
        sys.exit(1)
    elif rc == 0:
        args = command.split()
        if ">" in args:
            
            args.remove(">")
            os.close(1)                 # redirect child's stdout
            os.open("p4-output.txt", os.O_CREAT | os.O_WRONLY);
            os.set_inheritable(1, True)
            args = args[0]
            args = args.split()
            
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
        get_Input()
        
        #os.write(1,("Done waiting\n").encode())



def change_Dir(directory):
    os.chdir(directory)
    get_Input()

if '__main__' == __name__:
    main()
