# -*- coding: utf-8 -*-

class Internal:
    def assignment(self):
        a=int(input("Enter assignment-1 marks(out of 10): "))
        b=int(input("Enter assignment-2 marks(out of 10): "))
        if 0<=a<=10 and 0<=b<=10:
            return(a+b)/2
        else:
            print("Please enter assignment marks correctly")
            return None
    def mid(self):
        a=int(input("Enter mid-1 marks(out of 35): "))
        b=int(input("Enter mid-2 marks(out of 35): "))
        if 0<=a<=35 and 0<=b<=35:
            maximum=max(a,b)
            minimum=min(a,b)
            maximum=maximum*0.75
            minimum=minimum*0.25
            mid_max_marks=maximum*(20.0/35)
            mid_min_marks=minimum*(20.0/35)
            return mid_max_marks+mid_min_marks
        else:
            print("Please enter mid marks correctly")
            return None

n=int(input("Enter how many no.of subjects do you want to calculate internals for: "))
for i in range(1,n+1):
    print(f"\nSubject {i}:")
    marks=Internal()
    assignment_marks=marks.assignment()
    mid_marks=marks.mid()
    if assignment_marks is not None and mid_marks is not None:
        print("Your internal marks for subject {} is {}: ".format(i,round(assignment_marks+mid_marks,2)))
    else:
        print("Invalid marks entered ,skipping subject {}".format(i))
    print()

    
    