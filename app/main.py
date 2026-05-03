import os


def move_file(command: str) -> None:
    words_list = command.split()
    if words_list[0] != "mv" or len(words_list) != 3:
        return
    source, destination = words_list[1], words_list[2]
    if destination.endswith("/"):
        destination = os.path.join(destination, os.path.basename(source))
    dest_dir = os.path.dirname(destination)
    if dest_dir:
        current_path = ""
        for folder in dest_dir.split("/"):
            if current_path == "":
                current_path = folder
            else:
                current_path = current_path + "/" + folder
            if not os.path.exists(current_path):
                os.mkdir(current_path)
    with open(source, "r") as file:
        content = file.read()
    with open(destination, "w") as file:
        file.write(content)
    os.remove(source)
