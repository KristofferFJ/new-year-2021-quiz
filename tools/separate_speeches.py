lines = open("../input/all_speeches", encoding="utf-8").readlines()


def write_file(name, content):
    f = open("nytaarstaler/" + name[-5:-1] + ".txt", "w", encoding="utf-8")
    f.write(content)
    f.close()


filename = ""
current_speech = ""
for line in lines:
    if line.startswith("Dronningens nyt"):
        write_file(filename, current_speech)
        filename = line
        current_speech = ""
        continue
    current_speech += line

write_file(filename, current_speech)
