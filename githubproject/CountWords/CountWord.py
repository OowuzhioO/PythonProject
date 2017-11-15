import re

def countWord(file):
    # f = open(file, 'r').read()
    with open(file, 'r') as f:
        # f = f.read()
        print(f)
        # f = re.findall(r'[\w\-\_\.\']+', f)
        # print(len(f))





if __name__ == '__main__':
    file = 'subtitle.txt'
    countWord(file)