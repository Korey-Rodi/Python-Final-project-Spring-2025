import pywhatkit
import tkinter as tk
# import regex to check phone numbers more effectively
# import pynput to automate enter when chat doesnt send
# import time to allow enough time to enter next window

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
    root = tk.Tk()
    root.title("WhatsApp Messenger GUI")
    root.geometry("400x150")
    root.resizable(False, False)
    root.configure(bg="black")
    phoneNumberPrompt = tk.Label(root, text="Enter Phone Number Below", width=400,background="black",font=("Lato",20))
    phoneNumberPrompt.pack()
    phoneNumberField = tk.Entry(root, width=400, background="white",font=("arial",16),foreground="black")
    phoneNumberField.pack()
    phoneNumberField.insert(0,"+1###-###-####")
    textMessagePrompt = tk.Label(root, text="Enter Your Message Below", width=400,background="black",font=("Lato",20))
    textMessagePrompt.pack()
    textMessageField = tk.Entry(root, width=400, background="white",font=("arial",16),foreground="black")
    textMessageField.pack()
    textMessageField.insert(0,"Hello,John Doe!")
    sendButton = tk.Button(root, text="Send",width=400)
    sendButton.pack()
    root.mainloop()
    '''
    phoneNumber = input("Enter phone number +1###-###-####: ")
    while checkNumberValid(phoneNumber) == False:
        phoneNumber = input("Enter phone number +1###-###-####: ")
    phoneNumber = phoneNumber.replace("-", "")
    textMessage = input("enter your message: ")
    while checkMessage(textMessage) == False:
        textMessage = input("enter your message: ")
    pywhatkit.sendwhatmsg_instantly(phoneNumber, textMessage)
    '''

if __name__ == "__main__":
    main()