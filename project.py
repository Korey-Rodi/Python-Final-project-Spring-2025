import pywhatkit
import tkinter as tk
#import tkinter.filedialog
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

#def sendingMessageandImage(phoneNumberFormat,testMessageFormat,imageFormat):
#    pywhatkit.sendwhats_image(receiver: str, img_path: str, caption: str = "")

def main():
    root = tk.Tk()
    root.title("WhatsApp Messenger GUI")
    root.geometry("400x225")
    root.resizable(True, False)
    root.configure(bg="black")
    phoneNumberPrompt = tk.Label(root,text="Enter Phone Number Below",
                                 background="black",font=("Lato",20))
    phoneNumberPrompt.pack(fill="x")
    phoneNumberField = tk.Entry(root,background="white",
                                font=("arial",16),
                                foreground="black",borderwidth=5,
                                justify="center")
    phoneNumberField.pack(fill="x")
    phoneNumberField.insert(0,"+1###-###-####")
    textMessagePrompt = tk.Label(root,text="Enter Your Message Below",
                                 background="black",font=("Lato",20))
    textMessagePrompt.pack(fill="x")
    textMessageField = tk.Entry(root,background="white",
                                font=("arial",16),foreground="black",
                                borderwidth=5,justify="center")
    textMessageField.pack(fill="x")
    textMessageField.insert(0,"Hello,John Doe!")
    imagePrompt = tk.Label(root,text="Attach Your Image Below", background="black",font=("Lato",20))
    imagePrompt.pack(fill="x")
    imagePromptField = tk.Entry(root,background="white",
                                font=("arial",16),foreground="black",
                                borderwidth=5, justify="center")
    imagePromptField.pack(fill="x")
    imagePromptField.insert(0,"Enter File Directory")
    sendButton = tk.Button(root, text="Send",
                           command=lambda: MyClick(phoneNumberField, textMessageField))
    sendButton.pack(fill="x")
    root.mainloop()

if __name__ == "__main__":
    main()