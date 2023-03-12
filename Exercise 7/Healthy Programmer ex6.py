from pygame import mixer
from datetime import datetime
from time import time
def musiconloop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stopper:
            mixer.music.stop()
            break
def log_now(msg):
    with open('ExerciseR.txt' ,"a") as f:
        f.write(f"{msg} {datetime.now()}\n")
if __name__ == '__main__':
    # musiconloop('water.mp3',"stop")
    init_water=time()
    init_eyes=time()
    init_exercise=time()
    # watersecs=60*45
    # exercise=60*60
    # eyesec=60*20
    watersecs=10
    exercise=25
    eyesec=32
    while True:
        if time()-init_water>watersecs:
            print('Time to drink some water enter "drank" to stop the alarm')
            musiconloop('water.mp3',"drank")
            init_water=time()
            log_now('Drank water at ')
        elif time()-init_exercise>exercise:
            print('Time to do some exercise enter "exdone" to stop the alarm')
            musiconloop('workout.mp3',"exdone")
            init_exercise = time()
            log_now('Exercise at ')
        elif time() - init_eyes > eyesec:
            print('Give some rest to your eyes enter "eydone" to stop the alarm')
            musiconloop('eyerelax.mp3', "eydone")
            init_eyes = time()
            log_now('rest for eyes at ')
