import os

# text colours
class colour:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'

def print_title():
    print(colour.DARKCYAN + """                                                                                    
                                                            tttt                             lllllll                  
                                                        ttt:::t                              l:::::l                  
                                                        t:::::t                              l:::::l                  
                                                        t:::::t                              l:::::l                  
            ppppp   ppppppppp       eeeeeeeeeeee    ttttttt:::::ttttttt      aaaaaaaaaaaaa    l::::l     ssssssssss   
            p::::ppp:::::::::p    ee::::::::::::ee  t:::::::::::::::::t      a::::::::::::a   l::::l   ss::::::::::s  
            p:::::::::::::::::p  e::::::eeeee:::::eet:::::::::::::::::t      aaaaaaaaa:::::a  l::::l ss:::::::::::::s 
            pp::::::ppppp::::::pe::::::e     e:::::etttttt:::::::tttttt               a::::a  l::::l s::::::ssss:::::s
            p:::::p     p:::::pe:::::::eeeee::::::e      t:::::t              aaaaaaa:::::a  l::::l  s:::::s  ssssss 
            p:::::p     p:::::pe:::::::::::::::::e       t:::::t            aa::::::::::::a  l::::l    s::::::s      
            p:::::p     p:::::pe::::::eeeeeeeeeee        t:::::t           a::::aaaa::::::a  l::::l       s::::::s   
            p:::::p    p::::::pe:::::::e                 t:::::t    tttttta::::a    a:::::a  l::::l ssssss   s:::::s 
            p:::::ppppp:::::::pe::::::::e                t::::::tttt:::::ta::::a    a:::::a l::::::ls:::::ssss::::::s
            p::::::::::::::::p  e::::::::eeeeeeee        tt::::::::::::::ta:::::aaaa::::::a l::::::ls::::::::::::::s 
            p::::::::::::::pp    ee:::::::::::::e          tt:::::::::::tt a::::::::::aa:::al::::::l s:::::::::::ss  
            p::::::pppppppp        eeeeeeeeeeeeee            ttttttttttt    aaaaaaaaaa  aaaallllllll  sssssssssss    
            p:::::p                                                                                                  
            p:::::p                                                                                                  
            p:::::::p                                                                                                 
            p:::::::p                                                                                                 
            p:::::::p                                                                                                 
            ppppppppp
    """ + colour.END)

def print_flower():
    print(colour.DARKCYAN + """\
                                                                ....
                                                            ,;;'''';;,                    ,;;;;,
                                                  ,        ;;'      `;;,               .,;;;'   ;
                                               ,;;;       ;;          `;;,';;;,.     ,%;;'     '
                                             ,;;,;;       ;;         ,;`;;;, `;::.  %%;'
                                            ;;;,;;;       `'       ,;;; ;;,;;, `::,%%;'
                                            ;;;,;;;,          .,%%%%%'% ;;;;,;;   %;;;
                                    ,%,.      `;;;,;;;,    .,%%%%%%%%%'%; ;;;;;,;;  %;;;
                                    ;,`%%%%%%%%%%`;;,;;'%%%%%%%%%%%%%'%%'  `;;;;;,;, %;;;
                                    ;;;,`%%%%%%%%%%%,; ..`%%%%%%%%;'%%%'    `;;;;,;; %%;;
                                    `;;;;;,`%%%%%,;;/, .. `\"""'',%%%%%      `;;;;;; %%;;,
                                        `;;;;;;;,;;/////,.    ,;%%%%%%%        `;;;;,`%%;;
                                            ;;;/%%%%,%///;;;';%%%%%%,          `;;;%%;;,
                                            ;;;/%%%,%%%%%/;;;';;'%%%%%,             `%%;;
                                            .;;/%%,%%%%%//;;'  ;;;'%%%%%,             %%;;,
                                            ;;//%,%%%%//;;;'   `;;;;'%%%%             `%;;;
                                            ;;//%,%//;;;;'      `;;;;'%%%              %;;;,
                                            `;;//,/;;;'          `;;;'%%'              `%;;;
                                            `;;;;'               `;'%'                `;;;;
                                                                    '      .,,,.        `;;;;
                                                                        ,;;;;;;;;;;,     `;;;;
                                                                        ;;;'    ;;;,;;,    `;;;;
                                                                        ;;;      ;;;;,;;.   `;;;;
                                                                        `;;      ;;;;;,;;   ;;;;
                                                                            `'      `;;;;,;;  ;;;;
                                                                                    `;;,;, ;;;;
                                                                                        ;;, ;;;;
                                                                                            ';;;;;
                                                                                            ;;;;;
                                                                                            .;;;;'
                                                                                        .;;;;'
                                                                                        ;;;;;'
                                                                                        ,;;;;'
    """ + colour.END)
    input("")

