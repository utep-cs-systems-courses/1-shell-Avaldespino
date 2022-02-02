import os, sys, time, re



ls(path):
   rc = os.fork()

   if rc < 0:
       os.write(2,("Fork failed, returning").encode())
       sys.exit(1)

   elif rc == 0:                   # child

       
