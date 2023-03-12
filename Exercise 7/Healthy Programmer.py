import time

print('Welcome to Healthy Programmer system')
def water():
    import datetime
    now=datetime.datetime.now()
    localtime=now.hour
    if localtime in range (9,24):
        print('its now')
        k=0
        while k<18:
            print('drink some water')
            userinp=input('Have you drank water?\n if yes write drank\n')
            print(time.localtime())
            with open("ExerciseR.txt", "a") as f:
                f.write(f"{userinp}  {now.hour} :{now.minute} :{now.second}\n")
            from playsound import playsound
            playsound('Pouring-water-into-a-glass-water-cooler.mp3')
            time.sleep(1800)
            k+=1
water()
print('this is imp')
