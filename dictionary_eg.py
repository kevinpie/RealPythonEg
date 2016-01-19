import random
capitals_dict = {
'Alabama': 'Montgomery', 'Alaska': 'Juneau', 'Arizona': 'Phoenix', 'Arkansas': 'Little Rock', 'California': 'Sacramento', 'Colorado': 'Denver', 'Connecticut': 'Hartford', 'Delaware': 'Dover', 'Florida': 'Tallahassee', 'Georgia': 'Atlanta',
}

x = random.choice(capitals_dict.keys())
y = capitals_dict[x]

while True:
        z = raw_input("What is the captital of " + x)
        if z == y:
            print "Correct"
            exit()

        elif z == "exit":
            exit()

        else:
            print "Keep Going"


