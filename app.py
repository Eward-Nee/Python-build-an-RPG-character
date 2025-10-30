full_dot = '●'
empty_dot = '○'

def create_character(character_name,character_strength,character_intelligence, character_charisma):
    if (not isinstance(character_name,str)):
        return "The character name should be a string"
    elif (len(character_name) > 10):
        return "The character name is too long"
    elif (' ' in character_name):
        return "The character name should not contain spaces"
    
    if (not (isinstance(character_strength,int) and isinstance(character_intelligence,int) and isinstance(character_charisma,int))):
        return "All stats should be integers"
    elif (character_charisma < 1 or character_intelligence < 1 or character_strength < 1):
        return "All stats should be no less than 1"
    elif (character_charisma > 4 or character_intelligence > 4 or character_strength > 4):
        return "All stats should be no more than 4"
    elif ((character_strength + character_charisma + character_intelligence) != 7):
        return "The character should start with 7 points"

    return f"""{character_name}
STR {full_dot * character_strength}{empty_dot * (10 - character_strength)}
INT {full_dot * character_intelligence}{empty_dot * (10 - character_intelligence)}
CHA {full_dot * character_charisma}{empty_dot * (10 - character_charisma)}"""

print(create_character("ren", 4, 2, 1))