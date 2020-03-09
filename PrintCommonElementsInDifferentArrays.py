def check(a,b,c):
    a=a
    b=b
    c=c
    for x in range(len(a)):
        for y in range(len(b)):
            if(a[x]==b[y]):
                for z in range(len(c)):
                    if(b[y]==c[z]):
                        print("The number ",c[z]," is common in all the above arrays")
def main():
    a=input("Enter the elements of the first array").split()
    b=input("Enter the elements of the second array").split()
    c=input("Enter the elements of the third array").split()
    check(a,b,c)
main()