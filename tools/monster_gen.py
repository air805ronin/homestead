import yaml


def add_monster(monsters):
    listlength = len(monsters)
    monster_number = int(listlength) + 1
    print(f"List Length: {listlength}  Monster Number: {monster_number}")
    name = input("What is the name of the monster? ")
    action_text = input("What will the monster's action text be? ")
    inputsize = input("Is the monster 'small', 'medium', 'large', or 'giant'?")
    if inputsize == "small":
        size = 1
    elif inputsize == "medium":
        size = 2
    elif inputsize == "large":
        size = 3
    elif inputsize == "giant":
        size = 4
    hp_die = input("How many hit point dice will roll?")
    attacks = input("How many attacks will the monster get?")

    monster = {'name': name, 'action_text': action_text, 'size': size, 'hp_die': int(hp_die), 'attacks': int(attacks)}
    monsters[int(monster_number)] = monster
    print(monsters)


def save_file(monsters, dest):
    with open(dest, 'w') as file:
        yaml.dump(monsters, file, default_flow_style=False)


if __name__ == '__main__':

    monster_file = 'monster_list.yml'
    # Load the content of the existing file
    with open(monster_file) as file:
        monster_list = yaml.safe_load(file)

    done = False

    while not done:
        print('''
        What do you want to do?
        1.  Create a Monster
        2.  Print the list
        3.  Save and Quit
        ''')
        choice = input("What is your choice? ")

        if choice == '1':
            add_monster(monster_list)
        elif choice == '2':
            print(monster_list)
        elif choice == '3':
            print("saving and quitting")
            save_file(monster_list, monster_file)
            done = True