def petals_poem():
    print("""\t\tLife is a stream.
On which we strew
\t\tPetal by petal the flower of our heart;
The end lost in dream,
\t\tThey float past our view,
We only watch their glad, early start.
\t\tFreighted with hope,
Crimsoned with joy,
\t\tWe scatter the leaves of our opening rose;
Their widening scope,
\t\tTheir distant employ,
We never shall know. 
\t\tAnd the stream as it flows
Sweeps them away,
\t\tEach one is gone
Ever beyond into infinite ways.
\t\tWe alone stay
While years hurry on,
\t\tThe flower fared forth, though its fragrance still stays.
\n- Amy Howell""")
    input("")

def help():
    print("to move through rooms:\t'move (forward/back)' (travel to the next or previous room)\n\
to pick up items:\t'get (item name)' (add nearby item to inventory)\n\
to talk to someone:\t'talk to (character)' (will start dialogue with character specified)\n\
          \t\t'reply' (once dialogue has started, you can continue by replying)\n\
to dig in specific rooms:\t'dig' (requires a shovel in inventory)\n\
to revise controls:\t'help' (displays all of these commands)\n")

def prompt():
    print("hey, this is you.\n\n\
this is your destiny, and this is everything you've been living for. you've made choices every single day to end up right here. i'll help you, if you let me. we're friends after all.\n\n\
to move through rooms:\t'move (forward/back)' (travel to the next or previous room)\n\
to pick up items:\t'get (item name)' (add nearby item to inventory)\n\
to talk to someone:\t'talk to (character)' (will start dialogue with character specified)\n\
          \t\t'reply' (once dialogue has started, you can continue by replying)\n\
to dig in specific rooms:\t'dig' (requires a shovel in inventory)\n\
to revise controls:\t'help' (displays controls)\n")

    input("are you ready to move forward? press Enter to continue.\n")

