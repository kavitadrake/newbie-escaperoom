#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import random
import time

roomName = '' #For this newbie project, we will have main, purple, and yellow rooms.
doorPried = '' #The door to the purple room has to be pried open. This is a true/false on whether the that has been done yet.
doorUnlocked = '' #The door to the yellow room has to be unlocked. This is a true/false on whether that has happened.
chestUnlocked = '' #The chest in the main room has a crowbar you can take if the chest has been unlocked.
keySwapped = '' #The key on the pedestal needs to be swapped out with one hanging on the wall in the main room.
crowbarGone = '' #Has the crowbar been taken?
numComboTries = '' #Player has three tries on the combo lock.
redKeyLocation = '' #For this simple newbie project, I'm using variables for the few items available, rather than creating an inventory system.
blueKeyLocation = '' #See above
greenKeyLocation = '' #See above
orangeKeyLocation = '' #See above
crowbarLocation = '' #See above

#The following are all variables that change each time the game is reset.
deathKey = ''
hintWords = ''
chestKey = ''
purpleDoorKey = ''
deathKeyWeight = ''
chestKeyWeight = ''
purpleKeyWeight = ''
calendarDate = ''
bookOfDeath = ''
posterNumber = ''

#Code for requesting input
def requestNextStep():
    print('>>>')
    actionDesired = input()
    parseCommands(actionDesired)

#Whenever the floor opens up and collapses you into death. Can happen from any of the three rooms, in many instances.
def floorOpensYouDie():
    playAgain = ''
    print('''
    The floor suddenly shifts beneath you. Faster than you can respond, the
boards of the floor retract, leaving a gaping hole. You can't avoid tumbling
into the hole, landing on a pile of rotting bones and bodies. They...seem to 
be human! You gag as the stench you had only vaguely noticed becomes so strong
it cannot be ignored. As quickly as it retracted, the floor closes above your 
head, leaving you in utter darkness. Something grabs onto your ankle....
''')
    time.sleep(2)
    print('Thanks for playing our game! Do you want to try again? (yes or no)\n>>>')
    playAgain = input()
    if playAgain == 'yes' or playAgain == 'y':
        resetEscapeRoom()
    else:
        print('Okay, see you some other time. Goodbye!')
        exit()
        
#Code for parsing input
def parseCommands(inputPassed):

    inputArray = inputPassed.split(' ', 3)
    firstWord = inputArray[0]
    
    if firstWord == 'climb':
        climbUp(inputPassed)
    elif firstWord == 'look' or firstWord == 'l':
        lookAround(inputPassed)
    elif firstWord == 'unlock':
        unlockDoor(inputPassed)
    elif firstWord == 'leave':
        leaveRoom(inputPassed)
    elif firstWord == 'enter':
        enterCombo(inputPassed)
    elif firstWord == 'swap':
        swapKeyForKey(inputPassed)
    elif firstWord == 'take':
        takeSomething(inputPassed)
    elif firstWord == 'pry':
        pryOpenDoor(inputPassed)
    elif firstWord == 'open':
        openSomething(inputPassed)
    elif firstWord == 'quit' or firstWord == 'scream' or firstWord == 'yell' or firstWord == 'shout':
        floorOpensYouDie()
    else:
        helpText()

