import random

#Set the constants
OBJECT_PRONOUNS = ['Her', 'Him', 'Them']
POSSESIVE_PRONOUNS = ['Her', 'His', 'Their']
PERSONAL_PRONOUNS = ['She', 'He', 'They']
STATES = ['California', 'Texas', 'Florida', 'New York', 'Pennsylvania','Illinois', 'Ohio', 'Georgia', 'North Carolina', 'Michigan']
NOUNS = ['Athlete', 'Clown', 'Shovel', 'Paleo Diet', 'Doctor', 'Parent','Cat', 'Dog', 'Chicken', 'Robot', 'Video Game', 'Avocado','Plastic Straw','Serial Killer', 'Telephone Psychic']
PLACES = ['House', 'Attic', 'Bank Deposit Box', 'School', 'Basement','Workplace', 'Donut Shop', 'Apocalypse Bunker']
WHEN = ['Soon', 'This Year', 'Later Today', 'RIGHT NOW', 'Next Week']
HOOPERS = ['Steph Curry','Anthony Davis','Anthony Edwards','Ja Morant','Shai Gilgeous-alexander','Lebron James','Luka Doncic']
FOOTBALLERS = ['Cristiano Ronaldo','Neymar JR.','Mbappe','Lionel Messi']
VERB = ['slapped','punched','stabbed','snubbed','shot']

#create the bait generator functions
def generate_DontWantYouToKnowCB():
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return (f"What {noun1}s don\'t want you to know about {noun2}s")

def generate_therealreasonCB():
    athlete1 = random.choice(HOOPERS)
    athlete2 = random.choice(FOOTBALLERS)
    verb = random.choice(VERB)
    place = random.choice(PLACES)
    return (f'The Real Reason {athlete1} {verb.capitalize()} {athlete2} In The {place}')

def generate_wontbelieveCB():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    possesive_pronoun = random.choice(POSSESIVE_PRONOUNS)
    places = random.choice(PLACES)
    return (f"You won't believe what this {state} {noun} found in {possesive_pronoun} {places}")

def generateJobAutomatedHeadline():
    state = random.choice(STATES)
    noun = random.choice(NOUNS)
    #refernce this {% block %} periodicallt for logical insights
    i = random.randint(0, 2)
    pronoun1 = POSSESIVE_PRONOUNS[i]
    pronoun2 = PERSONAL_PRONOUNS[i]
    if pronoun1 == 'Their':
        return f'These {state} {noun}s That Didn\'t Think Robots Would Take {pronoun1} Job. {pronoun2} Were Wrong.'
    else:
        return f'This {state} {noun} Didn\'t Think Robots Would Take {pronoun1} Job. {pronoun2} Was Wrong.'
    #{% endblock %}

def generateBigCompaniesHateHerHeadline():  
    pronoun = random.choice(OBJECT_PRONOUNS)
    state = random.choice(STATES)
    noun1 = random.choice(NOUNS)
    noun2 = random.choice(NOUNS)
    return f'Big Companies Hate {pronoun}! See How This {state} {noun1} Invented a Cheaper {noun2}'


def main():
    print('_____________________Clickbait Headline Generator______________________')
    print('\nOur website needs to trick people into looking at ads!')
    while True:
        headlines = []
        print('Enter the number of clickbait headlines to generate:')
        response = input(":> ")
        if not response.isdecimal():
            print("Please enter a number\n")
        else:
            number_of_clickbaits = int(response)
            break
    while len(headlines) != number_of_clickbaits:
        random_option = random.randint(1,6)

        if random_option == 1:
            headline = generate_DontWantYouToKnowCB()
        elif random_option == 2:
            headline = generate_therealreasonCB()
        elif random_option == 3:
            headline = generate_wontbelieveCB()
        elif random_option == 4:
            headline = generateJobAutomatedHeadline()
        elif random_option == 5:
            headline = generateBigCompaniesHateHerHeadline()
        try:
            if headline != headlines[-1]:
                headlines.append(headline)
        except IndexError:
            headlines.append(headline)
            print("\n")
    for x in headlines:
        print(x+"\n")

if __name__ == '__main__':
   main()
    