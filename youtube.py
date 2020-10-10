import os

def main():
    directory = os.path.dirname(__file__)
    project = input('[] Insert project name: ')
    projectDirectory = directory + '\\' + project

    def createDirectory():
        checkDirectory = os.path.exists(projectDirectory)
        
        if checkDirectory:
            print ("[] This project already exists. " + projectDirectory)
            main()
        else:
            print ("[] Creating project directories: " + projectDirectory)
            os.mkdir(projectDirectory)
            os.mkdir(projectDirectory + '\\Audios')
            os.mkdir(projectDirectory + '\\Videos')
            os.mkdir(projectDirectory + '\\Photos')

            showDirectory = os.system('dir '+ projectDirectory)
            print (showDirectory)
            input("Press enter to continue")
    createDirectory()
main()