from easygui import*
import sys

while 1:
        msgbox("Welcome to Contech")
        msg="Which sites would you like"
        title="Site Names"
        choices=["Amazon","Myntra","Jabong","Snapdeal"]
        choice=choicebox(msg, title, choices)   
        if choice=="Amazon":
	   choice=choicebox["Clothes","Accessories","Electronics"]
	elif choice=="Myntra":
	   choice=choicebox["Jeans","T-Shirts","Shirts"]
	elif choice=="Jabong":
	   choice=choicebox["Sweat Shirts","Shorts","Shoes"]
	elif choice=="Snapdeal":
	   choice=choicebox["Sports Wear","Watches","Belts"] 
        msgbox("You chose: "+str(choice),"Site Names")
        msg="Do you want to continue?"
        title="Please Confirm"
        if ccbox(msg, title):
           pass
        else:
           sys.exit(0)
