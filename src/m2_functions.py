"""
Practice DEFINING and CALLING
     FUNCTIONS

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Amanda Stouder,
         their colleagues and Jess Thuer.
"""  # DONE PUT YOUR NAME IN THE ABOVE LINE.

###############################################################################
#
# DONE
#   Allow this module to use the  rosegraphics.py  module by marking the
#     src
#   folder in this project as a "Sources Root", as follows:
#
#     In the Project window (to the left), right click on the src  folder,
#     then select  Mark Directory As  ~  Sources Root.
#
###############################################################################

import rosegraphics as rg


def main():
    sides(3,4)
    draw('red',10)
    """"
    TESTS the functions that you will write below.
    You write the tests per the _TODO_s below.
    """


###############################################################################
#
# DONE  Define a function immediately blow this _TODO_.
#   It takes two arguments that denote, for a right triangle,
#   the lengths of the two sides adjacent to its right angle,
#   and it returns the length of the hypotenuse of that triangle.
#     HINT: Apply the Pythagorean theorem.
#
#   You may name the function and its parameters whatever you wish.
#
# DONE  In main, CALL your function and print the returned value,
#   to test whether you defined the function correctly.
#
###############################################################################
def sides(adj1,adj2):
    import math
    hyp = math.sqrt(adj1**2 + adj2**2)
    print(hyp)

###############################################################################
#
# DONE  Define a function immediately below this _TODO_.
#   It takes two arguments:
#     -- a string that represents a color (e.g. 'red')
#     -- a positive integer that represents the thickness of a Pen.
#
#   The function:
#     -- Constructs a TurtleWindow.
#     -- Constructs two SimpleTurtles, where:
#        - one has a Pen whose color is "green" and has the GIVEN thickness
#        - the other has a Pen whose color is the GIVEN color
#            and whose thickness is 5
#     -- Makes the first (green) SimpleTurtle move FORWARD 100 pixels, and
#        makes the other SimpleTurtle move BACKWARD 100 pixels.
#
#   You may name the function and its parameters whatever you wish.
#
# DONE  In main, CALL your function and print the returned value,
#   to test whether you defined the function correctly.
#
###############################################################################
def draw(color,pen_thickness):
        window = rg.TurtleWindow()
        t1 = rg.SimpleTurtle('turtle')
        t1.pen = rg.Pen('green',pen_thickness)
        t1.forward(100)
        t2 = rg.SimpleTurtle('turtle')
        t2.pen = rg.Pen(color,5)
        t2.backward(100)
        window.close_on_mouse_click()




###############################################################################
#
# DONE
#   COMMIT-and-PUSH your work (after changing this TO-DO to DONE).
#
#   As a reminder, here is how you should do so:
#     1. Select   VCS   from the menu bar (above).
#     2. Choose  Commit  from the pull-down menu that appears.
#     3. In the  Commit Changes  window that pops up:
#          - HOVER over the  Commit  button
#              (in the lower-right corner of the window)
#          - CLICK on  Commit and Push.
#          - Select  Push  when asked.
#
#   COMMIT adds the changed work to the version control on your computer
#   and PUSH adds the changed work into your Github repository in the "cloud".
#
#    COMMIT-and-PUSH your work as often as you want, but at least for each
#    module after you have tested the module and believe that it is correct.
#
###############################################################################

# -----------------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# -----------------------------------------------------------------------------
main()
