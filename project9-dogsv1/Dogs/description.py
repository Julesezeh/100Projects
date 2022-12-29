#SWITCHES
def shedding_switch(number):
    match number:
        case 0:
            return "They don't shed at all. Strange."
        case 1:
            return "They don't shed that much"
        case 2:
            return "They shed a little"
        case 3:
            return "They are quite the shedders"
        case 4:
            return "They shed a lot"
        case 5:
            return "They shed a bit TOO much"

def barking_switch(number):
    match number:
        case 0:
            return "They don't bark, at all.... Very strange"
        case 1:
            return "They hardly ever bark"
        case 2:
            return "They bark a little, but just that"
        case 3:
            return "They bark just fine"
        case 4:
            return "They bark really good"
        case 5:
            return "They are excellent at barking"

def energy_switch(number):
    match number:
        case 0:
            return "They don't have energy"
        case 1:
            return "They really don't have energy"
        case 2:
            return "They aren't so energetic"
        case 3:
            return "They have a little bit of energy"
        case 4:
            return "They are pretty energetic"
        case 5:
            return "They are very energetic"
    
def trainability_switch(number):
    match number:
        case 0:
            return "They are extremely difficult to train"
        case 1:
            return "They are really difficult to train"
        case 2:
            return "They are difficult to train"
        case 3:
            return "They aren't so easy to train"
        case 4:
            return "They can be trained pretty easily"
        case 5:
            return "They respond excellently to training"

def protective_switch(number):
    match number:
        case 0:
            return "They are not protective at all"
        case 1:
            return "They are really not protective"
        case 2:
            return "They are a bit protective"
        case 3:
            return "They are protective"
        case 4:
            return "They are very protective"
        case 5:
            return "RIDE or DIE level"

#DESCRIPTION FUNCTION
def description(json_response):
    name = json_response['name']
    max_growth = f"Can grow up to {int(json_response['max_height_male'])} inches for males and {int(json_response['max_height_female'])} inches for females"
    max_weight = f"Can weigh up to {int(json_response['max_weight_male'])} pounds for males and {int(json_response['max_weight_female'])} pounds for females"    
    shedding = shedding_switch(json_response['shedding'])
    
    min_life_span = int(json_response['min_life_expectancy'])
    max_life_span = int(json_response['min_life_expectancy'])
    span = f"Can live up to {max_life_span} years"

    energy_level = energy_switch(json_response['energy'])
    barking_level = barking_switch(json_response['barking'])
    trainability_level = trainability_switch(json_response['trainability'])
    protective_level = protective_switch(json_response['protectiveness'])
    
    image = json_response['image_link']

    details = {'name':name,'growth':max_growth,'weight':max_weight,'shedding':shedding,'life_span':span,'energy':energy_level,
    'trainability_level':trainability_level,'barking':barking_level,'protective':protective_level,'image_link':image}
    return details