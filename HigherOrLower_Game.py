#Higher OR Lower_Ver2   by   Dr.M-Dev:

import random
import art
import game_data
#ALL INFO in game_data is a LIST and keys inside it are name,follower_count,description,country.
# data = [
        # {'name': 'Instagram',
        # 'follower_count': 346,
        # 'description': 'Social media platform',
        # 'country': 'United States'}


print('''                                                                                                                                                  
                                                              ...::::.      ...::::::::    :.      .:.   
  5@@@@@@@@B!    &@@@@@@@&G:        ^G&@@@&P#@@@@B~          J@@@@@@@@@G.   #@@@@@@@@@@   .@@B    7@@?   
  G@@~::::J@@!   @@#     B@@.      :@@G::~&@@!::Y@@~         J@@~    ^@@B   #@@.           !@@J  .@@B    
  G@@     .@@Y   @@@    5&@#       ~@@!   B@&   :@@?         J@@:     &@#   #@@BBBBBBB      P@@: #@@.    
  7BP     .@@J   PBGGGGGB@@B       :BB^   B@&   :@@?         ~GP.     &@#   JGPYYYYYYY       &@# @@!     
  Y&&^....?@@7   #&P     J@@:  ##  ^&&~   B@&   ^@@?         ?@@7:  :7@@P   Y@& ......       ^@@@@P      
  P@@@@@@@@&?    &@B     ?@@:  ##  ~@@!   B@&   :@@?         ?@@@@@@@@#J    J&@@@@@@@@?       ?@@B  


                                                             !J!:                                                                
                                                              ^G@@&P7:                                                           
                                         .~7YGB#&&&&&&&#BG5?~:  .Y@@@@&G^                                                        
                                    :?P&@@@@@@@@@@@@@@@@@@@@@@@&G?J@@@@@&                                                        
                                .!G@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P   ...                                                 
                              ~B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@BG&&@@@@                                              
                            ?&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&                                             
                          7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#GYP#&J                                            
                        .B@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@!                                                
                       :&@@@@@@@@@@@@@@@@J7@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@P                                               
                      .@@@@@@@@@@@@@@@@#:  ^&@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@G                                              
                      #@@@@@@@@@@@@@@&7      P@@@@@@@@@@@@@B&@@@@@@@&@@#&@@@@@@@@@@J                                             
                     !@@@@@@@@@@@@@&?         ^#@@@@&&@@@@@@#PPGB##? B@5#@#@@@@@@@@@:                                            
                     B@@@@@@@@@@@G~             ^B@@@&GG#@@@@@@@#~   .&#J@Y&@@@@@@@@G                                            
                     @@@@@@@@@@~                  .?#@@@&BGPGBBJ      .#5G&J@@@@@@@@@.                                           
                   .@@@@@@@@@7      !PB##B4^        .^JG#&&P:  ^4B###P4?!~!?@@@@@@@@^                                           
                   .@@@@@@@@#      !4~.. .~4^                 ~4~....~4^    #@@@@@@@^   .~                                      
               ~BJ :@@@@@@@@BJYYYYYYJJJJYJJJJJJJ?!.     .!?JYYYJJYYYJJJYYYYY&@@@@@@@P7: .G#?.                                   
            .?BG^  &@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?...5@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@?  .Y#5:                                 
          :5BJ.    @@@@@@@@@&PJJJJJJ????JJJJ5&@@@@@@@@@@@@@@@GYJJ??????JJJJJYB@@@@@@@@@Y     7BB~                               
        !GG~       .YGG@@@@B        ...       G@@@@@@@@@@@@@:     .::.        !@@@@&GP7        ^G#?                             
     .JB5:             &@@@Y      4P..P@G.    7@@@@@@@@@@@@&    ^:^B@@@P.      @@@@~             .J#5.                          
     J@J               &@@@5     G@@4Y&@@&    ?@@@@?::^#@@@&   ~@4^B@@@@#     .@@@@~              ^#&:                          
      .5#J.            &@@@5     ?@@@@@@@P    7@@@@.   ?@@@&   .@@@@@@@@Y     .@@@@~           .J#P:                            
        .?#P:          #@@@G      .JGBBY:     5@@@&    ^@@@@.    ?B&&#P^      :@@@@~         ^PBJ.                              
           ~BB!        7@@@@5.              :P@@@@J     #@@@&!.             .!&@@@&        7BG~                                 
             :5#J.      ?@@@@@@@@@@@@@@@@@@@@@@@@J      .#@@@@@@&&&&&&&@&&@@@@@@@B.     :5BY.                                   
               .J#!      .7G&&@@@@@@@@@@@@@@&&G7.         ^5#&@@@@@@@@@@@@@@@&BJ:       7!                                      


 ''')


