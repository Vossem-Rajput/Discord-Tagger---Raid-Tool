import pyautogui
import time
import colored 
from colored import fg, attr
color = fg('blue')
color2 = fg('red')
color3 = fg('violet')
color4 = fg('yellow')
color5 = fg('green')
color6 = fg('#00FFFF')
reset = attr('reset')
print(color6 + "██████╗░██╗░██████╗░█████╗░░█████╗░██████╗░██████╗░  ████████╗░█████╗░░██████╗░░██████╗░███████╗██████╗░")
print(color6 +"██╔══██╗██║██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ╚══██╔══╝██╔══██╗██╔════╝░██╔════╝░██╔════╝██╔══██╗")
print(color6+"██║░░██║██║╚█████╗░██║░░╚═╝██║░░██║██████╔╝██║░░██║  ░░░██║░░░███████║██║░░██╗░██║░░██╗░█████╗░░██████╔╝")
print(color6 +"██║░░██║██║░╚═══██╗██║░░██╗██║░░██║██╔══██╗██║░░██║  ░░░██║░░░██╔══██║██║░░╚██╗██║░░╚██╗██╔══╝░░██╔══██╗")
print(color6 +"██████╔╝██║██████╔╝╚█████╔╝╚█████╔╝██║░░██║██████╔╝  ░░░██║░░░██║░░██║╚██████╔╝╚██████╔╝███████╗██║░░██║")
print(color6 +"╚═════╝░╚═╝╚═════╝░░╚════╝░░╚════╝░╚═╝░░╚═╝╚═════╝░  ░░░╚═╝░░░╚═╝░░╚═╝░╚═════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝"+reset)
print("")
print(color6+"██╗░░░██╗██████╗░░░░░█████╗░  ██████╗░██╗░░░██╗  ██╗░░░██╗░█████╗░░██████╗░██████╗███████╗███╗░░░███╗")
print(color6+"██║░░░██║╚════██╗░░░██╔══██╗  ██╔══██╗╚██╗░██╔╝  ██║░░░██║██╔══██╗██╔════╝██╔════╝██╔════╝████╗░████║")
print(color6+"╚██╗░██╔╝░░███╔═╝░░░██║░░██║  ██████╦╝░╚████╔╝░  ╚██╗░██╔╝██║░░██║╚█████╗░╚█████╗░█████╗░░██╔████╔██║")
print(color6+"░╚████╔╝░██╔══╝░░░░░██║░░██║  ██╔══██╗░░╚██╔╝░░  ░╚████╔╝░██║░░██║░╚═══██╗░╚═══██╗██╔══╝░░██║╚██╔╝██║")
print(color6+"░░╚██╔╝░░███████╗██╗╚█████╔╝  ██████╦╝░░░██║░░░  ░░╚██╔╝░░╚█████╔╝██████╔╝██████╔╝███████╗██║░╚═╝░██║")
print(color6+"░░░╚═╝░░░╚══════╝╚═╝░╚════╝░  ╚═════╝░░░░╚═╝░░░  ░░░╚═╝░░░░╚════╝░╚═════╝░╚═════╝░╚══════╝╚═╝░░░░░╚═╝"+reset)
print("")
print("")
print("")
print("")
print("")
print(color5+"Starting the Tagger"+reset)
print("")
print("")
print("")

tag1 = "@everyone"
tag2 = "@here"
msg = input(color2+"Please enter the message you want to Spam: "+reset)
print("")
n = input(color2+"How many times you want to Spam the tags with the desired message? = "+reset)
print("")
print("")
print("")
print("")
print("")
print("")
print(color4+"Checking the Tagger")
print("Check Done: No Errors")
print("Activating the Clock!"+reset)
print("")
print("")
print("")
print("")

seconds = 10
print("")
print("")
print("")
print("")
print("")
print("")

for i in range(seconds):
    print(str(seconds - i) + color4 +" Seconds remaining before the Tagging Starts."+reset)
    time.sleep(1)

print(color4+"Starting the Tagger."+reset)


for i in range(0, int(n)):
    pyautogui.typewrite(tag1 + msg + tag2 + '\n')

print(color5+"Tagger has successfully executed it's given task!")
print("")
print("")
print("")
print(color+"Made by Vossem#0009"+reset)
print("")
print("")
print("")
print("")
print("")
print("")
input("Thanks for using Discord Tagger by Vossem v2.0! Press any key to exit!")
