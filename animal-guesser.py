# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# This notebook is special because it contains a complete game... at
# least, it will when you've finished it. This will use all of the Python you've learned in lessons 1 - 10.

# <headingcell level=2>

# Introduction

# <markdowncell>

# But what does this game do?  This is a game where you, as a player,
# think of an animal, and the computer will ask questions to try and
# guess what you are thinking. It will look something like:

# <rawcell>

# Think of an animal. Would you like me to guess it? Yes
# Does the animal you are thinking have four legs? y
# Is your animal large and gray? no
# Is your animal an a cow? yeah
# Yay! I guessed it!

# <headingcell level=2>

# Initial Data

# <markdowncell>

# Before we can go anywhere, we need to set up the initial questions for
# our animals. We will use a dictionary that forms a *tree* of
# questions. What do I mean by that?
# 
# Maybe it would be good for me to draw a picture:
# 
# ![Initial Data Structure](files/animal-guesser-tree-1.png)

# <markdowncell>

# Did I call this a tree? Looks more like an upside-down tree, huh?
# Whatever we call it, we can start at the top, and work our way down
# the arrows to the bottom.
# 
# Let's suppose we are thinking of Bessy, our favorite cow on Grandpa's
# farm. We start at the top and answer the question in the square, "Does
# our animal have 4 legs?"
# Bessy does have 4 legs, so we follow the arrow labeled *Yes* and get
# to another square, and ask the question, "Is our animal large and
# gray?"
# 
# Bessie seems large, but she is black and white, so we follow the arrow
# that says, "No". This brings us to an oval shape with the name of an
# animal, "Cow". This is the answer, so we end the game.
# 
# ---------------------------------------------------------------------------
# 
# Let's play this game again, but this time, we are thinking of an
# octopus. At the top, we answer the question of "4 Legs?" by following
# the "No" arrow down to the oval that reads "Fish".
# 
# But we weren't thinking of a fish. This means, we need a *new branch*
# that has a question to distinguish a fish and an octopus.
# 
# ![Initial Data Structure](files/animal-guesser-tree-2.png)

# <markdowncell>

# This new branch needs to *replace* the `Fish` oval, so that our new
# tree... er, upside-down tree now looks more like a pyramid:
# 
# ![Initial Data Structure](files/animal-guesser-tree-3.png)

# <markdowncell>

# Does this make sense? Let's try to make our initial tree using a
# dictionary called `animals`.
# 
# Each "square" (in our diagrams above) will have three parts:
# 
#   * **question** will hold the question we can ask.
#   * **yes** will either point to an animal or another branch
#   * **no** will either point to an animal or another branch

# <codecell>

animals = {
    "question": "Does the animal you are thinking have four legs?",
    "no":  "fish",
    "yes": {
        "question": "Is your animal large and gray?",
        "yes": "elephant",
        "no": "cow"
    }
}

# <markdowncell>

# If the player says *no* to our first question, we end up with a
# `fish`. If the `fish` isn't correct, we will replace it with a new
# branch. That branch will have a question, the new animal, and the
# `fish`.
# 
# You can see this "sub branch" with `"yes"`, as it contains another
# dictionary. Now that you know how we will keep track of our questions, let's get on with the game.

# <headingcell level=2>

# Play the Game!

# <markdowncell>

# We will play our game by calling the `playGame` function.
# 
# This function has two jobs:
# 
#   * First, it will begin with some instructions. Feel free to help
#     your player know how to use our program.
# 
#   * Second, we ask the player if they want to play another round in
#     our game.

# <codecell>

def playGame():
    print """Hi! I'm an animal guesser. 
  
I will ask questions and try to guess what animal you are thinking.
Think of an animal. Got it in your head? Good!
"""
  
    while askYesNo("Would you like me to guess?"):
        walkTree(animals)    # playRound(animals)

# <markdowncell>

# The `playGame` function calls two other functions that we'll need to
# make, `askYesNo` and `walkTree`. The `askYesNo` function returns
# `True` if our player types in "Yes", and as long as they keep typing
# in "Yes" to this question, we'll keep calling `walkTree`.

# <headingcell level=2>

# Play a Round by Walking the Tree

# <markdowncell>

# Playing a round means we start at the top of our dictionary, and walk
# down the tree to the bottom when we get to an animal.
# 
# Since the tree is really just a lot of little branches, we could start
# at any branch, ask its question, and then move down from there. And if
# we pass in `animals` as the branch (that is, the top of the tree), we
# will play an entire game round. So, this function takes a `branch` as
# a parameter.
# 
# Given a branch, we use the `askYesNo` function with the question pinned to that branch. That gives us the *direction* (the lower branch) we need to follow. We store this new branch in the `newBranch` variable.
# 
# If this branch ends on an animal, we call `endGame`, otherwise, we call the
# `walkTree` function again, with the lower branch. Makes sense, right?

# <codecell>

