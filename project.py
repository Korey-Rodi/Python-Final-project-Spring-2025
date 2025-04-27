import pywhatkit
import tkinter as tk
from tkinter import messagebox
import re

def checkNumberValid(phoneNumber):
    pattern = r"\+\d{4}-\d{3}-\d{4}"
    if re.fullmatch(pattern,phoneNumber):
        return True
    else:
        return False
    
def checkMessage(textMessage):
    if len(textMessage) >= 1:
        return True
    else:
        return False
def clearFields(phoneNumberField,textMessageField):
    phoneNumberField.delete(0,tk.END)
    textMessageField.delete(0,tk.END)
    
def MyClick(phoneNumberField,textMessageField):
    phoneNumber = phoneNumberField.get()
    textMessage = textMessageField.get()
    if checkNumberValid(phoneNumber) and checkMessage(textMessage) == True:
        sendingMessage(phoneNumber,textMessage)
    if checkNumberValid(phoneNumber) == False:
        phoneNumberField.delete(0,tk.END)
        phoneNumberField.insert(0,"Invalid Number")
        messagebox.showwarning("Warning", "Please make sure to input valid Phone Number")
    if checkMessage(textMessage) == False:
        textMessageField.delete(0,tk.END)
        textMessageField.insert(0,"Invalid Message")
        messagebox.showwarning("Warning", "Please make sure to input valid text message")

def sendingMessage(phoneNumberFormat,textMessageFormat):
    pywhatkit.sendwhatmsg_instantly(phoneNumberFormat,textMessageFormat)

def main():
    root = tk.Tk()
    root.title("WhatsApp Messenger GUI")
    root.geometry("400x180")
    messagebox.showinfo("information", "this is an extension of your whatsApp web account" \
    " please make sure you have an active account, and all input fields are correctly entered")
    root.resizable(True, False)
    root.configure(bg="black")
    phoneNumberPrompt = tk.Label(root,text="Enter Phone Number Below",
                                 background="black",font=("Lato",20))
    phoneNumberPrompt.pack(fill="x")
    phoneNumberField = tk.Entry(root,background="white",
                                font=("arial",16),
                                foreground="black",borderwidth=5,
                                justify="center")
    phoneNumberField.pack(fill="x",expand=True)
    phoneNumberField.insert(0,"+1###-###-####")
    textMessagePrompt = tk.Label(root,text="Enter Your Message Below",
                                 background="black",font=("Lato",20))
    textMessagePrompt.pack(fill="x")
    textMessageField = tk.Entry(root,background="white",
                                font=("arial",16),foreground="black",
                                borderwidth=5,justify="center")
    textMessageField.pack(fill="x", expand=True)
    textMessageField.insert(0,"Hello,John Doe!")
    clearButton = tk.Button(root, text = "Clear all Fields",
                            command=lambda: clearFields(phoneNumberField,textMessageField))
    clearButton.pack(fill="x", expand=True)
    sendButton = tk.Button(root, text="Send",
                           command=lambda: MyClick(phoneNumberField, textMessageField))
    sendButton.pack(fill="x", expand=True)
    root.mainloop()

if __name__ == "__main__":
    main()