computer_parts = ["computer",
                  "monitor",
                  "keyboard",
                  "mouse",
                  "mouse_mat"
                  ]

for part in computer_parts:
    print(part)

print()
# print(computer_parts[2])
#
# print(computer_parts[0:3])
# print(computer_parts[-1])

# strings are immutable, lists are not

# immutable: int, float, bool (True and False), str (string), tuple, frozenset, bytes

# computer_parts[3] = "trackball"
print(computer_parts[3:])
# computer_parts[3:] = "trackball"
computer_parts[3:] = ["trackball"]

print(computer_parts)