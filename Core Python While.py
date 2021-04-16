while True:
    response = input(
        "put in integer that can be evenly divided by 7 to exit this loop: ")
    if int(response) % 7 == 0:
        print("here comes the break")
        break
    else:
        print("nope")
print()
print("yup")
