def banner_text(text: str = " ", screen_width: int = 80) -> None:   # this function does an action, does not return anything
    # see above for function annotations with default values, either annotate all or (param and return) or dont annotate

    if len(text) > screen_width - 4:
        # print("EEK!!")
        # print("This text exceeds the specified width")
        raise ValueError("String {0} is larger than specified width {1}".format(text, screen_width))

    if text == "*":
        print("*" * screen_width)
    else:
        output_string = "**{0}**".format(text.center(screen_width - 4))
        print(output_string)


banner_text("lol" * 20, 66)
banner_text(screen_width=80)
banner_text("*")
# banner_text("LOOOOL")
# banner_text("ROFLLLLL")
# banner_text("ANOTHA ONE")
# banner_text("*")
#
# print()
#
# result = banner_text("None will be returned")
# print(result)