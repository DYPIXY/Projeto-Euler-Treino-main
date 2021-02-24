import time
import os
import math

print("Hello",os.getlogin())
def start():

    path = os.path.dirname(__file__)
    os.chdir(path)
    print('')

    #list all files in directory that starts with "Project"
    def filesfunc():    
        ListFiles = []
        for s in os.listdir(path): 
            if s.startswith("Project"):
                ListFiles.append(s)
                ListFiles.sort()  
        print(ListFiles)

    #user input
    def keyboard():
        a = 0
        del a
        a = input("Select the number that represents one of the projects you want to run: ")
    
        #shrek 2 
        if a =="shrek2" or a=="Shrek2":
            pathx = os.path.dirname(__file__)
            path = str(pathx+"/doNotClick")
            os.chdir(path)
            os.system("python doNotClick.py")
            quit()
        try:
            a=int(a)
        except ValueError:
            print("you are supossed to enter a integer number")
            print (a)
            print (type(a))
            del af
            keyboard()

        #if a is not int:
    
        
        #this is for validate "1", "01" or "001" that come from the user    
        #if length invalid, restart the ~keyboard()~
        a = str(a)
        if len(a) == 1:
            a = str('00'+a)
        elif len(a)==2:
            a= str('0'+a)
        if len(a)!= 3:
            print("invalid key, please select a valid integer")
            keyboard()
        a = str(a)
        return a
    
    filesfunc()
    #create a string that will initiate the java Project
    NumOfExec = keyboard()
    FileToExec=str('Project'+NumOfExec)
    ExecWay = str('java '+FileToExec+'.java')

    #i had the idea of remake the project euler but in python and c or c++, but
    #i desist to do that in other languages because i prefer to do other projects than stuck with just one
    #and i already know the answer, so i don't think this will be good 
    
    exectime = time.time()
    print("")
    print('May this take a little bit time, so be patient')
    print("")
    os.system(ExecWay)
    print( "Executed in ≅",time.time() - exectime,'seconds')
    print("")
    
    def reset():
        reset = input("want to run it again? [y/n] ")
        if reset=="y" or reset=="Y":
            start()
        elif reset=="n" or reset=="N":
            print("")
            print("ok, closing, goodbye!")
        else:
            print("that's a not valid string, please try again")
            reset()
    reset()
    #end of ~start()~

#this call the function of ~def start()~ to make all the interactions above     
start()