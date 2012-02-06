import urllib
import random
url = "http://www.brainyquote.com/quotes_of_the_day.html"

f = urllib.urlopen(url)
s = f.readlines()
f.close()

quotes=[]

for line in s:
    if "huge\">" in line:
        quotes.append(line)
"""someone please explain why the for block below doesn't apply a permanent change to each line"""
#for somt in quotes:    
 #   somt = somt.replace('<span class="huge">','')
  #  somt = somt.replace('</span><br>','')

choice = random.randint(0,(len(quotes)-1))

quotes[choice] = quotes[choice].replace('<span class="huge">','')
quotes[choice] = quotes[choice].replace('</span><br>','')
quotes[choice] = quotes[choice].replace('\n','')



print"              n__n_"
print"             /  = =\\"
print"            /   ._Y_)"," ",quotes[choice]
print"___________/      \"\________________________________"
print"          (_/  (_,  \                  "
print"            \      ( \_,--\"\"\"\"--."
print"      __..-,-`.___,-` )-.______.' "
print"    <'     `-,'   `-, )-'    >"
print"     `----._/      ( /\"`>.--\""
print"            \"--..___,--\""
