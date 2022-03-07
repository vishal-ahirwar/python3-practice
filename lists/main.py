

print("welcome to the game of state -state")
states_of_india =[]
while True:
    user =input("type a(to append a state), s(to print all the states you have entered, q(quit the program))")
    if user.lower()=='q':
        print("okay")
        break
    elif user.lower()=='a':
        name=input("the name of states : ")
        states_of_india.append(name)
    else:
        total_states =len(states_of_india)
        i=0
        while i<total_states:
            print(states_of_india[i*-1])
            i+=1