#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++







def logo():
    print("WELCOME TO")
    print(art.logo)

def vs():
    print('''  ++++VS++++  ''')




#===========================================================================================================
#GLOBAL CONSTANTS :)
code_running = True
PLAYER_SCORE = 0
#------------------
def result_check(result, oldChar2_becomeChar1):
    global PLAYER_SCORE
    global code_running

    if result == "RIGHT":
        PLAYER_SCORE = PLAYER_SCORE +1
        #now...re-run the code
        print("\n" * 100)  # NEW GAME logoSPACESR
        print(f"YOU'RE RIGHT! you get a point :), your current score: {PLAYER_SCORE}")
        start_game(True, oldChar2_becomeChar1)
    else:
        print("\n")
        print(f"sorry, you got it wrong :(, you reached a score of: {PLAYER_SCORE}")
        code_running = False
    #----------------------------
        #player get +1 and re-run the game [that player score value...is separate from the start_game function]
        #and just setting inside the WHILE-LOOP that runs the code :)
        #or...just
        #re-read everything...and make it a GLOBAL_NUMBER ok?





#=======================
def compair(fact, guess, oldChar2_becomeChar1):
    player_guess = guess
    fact = fact
    #---------Chars:
    char1 = 0
    char2 = 0
  #______________________compair:
    if fact == "A_higher":
        char1 += 1
    elif fact == "A_lower":
        char2 += 1

    #++++
    if player_guess == "a" and char1 > char2:
        result = "RIGHT"
    elif player_guess == "b" and char2 > char1:
        result = "RIGHT"
    else:
        result = "WRONG"


    result_check(result, oldChar2_becomeChar1)




#=======================
def start_game(IsMovingOn, saved_character2):
    global PLAYER_SCORE
    # __________TITLE
    logo()
    print(f"Your current score: {PLAYER_SCORE}")
    #__________Generate 2 random numbers for 2 characters :>
    char_1_number = random.randint(0, len(game_data.data) - 1)
    char_2_number = random.randint(0, len(game_data.data) - 1)
    #why length - 1? because the length is 50!! and the max is 49! :)
    #
    char1 = game_data.data[char_1_number]
    char2 = game_data.data[char_2_number]
    #
    fact = ""
    #__________
    # IsMovingOn = bool (just to check if the player got it right, in that case,
    # you must turn Char1 into --------> the next Char2.
    # USING Char_Numbers like:    char_1_number   &   char_2_number
    # and saving them into a small list that can be sent around the other variables!!!
    # which is:
    oldChar2_becomeChar1 = "" #this is the empty value to store char <and a good re-set line of code>
    oldChar2_becomeChar1 = char_2_number

    if IsMovingOn:
        char_1_number = saved_character2 #this will make char1 into char2 :)
        char1 = game_data.data[char_1_number]

    #______________________________PROCESSING:
    #__________Question here
    #char1
    print(f"Compair A: {char1["name"]}, a {char1["description"]}, from {char1["country"]}")
    char1_value = char1["follower_count"]

    #Verses
    print("\n")
    vs()
    print("\n")

    #char2
    print(f"Compair B: {char2["name"]}, a {char2["description"]}, from {char2["country"]}")
    char2_value = char2["follower_count"]

    #__________CALCULATING FACT:
    if char1_value > char2_value: #fact = HIGHER
        fact = "A_higher"
        print(f"CHEAT: pssst :)   the answer is {fact}") #<!>CHEAT_For_Debugging :)
    elif char1_value < char2_value:
        fact = "A_lower"
        print(f"CHEAT: pssst :)   the answer is {fact}") #<!>CHEAT_For_Debugging :)
    else:
        print("<!>Data_Source_File_Error :[ <!>")
        char1_value += 1
        fact = "A_higher"
        #___INCASE SOMEONE MESSES WITH THE FILES xD

    #__________Player points & input
    player_guess = input("Guess, [A] or [B] :)").lower()

    #__________TIME TO COMPAIR
    try:
        if player_guess == "a" or player_guess == "b":
            compair( fact, player_guess, oldChar2_becomeChar1 )
    except ValueError:
        print("<!>INPUT ERROR<!> please use only the letter [A] or [B]")
        start_game(False, oldChar2_becomeChar1) #small-reset
    #just added a safety mechanism to reset the game, haha xD
    #WRITE A NOTE ABOUT THAT :)




#____________________________________________________________________________________________________________
while code_running:
    print("\n" * 50)  # RE-SET SPACER in case of grammatical error
    start_game(False, 0)#tart the code here

