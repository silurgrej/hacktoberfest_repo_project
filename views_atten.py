
from django.shortcuts import redirect, render
import os
import csv
from .models import FilesUpload
from pathlib import Path
# Create your views here.

filepath = os.getcwd()


def home(request):
    file, Error = checkattendance(attendance(), reference())

    return render(request, 'home.html', {'final': file, 'error': Error})


def FileUpload(request):
    try:
        if request.method == "POST":
            file2 = request.FILES["reference"]
            file3 = request.FILES["attendance"]
            document = FilesUpload.objects.create(file=file2)
            document = FilesUpload.objects.create(file=file3)
            return redirect(home)
    except:
        return render(request, "upload.html", {"error": 'Please upload both the files'})
    return render(request, "upload.html")


def fileread():
    filepath = os.getcwd()
    attend = open(filepath + '/media/attendance.txt', 'r')
    lines = attend.readlines()

    return lines


def attendance():
    lines = fileread()
    main = []
    for line in lines:

        if lines.index(line) % 2 != 0:
            line = line.lower()
            student = line.replace('present', '').replace(
                '-', "").replace(' ', "")
            main.append(student)
        else:
            line = line.upper()
            name = line.replace(line[-9:-1], '')
            if name == 'Satwik Vankayalapati\n'.upper():
                name = 'VANKAYALAPATI SAI VENKATA SATWIK\n'
            main.append(name)
    return main



def reference():
    all = open(filepath + '/media/reference.csv', 'r')
    csvreader = csv.reader(all)
    rows = []
    for row in csvreader:
        rows.append(row)
    del rows[0]
    # print(rows)
    return rows


def checkattendance(attendance, rowsMain):
    for student in rowsMain:
        for all in attendance:
            if student[1] + '\n' == all and attendance[attendance.index(all)-1] == student[2] + '\n':
                student[3] = '1'
                break
            else:
                student[3] = '0'
    try:
        filepath = str(Path.home() / "Downloads")
        f = open(filepath + R"\final-attendance.csv", "x")
        with open(filepath + R'\final-attendance.csv', 'w') as f:
            write = csv.writer(f)
            write.writerows(rowsMain)
        return filepath, '1'
    except FileExistsError:
        return filepath, '0'

