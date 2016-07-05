## designed to be run in console and not idle
## Andrew Mackay
#########################################################################
import random, os, time #Imports random, os and time modules. random  is used to generate code, os to clear console and time to add pauses.
#any variable starting with random. or os. or time. or self. can't have AM added before them as it will prevent the code from functioning
#########################################################################

#########################################################################
class AMp():#Template for Prisoner
    def __init__(self,AMi,AMj):#Runs when new object is created
        #I am unable to add AM to the begining of the above function.
        #__init__ is a reserved function name that runs when an object is created
        #changing it to AM__init__ would break the code
        #self has the same isue. if i change it, the object will not function
        self.AMname=AMi # Represents the Players Name
        self.AMwon=False # Indicates if the player has won
        self.AMRobot=AMj # Indicates if player is controlled by robot
#########################################################################

#########################################################################
def AMvalid_number(AMmsg):#used to validate a number between 0 and 999
    AMDone=False#used in while loop
    while AMDone==False:#while variable is false
            AMN_O_P=input(AMmsg)#asks for input using custom message
            if (AMN_O_P.isdigit())==False:#is it not a number (does not allow negitive numbers)
                print('Please enter a number no larger than 999.')#error messsage
                print("Please do not include any symbols.")#error message
            elif int(AMN_O_P)<1000:#is it less than 1000 
                AMDone=True#breaks loop
                AMcls()#cleares console
                return AMN_O_P#returns number
            else:#else
                print('Please enter a number no larger than 999')#error message
#########################################################################
def AMvalidate_three_number(): #3 digit input. validates and returns result.
    AMDone=False #Initiates variable
    while AMDone==False: # will loop while variable is False
        AMn=input('Code:')#user input saved as n
        if len(AMn) == 3 and AMn.isdigit():#if n is 3 long, is a number.
            AMDone=True#change of variable will end loop
            return AMn #will return 3 digit value
        else:#else
            print('Please enter a three digit number and nothing else')#loop will start again, asking the user to input again.
#########################################################################
        
#########################################################################
def AMcls():#clears the console
    print("Should have cleared")#prints message if not in console, indicating it should have cleared. if in console this should not be seen by the user.
    os.system('cls' if os.name=='nt' else 'clear')#checks the OS and gives a different commabd to cleare the console bassed on the OS
#########################################################################
    
#########################################################################
def AMGuard(AMPlayers):# used to create a Guard class
    AMDone = False#useb by while loop
    while AMDone == False:#while variable false
        AMoption=input("Guard: Player or Robot (P,R)")#Allows choice between human and robot guard
        AMcls()#clears console
        if AMoption == 'P' or AMoption == 'p':# if player
            AMDone=True#ends loop
            AMcode=int(AMvalidate_three_number())#takes code
            AMcls()#clears console
            return (AMcode,'P')#returs generated code and 'P' indicating it is a human guard.
        elif AMoption == 'R' or AMoption == 'r':# if robot
            AMDone=True#ends loop
            AMcode=random.randint(0,999)#generates code
            return (AMcode,'R')#returs generated code and 'R' indicating it is a robot guard.
        else:# if anything else
            print("Please enter a valid input")#error message
            print("'P' for Player/s")#error message
            print("'R' for robot")#error message
#########################################################################

#########################################################################
def AMprisinors(AMPlayers):#used to generate players
    #AMcls()#cleares console
    AMDone = False#used by while loop
    while AMDone == False:#while vasriable false
        AMoption=input("prisoners: Player/s or Robot (P,R)")#input
        AMcls()#cleares console
        if AMoption == 'P' or AMoption =='p':#if input is p or P
            AMN_O_P=AMvalid_number("How many prisoners? ")#input
                    
            for AMi in range(int(AMN_O_P)):#loop for how many players
                AMDone=False#used by while loop
                while AMDone==False:#while variable false
                    AMPlayer_Name=input("Player %s's name:" % (AMi+1))#input, dynamically changes player name
                    if ('AM'+AMPlayer_Name) in AMPlayers:#checks if already taken
                        print('Name taken or reserved. Please Pick another')#error message
                    elif len(AMPlayer_Name)<1:#if playername blank
                        print("Please do not leave blank")#error message
                    else:#else
                        AMPlayer_Name='AM'+AMPlayer_Name#adds 'AM' to playername
                        AMPlayers.insert(AMi+1,AMPlayer_Name)#asks for each name
                        AMDone=True#breaks loop
            for AMi in AMPlayers:#for each player
                globals()[AMi] = AMp(AMi,False)#creates instance of object using variable and making it global
            return AMPlayers#returns player name list
        elif AMoption == 'R' or AMoption == 'r':#if r
            AMPlayers.insert(1,'AMRobotP')#adds robot name to player list
            global AMRobotP#globalises variable
            AMRobotP = AMp('AMRobotP',True)#creates instance of robot prisoner
            return AMPlayers#returns playear name list
        else:#else
            print("Please enter a valid input")#error message
            print("'P' for Player/s")#error message
            print("'R' for robot")#error massage
           
#########################################################################     

