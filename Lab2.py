#!/usr/local/bin/python3
import sys
sys.path.append('/home/staff/kurban/python')

import csc220

csc220.showForm("This is the comment on the form area.")  

textarea = csc220.getInput('textarea')
textbox = csc220.getInput('textbox')

print ("<h2>This is at the bottom and can be used for any html output </h2><br>")

print ("textbox contains <b>{}</b> <br>".format( textbox ))
print ("textarea contains <b>{}</b> <br>".format( textarea ))


print("My Username is syu34")

def printLeftCircle():
    return print("""
   <circle cx="50" cy="50" r="40" stroke="green" stroke-width="10" fill="white" />
""")
    
def printRectangle():
    return print("""
  <rect width="200" height="100" x="110" y="0" rx="20" ry="20" fill="lightBlue" />
""")
    
def printRightCircle():
    return print("""
   <circle cx="400" cy="50" r="40" stroke="red" stroke-width="2" fill="white" />
""")

def printName():
    return print("""
    <text x="165" y="55" fill="black">Stephen Yu</text>
""")


print ('<svg height="1000" width="1000">')

# call a user defined function that prints the left circle 
printLeftCircle()
# call a user defined function that prints the right circle 
printRightCircle()
# call a user defined function that prints the rectangle 
printRectangle()
# call a user defined function that prints your name in the rectangle
printName()
print ('</svg>')

# I honor Parkland's core values by affirming that I have 
# followed all academic integrity guidelines for this work.

#Stephen Yu
