import os

def main():
    directory = os.path.dirname(__file__)
    project = input('Insira o nome do Projeto: ')
    projectDirectory = directory + '\\' + project

    def createDirectory():
        checkDirectory = os.path.exists(projectDirectory)
        
        if checkDirectory:
            print ("Este projeto já existe: " + projectDirectory)
            main()
        else:
            print ("Criando diretorios do projeto: " + projectDirectory)
            os.mkdir(projectDirectory)
            os.mkdir(projectDirectory + '\\Audios')
            os.mkdir(projectDirectory + '\\Videos')
            os.mkdir(projectDirectory + '\\Fotos')

            showDirectory = os.system('dir '+ projectDirectory)
            print (showDirectory)
            input("Press enter to continue")
    createDirectory()
main()