#########################################################################
def AMRobotGuesser(AMcode,AMlimit): #robot guess function
    AMover=False#used in while loop
    AMminimum=0#used to dynamically change lowest guess bassed on previous guesses
    AMmaximum=999#used to dynamically change highest guess bassed on previous guesses
    AMguesses=1#numebr of guesses
    AMlimit=int(AMlimit)#guess limit
    while AMover==False:#while variable false
        time.sleep(0.01)#pauses for 0.01s makes it look smooth as aposed to it instantly guessing the correct code
        #print("min: %s max: %s" % (AMminimum,AMmaximum))#for troubleshooting
        AMguess=random.randint(AMminimum,AMmaximum)#random number bassed on min max
        print("Guess %s: %s"% (AMguesses,(str(AMguess).zfill(3))))#prints robots guess
        if AMguesses >= AMlimit:#if at or over limit
            AMover=True#break loop
            print("Robot ran out of guesses!")#win message
            return True#retrn True
        elif AMguess == AMcode:#if guess correct
            print("Code broken after %s attempt(s)" % AMguesses)#win message
            AMover=True#breaks loop
            return True#retrn True
        elif AMguess>AMcode:#if too big
            AMguesses+=1#add 1 to guesses
            AMmaximum=AMguess-1#robot wont guess same number or higher again
        elif AMguess<AMcode:#if to small
            AMguesses+=1#add 1 to guesses
            AMminimum=AMguess+1#robot wont guess same or lower again
#########################################################################

#########################################################################
def AMHumanGuesser(AMi,AMguesses,AMcode):#function for player guessing
    print("%s's Turn"%AMi[2:])#pints name of player
    AMguess=int(AMvalidate_three_number())#uses function to get guess
    AMcls()#clears screen
    if AMguess == AMcode:#of correct
        print("Key correct! %s Wins!"%AMi)#win message
        print("It took %s %s attempt(s) to guess."%(AMi[2:],AMguesses))#win message
        return True#return true
    elif AMguess> AMcode:#if too high
        print("Too High")#message
        time.sleep(1)#wait 2s
        AMcls()#clear screen
        return False#return false
    elif AMguess< AMcode:#iff too small
        print("Too Low")#message
        time.sleep(1)#wait 2s
        AMcls()#clear screen
        return False#return false
#########################################################################
        
#########################################################################
def AMmain_game(AMPlayers,AMcode,AMlimit):# main game
    AMDone=False#used in while loop
    AMguesses=0#number of guesses
    AMlimit=int(AMlimit)#limit
    while AMDone == False:#while variable false
        AMguesses+=1#adds 1 to guesses
        for AMi in AMPlayers:#for evert player
            if globals()[AMi].AMRobot == True:#if a robot
                AMDone=AMRobotGuesser(AMcode,AMlimit)#run robot guesser
            elif AMDone==False:#if not na robot and game not over
                AMDone=AMHumanGuesser(AMi,AMguesses,AMcode)#run human guesser
        if AMguesses>=AMlimit and globals()[AMi].AMRobot == False and AMDone==False:#if at limit and not tobot but also game not voer
            AMDone=True#game over
            print("Players have run out of moves")#win message
        elif globals()[AMi].AMRobot == False and AMDone==False:# if not robot and game not over
            print("%s guesses each remaining!"% (AMlimit-AMguesses))#message displaying guesses left
            time.sleep(2)#wait 2 s
            AMcls()#clear screen
        
#########################################################################

#########################################################################
def AMplay_again(AMPlayers,AMp_or_r,AMlimit):#asks player if they want to go again
    AMDone=False#use in while loop
    while AMDone==False:#while variable false
        AMawnser=input('Would you like to play again? (Y/N)')#input
        if AMawnser == 'Y' or AMawnser== 'y':#if y or Y
            for AMi in AMPlayers:#for every player
                globals()[AMi].AMwon=False#reset win variable
            if AMp_or_r == 'P':#if guard was player
                AMcls()#clear screen
                AMcode=int(AMvalidate_three_number())#takes new code
                AMcls()#clear screen
                AMmain_game(AMPlayers,AMcode,AMlimit)#runs main game again
            else:#else
                AMcls()#clears screen
                AMmain_game(AMPlayers,(random.randint(0,999)),AMlimit)#generates new code
        elif AMawnser== 'N' or AMawnser== 'n':#if n or N
            print("Thanks for playing :)")#message
            time.sleep(2)#wait 2 s
            AMDone=True#ends loop
        else:#else
            print("Please enter a valid input")#message. program will end after this
#########################################################################
                
#########################################################################
AMPlayers=['Guard']#creates list of names
AMcode,AMp_or_r=AMGuard(AMPlayers)#runs guard setup. saves to two variables
AMlimit=AMvalid_number("How many guesses should each prisoner have? ")#sets guess limit
#x=Guard.code
AMPlayers=AMprisinors(AMPlayers)#sets up prisoners
AMcls()#clears screen
AMPlayers.pop(0)#removes reserved name from name list
AMmain_game(AMPlayers,AMcode,AMlimit)#runs main game
AMplay_again(AMPlayers,AMp_or_r,AMlimit)#runs play again
#########################################################################
