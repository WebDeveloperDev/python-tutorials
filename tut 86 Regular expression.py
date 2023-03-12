import re

mystr=r"Consequent to axxxx the acquisition, +914234231542  ccompany the +918839335330 Tatas will own a 100% +238855712418 stake in Air +919752852342 India (a full-service airline operating in domestic and international markets) as also 100% in its subsidiary Air India Express (a low-cost carrier airline that focusses on short-haul international operations especially in the Middle East market) and 50% in the joint venture Air India SATS (airport services on ground and cargo handling). The total permanent and contractual employee strength of Air India & AIXL is 13,500."
# print(str.find("to"))
# str.split(" ")
# l1=list(str.split(" "))
# print(r"\n") #print a row string
# patt=re.compile("Tatas")
# patt=re.compile("^Consequent") #^ if starts  with Consequent
# patt=re.compile("500.$") #$   if ends  with Consequent
# patt=re.compile("a*i*") #0 to infinite a and 0 to infinite i
# patt=re.compile("ax*") # "a" and whatever the frequency of "x"
# patt=re.compile("ax*") # "a" and whatever the frequency of "x"
# patt=re.compile("ax+") # "a" and more than one  frequency of "x"
# patt=re.compile("co{1}") # "c" and  one  frequency of "o"
# patt=re.compile("(co){1}|t") # "co" or t

# Special sequences
# patt=re.compile("\ACon") # if string starts wih Con
# patt=re.compile(r"\bth") # if word starts wih Con
# patt=re.compile(r"\d{5}") # no. of digits
# patt=re.compile(r"\d{2}%")
patt=re.compile(r'\+91\d{10}')

numberlst=[]
matches=patt.finditer(mystr)
for match in matches:
    print(match)
    span=match.span()
    numberlst.append(mystr[span[0]:span[1]])
    # print(mystr[0:10]) #it will slice the string
print(numberlst)