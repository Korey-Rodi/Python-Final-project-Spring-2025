#imports
import pywhatkit
# add regex to check phone numbers more effectively
import tkinter as tk

def checkNumberValid(phoneNumber):
    if len(phoneNumber) == 14:
        print("Valid Number")
        return True
    else:
        print("Invalid number or format. Please input a new number")
        return False

def checkMessage(textMessage):
    if len(textMessage) >= 1:
        print("Valid Message")
        return True
    else:
        print("Invalid message. Please input a new message")
        return False

def main():
    phoneNumber = input("Enter phone number +1###-###-####: ")
    while checkNumberValid(phoneNumber) == False:
        phoneNumber = input("Enter phone number +1###-###-####: ")
    phoneNumber = phoneNumber.replace("-", "")
    textMessage = input("enter your message: ")
    while checkMessage(textMessage) == False:
        textMessage = input("enter your message: ")
    pywhatkit.sendwhatmsg_instantly(phoneNumber, textMessage,5)


if __name__ == "__main__":
    main()