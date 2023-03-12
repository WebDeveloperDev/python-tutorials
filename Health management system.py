print('Welcome to Health Management system')
k=True
while k==True:
    userin=int(input(' press 1 to lock/set\n press 2 to execute data \n'))
    if userin==1:
        userin1=int(input('Select the clint\n press 1. for Harry \n press 2. for Rohan\n press 3. for Hammad \n or press 0 to exit\n'))
        if userin1==1:
            userin2=int(input('Select what ever you want to set \n press 1 for diet \n press 2 for exercise\n'))
            if userin2==1:
                with open('dietH.txt', 'a') as f:
                    userin3=input('Write food name which you have eaten \n')
                    def getdate():
                        import datetime
                        return datetime.datetime.now()
                    value=f"{userin3} :  {str(getdate())} \n"
                    f.write(value)
            elif userin2==2:
                with open('exerciseH.txt', 'a') as f:
                    userin3=input('Write exercise name which you have done \n')
                    def getdate():
                        import datetime
                        return datetime.datetime.now()


                    value = f"{userin3} :  {str(getdate())} \n"
                    f.write(value)
            else:
                print('no result')
        if userin1==2:
            userin2=int(input('Select what ever you want to set \n press 1 for diet \n press 2 for exercise\n'))
            if userin2==1:
                with open('dietR.txt', 'a') as f:
                    userin3=input('Write food name which you have eaten \n')
                    def getdate():
                        import datetime
                        return datetime.datetime.now()


                    value = f"{userin3} :  {str(getdate())} \n"
                    f.write(value)
            elif userin2==2:
                with open('exerciseR.txt', 'a') as f:
                    userin3=input('Write exercise name which you have done \n')
                    def getdate():
                        import datetime
                        return datetime.datetime.now()


                    value = f"{userin3} :  {str(getdate())} \n"
                    f.write(value)
            else:
                print('no result')
        if userin1 == 3:
            userin2 = int(input('Select what ever you want to set \n press 1 for diet \n press 2 for exercise\n'))
            if userin2 == 1:
                with open('dietHu.txt', 'a') as f:
                    userin3 = input('Write food name which you have eaten \n')
                    def getdate():
                        import datetime
                        return datetime.datetime.now()


                    value = f"{userin3} :  {str(getdate())} \n"
                    f.write(value)
            elif userin2 == 2:
                with open('exerciseHu.txt', 'a') as f:
                    userin3 = input('Write exercise name which you have done \n')
                    def getdate():
                        import datetime
                        return datetime.datetime.now()


                    value = f"{userin3} :  {str(getdate())} \n"
                    f.write(value)
            else:
                print('no result')
    elif userin==2:
        userin1 = int(input('Select the clint\n press 1. for Harry \n press 2. for Rohan\n press 3. for Hammad \n or press 0 to exit\n'))
        if userin1 == 1:
            userin2 = int(input('Select what you want to see \n press 1 for diet \n press 2 for exercise\n'))
            if userin2 == 1:
                with open('dietH.txt') as f:
                    print(f.read())
            elif userin2 == 2:
                with open('exerciseH.txt') as f:
                    print(f.read())
            else:
                print('no result')
        if userin1 == 2:
            userin2 = int(input('Select what  you want to see \n press 1 for diet \n press 2 for exercise\n'))
            if userin2 == 1:
                with open('dietR.txt') as f:
                    print(f.read())
            elif userin2 == 2:
                with open('exerciseR.txt') as f:
                    print(f.read())
            else:
                print('no result')
        if userin1 == 3:
            userin2 = int(input('Select what  you want to see \n press 1 for diet \n press 2 for exercise\n'))
            if userin2 == 1:
                with open('dietHu.txt') as f:
                    print(f.read())
            elif userin2 == 2:
                with open('exerciseHu.txt') as f:
                    print(f.read())
            else:
                print('no result')

    else:
        k=False