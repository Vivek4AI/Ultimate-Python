marks1 = int(input("Enter marks for sub1 : "))
marks2 = int(input("Enter marks for sub2 : "))
marks3 = int(input("Enter marks for sub3 : "))

total_percentage = (100*(marks1+marks2+marks3))/300

if(total_percentage>=40 and marks1>33 and marks2>33 and marks3>33):
    print(f"you are passed with {total_percentage} percent.")
else:
    print(f"OOPS ! you are failed with {total_percentage} percent.")