#The following chunk assigns all the random values for this instance of the game. They are unique every time the game loads. 
def resetEscapeRoom():
    
    global roomName
    global deathKey
    global hintWords
    global chestKey
    global purpleDoorKey
    global deathKeyWeight
    global chestKeyWeight
    global purpleKeyWeight
    global calendarDate
    global bookOfDeath
    global posterNumber    

    roomName = 'main'
            
    deathKey = random.choice(['red', 'blue', 'green'])

    if deathKey == 'red':
        hintWords = 'Beware the blood moon!'
        chestKey = random.choice(['blue','green'])
        if chestKey == 'blue':
            purpleDoorKey = 'green'
        else:
            purpleDoorKey = 'blue'
            
    elif deathKey == 'blue':
        hintWords = 'Beware the traitorous sea!'
        chestKey = random.choice(['red', 'green'])
        if chestKey == 'red':
            purpleDoorKey = 'green'
        else:
            purpleDoorKey = 'red'

    elif deathKey == 'green':
        hintWords = 'Beware the oxygen makers!'
        chestKey = random.choice(['red', 'blue'])
        if chestKey == 'red':
            purpleDoorKey = 'blue'
        else:
            purpleDoorKey = 'red'
        
    deathKeyWeight = random.randint(2,5)
    chestKeyWeight = random.randint(2,5)
    purpleKeyWeight = random.randint(2,5)
    
    calendarDate = random.randint(1,31)
    bookOfDeath = random.randint(6,14)
    posterNumber = random.randint(13,42)
    print('The chest key color is '+ chestKey + ' and it weighs ' + str(chestKeyWeight) + ' pounds.')
    print('The purple room key color is ' + purpleDoorKey + ' and it weighs ' + str(purpleKeyWeight) + ' pounds.')
    print('The death key color is ' + deathKey + ' and it weighs ' + str(deathKeyWeight) + ' pounds.')
    print('The calendar date is ' + str(calendarDate) + ', and the book of death is ' + str(bookOfDeath) + ' and the poster number is ' + str(posterNumber))
    print('The warning written on the wall is: ' + hintWords)
    print('''
    You open your eyes with a groan. Your head is pounding and your
mouth tastes gross. You are lying on the floor with no memory of how
you got here. You struggle against dizziness and eventually manage 
to stand upright and look around you.\n''')
    displayRoomDesc()
    requestNextStep()    
#End chunk assigning random values.

          


# In[2]:


#Code for climbing on table.
def climbUp(objectClimbed):
    global roomName
    inputArray = objectClimbed.split(' ', 2)
    lengthInput = len(inputArray)
    if lengthInput == 1:
        print('You try to climb the walls, but cannot find a grip on anything.')
        requestNextStep()
    if lengthInput > 1:
        secondWord = inputArray[1]
        if lengthInput > 2:
            thirdWord = inputArray[2]
    if secondWord == 'on' and lengthInput > 2:
        keyWord = thirdWord
    elif secondWord == 'on' and lengthInput == 2:
        print('Climb on what?')
        requestNextStep()
    elif secondWord != 'on':
        keyWord = secondWord
    if roomName == 'main':
        if keyWord != 'chest':
            print('The only thing you could conceivably climb on in here is the chest.')
            requestNextStep()
        else:
            print('''
    You clamber onto the chest. The ceiling is way too far above you to
make any difference to your status. You climb back down with a sigh.''')
            requestNextStep()
    elif roomName == 'purple':
        if keyWord == 'pedestal':
            print('''
    As you climb onto the pedestal, you hear a slight click and
feel the top of the pedestal sink a bit. With a rumble, the pedestal
shakes violently, causing you to fall to the floor.''')
            floorOpensYouDie()
        elif keyWord == 'bookshelf' or keyWord == 'shelf' or keyWord == 'books':
            print('''
    You try to carefully climb the bookshelf. However, your foot
happens to nudge the oddly bright red book. You hear a slight click.
The bookshelf shakes violently, causing you to fall to the floor.''')
            floorOpensYouDie()
        else:
            print('The only conceivable things to climb in here are the pedestal or the bookshelf.')
    elif roomName == 'yellow':
        if keyWord == 'table':
            print('''
    The words printed on the wall (NO CHEATING!!!) glare at you as you
climb onto the table. You hear a click, and the table tilts towards the
floor, making you fall.''')
            floorOpensYouDie()
        else:
            print('The only conceivable thing to climb in here is the table.')
        requestNextStep()


# In[3]:


