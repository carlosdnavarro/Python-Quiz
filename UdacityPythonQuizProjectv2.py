"""3 diffferent quizzes : Katana quiz, Ramen quiz, Pancit quiz"""

"""Quiz and answers about Katana"""

"""The et of the quiz is paraphrased from research on the net, mostly Wikipedia."""

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

blank_spaces = ["___1___", "___2___", "___3___", "___4___", "___5___"]


#Code based on the one posted on https://github.com/hazelparr/Fill-in-the-Blanks-Quiz/blob/master/fill-in-the-blanks.py


def answer(score):
    '''Prompts the user for their answer'''
    answer = raw_input("\nPlease type in your answer for {} : ".format(score)).lower()
    return anwer


def select_quiz():
#Asks user for desired level then returns corresponding quiz text and answers.
    quiztopic = ""
    print "\nQuiz Topics: \t Katana, \tRamen, \tPancit"
    quiz_list = ["Katana", "Ramen", "Pancit"]
    while level not in levels:
        quiztopic = raw_input("Please select a topic: ").upper()
        if level == "Katana":
            return Katana_quiz, Katana_answers
        elif level == "Ramen":
            return Ramen_quiz, Ramen_answers
        elif level == "Pancit":
            return Pancit_quiz, Pancit_answers
        else:
            print "Invalid input, please try again."
    
    

def startgame():
#Starts the game, then ends game by congratulating successful players.
    score = 0
    print "\nWelcome to my quiz. You've got five tries to finish \nGood luck, have fun."
    lives = 5
    user_quiz, user_answers = select_quiz()
    while score < len(blank_spaces):
        print user_quiz
        user_answer = answer(blank_spaces[score])
        if user_answer == answer[score]:
            print "\nCorrect! Well done.\n"
            user_quiz = user_quiz.replace(blank_spaces[score], user_answer)
            score += 1
        else:
            lives -= 1 #added this to try and give a life limit
            print "\nSorry, try again. You've got " + str(lives) + " guesses remaining.\n"
            if lives == 0: #This is my addition
                print "\nSorry, game over. Please try again.\n"
                break
    print "You got them all! Awesome job! \n"
    print user_level
    break
            

startgame()