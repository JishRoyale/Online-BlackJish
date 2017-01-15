import sys
import time
from random import randint
speed = 0.025
Text = "Welcome to BlackJish"
for i in Text:
   sys.stdout.write( i )
   time.sleep(speed)
sys.stdout.write("\n")
Text = "How many bots would you like?(1 min, 3 max)   "
for i in Text:
   sys.stdout.write( i )
   time.sleep(speed)
sys.stdout.write("\n")
Num_Bots = int(raw_input(">"))
Money = 20
Run_Program = True
while Run_Program == True:
   Text = "You have " + str(Money) + " coins."
   for i in Text:
      sys.stdout.write( i )
      time.sleep(speed)
   sys.stdout.write("\n")
   Text = "How much do you want to bet?(min 5)  "
   for i in Text:
      sys.stdout.write( i )
      time.sleep(speed)
   sys.stdout.write("\n")
   Bet = int(raw_input(">"))
   if Bet > Money or Bet < 5:
      quit()
   Bot1_Run = False
   Bot2_Run = False
   Bot3_Run = False
   Hand_Bust = False
   Bot1_Bust = False
   Bot2_Bust = False
   Bot3_Bust = False
   if Num_Bots == 1 or Num_Bots > 1:
       Bot1_Run = True
   if Num_Bots == 2 or Num_Bots > 2:
       Bot2_Run = True
   if Num_Bots == 3 or Num_Bots > 3:
       Bot3_Run = True
   Run_Deal = True
   Aces = ["Ace of Spades", "Ace of Clubs", "Ace of Hearts", "Ace of Diamonds"]
   Twos = ["Two of Spades", "Two of Clubs", "Two of Hearts", "Two of Diamonds"]
   Threes = ["Three of Spades", "Three of Clubs", "Three of Hearts", "Three of Diamonds"]
   Fours = ["Four of Spades", "Four of Clubs", "Four of Hearts", "Four of Diamonds"]
   Fives = ["Five of Spades", "Five of Clubs", "Five of Hearts", "Five of Diamonds"]
   Sixes = ["Six of Spades", "Six of Clubs", "Six of Hearts", "Six of Diamonds"]
   Sevens = ["Seven of Spades", "Seven of Clubs", "Seven of Hearts", "Seven of Diamonds"]
   Eights = ["Eight of Spades", "Eight of Clubs", "Eight of Hearts", "Eight of Diamonds"]
   Nines = ["Nine of Spades", "Nine of Clubs", "Nine of Hearts", "Nine of Diamonds"]
   Tens = ["Ten of Spades", "Ten of Clubs", "Ten of Hearts", "Ten of Diamonds"]
   Jacks = ["Jack of Spades", "Jack of Clubs", "Jack of Hearts", "Jack of Diamonds"]
   Queens = ["Queen of Spades", "Queen of Clubs", "Queen of Hearts", "Queen of Diamonds"]
   Kings = ["King of Spades", "King of Clubs", "King of Hearts", "King of Diamonds"]
   while Run_Deal == True:
       Taken_Cards = []
       Hand_Num1 = randint(1, 13)
       Hand_Num2 = randint(1, 13)
       Bot1_Num1 = randint(1, 13)
       Bot1_Num2 = randint(1, 13)
       Bot2_Num1 = randint(1, 13)
       Bot2_Num2 = randint(1, 13)
       Bot3_Num1 = randint(1, 13)
       Bot3_Num2 = randint(1, 13)
       Hand_Card1 = "This is blank"
       Hand_Card2 = "This is blank"
       Bot1_Card1 = "This is blank"
       Bot1_Card2 = "This is blank"
       Bot2_Card1 = "This is blank"
       Bot2_Card2 = "This is blank"
       Bot3_Card1 = "This is blank"
       Bot3_Card2 = "This is blank"
       Cards = [Hand_Num1, Hand_Num2, Bot1_Num1, Bot1_Num2, Bot2_Num1, Bot2_Num2, Bot3_Num1, Bot3_Num2]
       Cards2 = [Hand_Card1, Hand_Card2, Bot1_Card1, Bot1_Card2, Bot2_Card1, Bot2_Card2, Bot3_Card1, Bot3_Card2]
       Index = 0
       while Index < 8:
           Index2 = randint(0, 3)
           Card_Num = Cards [Index]
           if Card_Num == 1:
               Cards2 [Index] = Aces [Index2]
           elif Card_Num == 2:
               Cards2 [Index] = Twos [Index2]
           elif Card_Num == 3:
               Cards2 [Index] = Threes [Index2]
           elif Card_Num == 4:
               Cards2 [Index] = Fours [Index2]
           elif Card_Num == 5:
               Cards2 [Index] = Fives [Index2]
           elif Card_Num == 6:
               Cards2 [Index] = Sixes [Index2]
           elif Card_Num == 7:
               Cards2 [Index] = Sevens [Index2]
           elif Card_Num == 8:
               Cards2 [Index] = Eights [Index2]
           elif Card_Num == 9:
               Cards2 [Index] = Nines [Index2]
           elif Card_Num == 10:
               Cards2 [Index] = Tens [Index2]
           elif Card_Num == 11:
               Cards2 [Index] = Jacks [Index2]
           elif Card_Num == 12:
               Cards2 [Index] = Queens [Index2]
           elif Card_Num == 13:
               Cards2 [Index] = Kings [Index2]
           Taken_Cards.append(Cards2 [Index])
           Index = Index + 1
       Dual_Cards = len(set(Taken_Cards))
       if Dual_Cards == 8:
           Run_Deal = False
       else:
           pass
   Hand_Aces = 0
   Bot1_Aces = 0
   Bot2_Aces = 0
   Bot3_Aces = 0
   Hand_Card1 = Taken_Cards [0]
   Hand_Card2 = Taken_Cards [1]
   Bot1_Card1 = Taken_Cards [2]
   Bot1_Card2 = Taken_Cards [3]
   Bot2_Card1 = Taken_Cards [4]
   Bot2_Card2 = Taken_Cards [5]
   Bot3_Card1 = Taken_Cards [6]
   Bot3_Card2 = Taken_Cards [7]
   if Hand_Num1 == 13 or Hand_Num1 == 12 or Hand_Num1 == 11:
       Hand_Num1 = 10
   if Hand_Num1 == 1:
       Hand_Num1 = 11
       Hand_Aces = Hand_Aces + 1
   if Hand_Num2 == 13 or Hand_Num2 == 12 or Hand_Num2 == 11:
       Hand_Num2 = 10
   if Hand_Num2 == 1:
       Hand_Num2 = 11
       Hand_Aces =Hand_Aces + 1
   if Bot1_Num1 == 13 or Bot1_Num1 == 12 or Bot1_Num1 == 11:
       Bot1_Num1 = 10
   if Bot1_Num1 == 1:
       Bot1_Num1 = 11
       Bot1_Aces = Bot1_Aces + 1
   if Bot1_Num2 == 13 or Bot1_Num2 == 12 or Bot1_Num2 == 11:
       Bot1_Num2 = 10
   if Bot1_Num2 == 1:
       Bot1_Num2 = 11
       Bot1_Aces = Bot1_Aces + 1
   if Bot2_Num1 == 13 or Bot2_Num1 == 12 or Bot2_Num1 == 11:
       Bot2_Num1 = 10
   if Bot2_Num1 == 1:
       Bot2_Num1 = 11
       Bot2_Aces = Bot2_Aces + 1
   if Bot2_Num2 == 13 or Bot2_Num2 == 12 or Bot2_Num2 == 11:
       Bot2_Num2 = 10
   if Bot2_Num2 == 1:
       Bot2_Num2 = 11
       Bot2_Aces = Bot2_Aces + 1
   if Bot3_Num1 == 13 or Bot3_Num1 == 12 or Bot3_Num1 == 11:
       Bot3_Num1 = 10
   if Bot3_Num1 == 1:
       Bot3_Num1 = 11
       Bot3_Aces = Bot3_Aces + 1
   if Bot3_Num2 == 13 or Bot3_Num2 == 12 or Bot3_Num2 == 11:
       Bot3_Num2 = 10
   if Bot3_Num2 == 1:
       Bot3_Num2 = 11
       Bot3_Aces = Bot3_Aces + 1
   Score = Hand_Num1 + Hand_Num2
   Bot1_Score = Bot1_Num1 + Bot1_Num2
   Bot2_Score = Bot2_Num1 + Bot2_Num2
   Bot3_Score = Bot3_Num1 + Bot3_Num2
   Hand = []
   Hand.append(Hand_Card1)
   Hand.append(Hand_Card2)
   Text = "Dealer: Here are your cards."
   for i in Text:
      sys.stdout.write( i )
      time.sleep(speed)
   sys.stdout.write("\n")
   Text = "You recived the " + Hand_Card1 + " and the " + Hand_Card2 + "."
   for i in Text:
      sys.stdout.write( i )
      time.sleep(speed)
   sys.stdout.write("\n")

   Bust = False
   while Bust == False:
      Text = "Do you want to twist or stick?   "
      for i in Text:
         sys.stdout.write( i )
         time.sleep(speed)
      sys.stdout.write("\n")
      Choice = raw_input(">")
      if Choice == "twist":
           Hand_Num3 = randint(1, 13)
           Card_Num = Hand_Num3
           Run_Deal = True
           while Run_Deal == True:
               Dual_Cards = len(set(Taken_Cards))
               Index2 = randint(0, 3)
               if Card_Num == 1:
                   Card = Aces [Index2]
               elif Card_Num == 2:
                   Card = Twos [Index2]
               elif Card_Num == 3:
                   Card = Threes [Index2]
               elif Card_Num == 4:
                   Card = Fours [Index2]
               elif Card_Num == 5:
                   Card = Fives [Index2]
               elif Card_Num == 6:
                   Card = Sixes [Index2]
               elif Card_Num == 7:
                   Card = Sevens [Index2]
               elif Card_Num == 8:
                   Card = Eights [Index2]
               elif Card_Num == 9:
                   Card = Nines [Index2]
               elif Card_Num == 10:
                   Card = Tens [Index2]
               elif Card_Num == 11:
                   Card = Jacks [Index2]
               elif Card_Num == 12:
                   Card = Queens [Index2]
               elif Card_Num == 13:
                   Card = Kings [Index2]
               Taken_Cards.append(Card)
               Dual_Cards2 = len(set(Taken_Cards))
               if Dual_Cards == Dual_Cards2 - 1:
                   Run_Deal = False
           Hand.append(Card)
           Taken_Cards.append(Card)
           if Card_Num == 13 or Card_Num == 12 or Card_Num == 11:
               Card_Num = 10
           if Card_Num == 1:
               Card_Num = 11
               Hand_Aces = Hand_Aces + 1
           Score = Score + Card_Num
           Text = "Dealer: Here is your card."
           for i in Text:
              sys.stdout.write( i )
              time.sleep(speed)
           sys.stdout.write("\n")
           Text = "You recived the " + Card + "."
           for i in Text:
              sys.stdout.write( i )
              time.sleep(speed)
           sys.stdout.write("\n")
           if Score > 21 and Hand_Aces == 0:
               Hand_Bust = True
               Bust = True
           elif Score > 21 and Hand_Aces > 0:
               Score = Score - 10
               Hand_Aces = Hand_Aces - 1
               if Score > 21 and Hand_Aces > 0:
                   Score = Score - 10
                   Hand_Aces = Hand_Aces - 1
      elif Choice == "stick":
           Bust = True
      else:
           pass

   if Bot1_Run == True:
       Bust = False
       Bot1 = []
       Bot1.append(Bot1_Card1)
       Bot1.append(Bot1_Card2)
       while Bust == False:
           Chance = randint(10, 18)
           if Chance > Bot1_Score:
               Choice = True
           elif Bot1_Score < 16:
               Choice = True
           else:
               Choice = False
           if Choice == True:
               Card_Num = randint(1, 13)
               Run_Deal = True
               while Run_Deal == True:
                   Dual_Cards = len(set(Taken_Cards))
                   Index2 = randint(0, 3)
                   if Card_Num == 1:
                       Card = Aces [Index2]
                   elif Card_Num == 2:
                       Card = Twos [Index2]
                   elif Card_Num == 3:
                       Card = Threes [Index2]
                   elif Card_Num == 4:
                       Card = Fours [Index2]
                   elif Card_Num == 5:
                       Card = Fives [Index2]
                   elif Card_Num == 6:
                       Card = Sixes [Index2]
                   elif Card_Num == 7:
                       Card = Sevens [Index2]
                   elif Card_Num == 8:
                       Card = Eights [Index2]
                   elif Card_Num == 9:
                       Card = Nines [Index2]
                   elif Card_Num == 10:
                       Card = Tens [Index2]
                   elif Card_Num == 11:
                       Card = Jacks [Index2]
                   elif Card_Num == 12:
                       Card = Queens [Index2]
                   elif Card_Num == 13:
                       Card = Kings [Index2]
                   Taken_Cards.append(Card)
                   Dual_Cards2 = len(set(Taken_Cards))
                   if Dual_Cards == Dual_Cards2 - 1:
                       Run_Deal = False
               Bot1.append(Card)
               if Card_Num == 13 or Card_Num == 12 or Card_Num == 11:
                   Card_Num = 10
               Bot1_Score = Bot1_Score + Card_Num
               if Bot1_Score > 21 and Bot1_Aces == 0:
                   Bot1_Bust = True
                   Bust = True
               elif Bot1_Score > 21 and Bot1_Aces > 0:
                   Bot1_Score = Bot1_Score - 10
                   Bot1_Aces = Bot1_Aces - 1
                   if Bot1_Score > 21 and Bot1_Aces > 0:
                       Bot1_Score = Bot1_Score - 10
                       Bot1_Aces = Bot1_Aces - 1
           elif Choice == False:
               Bust = True    

   if Bot2_Run == True:
       Bust = False
       Bot2 = []
       Bot2.append(Bot2_Card1)
       Bot2.append(Bot2_Card2)
       while Bust == False:
           Chance = randint(10, 18)
           if Chance > Bot2_Score:
               Choice = True
           elif Bot2_Score < 16:
               Choice = True
           else:
               Choice = False
           if Choice == True:
               Card_Num = randint(1, 13)
               Run_Deal = True
               while Run_Deal == True:
                   Dual_Cards = len(set(Taken_Cards))
                   Index2 = randint(0, 3)
                   if Card_Num == 1:
                       Card = Aces [Index2]
                   elif Card_Num == 2:
                       Card = Twos [Index2]
                   elif Card_Num == 3:
                       Card = Threes [Index2]
                   elif Card_Num == 4:
                       Card = Fours [Index2]
                   elif Card_Num == 5:
                       Card = Fives [Index2]
                   elif Card_Num == 6:
                       Card = Sixes [Index2]
                   elif Card_Num == 7:
                       Card = Sevens [Index2]
                   elif Card_Num == 8:
                       Card = Eights [Index2]
                   elif Card_Num == 9:
                       Card = Nines [Index2]
                   elif Card_Num == 10:
                       Card = Tens [Index2]
                   elif Card_Num == 11:
                       Card = Jacks [Index2]
                   elif Card_Num == 12:
                       Card = Queens [Index2]
                   elif Card_Num == 13:
                       Card = Kings [Index2]
                   Taken_Cards.append(Card)
                   Dual_Cards2 = len(set(Taken_Cards))
                   if Dual_Cards == Dual_Cards2 - 1:
                       Run_Deal = False
               Bot2.append(Card)
               if Card_Num == 13 or Card_Num == 12 or Card_Num == 11:
                   Card_Num = 10
               Bot2_Score = Bot2_Score + Card_Num
               if Bot2_Score > 21 and Bot2_Aces == 0:
                   Bot2_Bust = True
                   Bust = True
               elif Bot2_Score > 21 and Bot2_Aces > 0:
                   Bot2_Score = Bot2_Score - 10
                   Bot2_Aces = Bot2_Aces - 1
                   if Bot2_Score > 21 and Bot2_Aces > 0:
                       Bot2_Score = Bot2_Score - 10
                       Bot2_Aces = Bot2_Aces - 1
           elif Choice == False:
               Bust = True

   if Bot3_Run == True:
       Bust = False
       Bot3 = []
       Bot3.append(Bot3_Card1)
       Bot3.append(Bot3_Card2)
       while Bust == False:
           Chance = randint(10, 18)
           if Chance > Bot3_Score:
               Choice = True
           elif Bot3_Score < 16:
               Choice = True
           else:
               Choice = False
           if Choice == True:
               Card_Num = randint(1, 13)
               Run_Deal = True
               while Run_Deal == True:
                   Dual_Cards = len(set(Taken_Cards))
                   Index2 = randint(0, 3)
                   if Card_Num == 1:
                       Card = Aces [Index2]
                   elif Card_Num == 2:
                       Card = Twos [Index2]
                   elif Card_Num == 3:
                       Card = Threes [Index2]
                   elif Card_Num == 4:
                       Card = Fours [Index2]
                   elif Card_Num == 5:
                       Card = Fives [Index2]
                   elif Card_Num == 6:
                       Card = Sixes [Index2]
                   elif Card_Num == 7:
                       Card = Sevens [Index2]
                   elif Card_Num == 8:
                       Card = Eights [Index2]
                   elif Card_Num == 9:
                       Card = Nines [Index2]
                   elif Card_Num == 10:
                       Card = Tens [Index2]
                   elif Card_Num == 11:
                       Card = Jacks [Index2]
                   elif Card_Num == 12:
                       Card = Queens [Index2]
                   elif Card_Num == 13:
                       Card = Kings [Index2]
                   Taken_Cards.append(Card)
                   Dual_Cards2 = len(set(Taken_Cards))
                   if Dual_Cards == Dual_Cards2 - 1:
                       Run_Deal = False
               Bot3.append(Card)
               if Card_Num == 13 or Card_Num == 12 or Card_Num == 11:
                   Card_Num = 10
               Bot3_Score = Bot3_Score + Card_Num
               if Bot3_Score > 21 and Bot3_Aces == 0:
                   Bot3_Bust = True
                   Bust = True
               elif Bot3_Score > 21 and Bot3_Aces > 0:
                   Bot3_Score = Bot3_Score - 10
                   Bot3_Aces = Bot3_Aces - 1
                   if Bot3_Score > 21 and Bot3_Aces > 0:
                       Bot3_Score = Bot3_Score - 10
                       Bot3_Aces = Bot3_Aces - 1
           elif Choice == False:
               Bust = True
   Text =  "Dealer: Show your hands."
   for i in Text:
      sys.stdout.write( i )
      time.sleep(speed)
   sys.stdout.write("\n")
   if Hand_Bust == False:
      Text = "You: I scored " + str(Score) + "."
      for i in Text:
         sys.stdout.write( i )
         time.sleep(speed)
      sys.stdout.write("\n")
   else:
      Text = "You: I went bust"
      for i in Text:
         sys.stdout.write( i )
         time.sleep(speed)
      sys.stdout.write("\n")
      Score = 0
   Text = "You: I had these: "
   for i in Text:
      sys.stdout.write( i )
      time.sleep(speed)
   for i in range(0, len(Hand)):
      Text = Hand [i]
      for i in Text:
         sys.stdout.write( i )
         time.sleep(speed)
      sys.stdout.write(", ")
   sys.stdout.write("\n")
   if Bot1_Run == True:
      if Bot1_Bust == False:
         Text = "Player 1: I scored " + str(Bot1_Score) + "."
         for i in Text:
            sys.stdout.write( i )
            time.sleep(speed)
         sys.stdout.write("\n")
      else:
         Text = "Player 1: I went bust"
         for i in Text:
            sys.stdout.write( i )
            time.sleep(speed)
         sys.stdout.write("\n")
         Bot1_Score = 0
      Text =("Player 1: I had these: ")
      for i in Text:
         sys.stdout.write( i )
         time.sleep(speed)
      for i in range(0, len(Bot1)):
         Text = Bot1 [i]
         for i in Text:
            sys.stdout.write( i )
            time.sleep(speed)
         sys.stdout.write(", ")
      sys.stdout.write("\n")
   if Bot2_Run == True:
      if Bot2_Bust == False:
         Text = "Player 2: I scored " + str(Bot2_Score) + "."
         for i in Text:
            sys.stdout.write( i )
            time.sleep(speed)
         sys.stdout.write("\n")
      else:
         Text = "Player 2: I went bust"
         for i in Text:
            sys.stdout.write( i )
            time.sleep(speed)
         sys.stdout.write("\n")
         Bot2_Score = 0
      Text = ("Player 2: I had these: ")
      for i in Text:
         sys.stdout.write( i )
         time.sleep(speed)
      for i in range(0, len(Bot2)):
         Text = Bot2 [i]
         for i in Text:
            sys.stdout.write( i )
            time.sleep(speed)
         sys.stdout.write(", ")
      sys.stdout.write("\n")
   else:
      Bot2_Score = 0
   if Bot3_Run == True:
      if Bot3_Bust == False:
         Text = "Player 3: I scored " + str(Bot3_Score) + "."
         for i in Text:
            sys.stdout.write( i )
            time.sleep(speed)
         sys.stdout.write("\n")
      else:
         Text = "Player 3: I went bust"
         for i in Text:
            sys.stdout.write( i )
            time.sleep(speed)
         sys.stdout.write("\n")
         Bot3_Score = 0
      Text = ("Player 3: I had these: ")
      for i in Text:
            sys.stdout.write( i )
            time.sleep(speed)
      for i in range(0, len(Bot3)):
         Text = Bot3 [i]
         for i in Text:
            sys.stdout.write( i )
            time.sleep(speed)
         sys.stdout.write(", ")
      sys.stdout.write("\n")
   else:
      Bot3_Score = 0
   Position = 1
   if Score < Bot1_Score:
      Position = Position +1
   if Score < Bot2_Score:
      Position = Position +1
   if Score < Bot3_Score:
      Position = Position +1
   if Position == 1:
      Text = "You came first."
      for i in Text:
         sys.stdout.write( i )
         time.sleep(speed)
      sys.stdout.write("\n")
      Text = "You gained " + str(Bet) + " coins."
      for i in Text:
         sys.stdout.write( i )
         time.sleep(speed)
      sys.stdout.write("\n")
      Money = Money + Bet
      Text = "You now have " + str(Money) + " coins."
      for i in Text:
         sys.stdout.write( i )
         time.sleep(speed)
      sys.stdout.write("\n")
   elif Position == 2:
      Text = "You came second."
      for i in Text:
         sys.stdout.write( i )
         time.sleep(speed)
      sys.stdout.write("\n")
      if Bot2_Run == False:
         Text = "You lost " + str(Bet) + " coins."
         for i in Text:
            sys.stdout.write( i )
            time.sleep(speed)
         sys.stdout.write("\n")
         Money = Money - Bet
         Text = "You now have " + str(Money) + " coins."
         for i in Text:
            sys.stdout.write( i )
            time.sleep(speed)
         sys.stdout.write("\n")
   elif Position == 3:
      Text = "You came third."
      for i in Text:
         sys.stdout.write( i )
         time.sleep(speed)
      sys.stdout.write("\n")
      if Bot3_Run == False:
         Text = "You lost " + str(Bet) + " coins."
         for i in Text:
            sys.stdout.write( i )
            time.sleep(speed)
         sys.stdout.write("\n")
         Money = Money - Bet
         Text = "You now have " + str(Money) + " coins."
         for i in Text:
            sys.stdout.write( i )
            time.sleep(speed)
         sys.stdout.write("\n")
   elif Position == 4:
      Text = "You came fouth."
      for i in Text:
         sys.stdout.write( i )
         time.sleep(speed)
      sys.stdout.write("\n")
      Text = "You lost " + str(Bet) + " coins."
      for i in Text:
         sys.stdout.write( i )
         time.sleep(speed)
      sys.stdout.write("\n")
      Money = Money - Bet
      Text = "You now have " + str(Money) + " coins."
      for i in Text:
         sys.stdout.write( i )
         time.sleep(speed)
      sys.stdout.write("\n")
      if Money < 5:
         Text = "You have less money than the minimum bet. Thank you for playing."
         for i in Text:
            sys.stdout.write( i )
            time.sleep(speed)
         quit()
   Text = "Do you want to coninue?(y/n)   "
   for i in Text:
      sys.stdout.write( i )
      time.sleep(speed)
   sys.stdout.write("\n")
   Continue = raw_input(">")
   if Continue == "n":
      Run_Program = False

      
    
