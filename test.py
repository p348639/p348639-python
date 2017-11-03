entry =  int(input("enter numbers:"))
print("entered value",entry)
while entry <5:
    if entry==0:
        print("entered value is 0") 
    elif entry==1: 
        entry=entry+1
    elif entry==2:
         entry=entry+2
         print("updated",entry) 
    else:
        entry=entry+1
        print("out of if and inside else",entry)
    
print("number after count", entry)

#else:
#    print(" else number entered is 0")
    
