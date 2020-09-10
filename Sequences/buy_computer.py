available_parts = ["computer",
                   "monitor",
                   "keyboard",
                   "mouse",
                   "mouse mat",
                   "hdmi"]
current_choice = "-"
# valid_choices = [str(i) for i in range(1, len(available_parts) + 1)]
valid_choices = []
for i in range(1, len(available_parts) + 1):
    valid_choices.append(str(i))

print(valid_choices)
computer_parts = []

while current_choice != "0":
    if current_choice in valid_choices:
    # if current_choice in "123456":
        index = int(current_choice) - 1
        chosen_part = available_parts[index]
        if chosen_part in computer_parts:
            print("Removing {}".format(current_choice))
            computer_parts.remove(chosen_part)
        else:
            print("Adding {}".format(current_choice))
            computer_parts.append(chosen_part)
        # computer_parts.append(current_choice)
        print("Current cart {}".format(computer_parts))
    else:
        print("Please add options from the list below:")
        # for part in available_parts:
        #     print("{0}: {1}".format(available_parts.index(part) + 1, part))
        for number, part in enumerate(available_parts): # enumerate provides pair of values, for for all iterable types
            print("{0}: {1}".format(number + 1, part))

    current_choice = input()

print(computer_parts)