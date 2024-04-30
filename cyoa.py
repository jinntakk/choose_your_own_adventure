name = input("What's your name?: ")

print(f"Welcome! {name} Choose carefully.")

answer = input("You are walking along and come across a path dividing the road to the left and to the right.\
 Which way do you go?: ").lower()

if answer == 'left':
    answer = input("You keep walking and come across a bridge. Do you turn back or keep going?: (turn/keep going)").lower()

    if answer == 'turn':
        answer = input("You have come back to the cross road. Which way? (left/right): ")
    elif answer == 'keep going':
        print('You are swept up by a tornado and die. Goodbye.')
    else:
        print('lncorrect response. Goodbye.')

elif answer == 'right':
    answer = input('Oh no! an alligator in your way and it looks hungry! Do you pick up a stick and fight or run away? (fight/run away): ').lower()

    if answer == 'fight':
        print('You get eaten by the alligator. Game over.')
    elif answer == 'run away':
        print('You turn to run away but find out there are alligators behind you as well. They gang up on you and eat you. Game over.')
    else:
        print('lncorrect response. Goodbye.')
        
else:
    print('lncorrect response. Goodbye.')
    
