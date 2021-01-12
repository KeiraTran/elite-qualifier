import random

 # print('Aria: ' + reply)


#Creating GUI with tkinter
import tkinter
from tkinter import *


jokes = ["What do you call a pig that does karate? Pork chop.",
         "How do you organize a space party? You planet.",
         "What job did the frog have at the hotel? Bellhop.",
         "What do you call an alligator in a vest? An investigator.",
         "What do you call a lazy kangaroo? A pouch potato."]

greetings = ["Hello.", "Hi!", "Hello there.", "Salutations.", "Greetings.", "Nice to meet you!", "Hiya!", "Nice to see you.", "Howdy."]
greetings_lower = [i.lower() for i in ["Hello", "Hi!", "Hi", "Hello there", "Salutations", "Greetings", "Nice to meet you!", "Hiya!", "Nice to see you", "Howdy"]]

gratitude_res = ["You're welcome!", "Happy to help!", "No problem!", "My pleasure!", "Have a great day!"]

menu = ("\n__________________________\nDrinks\n__________________________\nLemonade: $2\nSoda: $2\nTea: $3\n\n__________________________\nBurgers\n__________________________\nCheeseburger: $5\nVeggie Burger: $12\nBacon Burger: $15\nChili Burger: $15\n\n__________________________\nSides\n__________________________\nFrench Fries: $5\nOnion Rings: $6\nPickles: $1\nMacaroni and Cheese: $5\n")

lemonade = 2
soda = 2
tea = 3
cheeseburger = 5
veggie_burger = 12
bacon_burger = 15
chili_burger = 15
french_fries = 5
onion_rings = 6
pickles = 1
mac = 5

order = []
total = 0

def getReply(message):
  if message != '': 

      if 'who' in message and 'you' in message:
          reply = "Hello, I'm Aria."
      elif 'joke' in message:
          reply = random.choice(jokes)
      elif message in greetings or message in greetings_lower:
          reply = random.choice(greetings)
      elif message == "bye":
          reply = "Bye-bye! Thanks for chatting!"
      elif 'how are you' in message:
          reply = "I'm doing great! Thanks for asking!"
      elif 'thank you' in message: 
          reply = random.choice(gratitude_res)
      elif 'menu' in message:
          reply = menu
      elif 'hours' in message:
          reply = "We're open every day from 10AM to 10PM."
      else:
          reply = "Sorry, I don't understand"
      return reply
      '''
      elif 'order' in message:
          place = input("Okay! Please write your order in this format\n\nCheeseburger, Cheeseburger, Veggie Burger, Lemonade\n\nRemember to separate your items by commas.")
          for item in place:
            list = str.split (",")
            for i in list:
                i.lower()
                order.append(i)
                total+= order(i)
            reply = total
      '''

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

base = Tk()
base.title("Aria Bot")
base.geometry("800x500")
base.resizable(width=FALSE, height=FALSE)

#Create Chat window
ChatLog = Text(base, bd=0, bg="white", height="8", width="50", font="Arial",)

ChatLog.config(state=DISABLED)

#Bind scrollbar to Chat window
scrollbar = Scrollbar(base, command=ChatLog.yview, cursor="arrow")
ChatLog['yscrollcommand'] = scrollbar.set

#Create Button to send message
SendButton = Button(base, font=("Verdana",12,'bold'), text="Send", width="12", height=5, bd=0, bg="#32de97", activebackground="#3c9d9b",fg='#ffffff', command= send )

#Create the box to enter message
EntryBox = Text(base, bd=0, bg="white",width="29", height="5", font="Arial")
#EntryBox.bind("<Return>", send)


#Place all components on the screen
scrollbar.place(x=376,y=6, height=386)
ChatLog.place(x=6,y=6, height=386, width=370)
EntryBox.place(x=128, y=401, height=90, width=265)
SendButton.place(x=6, y=401, height=90)

print ("Hello! My name is Aria, and I'm a restaurant bot! If you wish to end the chat, please type 'bye'\n")
print ("Here's some special keywords that will help improve your dining experience.\n")
print ("Type 'menu' to bring up our menu.\nType 'hours' to know our hours of operation.\n")

base.mainloop()



def init_chat():

 # message = input("Hello! My name is Aria! Chat with me! If you wish to end the chat, please type 'bye'\n")

  while message != "bye":
    #Ask the user for more input, then use that in your response
    message = input(getReply(message) + "\n")



if __name__ == "__main__":
  init_chat()

