import pywhatkit
import tkinter as tk
from tkinter import messagebox
import re
import pygame

def play_error_sound():
    pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("/Users/koreyrodi/Desktop/errorsound.wav")
    pygame.mixer.music.play()

def play_send_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("/Users/koreyrodi/Desktop/sendingSound.mp3")
    pygame.mixer.music.play()

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
    phoneNumberField.config(highlightbackground="black", highlightthickness=1)
    textMessageField.config(highlightbackground="black", highlightthickness=1)
    
def MyClick(phoneNumberField,textMessageField):
    phoneNumber = phoneNumberField.get()
    textMessage = textMessageField.get()
    if checkNumberValid(phoneNumber) and checkMessage(textMessage) == True:
        sendingMessage(phoneNumber,textMessage,phoneNumberField,textMessageField)
    elif checkNumberValid(phoneNumber) == False and checkMessage(textMessage) == False:
        phoneNumberField.delete(0,tk.END)
        textMessageField.delete(0,tk.END)
        phoneNumberField.config(highlightbackground="#cc0606",highlightthickness=1)
        textMessageField.config(highlightbackground="#cc0606",highlightthickness=1)
        phoneNumberField.insert(0,"Invalid Number")
        textMessageField.insert(0,"Invalid Message")
        play_error_sound()
        messagebox.showerror("Error", "Please make sure to input a valid Phone Number and Message")
    elif checkNumberValid(phoneNumber) == False:
        phoneNumberField.delete(0,tk.END)
        phoneNumberField.config(highlightbackground="#cc0606",highlightthickness=1)
        phoneNumberField.insert(0,"Invalid Number")
        play_error_sound()
        messagebox.showerror("Error", "Please make sure to input valid Phone Number")
    elif checkMessage(textMessage) == False:
        textMessageField.delete(0,tk.END)
        textMessageField.config(highlightbackground="#cc0606",highlightthickness=1)
        textMessageField.insert(0,"Invalid Message")
        play_error_sound()
        messagebox.showerror("Error", "Please make sure to input valid text message")

def sendingMessage(phoneNumberFormat,textMessageFormat,phoneNumberField,textMessageField):
    phoneNumberField.config(highlightbackground="#146604",highlightthickness=3)
    textMessageField.config(highlightbackground="#146604",highlightthickness=3)
    play_send_sound()
    pywhatkit.sendwhatmsg_instantly(phoneNumberFormat,textMessageFormat)

def main():
    messagebox.showinfo("information", "This is an extension of your whatsApp web account" \
    " please make sure you have an active account, and all input fields are correctly entered")
    root = tk.Tk()
    root.title("WhatsApp Messenger GUI")
    root.geometry("400x200")
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
    sendButton.pack(fill="x",expand=True)
    root.mainloop()

if __name__ == "__main__":
    main()