f = open("abcd.text","a")
f.truncate(0)
f.write("NAME AGE PHONE_NUMBER EMAIL_ID\n")

condition =True
while condition:
    student_info = input("Enter the INFO of Student :")
    student_lst = student_info.split(" ")
    print("\nEntered student INFO is -\nName:{}\nAge:{}\nPhone_Number:{}\nEmail_ID:{}".format(student_lst[0],student_lst[1],student_lst[2],student_lst[3]))
    re_enter_info=input("Check the entered info, if it was wrong : press w, else : c ")
    if re_enter_info=="w":
        student_info = input("Re-Enter the INFO of Student :")
        student_lst = student_info.split(" ")
        f.write(student_info + "\n")
        print("\nEntered student INFO is -\nName:{}\nAge:{}\nPhone_Number:{}\nEmail_ID:{}".format(student_lst[0],student_lst[1],student_lst[2],student_lst[3]))
    else :
        f.write(student_info+ "\n")
    condition_check=input("Type (yes/no) , to enter another student_info :")
    if condition_check == "yes":
        condition=True
    else:
        condition=False
f.close()
