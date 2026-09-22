students={}
while True:
    
    print("1.Add student")
    print("2.view students")
    print("3.search students")
    print("4.update students")
    
    choice=input("enter your choice:")
    if choice=='1':

        print("Add student")
        name=input("enter student name:")
        age=int(input("enter age:"))
        roll_no=int(input("enter roll_no:"))
        email=input("enter email:")
        
        
    
        chem_marks=input("enter chemistry marks:")
        eng_marks=input("enter english marks:")
        
        math_marks=input("enter mathematics marks:")
        std_name=name.capitalize()
        print("student_name:",std_name)
        age=int(age)
        chem_marks=int(chem_marks)
        eng_marks=int(eng_marks)
        math_marks=int(math_marks)
        if email.endswith("@gmail.com"):
            print("yes")
        else:
            print("no")
            
            student={
                'std_name':std_name,
                'age':age,
                'roll_no':roll_no,
                'email':email,
                'chem_marks':chem_marks,
                'eng_marks':eng_marks,
                'math_marks':math_marks
        }
        students[roll_no]=student
            


    elif choice=='2':
        print("view students")
    
        print(students.keys())
        print(students.values())
        print(students.items())
    elif choice=='3':
        print("search students")
        search_roll=int(input("enter roll no:"))
        record=students.get(search_roll)
        if record:
            print(record)
        else:
            print("not found")
    elif choice=='4':
        print("update students")
        update_roll=int(input("enter update roll no:"))
        
        if update_roll in students:
            new_age=int(input("enter update age:"))
            new_name=input("enter update name:")
            new_email=input("enter update email:")
            new_chem=int(input("enter update chemistry marks:"))
            new_math=int(input("enter update chemistry marks:"))
            new_eng=int(input("enter update chemistry marks:"))
            students[update_roll].update({"age":new_age})
            students[update_roll].update({"std_name":new_name})
            students[update_roll].update({"email":new_email})
            students[update_roll].update({"chem_marks":new_chem})
            students[update_roll].update({"eng_marks":new_eng})
            students[update_roll].update({"math_marks":new_math})
            print(students[update_roll])
    elif choice=='5':
        print("student result")
        
        select_std=int(input("enter selected student roll no:"))
        if select_std in students:
            #tot_marks=int(input("enter total marks:"))
            c_marks=students[select_std]['chem_marks']
            e_marks=students[select_std]['eng_marks']
            m_marks=students[select_std]['math_marks']
            total_marks=c_marks+e_marks+m_marks
            percentage=total_marks/300*100
            print("total marks of selected student",total_marks)
            print("percetange of total marks:",percentage)
            if percentage >=90 :
                print("grade A+")
                print("pass")
            elif percentage >=80 :
                print("grade A")
                print("pass")
            elif percentage >=70 :
                print("grade B ")
                print("pass")
            elif percentage >=60 :
                print("grade C ")
                print("pass")
            else:
                print("failll")
    elif choice=='6':
        print("analyze marks")
        sel_student=int(input("enter roll no:"))
        if sel_student in students:

            c=students[sel_student]["chem_marks"]
            e=students[sel_student]["eng_marks"]
            m=students[sel_student]["math_marks"]
        marks_list=[c,e,m]
        
        
        print(marks_list)
        marks_list.sort()
        print("in ascending order:",marks_list)
        
        print("lowest marks",marks_list[0])
        print("highest marks",marks_list[-1])
        print("first two marks",marks_list[0:2])
        print("last two marks",marks_list[-2:])
        print("reverse marks",marks_list[::-1])
        marks_list.sort(reverse=True)
        print("in descending order:",marks_list)
    elif choice=='7':
        print("student statistics")
        select_std=int(input("enter roll no:"))
        if select_std in students:
            marks_list=[
                students[select_std]["chem_marks"],
                students[select_std]["eng_marks"],
                students[select_std]["math_marks"]
            ]
            lowest=marks_list[0]
            greatest=marks_list[0]
            even_count=0
            odd_count=0
        
            for i in marks_list:
                if i%2!=0:
                    print("even marks:",i)
                    even_count+=1
                elif i%2==0:
                    print("odd marks:",i)
                    odd_count+=1
                if i%5==0:
                    print("divisible  by 5:",i)
                if i<lowest:
                    lowest=i
                elif i>greatest:
                    greatest=i
            print("lowest marks:",lowest)
            print("greatest marks:",greatest)
            print("total even count:",even_count)
            print("total odd count:",odd_count)
    elif choice=='8':
        print("subject analysis")

        sub_sets={
            "chem_marks",
            "eng_marks",
            "math_marks"
        }
        print(sub_sets)
        sub_sets.add("urdu_marks","information securtiy","information securtiy")
        print("after addition:",sub_sets)
        sub_sets.remove("urdu_marks")
        print("after remove:",sub_sets)
        sub_sets.pop()
        print("after pop:",sub_sets)
        sub_sets.union()
        print("after union:",sub_sets)
        sub_sets.intersection()
        print("after intersection:",sub_sets)
        sub_sets.clear()
        print("after clear:",sub_sets)
    elif choice=='9':
        print("number analysis")

    
        std_name=input("enter student name:")
        print("length of student name",len(std_name))
        print("first character:",std_name[0])
        print("last character:",std_name[-1])
        print("first 3 letter",std_name[0:3])
        print("last 3 characters:",std_name[-3:])
        print("no of a",std_name.count('a'))
        print("position of a",std_name.find('a'))
        
        std_name.replace(" ",'-')
        std_name=std_name.capitalize()
        print(std_name)
    elif choice=='11':
        print("tuple requirements")
        my_list=[chem_marks,eng_marks,math_marks]
        my_list=tuple(my_list)
        print(my_list)
        print("count the number",my_list.count(85))
        print("find the index",my_list.index(85))
    if choice=='10':
        print("string analysis requirement")
        num=int(input("enter a number"))
        def even_chk(num):
            if num%2==0:
                print("num is even",num)
            else:
                print("num is odd:",num)
                return num
        even_chk(num)
        def find_fact(num):
                fact=1
                for i in range(1,num+1):
                    fact=fact*i
                print("factorial:",fact)
                return fact
        find_fact(num)
        def palindrom_chk(num):
            original=str(num)
            reverse=original[::-1]
            if original==reverse:
                print("number is palindromic")
            else:
                print("number is not palindromic")
        palindrom_chk(num)


        

            


                
                    
                    

            

            



            
           
        

      
       
   

