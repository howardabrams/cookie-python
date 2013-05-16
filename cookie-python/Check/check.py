from IPython.display import display, Image
from random import random, randint
import string

def check(number, exercise, *arguments):
    """Checks each exercise in the assignments of a Notebook.

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
    else:
        print "Assignment", number, "Exercise", exercise, "is not completed."

def check1(exercise, value):
    if exercise == 1:
        if value == 42:
            print "You did it! Have a cookie."
            return Image(url='http://is.gd/Zc7ym2')
        else:
            print "You need to change the _ symbol to the number 42."

    elif exercise == 2:
        if value == 2.5:
            print "You did it! Have another cookie."
            return Image(url='http://is.gd/Zc7ym2')
        else:
            print "You need to change the _ symbol to the number 2.5"

    elif exercise == 3:
        if value != None and len(value) > 2:
            print "Hello, " + value + ", it is nice to meet you."
            return Image(url='http://image.shutterstock.com/display_pic_with_logo/627865/627865,1324369583,1/stock-vector--two-dogs-greet-each-other-91135244.jpg')
        else:
            print 'You need to change the _ symbol to the number you name inside quotes, like "David"'


    elif exercise == 4:
        if value != None and value.find("at's ball") > -1:
            print "Good job! Here is Pat's ball:"
            return Image(url='http://is.gd/utzKZX')
        else:
            print "The sentence should say something about Pat's ball."

    elif exercise == 5:
        if value != None and value.find("\n") > -1:
            print "Good job! This deserves an award."
            return Image(url='http://is.gd/GLWJuE')
        else:
            print 'You need to change the _ symbol to a string with more than one line.'

def check2(exercise, value):
    if exercise == 1:
        pi = str(value)
        if pi.startswith("3.14"):
            l = len(pi)-2
            print "Good job! You know pi to", l, "places. Have some pie on me...."
            return Image(url='http://25.media.tumblr.com/tumblr_mc7g0fQWLF1qlu5vyo1_500.jpg')
        else:
            print "Just like our previous assignments, you need to replace the _ symbol above with the answer. In this case, the answer begins with 3. something something."

    elif exercise == 2:
        if value > 28 and value < 29:
            print "Good job! The area is", value, " since the radius is half the diameter, r must be 3."
        else:
            print "Hint: The diameter is 6, but the formula uses `r` which is the radius."

def dice(side):
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

# 10 sided: http://openclipart.org/people/wirelizard/ten_sided_dice.svg
