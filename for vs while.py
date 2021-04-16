import random
for count in range(1, 21):
    print("Down!")
    print("Up!")
    print(count, "!")
    print()


sarge_is_awake = True  # if set False loop will never run
count = 0

while sarge_is_awake:
    print("Down!")
    sarge_is_awake = False  # loop will continue 1 time, random only changes T to F
    print("Up!")
    # set variable back before end of loop to continue to "if" statement
    sarge_is_awake = True
    count += 1
    print(count, "!")
    print()

    if random.randrange(0, 100) == 0:
        print("random generator")
        sarge_is_awake = False


while not sarge_is_awake:
    print("Sarge Down! give him coffee!")
