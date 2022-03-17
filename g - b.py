import random

boys=["ali", "reza", "yasin", "benyamin", "mehrdad", "sajjad", "aidin", "shahin" , "saeed", "soheil", "misagh"]

girls=["sara", "zari", "neda", "homa", "eli", "goli", "mary", "mina" , "saha", "atefe" , "hanane"]

marriage=[]

for i in range(len(boys)):
    boy =random.choice(boys)
    girl =random.choice(girls)
    
    boys.remove(boy)
    girls.remove(girl)
    marriage.append((boy,girl))
    
print(marriage)  