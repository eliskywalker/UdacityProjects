


#This is my unsuccesful attemtp at making the play_game function smaller from the original in the file
#Eli-Ortigoza-fill-in-the-blanks-corrected.py, Here in quizpiecetester3.py I modified a few things based on the feedback I got
#the last time I submitted my project but now it is not synching correctly and not giving correct updates
#I was told that spliting was not needed and given hints on how i might just replace the portion of the strings that matched a
#concatenation of "___"+str(blank_number)+"___" which it does replace the current blank, but in the next iteration, it forgets about that
#last update and only replaces the current blank with the correct answer.

#Also, this function does not stop after getting to blank number 5, it keeps asking for the blank 6 eventhough it is not existent.



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
