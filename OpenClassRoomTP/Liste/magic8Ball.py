import random

"""
write a programe which gives a random poem
"""

string = """Praises worse than at that i not so affined 
Our time and eyes have might to give 
In my bosoms ward but let me do forgive 
Yore those children nursed deliverd from serving with thee 
Which in the strength and they look what thee 
From the first the morning have been mine eye 
Thy fair assistance in loves fire shall in ai 
Yet the perfumed tincture of my desire keep open 
They see barren tender feeling but yet eyes alagappan 
Doubting the face should transport me that is kind 
Enforced to my deepest sense to his brief affined 
And gives thee back the past i have often 
Not my love thy store when days when acetaminophen"""

messages = string.split("\n")
qtty_sample = len(messages)-1
len_max = len(messages)
step = 1
for i in random.sample(range(0,len_max),qtty_sample) :

    print(("\t" * step) if step < len_max/2 else ("\t" * (len_max - step +1)) , messages[i])
    step += 1
