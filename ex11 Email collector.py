import re
para="My name is dev and my email it is talk2devendra.solanki@gmail.com .harry email is cwd@gmail.com and ravi email is ravi@gmail.com and one of my frind email is anandsharma@gmail.com thats all bye."
# patt=re.compile("is")
patt=re.compile(r"\S+@\S+")
matches=patt.findall(para)
emaillst=[]
with open("email.txt","a") as f:
    for match in matches:
        print(match)
        emaillst.append(match)
        f.write(f"{matches.index(match)+1}. {match}\n")
print(emaillst)