from datetime import datetime

text = f"Text -- {datetime.now().strftime('%H:%M:%S')}"

filename = f"{ datetime.now().strftime('%d-%m-%Y') }-file.txt"

with open(filename, "a+") as file:

    file.seek(0)

    data = file.read(100)
    if len(data) > 0 :

        file.write("\n")

    file.write(text)