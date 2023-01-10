
#check if string contains repeatative characters or not

str=input()
check=0
for i in str:
    count=str.count(i)
    if(count>1):
        check=1
        break
if(check==1):
    print("yes it contains repeated characters")
else:
    print("no it do not contains repeated characters") 