#! /usr/bin/python3
import os, sys, time, re
def get_Input():
    os.write(2,(os.getcwd()).encode())
    os.write(2,(">>").encode())

    fdIn = os.read(0,100).decode()
    
   

   
    while True:
    
        if fdIn.encode() == "exit\n".encode():
            sys.exit(1)
        os.write(2,(fdIn).encode())
        os.write(2,("\n").encode())
        
        change = fdIn.split()
        if change[0] == "cd":
            change_Dir(change[1])
        else:
            if "|" in change:
                pipe(fdIn)
            else:
                execute_Command(fdIn)
#parse out string to pass out input to both childs
def pipe(args):
    pr,pw = os.pipe()
    args = args.split()
    out = args.pop()
    args.pop()
    entrance = args.pop()

    for f in (pr,pw):
        os.set_inheritable(f,True)

    rc = os.fork()
    if rc < 0 :
        os.write(2,("Fork failed").encode())
        sys.exit(1)
    elif rc == 0:
        os.close(1)
        os.dup(pw)
        for dir in re.split(":", os.environ['PATH']):
            program = "%s/%s" % (dir,entrance)
            
            try:
                os.execve(program,entrance,os.environ)
            except FileNotFoundError:
                pass
        os.write(2,("Program Not found").encode())
        print("\n")
        sys.exit(1)

        
    rc2 = os.fork()
    if rc2 < 0 :
        os.write(2,("Fork failed").encode())
        sys.exit(1)
    elif rc2 == 0:
        
        os.close(0)
        os.dup(pr)
        for dir in re.split(":", os.environ['PATH']):
            program = "%s/%s" % (dir,out)
            
            try:
                os.execve(program,out,os.environ)
            except FileNotFoundError:
                pass
        os.write(2,("Program Not found").encode())
        print("\n")
        sys.exit(1)




        #Make this a on/off thing from user
    waitForChild = os.wait()
    for fd in (pr,pw):
        os.close(fd)
    get_Input()
        
        #os.write(1,("Done waiting\n").encode())

    

            
def main():
    pid = os.getpid()
    
    get_Input()
#For both out and in, make sure they get used inside the child
def redirect_output(args):
            
        args.remove(">")
        os.close(1)                 # redirect child's stdout
        os.open(args[1], os.O_CREAT | os.O_WRONLY);
        os.set_inheritable(1, True)
        args = args[0]
        args = args.split()
        execute_Command(args)
        

def redirect_input(args):
            
        args.remove("<")
        os.close(0)                 # redirect child's stdout
        os.open(args[1], os.O_RDONLY);
        os.set_inheritable(0, True)
        args = args[0]
        args = args.split()
        return args

    
def execute_Command(command):
    rc = os.fork()

    if rc < 0 :
        os.write(2,("Fork failed").encode())
        sys.exit(1)
    elif rc == 0:
        args = command.split()
        if "<" in args:
            args = redirect_input(args)
        if ">" in args:
            args = redirect_output(args)
        for dir in re.split(":", os.environ['PATH']):
            program = "%s/%s" % (dir,args[0])
            
            try:
                os.execve(program,args,os.environ)
            except FileNotFoundError:
                pass
        os.write(2,("Program Not found").encode())
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
