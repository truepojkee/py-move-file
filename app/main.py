import os


def move_file(command: str) -> None:
    words_list = command.split()
    destination = words_list[2]
    path = destination.split("/")

    if words_list[0] != "mv":
        return

    current_path = ""
    for folder in path[:-1]:
        current_path = os.path.join(current_path, folder)
        if not os.path.exists(current_path):
            os.mkdir(current_path)

    if (len(words_list) == 3 and words_list[0] == "mv"
            and words_list[1] != words_list[2]):
        os.rename(words_list[1], words_list[2])
