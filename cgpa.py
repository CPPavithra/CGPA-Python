# importing modules
from pywebio.input import *
from pywebio.output import *
from pywebio.session import run_js
 
def writefile(info):
    f = open("student.dat", "a")
    cgpa = (3 * int(info['maths']) + 2 * int(info['english']) + 4 * int(info['eee']) + 5 * int(info['semi']) + 6 * int(info['pps'])) / 20;
    s1 = str(cgpa)+"-"+info['name']+"-"+info['maths']+'-'+info['pps']+'-'+info['eee']+'-'+info['semi']+'-'+info['english']+'\n';
    f.write(s1)
    f.close()
    
def searchfile(info):
        f1 = open('student.dat', 'r')
        Lines = f1.readlines()
 
        count = 0
        # Strips the newline ch(aracter
        for line in Lines:
            x = line.split("-")
            if x[1] == info['name']:
                put_table([
                ['Name', 'Maths','PPS','EEE','Physics','English','CGPA'],
                [x[1], x[2],x[3],x[4],x[5],x[6],x[0]]
                ])
                count+=1
        if count == 0:
            img = open('fileempty.png', 'rb').read()  
            put_image(img, width='50px')
            
def searchcgpa(info):
        f1 = open('student.dat', 'r')
        Lines = f1.readlines()
 
        count = 0
        # Strips the newline character
        for line in Lines:
            x = line.split("-")
            if x[0] > info['cgpa']:
                put_table([
                ['Name', 'Maths','PPS','EEE','Physics','English','CGPA'],
                [x[1], x[2],x[3],x[4],x[5],x[6],x[0]]
                ])

def sort():
     with open('student.dat', 'r') as r:
         for line in sorted(r,reverse=True):
            x = line.split("-")
            put_table([
                ['Name', 'Maths','PPS','EEE','Physics','English','CGPA'],
                [x[1], x[2],x[3],x[4],x[5],x[6],x[0]]
   ])


while True:
  with use_scope('scope3'):
    clear('scope3');
    put_row(put_code("STUDENT CGPA CALCULATION SYSTEM"))

    put_text("1 -> Enter students marks")
    put_text("2 -> Display all students")
    put_text("3 -> Arrange students")
    put_text("4 -> Extract Student CGPA")
    put_text("5 -> Search for CGPA with condition")
    put_text("6 -> Exit")
    p = int(input("What is your choice"))

    if p == 1:
        info = input_group("Student Marks",[
        input('Please enter students name', name='name'),
        input('Please enter Maths marks', name='maths'),
        input('Please enter PPS marks', name='pps'),
        input('Please enter EEE marks', name='eee'),
        input('Please enter Semiconductor marks', name='semi'),
        input('Please enter English marks', name='english'),
        

    ], validate=writefile)



    if p == 2:
        f = open("student.dat", "r")
        count=0
        for line in f:
            x = line.split("-")
            count+=1
            put_table([
            ['Name', 'Maths','PPS','EEE','Physics','English','CGPA'],
            [x[1], x[2],x[3],x[4],x[5],x[6],x[0]]
             ])
        if count == 0:
            img = open('fileempty.png', 'rb').read()  
            put_image(img, width='50px')

    if p == 3:
        sort();    

    if p == 4:
        info = input_group("Student Marks",[
        input('Please enter student name', name='name'),
    ], validate=searchfile)


    if p == 5:
        info = input_group("Student Marks",[
        input('Please enter CGPA', name='cgpa'),
    ], validate=searchcgpa)

    if actions("Continue?",["continue", "exit"])=="exit":
        break


