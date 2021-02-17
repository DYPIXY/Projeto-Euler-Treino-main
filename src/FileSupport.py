import time
import os

path = os.path.dirname(__file__)
os.chdir(path)

print('')
print("Hello",os.getlogin())
 
def filesfunc():    
    ListFiles = []
    for s in os.listdir(path): 
        if s.startswith("Project"):
            ListFiles.append(s)
            ListFiles.sort()  
    print(ListFiles)

def keyboard():
    a = int(input("Select the number that represents one of the projects you want to run: "))
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
#i desist to do that in other languages because i prefer to do other projects than stuck with just one
#def filetype():

ExecWay = str('java '+FileToExec+'.java')

'''
        dotfile = '.java'
    elif a=='Python' or 'python':
        ExecWay = str('python '+FileToExec+'.py')
        dotfile = '.py'
    elif a=='c++' or 'C++':
        ExecWay = str(' '+FileToExec+' ')
        dotfile = '.cc'
    print('Archive is a "'+dotfile+'"')
    return ExecWay
'''
#ChoosedExec = filetype()
exectime = time.time()
print('')
os.system(ExecWay)
print( "Executed in ≅",time.time() - exectime,'seconds')