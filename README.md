



def play_game(selected_string, current_quiz,  current_answers):
    replaced = []
    print selected_string
    tries = 5
    current_quiz = current_quiz.split()
    for word in current_quiz:
        guess = is_word_a_blank_in_current_blanks(word, current_blanks)
        print word
        print guess
        if guess != None:
            user_input = raw_input("what should be substituted in for " + guess + "? ")
            blank_number = index_of_answer_in_answers(guess,current_blanks,user_input,current_answers)
            while user_input != current_answers[blank_number]:
                tries = tries - 1
                incorrect_guess(tries, blank_number,selected_string)
                if tries == 0:
                    return None
                else:
                    user_input = raw_input("what should be substituted in for " + guess + "? ")
                    updated_quiz =  " ".join(replaced) + selected_string[int(selected_string.find(guess)) + len(guess):]
            word = word.replace(guess,user_input)
            replaced.append(word)
            updated_quiz =  " ".join(replaced) + selected_string[int(selected_string.find(guess)) + len(guess):]
            print updated_quiz
            selected_string = updated_quiz
        else:
            replaced.append(word)
    replaced = " ".join(replaced)
    return replaced

run_game()
