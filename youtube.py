import os


def main():
    system_options = ['posix', 'nt']
    system_detect = os.name

    current_directory = os.path.dirname(__file__)

    project_name = input('[] Insert project name: ')

    def create_windows():
        try:
            project_directory = current_directory + '\\' + project_name
            print("[] Creating project directories: " + project_directory)
            os.mkdir(project_directory)
            os.mkdir(project_directory + '\\Audios')
            os.mkdir(project_directory + '\\Videos')
            os.mkdir(project_directory + '\\Photos')

            show_directory = os.system('dir ' + project_directory)
            print(show_directory)
            input("[] Press enter")
        except FileExistsError:
            print('[] Project already exists.')

    def create_linux():
        try:
            project_directory = current_directory + project_name
            print("[] Creating project directories: " + project_directory)
            os.mkdir(project_directory)
            os.mkdir(project_directory + '/' + 'Audios')
            os.mkdir(project_directory + '/' + 'Videos')
            os.mkdir(project_directory + '/' + 'Photos')

            show_directory = os.system('ls ' + project_directory)
            print(show_directory)
            input("[] Press enter")
        except FileExistsError:
            print('[] Project already exists.')

    if system_detect in str(system_options):
        if system_detect == 'posix':
            create_linux()
        if system_detect == 'nt':
            create_windows()


if __name__ == '__main__':
    main()
