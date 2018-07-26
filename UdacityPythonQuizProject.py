"""3 diffferent quizzes : Katana quiz, Ramen quiz, Pancit quiz"""

"""Quiz and answers about Katana"""

Katana_quiz = ("The ___1___ was one of the traditional Japanese swords used by the ___2___, the nobility during the feudal periods." 
	"\nIt is characterized by its curves, singe-edge blade, and its long grip to accommodate the use of two hands."
	"\nTraditionally, the ___1___ is forged from a specialized Japanese steel called ___3___." 
	"\nThis steel is heated and folded onto itself many times over, resulting in several layers of steel with different carbon concentrations." 
	"\nThis helps to remove impurities and even out the carbon." 
	"\nWhen this block of steel is drawn out, it is usually straight, or only slightly curved." 
	"\nThe curve on the blade is achieved through a process called differential hardening."
	"\nThe smith covers the blade with several layers of ___4___, with the edge coated with a thinner layer compared to the sides and the spine." 
	"\nThe blade is heated then quenched, and this process results in a hard edge while maintaining softer, more flexible sides, spine, and core." 
	"\nThis also results in a unique pattern along the sides of the blade called a ___5___, and each smith has their own unique style.")

Katana_answers = ["katana", "samurai", "tamahagane",	"clay", "hamon"]

Ramen_quiz = ("Ramen is a Japanese noodle dish, made of wheat noodles served in a broth made from meat and/or seafood."
	"\nApart from the broth, there are generally three flavors in most ramen shops:"
	"\n___1___, for salt-based flavor; ___2___, flavored with soy sauce; and miso, the fermented soy beans used to flavor many Japanese dishes."
	"\nThe secret to the noodles is the addition of ___3___, or alkaline salts."
	"\nThis gives the noodles their distinct yellow shade and firm, chewy texture."
	"\nThe dish comes with a variety of toppings like chashu, roasted pork; menma, fermented bamboo shoots; scallions, nori, and a seasoned ___4___called aji tamago."
	"\nA unique form of ramen is ___5___, which concentrates the broth into more of a dipping sauce, and serves the noodles and broth in separate vessels.")

Ramen_answers = ["shio", "shoyu", "kansui", "egg", "tsukemen"]

Pancit_quiz = ("___1___ is the iconic noodle dish of the Philippines."
	"\nIntroduced by ___2___-Filipino settlers in the archipelago, over the centuries the dish has been adopted into local cuisine, of which now there are many varieties."
	"\nProbably the most common is variety is ___3___, made from thing rice noodles flavored with soy sauce, possibly some fish sauce, and various meat and vegetables."
	"\nOne of the more colorful and flavorful variations is ___4___, which uses thin rice noodles flavored with a thick, yellow-orange sauce made from shrimp,"
	"\nand topped with various ingredients like pork rinds, hard boiled eggs, shrimp, green onion, and other flavors."
	"\nEach region of the Philippines has their own unique, local variety of the dish."
	"\nMost people like to add a bit of the juice from a ___5___, a local citrus fruit, for added flavor.")

Pancit_answers = ["Pancit", "Chinese", "bihon", "palabok", "calamansi"]

quiz_list = ["Katana", "Ramen", "Pancit"]

blank_spaces = ["___1___", "___2___", "___3___", "___4___", "___5___"]

lives_easy = 5
lives_medium = 4
lives_hard = 3
lives_veryhard = 2
lives_insane = 1

def choose_quiz():
    """Prompts player to pick a type of quiz and loads the quiz"""
    #Input = player_quiz (raw input from player)
    #Output = Player's chosen quiz
    while True:
        player_quiz = raw_input("Please, select a quiz you want to play: "
                          "(Katana, Ramen, or Pancit): ")
        if player_quiz == "Katana":
            return Katana_quiz
        elif player_quiz == "Ramen":
            return Ramen_quiz
        elif player_quiz == "Pancit":
            return Pancit_quiz
        else:
            print "Choice invalid, please pick again!" 

def answers_for_quiz():
    """ Loads appropiate answers to the quiz that player has chosen"""
    #Input = player quiz (raw input from player)
    #Output = loaded quiz answers from the quiz player chose
    player_quiz_pick = choose_quiz()
    if player_quiz_pick == Katana_quiz:
        return Katana_answers
    elif player_quiz_pick == Ramen_quiz:
        return Ramen_answers
    elif player_quiz_pick == Pancit_quiz:
        return Pancit_answers

def player_level():
    """ Loads a difficulty that player chooses """
    #Input = player_level_input (raw input of player choosing a difficulty)
    #Output = corresponding number of lives:
    #Easy = 5 lives, Medium = 4 lives
    #Hard = 3 lives, Superhard = 2 lives
    #Insane = 1 life
    while True:
        player_level_input = raw_input("Please type in a difficulty level: "
                                 "(Easy, Medium, Hard, Very Hard, Insane): ")
        if player_level_input == "easy":
            return lives_easy #Easy = 5 lives
        elif player_level_input == "Medium":
            return lives_medium #Medium = 4 lives
        elif player_level_input == "Hard":
            return lives_hard #Hard = 3 lives
        elif player_level_input == "Very Hard":
            return lives_veryhard #Very Hard = 2 lives
        elif player_level_input == "Insane":
            return lives_insane #Insane = 1 life
        else:
            print "Invalid response. Please try again!"

def correct_answer(player_answer, list_of_answers, answers_index):
    """ Checks whether the the answer from player matches with the answer list. """
    #Input: player_answer (Raw input that player enters in order to fill in the blank.)
    #Output: "Correct!" or "Sorry. Try again." This output will be later used in the game.
    if player_answer == list_of_answers[answers_index]:
        return "Correct! Good job!"
    return "Sorry. Try again."

def startgame():
    """Functions that sets up a game so we can play it """
    player_quiz_pick, playerlives, list_of_answers = choose_quiz(), player_level(), answers_for_quiz()
    print player_quiz_pick
    print "\nYou will get 5 guesses for this game. Good luck.\n"
    blanks_index, answers_index, player_lives = 0, 0, 0

    #for elements in blank_space:
    while blanks_index < len(blank_space):
        player_answer = raw_input("Please type in your answer for " + blank_space[blanks_index] + ": ")
        if correct_answer(player_answer,list_of_answers,answers_index) == "Right answer!":
            print "Correct answer! Keep going!\n"
            player_quiz_pick = player_quiz_pick.replace(blank_space[blanks_index],player_answer)
            answers_index += 1
            blanks_index += 1
            print player_quiz_pick
            if blanks_index == len(blank_space):
                print "You got it! Congratulations!"
        else:
            player_level_pick -= 1
            if player_level_pick == 0:
                print "Game over! Maybe next time!"
                break
            else:
                print "Try again. You have " + str(player_level_pick) + " guesses left."

startgame()
