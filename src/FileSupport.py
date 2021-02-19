import time
import os

print("Hello",os.getlogin())
def start():

    path = os.path.dirname(__file__)
    os.chdir(path)

    print('')
    
    def filesfunc():    
        ListFiles = []
        for s in os.listdir(path): 
            if s.startswith("Project"):
                ListFiles.append(s)
                ListFiles.sort()  
        print(ListFiles)

    def keyboard():
        a = input("Select the number that represents one of the projects you want to run: ")
        
        a = str(a)
        if len(a) == 1:
            a = str('00'+a)
        elif len(a)==2:
            a= str('0'+a)
        if len(a)!= 3:
            print("invalid key, please select a valid integer")
        a = str(a)
        return a

    filesfunc()

    NumOfExec = keyboard()
    FileToExec=str('Project'+NumOfExec) 
    ExecWay = str('java '+FileToExec+'.java')

    #i desist to do that in other languages because i prefer to do other projects than stuck with just one

    exectime = time.time()
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
    #end of "start()"

start()