game_data = {
   'easy': {
        'quiz': 'Psalms 119:1 ___1___ are ___2___ of ___3___ who follow the ___4___ of the ___5___',
        'answers': ['Joyful', 'people', 'integrity', 'instructions', 'Lord']
    },
   'medium': {
        'quiz': 'Psalms 119:2 ___1___ are those who ___2___ his ___3___ and ___4___ for Him with all their ___5___',
        'answers': ['Joyful', 'obey', 'laws', 'search', 'hearts']
    },
   'hard': {
        'quiz': 'Psalms 119:3 ___1___ do not ___2___ with ___3___ and ___4___ only in His ___5___',
        'answers': ['They', 'compromise', 'evil', 'walk', 'paths']
    }
}


current_blanks = ["___1___","___2___","___3___","___4___","___5___"]

difficulty_levels = ['easy', 'medium', 'hard']

#this function verifies that the selection(user_selected_level) is in fact an available option from the list "difficulty_levels"
def selection_in_difficulty_levels(selection, difficulty_levels):
    for level in difficulty_levels:
        if level in selection:
            return level
    return -1
#this function verifies if a word (string pieces separated by spaces from the "current quiz") is in fact an item from the list "current_blanks"
#def gap_number_in_current_blanks(blank_number, current_blanks):
def is_gap_number_in_current_blanks(blank, current_blanks):
    for gap_number in current_blanks:
        if gap_number in blank:
            return gap_number
    return None



def index_of_answer_in_answers(guess,current_blanks,user_input, current_answers):
    for index, answer in enumerate(current_answers):
        if answer == user_input:
            return index
        else:
            for index, gap in enumerate(current_blanks):
                if gap == guess:
                    return index


#this function outputs the correct response based on the number of times the user's guess has been incorrect
def incorrect_guess(tries,blank_number,selected_string):
    if tries > 1:
        print "\nThat isn't the correct answer!  Let's try again; you have "+ str(tries) + " tries left!"
        print "\nThe current paragraph reads as such:\n"
        print selected_string
    else:
        if tries ==1:
            print "That isn't the correct answer!  You only have "+ str(tries) + " try left!  Make it count!"
            print "The current paragraph reads as such:\n"
            if blank_number == 0:
                print selected_string
        else:
            if tries == 0:
                print "You've failed too many straight guesses!  Game over!"
    return tries
#this funciton provides choices of difficulty_levels, collects the correct user_selected_level,
#assigns the corresponding set of values to the main variables (selected_string, current_quiz and current_answers)
#and summons the play_game function
def user_choice():
    selection = []
    selected_string = ''
    user_prompt = """Please select a game difficulty by typing it in!
Possible choices include easy, medium, and hard.\n"""
    user_selected_level = raw_input (user_prompt).lower()
    while user_selected_level not in difficulty_levels:
        print "That's not an option!\n"
        user_selected_level = raw_input (user_prompt).lower()
    selection = selection_in_difficulty_levels(user_selected_level,difficulty_levels)
    print "You have chosen: " + user_selected_level + """!\nYou will get 5 guesses per problem\n
The current paragraph reads as such:\n"""
    return (game_data[user_selected_level]['quiz'], game_data[user_selected_level]['answers'])

def run_game():
    current_quiz, current_answers = user_choice()
    selected_string = current_quiz
    play_game(selected_string, current_quiz, current_answers)

#based on the user_choice function outputs, manage correct and incorrect guesses and providing immediate feedback (quiz updates),
#and allowing a max of 5 mistakes (tries)

def play_game(selected_string, current_quiz,  current_answers):
    print selected_string
    tries = 5
    
    for blank in current_blanks:
        guess = is_gap_number_in_current_blanks("___"+str(blank_number+1)+"___", current_blanks)
        if guess != None:
            print guess
            user_input = raw_input("what should be substituted in for " + guess + "? ")
            blank_number = index_of_answer_in_answers(guess,current_blanks,user_input,current_answers)

            while blank_number != None and tries != 0:
                if user_input == current_answers[blank_number]:
                    print selected_string.replace(("___"+str(blank_number+1)+"___"),current_answers[blank_number])

                    blank_number = blank_number + 1
                    user_input = raw_input("what should be substituted in for " + "___"+str(blank_number+1)+"___" + "? ")
                else:
                    tries = tries - 1
                    incorrect_guess(tries, blank_number,selected_string)
                    if tries == 0:
                        return None
    return current_quiz

run_game()