#Whenever we need to show the description of the room we're in. Should be referred to most by simple input of 'look' or 'l'
def displayRoomDesc():
    global roomName
    if roomName == 'main':
        print('This is the main room.')
    elif roomName == 'purple':
        print('This is the purple room.') 
    elif roomName == 'yellow':
        print('This is the yellow room.')
    else:
        print('You are in the ether!')


# In[4]:


#Code for input of take. Objects to handle: key, colored key, crowbar, yellow room key, book, red book, lock, pedestal
def takeSomething(objectTaken):
    print('Eventually some code for taking something should go here.')


# In[5]:


#Code for input of open. Objects to open: chest, purple door, yellow door, door, lock
def openSomething(objectOpened):
    print('Eventually some code for opening something should go here.')


# In[6]:


#Code for input of pry. Objects to pry: purple door, yellow door, door
def pryOpenDoor(objectPried):
    print('When the person tries to pry open the door...')


# In[7]:


#Code for input of swap. Objects to swap: key
def swapKeyForKey(objectSwapped):
    print('When the person tries to swap one of the keys for the one on the pedestal.')


# In[8]:


#Code for entering combination in lock
def enterCombo(comboNumbers):
    print('A person will have to enter all three numbers at once.')


# In[9]:


#Code for all the things to look at.
def lookAround(lookTarget):
    print('You looked at something!')


# In[10]:


#Code for commands that don't fit our expected syntax, or when typing 'help'
def helpText():
    print('Whether you asked for it or not, here is the help suggestions.')


# In[11]:


#Code for input of leave. 
def leaveRoom(objectLeft):
    global roomName
    global doorPried
    global doorUnlocked
    inputArray = objectLeft.split(' ', 1)
    lengthInput = len(inputArray)
    if roomName == 'purple' or roomName == 'yellow':
        roomName = 'main'
        print('You leave this room to go back to the starting room. The door swings shut behind you.')
        requestNextStep()
    if roomName == 'main':
        if doorPried != 'yes' and doorUnlocked != 'yes':
            print('''
    You try to leave the room, but both doors are securely shut. The door
painted yellow looks like it needs to be unlocked, and the purple door,
having no handle, would have to be opened from the other side, or pried open.''')
            requestNextStep()
        if lengthInput == 1:
            print('Leave to where? (leave purple or leave yellow)')
            requestNextStep()
        if doorPried == 'yes' and 'purple' in inputArray:
            print('You walk through the pried-open purple door, and it swings mostly shut behind you.')
            roomName = 'purple'
        elif doorUnlocked == 'yes' and 'yellow' in inputArray:
            print('You walk through the unlocked yellow door, and it swings mostly shut behind you.')
            roomName = 'yellow'
        elif doorPried != 'yes' and 'purple' in inputArray:
            print('You pound fruitlessly on the purple door. It would probably have to be pried open.')
        elif doorUnlocked != 'yes' and 'yellow' in inputArray:
            print('You jiggle the handle on the yellow door. It is firmly locked.')
        else:
            print('You\'ve been trapped here by some madman. You can\'t leave!')
    requestNextStep()


# In[ ]:


#Code for unlocking door.
def unlockDoor(objectUnlocked):
    global doorUnlocked
    global doorPried
    global roomName
    global redKeyInHand
    global blueKeyInHand
    global greenKeyInHand
    inputArray = objectUnlocked.split(' ', 1)
    lengthInput = len(inputArray)
    if roomName == 'purple':
        print('''
    There's not really anything to unlock in here. The door to the main
room can't even shut securely, after you pried it open.''')
    if roomName == 'yellow':
        print('''
    If you're hoping to unlock the big red door, you're going to
have to 'enter numbers' into the combination lock. The door back
to the main room remains unlocked.''')
    if roomName == 'main':
        if lengthInput == 1:
            print('Unlock what? If you have the right keys, you could unlock chest or unlock yellow door.')
            requestNextStep()
        

    requestNextStep()


# In[ ]:





# In[ ]:


resetEscapeRoom() 


# In[ ]:





# In[ ]:




