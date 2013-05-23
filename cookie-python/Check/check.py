from IPython.display import display, Image
from random import random, randint
import string
import math

def check(number, exercise, *arguments):
    """Checks each exercise in the assignments of the Cookie Python Notebook.

       - `number` is the assignment notebook number, or name.
       - `exercise` the exercise number, starting with 1.
       - Other parameters are values specific to the exercise."""

    value = None
    if len(arguments) > 0:
        value = arguments[0]

    if number == 1:
        return check1(exercise, value)
    elif number == 2:
        return check2(exercise, value)
    elif number == 3:
        return check3(exercise, arguments[0], arguments[1])
    else:
        print "Assignment", number, "Exercise", exercise, "is not completed."

def check1(exercise, value):
    """Check the exercises for Assignment 01-Buckets and Variables.

    Parameters:
    * `exercise` - The exercise number from 1 to 5
    * `value` - The parameter value for the exercise number."""

    if exercise == 1:
        if value == 42:
            print "You did it! Have a cookie."
            return Image(url='http://openclipart.org/image/250px/svg_to_png/130009/cookie.png')
        else:
            print "You need to change the _ symbol to the number 42."

    elif exercise == 2:
        if value == 2.5:
            print "You did it! Have another cookie."
            return Image(url='http://openclipart.org/image/250px/svg_to_png/130009/cookie.png')
        else:
            print "You need to change the _ symbol to the number 2.5"

    elif exercise == 3:
        if value != None and len(value) > 2:
            print "Hello, " + value + ", it is nice to meet you."
            return Image(url='http://openclipart.org/image/250px/svg_to_png/167186/Hello.png')
        else:
            print 'You need to change the _ symbol to the number you name inside quotes, like "David"'


    elif exercise == 4:
        if value != None and value.find("at's ball") > -1:
            print "Good job! Here is Pat's shiny ball:"
            return Image(url='http://openclipart.org/image/250px/svg_to_png/1413/molumen_blue_cristal_ball.png')
        else:
            print "The sentence should say something about Pat's ball."

    elif exercise == 5:
        if value != None and value.find("\n") > -1:
            print "Good job! This deserves an award."
            show_award()
        else:
            print 'You need to change the _ symbol to a string with more than one line.'

def show_award():
    return Image(url='http://openclipart.org/image/250px/svg_to_png/151087/logo_mogo.png')

def check2(exercise, value):
    """Check the exercises for Assignment 02-Operators.

    Parameters:
    * `exercise` - The exercise number from 1 to 2
    * `value` - The parameter value for the exercise number."""

    if exercise == 1:
        pi = str(value)
        if pi.startswith("3.14"):
            l = len(pi)-2
            print "Good job! You know pi to", l, "places. Have some pie on me...."
            return Image(url='http://25.media.tumblr.com/tumblr_mc7g0fQWLF1qlu5vyo1_500.jpg')
        else:
            print "Just like our previous assignments, you need to replace the _ symbol above with the answer. In this case, the answer begins with 3. something something."

    elif exercise == 2:
        pi1 = str(value)
        pi2 = str(math.pi)

        print pi2
        print

        if pi1.startswith("3.14"):
            d = len(pi2) - len(pi1)
            if d <= 0:
                print "Wow! Your version of pi is great! You are amazing. However, math.pi may be a little quicker to type."
            elif d > 0:
                print "Python stores", d, "more digits to pi. So maybe you should use that variable in the next exercise."

    elif exercise == 3:
        if value > 28 and value < 29:
            print "Good job! The area is", value, " since the radius is half the diameter, r must be 3."
        else:
            print "Hint: The diameter is 6, but the formula uses `r` which is the radius."

# This function is used in assignment/lesson 03- Calling Functions
def dice(side):
    "This function takes a number from 1 to 6, and it returns a picture of a six-sided die with that number on it."
    if side == 1:
        return Image('http://openclipart.org/image/250px/svg_to_png/96079/dado_1.png')
    elif side == 2:
        return Image('http://openclipart.org/image/250px/svg_to_png/96085/dado_2.png')
    elif side == 3:
        return Image('http://openclipart.org/image/250px/svg_to_png/96091/dado_3.png')
    elif side == 4:
        return Image('http://openclipart.org/image/250px/svg_to_png/96097/dado_4.png')
    elif side == 5:
        return Image('http://openclipart.org/image/250px/svg_to_png/96103/dado_5.png')
    elif side == 6:
        return Image('http://openclipart.org/image/250px/svg_to_png/96109/dado_6.png')
    else:
        print "The number for 'side' must be 1, 2, 3, 4, 5, or 6."

def check3(exercise, first, second):
    """Check the exercises for Assignment 03-Calling Functions.

    Parameters:
    * `exercise` - The exercise number from 1 to 2
    * `first` - The parameter value for the exercise number."""

    if exercise == 1:
        if first and first > 0:
            print "The square root of your random number is", first

    elif exercise == 2:
        if first == second:
            print "Yes, you guessed right. Have a cookie shaped like a multiplication sign."
            return Image('http://openclipart.org/image/250px/svg_to_png/68365/x-cookie.png')
        else:
            print "Nope. Your random number was", second, "since", math.sqrt(second), "x", math.sqrt(second), "is", second

def show_pony(name):
    """Shows a picture of a pony based on its name."""
    if name == "Applejack":
        return Image("http://images2.wikia.nocookie.net/__cb20130419182238/mlp/images/thumb/d/d8/Applejack_S01E13_cropped.png/250px-Applejack_S01E13_cropped.png")
    elif name == "Fluttershy":
        return Image("http://images3.wikia.nocookie.net/__cb20130317084227/mlp/images/thumb/3/3a/Fluttershy_trotting_CROPPED_S2E7.png/250px-Fluttershy_trotting_CROPPED_S2E7.png")
    elif name == "Scootaloo":
        return Image("http://images2.wikia.nocookie.net/__cb20130109015850/mlp/images/thumb/d/de/Scootaloo_offering_help_crop_S1E24.png/250px-Scootaloo_offering_help_crop_S1E24.png")
    elif name == "Caramel":
        return Image("http://images4.wikia.nocookie.net/__cb20110706134227/mlp/images/thumb/0/09/Caramel.png/250px-Caramel.png")
    elif name == "Rainbow Dash":
        return Image("http://images1.wikia.nocookie.net/__cb20130307050703/mlp/images/thumb/4/4b/Rainbow_Dash_Wonderbolt_fantasy_cropped_S1E3.png/250px-Rainbow_Dash_Wonderbolt_fantasy_cropped_S1E3.png")
    elif name == "Big McIntosh":
        return Image("http://images3.wikia.nocookie.net/__cb20111110054616/mlp/images/thumb/2/2e/Big_McIntosh_onstage_S2E05.png/250px-Big_McIntosh_onstage_S2E05.png")
    elif name == "Braeburn":
        return Image("http://images2.wikia.nocookie.net/__cb20120715144761/mlp/images/thumb/3/36/Braeburn_S1E21_thumb.png/250px-Braeburn_S1E21_thumb.png")
    elif name == "Cheerilee":
        return Image("http://images2.wikia.nocookie.net/__cb20111015001440/mlp/images/a/a3/Cheerilee_next_to_easel_cropped_S1E12.png")
    else:
        print "I don't have a picture of a pony named,", name

def is_prime(number):
    if number < 1:
        return False
    elif number < 4:
        return True
    elif number % 2 == 0:
        return False
    else:
        for i in range(5, number / 2, 2):
            if number % i == 0:
                return False
        return True 

def pokemon(monster):
    if monster["name"] == "Charmander":
        return Image("http://cdn.bulbagarden.net/upload/thumb/7/73/004Charmander.png/185px-004Charmander.png")
    elif monster["name"] == "Pikachu":
        return Image("http://cdn.bulbagarden.net/upload/thumb/0/0d/025Pikachu.png/205px-025Pikachu.png")
    elif monster["name"] == "Bulbasaur":
        return Image("http://cdn.bulbagarden.net/upload/thumb/2/21/001Bulbasaur.png/170px-001Bulbasaur.png")
    else:
        print "Sorry, I don't know anything about that Pokemon."
