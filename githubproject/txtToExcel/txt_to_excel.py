import xlwt

def toExcel(file):
    with open(file, 'r', encoding='utf-8') as f:
        data = f.read()
        data = eval(data)
        student = list()
        for k,v in data.items():
            student.append(int(k))
            student.extend(data[k])
        # print(type(data))
        # print(data)
        # print('=' * 200)
        # print(student)
    file = xlwt.Workbook()
    table = file.add_sheet('student')

    for i in range(len(student)):
        if not i % 5:
            horz_left(i // 5, i % 5, student[i], table)
        else:
            table.write(i // 5, i % 5, student[i])
    file.save('student.xls')

def horz_left(x, y, data, table):
    algnt = xlwt.Alignment()
    algnt.horz = xlwt.Alignment.HORZ_LEFT
    style = xlwt.XFStyle()
    style.alignment = algnt
    table.write(x, y, data, style)

if __name__ == '__main__':
    toExcel('student.txt')