def walkTree(branch):
    # Since we are currently at a branch, we can ask its question.
    direction = askYesNo( branch["question"] )
    newBranch = lowerBranch(branch, direction)

    # If answer to our question is not an animal, then we have another
    # branch, and we just recall this function with the new branch:
    # Otherwise, we end the game.

    if foundAnimal(newBranch):
        endGame(newBranch, branch, direction)
    else:
        walkTree(newBranch)

# <markdowncell>

# The `walkTree` needs some new functions to help it out. We need:
# 
#   * `lowerBranch` to look at the lower branch
#   * `foundAnimal` to see if we have found an animal
#   * `endGame` to end the round
# 
# We'll do these in order.

# <headingcell level=2>

# Looking at a Lower Branch

# <markdowncell>

# Moving from branch to branch is called *walking the tree*, so moving
# from one branch to another must be *a step*, right?
# 
# If the player answers *yes* to a question, we need to follow the
# `"yes"` branch. Which direction we follow is given by the `direction`
# parameter. If `direction` is `True`, we return the branch on the
# `"yes"`, and  `direction` is `False`, we return the branch on the
# `"no"`.

# <codecell>

def lowerBranch(branch, direction):
    if direction:
        return branch["yes"]
    else:
        return branch["no"]

# <markdowncell>

# To test this function, we can use the top of our `animals` as a
# branch, and see what we end up when we give it a `True` or `False`
# for the `direction`.
# 
# Of course, when we start, the `False` direction gives us a
# subbranch. Let's create a variable to this, and then test that to see
# if it ends with either `"cow"` or `"elephant"`. What this means is
# that if the `lowerBranch` gives us something wrong, then our tests
# will not be right, and we'll be able to fix it.

# <codecell>

assert( lowerBranch(animals, False) == "fish" )
  
subbranch = lowerBranch(animals, True) 
assert( lowerBranch(subbranch, False) == "cow")
assert( lowerBranch(subbranch, True) == "elephant")

# <headingcell level=3>

# Found an Animal?

# <markdowncell>

# This little function will make it more clear that we have reached the
# end of the tree and we have bagged ourselves an animal.
# 
# This function returns `True` if we have an animal (that is a string
# that has the name of the animal) and `False` if we have another branch
# with a question.
# 
# We know we have an animal if the `branch` that we pass in is a
# *string*, and we are on a branch if we have a *dictionary*. 
# We use the `isinstance` function that we've seen before to check what we have.
# To check if we have a *dictionary*, we give it the word, `dict`.

# <codecell>

def foundAnimal(branch):
    return not isinstance(branch, dict)

# <markdowncell>

# To test this function, we really need just need to pass in both types
# of data. Our `animals` variable is a good example of a dictionary we
# can use.

# <codecell>

assert(     foundAnimal("dog") )
assert( not foundAnimal(animals) )

# <headingcell level=2>

# Ending a Game Round

# <markdowncell>

# When we call the `endGame` function, we've walk down to the bottom and
# found ourselves with an animal. This animal *may be* what our player
# is thinking, in which case, we've won. Or, the player has a new animal
# for us to learn about.

# <codecell>

def endGame(branch, parent, direction):
    if askYesNo( "Is your animal " + showAnimal(branch) + "?" ):
        print "Yay! I guessed it!"
    else:
        storeNewAnimal(parent, whichSide(direction), branch)

# <markdowncell>

# This function calls two other functions:
# 
#   * `showAnimal` will show an animal properly. I'll tell you what I mean in just a minute.
#   * `storeNewAnimal` will replace the position of an animal with a new subbranch.
#   * `whichSide` will convert a `True` direction into a `"yes"` so that we know where to store our new animal.
# 
# Let's talk about the `whichSide` function first.

# <headingcell level=2>

# Which Side is it On?

# <markdowncell>

# A helper function changes `True` to the string `"yes"` and `False`
# to `"no"` string, so that we can we know where to store our new animal.

# <codecell>

def whichSide(yes):
    if yes:
        return "yes"
    else:
        return "no"

# <markdowncell>

# Let's test our little `whichSide` function:

# <codecell>

assert(  whichSide(True) == "yes" )
assert(  whichSide(False) == "no" )

# <headingcell level=2>

# Showing an Animal

# <markdowncell>

# What is the difference between a cow and an octopus? One starts
# with an "A" and the other starts with an "N" ... get it? "a cow"
# and "aN octopus"? I guess that is a really bad joke, but if you are
# going to print a sentence in English with the animal word, we need
# to know if we should put a string "a" or "an" in front of it.
# 
# We make a `showAnimal` function that decides which to print.

# <codecell>

def showAnimal(animal):
    t = animal.lower()
    if t.startswith('a') or t.startswith('e') or t.startswith('i') or t.startswith('o') or t.startswith('u'):
        return "an " + animal
    else:
        return "a " + animal

# <markdowncell>

# Let's make sure that our function works the way we expect:

# <codecell>

assert( showAnimal("dog").startswith("a ") )
assert( showAnimal("aardvark").startswith("an ") )
assert( showAnimal("elephant").startswith("an ") )
assert( showAnimal("Ichthyosaur").startswith("an ") )
assert( showAnimal("yak").startswith("a ") )
assert( showAnimal("horse").startswith("a ") )

