import pyfiglet
import time

def textgen():
   print("slant, banner3-D, block, big, isometric1")
   font1 = input("what font?")
   thetext = input("What is the text?")
   ascii_art = pyfiglet.figlet_format(thetext, font=font1)
   print(ascii_art)
   time.sleep(1)
   with open("output.txt", "w") as file:
      file.write(ascii_art)
   print("ASCII art saved to output.txt")

textgen()
