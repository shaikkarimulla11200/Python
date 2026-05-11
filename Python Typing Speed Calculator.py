#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from time import *
import random as r

error = 0
def mistake(paratext,usertext):
    error = 0
    for i in range (len(paratext)):
        try :
           if paratext[i] != usertext[i]:
             error = error + 1
        except:
             error = error + 1
    return (error)

def speed_time(time_s,time_e,userinput):
    time_delay = time_e - time_s
    time_taken = round(time_delay,2)
    speed = len(userinput)/time_taken
    return round(speed)
while True :
    Check = input(" Type Yes/No For Start/Restart")
    if Check.lower() == "yes":
        text = ["Success is not built overnight but through consistent effort, patience, and learning from failure. Every small step matters in shaping a bigger outcome. Staying focused on your goals while adapting to challenges helps create growth. Discipline and determination together form the foundation for achieving meaningful and lasting success in life.",
            "Technology has transformed the way people communicate, learn, and work in modern society. It connects individuals across the world instantly and provides access to vast information. However, balancing its use is important to avoid dependency. Responsible usage ensures productivity, creativity, and meaningful human interactions without losing personal well being.",
            "Nature offers peace, balance, and inspiration to those who take time to observe it closely. From flowing rivers to silent mountains, every element teaches harmony and resilience. Protecting the environment is essential for future generations. Small actions like reducing waste and conserving resources can create a significant positive impact over time."]
        test = r.choice(text)

        print(test)
        print()
        print()
        time_1 = time()
        text_input = input("Enter :")
        time_2 = time ()

        print("Speed", speed_time(time_1,time_2,text_input))
        print("error:",mistake(test,text_input))
    elif Check.lower() == "no":
      print("Thank You")
      break
    else :
        print("Invalid Option")




# In[ ]:




