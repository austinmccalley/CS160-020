'''
Austin McCalley
CS 160-020

Problem:
The local middle school would like some text adventure games to keep their students occupied during down time. The school is leaving it up to your skill and good judgement to develop a game. You need to have five different endings, but other than the requirement, you are free to do  whatever else you want.


Understanding the Problem:
The problem is asking to create a game which takes input from the user and itterate through if/else statements to get to a desired output. The requirements for the game our to create a text based adventure game with multiple outcomes which depends on what the user inputs into the game/program.


'''

def checkInput():
    curr_input = input('\nWhat is your next move(Right, Left, Forward, Backwards)? \n')
    # Prints the current user input
    # print(curr_input)
    return curr_input


if __name__ == '__main__':
    print('Welcome to Austin McCalley\'s text based adventure game....')
    print('\n\nYou find yourself in lost on the beautiful campus of Oregon State University but you do not know where to go. You look down at your watch and realize class starts in six minutes and you need to find you way to class. You are at a cross road with four posibilities to go to find your next class.')

    curr_user_input = checkInput()


    # Level 1
    if curr_user_input == 'Left':
        # Go left
        print('You find yourself in the middle of the Memorial Union Quad with students pushing you out of the way to get to class on time. You were pushed to the ground and you lost your map. Now you have to go blind throughout the campus. You have five minutes left until class starts.')

        # Redfine the current user input
        curr_user_input = checkInput()

        # Level 2
        if curr_user_input == 'Left':
            # Go Left
            print('You find yourself inside of the Memorial Union Quad asleep on the couches with two minutes until your class starts. Probably in the better interest to just miss class and sleep it off.')

            # Redfine the current user input
            curr_user_input = checkInput()

        elif curr_user_input == 'Right':
            # Go Right
            print('You found your way to the Valley Library and you get lost in a good book about the early adaptations of the tree frog. Luckily you get an email on your phone saying that class has been delayed by 15 minutes so you have time to finish your chapter. You have 10 minutes until class starts now.')

        elif curr_user_input == 'Forward':
            # Go Forward
            print('You found yourself in the middle of Goss Stadium on the pitchers mound staring down someone who oddly looks like your cousin. You have 5 minutes until class starts now')

        elif curr_user_input == 'Backwards':
            # Go Backwards
            print('You find yourself in the wrong class where people are studying the aboriginal\'s of Australia and their economy.')




    elif curr_user_input == 'Right':
        # Go right
        pass
    elif curr_user_input  == 'Forward':
        # Go forward
        pass
    elif curr_user_input == 'Backwards':
        # Go backwards
        pass
    else:
        print('Please provide a correct input.')
