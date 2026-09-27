## Creating a CGPA calulator for VIT'ans
print("Welcome to VIT'ian CGPA CALCULATOR\n")
print("Let's now calcuate the first semester's GPA\n")
def GPA_Calculator():
    Total_credits=int(input("Enter the Total credits for the current semester :"))
    Number_of_courses=int(input("Enter the total number of course for the current semester :"))
    print("Now Enter the required details of the courses completed to calculate the GPA of the semester")
    list_courses=[]
    list_grades=[]
    GPA=0
    for i in range(0,Number_of_courses):
        print()
        Type_of_course=int(input("Enter 1 if the course is a Theory course(LTP/LT) else if the course is a Laboratory/Projcet(PJ) based enter 2 :\n"))
        Course_credit=int(input("Enter the course credits :"))
        if(Type_of_course==1):
            CAT1=float(input("Enter your cat1 marks of this course out of 50 :"))
            CAT2=float(input("enter your cat2 marks of this course out of 50 :"))
            TEE=float(input("Enter your Term-end marks of this course out of 100 :"))
            Internals=float(input("Enter your internal marks out of 40:"))
            Attendance_percentage=float(input("Enter your attendance percentage :"))
            Class_avg=float(input("Enter your class Average out of 100:"))
            SD=float(input("Enter the standard devaition of the class :"))
            if(CAT1 <= 50 and CAT2 <= 50 and TEE <= 100 and Internals <= 40 and Attendance_percentage <= 100 and Class_avg <= 100):
                #Calculation TEE and CAT marks according to their weightage
                CAT1=(CAT1/50)*15
                CAT2=(CAT2/50)*15
                TEE=(TEE/100)*30
                #Caculation of Attendance marks
                if(Attendance_percentage>=96):
                    Attendance_marks=5
                elif(Attendance_percentage>=91 and Attendance_percentage<=95):
                    Attendance_marks=4
                elif(Attendance_percentage>=86 and Attendance_percentage<=90):
                    Attendance_marks=3
                elif(Attendance_percentage>=81 and Attendance_percentage<=85):
                    Attendance_marks=2
                elif(Attendance_percentage>=75 and Attendance_percentage<=80):
                    Attendance_marks=1
                else:
                    Attendance_marks=0
                Total_marks=CAT1+CAT2+TEE+Internals+Attendance_marks
                #Calculation of grade
                if(Attendance_marks==0):
                    Grade="F"
                    Grade_points=0
                else:
                    if(Total_marks>(Class_avg+(1.50*SD))):
                        Grade="S"
                        Grade_points=10
                    elif(Total_marks>(Class_avg+(0.50*SD)) and (Total_marks<=(Class_avg+(1.50*SD)))):
                        Grade="A"
                        Grade_points=9
                    elif(Total_marks>(Class_avg-(0.50*SD)) and (Total_marks<=(Class_avg+(0.50*SD)))):
                        Grade="B"
                        Grade_points=8
                    elif(Total_marks>(Class_avg-(1.0*SD)) and (Total_marks<=(Class_avg-(0.50*SD)))):
                        Grade="C"
                        Grade_points=7
                    elif(Total_marks>(Class_avg-(1.50*SD)) and (Total_marks<=(Class_avg-(1.0*SD)))):
                        Grade="D"
                        Grade_points=6
                    elif(Total_marks>(Class_avg-(2.0*SD)) and (Total_marks<=(Class_avg-(1.50*SD)))):
                        Grade="E"
                        Grade_points=5
                    else:
                        Grade="F"
                        Grade_points=0
                list_courses+=[Course_credit,Grade,Grade_points]
            else:
                print("Invalid Input, Enter the input with great care!")
                break
        else:
            TEE=float(input("Enter your Term-end marks of this course out of 100 :"))
            Internals=float(input("Enter your internal marks out of 10:"))
            Lab_assignment=float(input("Enter your Lab assignemnt marks out of 60 :"))
            TEE=(TEE/100)*30
            Total_marks=TEE+Internals+Lab_assignment
            if(TEE <= 100 and Internals<=10 and Lab_assignment<=60):
                if(Total_marks>90):
                    Grade="S"
                    Grade_points=10
                if(Total_marks>80 and Total_marks<=90):
                    Grade="A"
                    Grade_points=9
                if(Total_marks>70 and Total_marks<=80):
                    Grade="B"
                    Grade_points=8
                if(Total_marks>60 and Total_marks<=70):
                    Grade="C"
                    Grade_points=7
                if(Total_marks>50 and Total_marks<=60):
                    Grade="D"
                    Grade_points=6
                if(Total_marks>40 and Total_marks<=50):
                    Grade="E"
                    Grade_points=5
                else:
                    Grade="F"
                    Grade_points=0
                list_courses+=[Course_credit,Grade,Grade_points]
            else:
                print("The inputs are invalid, please enter the inputs correctly again")
                break
    print("The course credits along with their Grade and Grade points are displayed below\n")
    print(list_courses)
    
    #Calculation of the semester's GPA
    for i in range (0,len(list_courses),+3):
        GPA=GPA+((list_courses[i]*list_courses[i+2])/Total_credits)
        GPA=round(GPA, 2)
    print("The GPA of the current semester is :",GPA,"\n")
    return GPA,Total_credits
list_GPA=[]
list_Total_credits=[]
Total_credits_completed=0
for i in range(0,8):
    Choice=int(input("Enter 1 to calculate the Semester's GPA and CGPA, Enter 2 to exit :\n"))
    if(Choice==1):
        CGPA_=0
        CGPA=0
        GPA_,Total_Credits=GPA_Calculator()
        list_GPA.append(GPA_)
        list_Total_credits.append(Total_Credits)
        Total_credits_completed=Total_credits_completed+Total_Credits
        for i in range(0,len(list_GPA)):
            CGPA_=CGPA_+(list_GPA[i]*list_Total_credits[i])
        CGPA=CGPA_/Total_credits_completed
        CGPA=round(CGPA, 2)
        if(CGPA>10.0):
            print("You have made a mistake in entering the inputs please do enter the inputs with care!")
            break
        else:
            print("Your CGPA is :",CGPA)
    else:
        print("Thank you for using VIT'ian CGPA Calculator")
        break
