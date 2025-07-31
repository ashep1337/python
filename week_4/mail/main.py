with open("Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

    for name in name_list:
        name.strip("'$'\n'")
        with (
            open((f"Output/ReadyToSend/invite_for_{name}"), mode="w") as file,
            open("Input/Letters/starting_letter.txt") as temp,
        ):
            file.write(temp.read())

        with open((f"Output/ReadyToSend/invite_for_{name}"), "r+") as file:
            content = file.read()
            content = content.replace("[name]", name)
            file.seek(0)
            file.write(content)