# clear screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# Map
rooms = {
    'First Room': {
        'Forward': 'Second Room', 
        'Prompt': "You walk into a dimly lit room. In front of you, a " + colour.GREEN + "child" + colour.END + " is crying, hands on his face, rubbing away at whatever sorrow his little head can suffer from.",
        'Item': None,
        'Character': 'child',
        'Dialogue': [
            '“My-my-my grandpa’s ball. (sobs) it’s gone! It’s lost! Now he’s gonna be sad and then he’s gonna be angry (sobs) at me and then I’m gonna be sad and then we (sobs) won’t play together a-a-and-and-and-”',
            '"I don\'t want to leave. Can you find it for me? (sniffles)”',
            '“Really? You\'ll find it? Really? Really? Thank you!”'
        ],
        'AltDialogue': "T-thank you so much! (he sprints to you to hug you around your legs, then takes the football with haste and hugs it too.). My grandfather always used to tell me not to play indoors, after this one time. All I did was " + colour.YELLOW + "kick the ball" + colour.END + " a little too hard, but I broke the glass. You know... I can let you have the ball for a while, if you want to play with it!"
    },
    'Second Room': {
        'Forward': 'Third Room', 
        'Back': 'First Room', 
        'Prompt': "There is a " + colour.GREEN + "girl" + colour.END + " sitting in front of you. The only light source in the room is a spotlight shone over her. She is ripping off the petals of a scorpion grass "  + colour.CYAN + "flower" + colour.END + ". She's surrounded by hundreds - no, thousands of them. The petals drift silently, and collapse in a brilliant hue of blue. She\'s your first love. All of a sudden, you're 15, and you haven\'t felt this nervous in years.",
        'Item': 'flower',
        'Character': 'girl',
        'Dialogue': [
            '“What do you want? There’s nothing for me to say to you.”',
            '“You’re really asking something like that? Honestly, you’re a ******. Why does it have to be you? Why can’t I just forget about you?”',
            '“I don’t care. Maybe if you could put this flower back together, I’d consider it. But you can’t, so just stop.”',
            '"Just run away again, why don’t you? That’s all you’re ever good for, anyway. So go on, leave me alone."',
            '"..."',
            '"Fine."',
            '"..."',
            '"I’m sorry about what I said. I didn’t really mean it. I get it, you were scared. So you ran away. But you came back, I don’t think most people would do that. I guess that makes you special."',
            '"I wish you stayed then as well. All I ever wanted was to be happy with you. Can’t you see that? I’m alone now, whether you loved me or not."',
            '"So don’t run away again, please. Just stay with me for a bit."',
            '"..."',
            '"No, I think I’m fine here. I’m not really sure what’s past this room, and I don’t think I wanna know."',
            '"You know, every time I ripped a petal off these flowers, I made a wish."',
            '"Am I selfish?"'
        ]
    },
    'Third Room': {
        'Forward': 'Final Room', 
        'Back': 'Second Room', 
        'Prompt': "The room's warm, and it's the first time you notice how cold it's been until now. A rugged looking " + colour.GREEN + "man" + colour.END + ", much older in age, sits in front of you on a mesh office chair. He stares at you through the thick of his eyebrows.\nA rusty " + colour.CYAN + "shovel" + colour.END + " lays on the ground in front of you, the light reflecting off the tiny speck of silver that remains unadulterated.",
        'Item': 'shovel',
        'Character': 'man',
        'Dialogue': [
            '“Did I tell you to stop digging?”',
            '“You\'re pissing me off, you know that? This work ethic... where\'d you get it from? I never taught you to live like this.”',
            '“Get back down there, and don\'t look up until the sun\'s boiling the back of your neck.”'
        ],
        'DigMessage': "You heave the shovel at the ground beneath your feet and throw the earth over your shoulder."
    },
    'Final Room': {
        'Prompt': "You flick the switch on. You've stepped into a room of quite the calibre. On your right, there is a king-size bed, centred flush to the wall, draped in white sheets. In the middle of the room, a square "  + colour.YELLOW + "patch of dirt" + colour.END + " no bigger than the top of a bedside desk. \nIts edges are boarded off by thick wooden planks. At the front of the room, a giant" + colour.YELLOW + " mirror" + colour.END + " meets the ceiling and both adjacent walls. A 2006 World Cup replica" + colour.CYAN + " football" + colour.END + " lies in the corner of the room.\
        \nThis is it. This is everything you've been working for. If you still have your shovel on you, you can dig down into the dirt and make a tunnel. Every day, the dirt will go back to normal, and you will be paid handsomely by the hour. \nYou can even leave the game once you say, " + colour.YELLOW + "I accept" + colour.END + ". \nDo you accept these conditions?",
        'Back': 'Third Room', 
        'Item': 'football'
    }
}

# List of vowels
vowels = ['a', 'e', 'i', 'o', 'u']

# List to track inventory
inventory = []

# Tracks current room
current_room = "First Room"

# Tracks last move
msg = ""

dialogue_index = {
    'child': 0,
    'girl': 0,
    'man': 0
}

active_character = None

last_valid_dialogue = ""

# Function to handle dialogue progression
def handle_dialogue(character):
    global dialogue_index
    if character in dialogue_index:
        index = dialogue_index[character]
        if index < len(rooms[current_room]['Dialogue']):
            return rooms[current_room]['Dialogue'][index]
    return None

clear()
petals_poem()
clear()
print_title()
print_flower()
clear()
prompt()

