import pywhatkit
import tkinter as tk
import re

def checkNumberValid(phoneNumber):
    pattern = r"\+\d{4}-\d{3}-\d{4}"
    if re.fullmatch(pattern,phoneNumber):
        #print(re.fullmatch)
        return True
    else:
        return False
    
def checkMessage(textMessage):
    if len(textMessage) >= 1:
        #print("Valid Message")
        return True
    else:
        #print("Invalid message. Please input a new message")
        return False
    
def MyClick(phoneNumberField,textMessageField):
    phoneNumber = phoneNumberField.get()
    textMessage = textMessageField.get()
    if checkNumberValid(phoneNumber) and checkMessage(textMessage) == True:
        sendingMessage(phoneNumber,textMessage)
    else:
        textMessageField.delete(0,tk.END)
        phoneNumberField.delete(0,tk.END)
        textMessageField.insert(0,"Invalid Message and or Number")
        phoneNumberField.insert(0,"Invalid Message and or Number")


def sendingMessage(phoneNumberFormat,textMessageFormat):
    pywhatkit.sendwhatmsg_instantly(phoneNumberFormat,textMessageFormat)

def sendingMessageandImage(phoneNumberFormat,testMessageFormat,imageFormat):
    pass


def main():
    root = tk.Tk()
    root.title("WhatsApp Messenger GUI")
    root.geometry("400x200")
    root.resizable(False, False)
    root.configure(bg="black")
    phoneNumberPrompt = tk.Label(root, text="Enter Phone Number Below", width=400,background="black",font=("Lato",20))
    phoneNumberPrompt.pack()
    phoneNumberField = tk.Entry(root, width=400, background="white",font=("arial",16),foreground="black",borderwidth=5)
    phoneNumberField.pack()
    phoneNumberField.insert(0,"+1###-###-####")
    textMessagePrompt = tk.Label(root, text="Enter Your Message Below", width=400,background="black",font=("Lato",20))
    textMessagePrompt.pack()
    textMessageField = tk.Entry(root, width=400, background="white",font=("arial",16),foreground="black",borderwidth=5)
    textMessageField.pack()
    textMessageField.insert(0,"Hello,John Doe!")
    imagePrompt = tk.Label(root, text="Attach Image", width=400,background="black",font=("Lato",20))
    imagePrompt.pack()
    sendButton = tk.Button(root, text="Send",width=400,command=lambda: MyClick(phoneNumberField, textMessageField))
    sendButton.pack()
    root.mainloop()

if __name__ == "__main__":
    main()