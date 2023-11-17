
with open("Input/invited/invited_names.txt", mode="r") as file:
    names = file.read().splitlines()

text = "[name]"

for i in range(0, len(names)):
    with open("Input/template/template.txt") as file:
        f = file.read()

        f = f.replace(text, names[i])

    loc = "Output/Indi_letters/" + names[i] + ".txt"

    with open(loc, mode="w") as file2:
        file2.write(f)