while True:

    clear()

    print(f"Inventory : {inventory}\n{'-' * 27}")

    if active_character is None:
        print(msg)
    else:
        print(last_valid_dialogue)
    
    if active_character is None and 'Prompt' in rooms[current_room]:
        print(rooms[current_room]['Prompt'])

    # Item indicator
    if "Item" in rooms[current_room].keys() and rooms[current_room]["Item"] is not None:
        nearby_item = rooms[current_room]["Item"]

    if "Character" in rooms[current_room].keys() and rooms[current_room]["Character"] is not None:
        nearby_character = rooms[current_room]["Character"]

    user_input = input("\nWhat will you do?:\n")

    next_move = user_input.split(' ')

    action = next_move[0].title()

    item = "Item"
    direction = "null"
    character = "Character"

    if len(next_move) > 1:
        if action == "Talk" and next_move[1].lower() == "to":
            character = " ".join(next_move[2:]).lower()
        else:
            item = next_move[1:]
            direction = next_move[1].title()
            item = " ".join(item).lower()
    
    if action == "Help":
        clear()
        help()
        input("")

    # Moving between rooms
    if action == "Move" and active_character is None:
        try:
            current_room = rooms[current_room][direction]
            msg = f"You move {direction.lower()}"
            last_valid_dialogue = ""
        except:
            msg = "You can't go that way."
    
    elif action == "Get" and active_character is None:
        try:
            if item == rooms[current_room]["Item"]:
                if item not in inventory:
                    inventory.append(rooms[current_room]["Item"])
                    msg = f"You picked up the {item}"
                    last_valid_dialogue = ""
                else:
                    msg = f"You already have the {item}"
            else:
                msg = f"Can't find {item}"
        except:
            msg = f"Can't find {item}"

    elif action == "Talk" and len(next_move) > 2 and next_move[1].lower() == "to":
        try:
            if character == rooms[current_room]["Character"]:
                if character == 'child' and current_room == 'First Room' and 'football' in inventory:
                    active_character = character
                    msg = rooms[current_room]['AltDialogue']
                else:
                    msg = ""
                    active_character = character
                    dialogue = handle_dialogue(character)
                    if dialogue:
                        msg = dialogue
                        last_valid_dialogue = dialogue
                        dialogue_index[character] += 1
                    else:
                        msg = f"No more dialogue available for {character}. Reply if you understand."
                        last_valid_dialogue = msg
            else:
                msg = f"Can't find {character}"
        except KeyError:
            msg = f"Can't find {character}"

    elif action == "Reply" and active_character is not None:
        dialogue = handle_dialogue(active_character)
        if dialogue:
            msg = dialogue
            last_valid_dialogue = dialogue
            dialogue_index[active_character] += 1
        else:
            msg = f"No more dialogue available for {active_character}."
            last_valid_dialogue = msg
            active_character = None
    elif action == "Rust" and active_character is None:
        print("Well, once there was only dark. If you ask me, the light's winning.")
        input("")

    elif action == "Dig" and current_room == "Third Room":
        if "shovel" in inventory:
            active_character = character
            msg = rooms[current_room]["DigMessage"]
        else:
            msg = "You need a shovel to dig."

    elif action == "I" and len(next_move) > 1 and next_move[1].lower() == "accept" and current_room == "Final Room":
        clear()
        break

    elif action == "Kick" and len(next_move) > 1 and next_move[1].lower() == "football" and current_room == "Final Room" and "football" in inventory:
        clear()
        msg = "You're a little rusty, but you manage to do a flick up and get some juggles going. You take a volley at the wall, but in an attempt to put some spin on it, it flies straight at the mirror. Unbelievably, the entire mirror shatters as if it were made of sugarglass, and you stare at the abyss ahead of you.\nThe football in your hands begins to glow, and the leather panels holding its shape collapse open, resembling a water lotus. You take a step forward into the dark, and you feel the ground transition into moist grass. The wind's sharp, and your dry face is copping the worst of it. \nIt smells like winter.\n"
        print(msg)
        input("")
        break

    elif action == "Plant" and len(next_move) > 1 and next_move[1].lower() == "flower" and current_room == "Final Room" and "flower" in inventory:
        clear()
        msg = "As tarnished as it may be, you practically stab the flower (which has been reduced to stem and pistil) into the patch of dirt. The dirt patch begins to slides over, revealing a bottomless tunnel. You jump down the tunnel and miraculously survive the fall. \nYou're on a beach. The sun is rising. The sand under your toes is too comforting for you to notice how cold it is. \nA woman in a wedding gown runs towards you, throwing balls of wet sand at you. You laugh, until you realise she's gotten your suit dirty. You laugh even harder. Do you deserve this? How selfish... \nIt smells like summer.\n"
        print(msg)
        input("")
        break

    elif action == "Exit":
        break
    else:
        msg = "Invalid command"