# <headingcell level=2>

# Storing a New Animal

# <markdowncell>

# The player was thinking of something that our program doesn't know
# about. No problem. We just need to know the name of this animal,
# and a *question* that the program can ask to distinguish it.
# 
# In order to store it back in our `animals` tree... er, pyramid, we
# need to know three things:
# 
#   * **higherBranch** is the point at the end of the branch where we will store
#   * **side** is either "yes" or "no" and gives us the spot in the
#     higher branch to store our *new* branch
#   * **oldAnimal** is the text string with the name of the animal we
#     thought it might be. We need to move this animal down into our
#     new branch.

# <codecell>

def storeNewAnimal(higherBranch, side, oldAnimal):
    print "Shoot. What animal were you thinking?"
    newAnimal = raw_input().lower()
        
    print "What question could I ask to distinguish between", showAnimal(oldAnimal), "and", showAnimal(newAnimal), "?"
    newQuestion = raw_input()
        
    higherBranch[side] = {
        "question": turnIntoAQuestion(newQuestion),
        "yes": newAnimal,
        "no": oldAnimal
    }

# <markdowncell>

# After complaining that we lost, we have to ask our player the name of
# the animal he or she was thinking of. To get let our player type
# something that and then store it, we use the `raw_input`
# function. Whatever is typed, comes back, and we convert it to lower
# case, so `"Porcupine"` is assigned to `newAnimal` as `"porcupine"`.
# 
# Next we ned to get a question that we will store in our new branch to
# decided between the old animal and the new one we are just learning
# about.
# 
# To store our new branch, we just set either the `"yes"` or `"no"` in
# the `higherBranch` to our new dictionary that has the question and
# both animals.
# 
# You've seen the `showAnimal` function above, but we need to write a
# helper function called, `turnIntoAQuestion`.

# <headingcell level=3>

# Turning a Statement into a Question

# <markdowncell>

# When we ask the player for a new question, we need to make sure that
# what is given to us, doesn't end with a question mark, we need to add it.
# 
# To do this, we use the `endswith` function (which is similar to
# `startswith`, but checks the end of the text string.

# <codecell>

def turnIntoAQuestion(words):
    if words.endswith("?"):
        return words
    else:
        return words + "?"

# <markdowncell>

# We can easily test this, right? We just have to make sure that every
# string of text letters we give it, gives us back a string of text that
# ends with a question mark.

# <codecell>

assert( turnIntoAQuestion("This isn't a question").endswith("?") )
assert( turnIntoAQuestion("Is this a question?").endswith("?") )

# <headingcell level=3>

# Yes and No Questions

# <markdowncell>

# Almost all of the questions we ask the player of our game are
# *yes* and *no* questions. However, we want to make sure that if the
# player types "yes" or "y", or even "Yes" (notice the capital) to all
# mean *yes*.
# 
# In this `isYes` function, we take the player's `answer` and first
# convert it to lower-case. This turns "Yes" into "yes" and "N" into
# "n". We do this to make the comparison easier.
# 
# Since "Yes" and "y" will be the same to our program, we really just
# need to look at the first letter. To do this, we use the `startswith`
# *method*. A method is like a function, but it only works by being
# *attached* to something.
# 
# In this function, we can a string of text characters, and attach this
# `lower` method to to, and then attach a `startswith` function to
# that. We end up with `True` if our player types "Yes" or "y".

# <codecell>

def isYes(answer):
    if answer.lower().startswith("y"):
        return True
    else:
        return False

# <markdowncell>

# We can make sure this function works, by making a few calls to `assert`:

# <codecell>

assert(     isYes("Yes") )
assert(     isYes("Y") )
assert(     isYes("yes") )
assert(     isYes("y") )
assert( not isYes("No") )
assert( not isYes("n") )

# <markdowncell>

# We need a function that lets us give it a question that it will show
# to the player, and then allow our player to type in something. Showing
# things are easy, we just use `print`, but how do we get *something*?
# 
# Python has a function, `raw_input` that when called, Python stops,
# lets the player type something, and whatever the player types is given
# back to us. We will take that, and give it to our `isYes` function.
# 
# This means that the `askYesNo` function will take a string as a
# question, and return either `True` for *yes* and `False` for *No*.

# <codecell>

def askYesNo(question):
    print question,
    return isYes( raw_input() )

# <headingcell level=2>

# Finishing Touches

# <markdowncell>

# We have now written all of the functions, including our big function, `playGame`. In fact, all we need to do is just call it:

# <codecell>

playGame()

# <markdowncell>

# If you **Play** that cell, we'll get an error, because in the Notebook, the `raw_input` function doesn't work. What we need to do is make a **Python Program**. Here's what you do:
# 
#   * Click the **File** menu above.
#   * Select **Download As...**
#   * Select **Python**.
# 
# This will put a file in your `Downloads` folder that you can
# double-click and play!

