import os

destination_files = dict()
comment_line = 0
blank_line = 0
code_line = 0


def processFiles(path):
    global destination_files

    files = os.listdir(path)
    for file in files:
        if file.endswith('.py'):
            filepath = os.path.join(path, file)
            destination_files[file] = filepath
    print(destination_files)


def anaylysizeFiles(files):
    global comment_line
    global blank_line
    global code_line
    for filename,file in files.items():
        with open(file, 'r') as pyfile:
            lines = pyfile.readlines()
            for line in lines:
                line = line.strip()
                if not line:
                    blank_line += 1
                elif line.startswith('#'):
                    comment_line += 1
                else:
                    code_line += 1
    print('code line: ', code_line)
    print('comment line: ', comment_line)
    print('blank line: ', blank_line)



processFiles('/Applications/python/PythonProject/githubproject/ AnalysizeFile')
anaylysizeFiles(destination_files)