import random
#Creating GUI with tkinter
import tkinter
from tkinter import *
import re



def start(): 
  EntryBox.delete("0.0",END)
  ChatLog.config(state=NORMAL)
  ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
  reply = reply = "Hello! Welcome to ((insert store name)). We hope everything was to your liking. Ready to check out?"
  ChatLog.insert(END, "Aria: " + str(reply) + '\n\n')
  ChatLog.config(state=DISABLED)
  ChatLog.yview(END)

  #Create Button to checkout
  checkoutButton = Button(base, font=("Verdana",12,'bold'), text="Checkout", width="12", height=5, bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff', command= checkout )
  checkoutButton.place(x=6, y=401, height=90)


#BOT'S RESPONSE BANK
jokes = ["What do you call a pig that does karate? Pork chop.",
         "How do you organize a space party? You planet.",
         "What job did the frog have at the hotel? Bellhop.",
         "What do you call an alligator in a vest? An investigator.",
         "What do you call a lazy kangaroo? A pouch potato."]

greetings = ["Hello.", "Hi!", "Hello there.", "Salutations.", "Greetings.", "Nice to meet you!", "Nice to see you.", "Howdy."]
greetings_lower = [i.lower() for i in ["Hello", "Hi!", "Hi", "Hello there", "Salutations", "Greetings", "Nice to meet you!", "Hiya!", "Nice to see you", "Howdy"]]

gratitude_res = ["You're welcome!", "Happy to help!", "No problem!", "My pleasure!", "Have a great day!"]

#TAKES TYPED MESSAGES FROM USER AND OUTPUTS A REPLY+EMOTION FROM BOT
def getReply(message):
  if message != '': 
      if 'who' in message and 'you' in message:
          reply = "My name is Aria! I was designed in 2020 to help with internet transactions. Nice to meet you!"
          emotion('wink')
      elif 'joke' in message:
          reply = random.choice(jokes)
          emotion('laugh')
      elif message in greetings or message in greetings_lower:
          reply = random.choice(greetings)
      elif message == "bye":
          reply = "Bye-bye! Thanks for chatting!"
      elif 'how are you' in message:
          reply = "I'm doing great! Thanks for asking!"
      elif 'thank' in message: 
          reply = random.choice(gratitude_res)
      elif 'hours' in message:
          reply = "We're open every day from 10AM to 10PM."
      else:
          reply = "Sorry, I don't understand"
          emotion('confused')
  return reply


#ASKS THE USER TO SELECT ITEMS
def checkout():
  EntryBox.delete("0.0",END)
  ChatLog.config(state=NORMAL)
  ChatLog.config(foreground="#442265", font=("Verdana", 12 ))
  reply = 'Great! Please enter the products that you would like to check out.'
  ChatLog.insert(END, "Aria: " + str(reply) + '\n\n')
  ChatLog.config(state=DISABLED)
  ChatLog.yview(END)
  listbox.place(x=60, y=131, height=150, width=265)

  confirmButton = Button(base, font=("Verdana",12,'bold'), text="Confirm Items", width="12", height=5, bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff', command= confirm)
  confirmButton.place(x=6, y=401, height=90)
  
  
#THE USER CONFIRMS THEIR ORDER AND THE BOT RETURNS THE TOTAL 
def confirm():  
  EntryBox.delete("0.0",END)
  ChatLog.config(state=NORMAL)
  ChatLog.config(foreground="#442265", font=("Verdana", 12 ))

  # Prints the order that the user made
  values = [listbox.get(idx) for idx in listbox.curselection()]
  print (values)

  value = (', '.join(values))
  print (value)
  
  #listbox.place(x=60, y=131, height=150, width=265)
  listbox.destroy()
  
  # Prints the list of values
  costPattern = r"\d+"
  costMatch = re.findall(costPattern, value)
  print (costMatch)

  newTotal = [int(i) for i in costMatch] 
  
  # Printing modified list  
  print ("Modified list is : " + str(newTotal)) 
  
  # Adding the values
  total = 0
  for ele in range(0, len(newTotal)):
    total = total + newTotal[ele]
 
  # Printing total value
  print("Sum of all elements in given list: ", total)
  
  
  replyConfirm = (', '.join(values))
  replyTotal = 'Your total is: $' + str(total) + '. Thank you for shopping with us today!'
  ChatLog.insert(END, "Aria: " + str(replyConfirm) + '\n\n')
  ChatLog.insert(END, "Aria: " + str(replyTotal) + '\n\n')
  ChatLog.config(state=DISABLED)
  ChatLog.yview(END)
  endButton = Button(base, font=("Verdana",12,'bold'), text="End Conversation", width="12", height=5, bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff', command= endConversation)
  endButton.place(x=6, y=401, height=90)

#ENDS THE CODE
def endConversation():
    base.destroy()

#Unused code to return to the select purchase screen
''''
  backToCheckoutButton = Button(base, font=("Verdana",12,'bold'), text="Back To Checkout", width="15", height=5, bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff', command= checkout )
  backToCheckoutButton.place(x=180, y=401, height=90)
'''

#PRESS TO SEND A MESSAGE TO BOT
def send():
    message = EntryBox.get("1.0",'end-1c').strip()
    EntryBox.delete("0.0",END)
    ChatLog.config(state=NORMAL)
    ChatLog.insert(END, "You: " + message + '\n\n')
    ChatLog.config(foreground="#442265", font=("Verdana", 12 ))

    reply = getReply(message)
    ChatLog.insert(END, "Aria: " + str(reply) + '\n\n')

    ChatLog.config(state=DISABLED)
    ChatLog.yview(END)


#CONDITIONAL FOR EMOTIONS
def emotion(s):
  if s == 'happy': 
    newCanvas.create_image(150, 200, image = smile)
  elif s == 'laugh':
    newCanvas.create_image(150, 200, image = laugh)
  elif s == 'confused':
    newCanvas.create_image(150, 200, image = confused)
  elif s == 'wink':
    newCanvas.create_image(150, 200, image = wink)
  else: 
    newCanvas.create_image(150, 200, image = smile)




#SETTING UP WINDOWS
base = Tk()
base.title("ChatBot")
base.geometry("800x500")
base.resizable(width=FALSE, height=FALSE)

left_frame = Frame(base, width=370, height=370, bg='white')
left_frame.grid(row=0, column=0, padx=10, pady=5)

#ADDING TKINTER COMPONENTS
#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)
ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="arrow")
ChatLog['yscrollcommand'] = scrollbar.set

#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
#EntryBox.bind("<Return>", send)

#Create Button to start conversation
startButton = Button(base, font=("Verdana",12,'bold'), text="Talk to Aria", width="12", height=5, bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff', command= start)

#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="6", height=5, bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff', command= send )



#Play gifs
#Create frame that gif will play in
right_frame = Frame(base, width=300, height=390, bg='white')
right_frame.grid(row=0, column=1, padx=10, pady=5)

# the label for intro_message 
#intro_message = Label(base, text = "Press 'Send' to get started").place(x = 460, y = 30)   

newCanvas = Canvas(right_frame, width=300, height=385, bg='white')
newCanvas.grid(row=0, column=0, padx=0, pady=0)

# load the .gif image file
# put in your own gif file here, may need to add full path
# like 'C:/WINDOWS/Help/Tours/WindowsMediaPlayer/Img/mplogo.gif'
smile = PhotoImage(file = './images/smile.png')
laugh = PhotoImage(file = './images/laugh.png')
confused = PhotoImage(file = './images/confused.png')
wink = PhotoImage(file = './images/wink.png')

# put gif image on canvas
#Later, this should include if statements to display different emotions

newCanvas.create_image(150, 200, image = smile)


#CREATE LISTBOX
listbox = Listbox(base, selectmode = "multiple", height = 10,  width = 15,  bg = "grey",  activestyle = 'dotbox',  font = "Helvetica", fg = "yellow") 
    
# insert elements by their 
# index and names. 
listbox.insert(1, "Soup: $13") 
listbox.insert(2, "Pizza: $15") 
listbox.insert(3, "Sorbet: $6") 
listbox.insert(4, "Baguette: $4") 
listbox.insert(5, "Burrito: $10") 


#Place all components on the screen
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
startButton.place(x=6, y=401, height=90)
EntryBox.place(x=440, y=401, height=90, width=265)
SendButton.place(x=350, y=401, height=90)


#Run the code
base.mainloop()



def init_chat():
  #Ask the user for more input, then use that in your response
  message = input(getReply(message) + "\n")


if __name__ == "__main__":
  init_chat()

