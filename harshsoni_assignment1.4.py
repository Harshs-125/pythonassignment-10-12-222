#slicing from 2 position element to 5 position
def slice(*args):
    for i in args :
        print(i[1:5])
#output [2,3,4,5]

slice([1,2,3,4,5,6],[100,200,300,400,500,600],['a','b','c','d','e','f'])

#palindrome or not
def ispalindrome(*args):
    for str in args:
        str2=str[::-1]
        if str==str2:
            print("Yes it is palindrom")
        else:
            print("No it is not palindrom")


ispalindrome('naman','manan','harsh')

#check if string contains repeatative characters or not
def isrepeatative(*args):
    for str in args :
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

isrepeatative("harsh",'abc','ababa')