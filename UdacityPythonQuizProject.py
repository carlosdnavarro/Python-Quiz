"""3 diffferent quizzes : Katana quiz, Ramen quiz, Pancit quiz"""

#Quiz and answers about Katana

#The text of the quiz is paraphrased from research on the net, mostly Wikipedia.

Katana_quiz = ("\nThe ___1___ was one of the traditional Japanese swords used by the ___2___, the nobility during the feudal periods." 
    "\nIt is characterized by its curves, singe-edge blade, and its long grip to accommodate the use of two hands."
    "\nTraditionally, the ___1___ is forged from a specialized Japanese steel called ___3___." 
    "\nThis steel is heated and folded onto itself many times over, resulting in several layers of steel with different carbon concentrations." 
    "\nThis helps to remove impurities and even out the carbon." 
    "\nWhen this block of steel is drawn out, it is usually straight, or only slightly curved." 
    "\nThe curve on the blade is achieved through a process called differential hardening."
    "\nThe smith covers the blade with several layers of ___4___, with the edge coated with a thinner layer compared to the sides and the spine." 
    "\nThe blade is heated then quenched, and this process results in a hard edge while maintaining softer, more flexible sides, spine, and core." 
    "\nThis also results in a unique pattern along the sides of the blade called a ___5___, and each smith has their own unique style.")

Katana_answers = ["katana", "samurai", "tamahagane",    "clay", "hamon"]

#Quiz and answers about Ramen

Ramen_quiz = ("\nRamen is a Japanese noodle dish, made of wheat noodles served in a broth made from meat and/or seafood."
    "\nApart from the broth, there are generally three flavors in most ramen shops:"
    "\n___1___, for salt-based flavor; ___2___, flavored with soy sauce; and miso, the fermented soy beans used to flavor many Japanese dishes."
    "\nThe secret to the noodles is the addition of ___3___, or alkaline salts."
    "\nThis gives the noodles their distinct yellow shade and firm, chewy texture."
    "\nThe dish comes with a variety of toppings like chashu, roasted pork; menma, fermented bamboo shoots; scallions, nori, and a seasoned ___4___, called aji tamago."
    "\nA unique form of ramen is ___5___, which concentrates the broth into more of a dipping sauce, and serves the noodles and broth in separate vessels.")

Ramen_answers = ["shio", "shoyu", "kansui", "egg", "tsukemen"]

#Quiz and answers about Pancit

Pancit_quiz = ("\nToday, ___1___ is arguably the most iconic noodle dish of the Philippines."
    "\nIntroduced by Chinese-Filipino settlers in the archipelago, over the centuries the dish has been adopted into local cuisine, of which now there are many varieties."
    "\nProbably the most common is variety is ___1___ ___2___, made from thing rice noodles flavored with soy sauce, possibly some fish sauce, and various meat and vegetables."
    "\n A variant that sticks closer to Chinese chow mein or lo mein is ___1___ ___3___, which uses wheat noodles."
    "\nOne of the more colorful and flavorful variations is ___1___ ___4___, which uses thin rice noodles flavored with a thick, yellow-orange sauce made from shrimp,"
    "\nand topped with various ingredients like pork rinds, hard boiled eggs, shrimp, green onion, and other flavors."
    "\nEach region of the Philippines has their own unique, local variety of the dish."
    "\nMost people like to add a bit of the juice from a ___5___, a local citrus fruit, for added flavor.")

Pancit_answers = ["pancit", "bihon", "canton", "palabok", "calamansi"]

blank_spaces = ["___1___", "___2___", "___3___", "___4___", "___5___"]

def difficulty(): 
    '''
    Player selects his difficulty. This function requests for the player to enter his choice of  difficulty as a raw input.
    If raw input is a valid choice, the function returns the corresponding amount of lives/attempts.
    Otherwise, it asks the player to try again.
    '''
    while True:
        player_diff_input = raw_input("\nWelcome to my quiz. Please type in a difficulty level:\n"
                                 "\nEasy (5 tries), \nMedium (4 tries), \nHard (3 tries)," 
                                 "\nVery Hard (2 tries), \nInsane (1 try): ").lower()
        if player_diff_input == "easy":
            return lives_easy #Easy = 5 lives
        elif player_diff_input == "medium":
            return lives_medium #Medium = 4 lives
        elif player_diff_input == "hard":
            return lives_hard #Hard = 3 lives
        elif player_diff_input == "very hard":
            return lives_veryhard #Very Hard = 2 lives
        elif player_diff_input == "insane":
            return lives_insane #Insane = 1 life
        else:
            print "\nInvalid response. Please try again!"

lives_easy = 5
lives_medium = 4
lives_hard = 3
lives_veryhard = 2
lives_insane = 1 

def select_quiz(): 
    '''
    Player selects the topic of his quiz.
    This function requests for the player to select the topic for his quiz.
    If raw input is a valid choice, the function returns the corresponding quiz text and list of answers.
    Otherwise, it asks the player to try again.
    '''
    quiztopic = ""
    print "\nQuiz Topics: Katana, Ramen, Pancit"
    quiz_list = ["katana", "ramen", "pancit"]
    while quiztopic not in quiz_list:
        quiztopic = raw_input("Please select a topic: ").lower()
        if quiztopic == "katana":
            print "\nHere's your quiz:\n"
            return Katana_quiz, Katana_answers
        elif quiztopic == "ramen":
            print "\nHere's your quiz:\n"
            return Ramen_quiz, Ramen_answers
        elif quiztopic == "pancit":
            print "\nHere's your quiz:\n"
            return Pancit_quiz, Pancit_answers
        else:
            print "Invalid input, please try again."

def answer(score): 
    '''
    Prompts the user for their answer
    '''
    answer = raw_input("\nPlease type in your answer for " + str(score) + " :").lower()
    return answer


def startgame(): 
    '''
    Game proper.
    The function starts at score 0 (matching the list index) and prints the text for the player's 
    chosen quiz. If the player inputs correct answer, score and index increase by one, the 
    corresponding blank is replaced by the correct answer, and the updated quiz is printed.
    Otherwise, the function deducts one life/attempt, and asks the player to try again.
    '''
    score = 0
    lives = difficulty()
    user_quiz, user_answers = select_quiz()
    print "\nYou've got " + str(lives) + " tries to finish \nGood luck, have fun."
    while score < len(blank_spaces):
        print user_quiz
        user_answer = answer(blank_spaces[score])
        if user_answer == user_answers[score]:
            print "\nCorrect! Well done.\n"
            user_quiz = user_quiz.replace(blank_spaces[score], user_answer)
            score += 1
        else:
            lives -= 1
            print "\nWrong answer. You've got " + str(lives) + " guesses remaining.\n"
            if lives == 0:
                print "\nSorry, game over. Please try again.\n"
                break
    print user_quiz + "\n\nYou got them all! Awesome job!\n\nThanks for playing!"
          

startgame()
