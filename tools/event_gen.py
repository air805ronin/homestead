import yaml


def add_event(events):
    listlength = len(events)
    event_number = int(listlength) + 1
    print(f"List Length: {listlength} Event Number: {event_number}")
    action_text = input("What will the event's action text be? ")
    cash = input("How much cash will the player gain?")
    iron = input("How much iron will the player gain?")
    leather = input("How much leather will the player gain?")
    wood = input("How much wood will the player gain?")
    stone = input("How much stone will the player gain?")
    clay = input("How much clay will the player gain?")

    event = {'action_text': action_text, 'cash': int(cash), 'iron': int(iron), 'leather': int(leather), 'wood': int(wood), 'stone': int(stone), 'clay': int(clay)}
    events[int(event_number)] = event
    print(events)


def save_file(events, dest):
    with open(dest, 'w') as file:
        yaml.dump(events, file, default_flow_style=False)


if __name__ == '__main__':

    event_file = 'event_list.yml'
    # Load the content of the existing file
    with open(event_file) as file:
        event_list = yaml.safe_load(file)

    done = False

    while not done:
        print('''
        What do you want to do?
        1.  Create an Event
        2.  Print the list
        3.  Save and Quit
        ''')
        choice = input("What is your choice? ")

        if choice == '1':
            add_event(event_list)
        elif choice == '2':
            print(event_list)
        elif choice == '3':
            print("saving and quitting")
            save_file(event_list, event_file)
            done = True
