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
    inputs = ['Left','Right','Forward','Backwards']
    if curr_input in inputs:
        return curr_input
    else:
        print('Please try again')
        return checkInput()
   
    return curr_input


if __name__ == '__main__':
    print('Welcome to Austin McCalley\'s text based adventure game....')
    print('\n\nYou find yourself in lost on the beautiful campus of Oregon State University but you do not know where to go. You look down at your watch and realize class starts in six minutes and you need to find you way to class. You are at a cross road with four posibilities to go to find your next class.')

    curr_user_input = checkInput()


    # NOTE: Level 1
    if curr_user_input == 'Left':
        # Go left
        print('You find yourself in the middle of the Memorial Union Quad with students pushing you out of the way to get to class on time. You were pushed to the ground and you lost your map. Now you have to go blind throughout the campus. You have five minutes left until class starts.')

        # Redfine the current user input
        curr_user_input = checkInput()

        # NOTE: Level 2
        if curr_user_input == 'Left':
            # Go Left
            print('You find yourself inside of the Memorial Union asleep on the couches with two minutes until your class starts. Probably in the better interest to just miss class and sleep it off.')

            # Redfine the current user input
            curr_user_input = checkInput()
                # NOTE: Level 3
            if curr_user_input == 'Left':
                # Go Left
                print('You fall asleep on one of the couches to your left and sleep through your class. Maybe tomorrow\'s class will be easier to find')
                # END

            elif curr_user_input == 'Right':
                # Go Right
                print('You stumble into a random class and find yourself in a macroeconomics class. You decide that this is the "correct" class for you to be in.')
                # END

            elif curr_user_input == 'Forward':
                # Go Forward
                print('Benny the Beaver comes out of no where and he brings you to the edge of the Memorial Union and starts repeating the Lion King speech, explaniing how everything the light touches is yours.')
                # END

            elif curr_user_input == 'Backwards':
                # Go Backwards
                print('You sprint across campus and stumble in to class with 15 seconds to spare. You find your seat and wonder what other possibilities could be out there.')
                # END

        # NOTE: Level 2
        elif curr_user_input == 'Right':
            # Go Right
            print('You found your way to the Valley Library and you get lost in a good book about the early adaptations of the tree frog. Luckily you get an email on your phone saying that class has been delayed by 15 minutes so you have time to finish your chapter. You have 10 minutes until class starts now.')

            # Redfine the current user input
            curr_user_input = checkInput()

            # NOTE: Level 3
            if curr_user_input == 'Left':
                # Go Left
                print('With your new found knowledge of tree frogs you grow the same adaptations of tree frogs and are able to bound around campus to find your class.')
                # END

            elif curr_user_input == 'Right':
                # Go Right
                print('Suddenly you are in a mood craving a insect salad. You find yourself in the biology lab and asking to "borrow" some of their insects to use as a meal. You end up sitting on the floor, eating insects and not going to class.')
                # END

            elif curr_user_input == 'Forward':
                # Go Forward
                print('You get lost in your thoughts and find yourself in a rain forest imagining you are a tree frog bouncing from leaf to leaf with the tropical rain pouring down on yourself.')
                # END

            elif curr_user_input == 'Backwards':
                # Go Backwards
                print('You decide to take those extra minutes of reading and suddenly wake up at 3:00am with books about tree frogs sorrounding you.')
                # END


        elif curr_user_input == 'Forward':
            # Go Forward
            print('You found yourself in the middle of Goss Stadium on the pitchers mound staring down someone who oddly looks like your cousin. You have 5 minutes until class starts now')

            # Redfine the current user input
            curr_user_input = checkInput()

            # NOTE: Level 3
            if curr_user_input == 'Left':
                # Go Left
                print('The person that weirdly looks like your cousin beckins you to through the ball that is your hand. You throw it and suddenly chearing errupts around you and you glance around and you just helped the Beaver Baseball team win another national championship with a no hitter final game.')
                # END

            elif curr_user_input == 'Right':
                # Go Right
                print('You run to your right and find yourself stuck in the middle of Resser Stadium calling the next play for the football team. The ball is snapped to your hand and you catapult it down the field into the hands of a wide receiver for another touchdown.')
                # END

            elif curr_user_input == 'Forward':
                # Go Forward
                print('You throw the ball at the weird cousin down the field and he hits the ball right back at your head knocking you out. You wake up 8 months later in the hospital, you hope that they refunded your tution for that term.')
                # END

            elif curr_user_input == 'Backwards':
                # Go Backwards
                print('You throw the ball at the person and the snap of the bat wakes you up and your asleep in a biology class, luckily its the correct class.')
                # END

        elif curr_user_input == 'Backwards':
            # Go Backwards
            print('You find yourself in the wrong class where people are studying the aboriginal\'s of Australia and their economy. You trip over a chair and hit your head where you wake up back in your bed. Might as well just sleep until your next class.')
            #END

    elif curr_user_input == 'Right':
        # Go right
        print('You find the correct class which you belong in. You find a seat and listen to the amazing lecture on the whales living in the northern artic circle.')
        #END

    elif curr_user_input  == 'Forward':
        # Go forward
        print('You stumble into a class studying the effects of human physcology during adolescent years. It isn\'t quite the class you were looking for but it reminds you of your sisters major so you stay.')
        #END

    elif curr_user_input == 'Backwards':
        # Go backwards
        print('You trip backwards of a root and fall into the arms of Benny the Beaver, your knight in shinning armour. He takes you by the hand and guides you to your class where you are able to get there on time.')
        #END

