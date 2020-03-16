import csv, random, os
# set up directory
file_name = "data.csv"
dirname = os.path.dirname(__file__)
data_file = os.path.join(dirname, file_name)
version = "0.1"
print(f"WELCOME TO RANDOM ART PROMPTER {version}\n----------------------------------")

more = "y"
while more == "y":
    # So apparantly because the code to create row_num reads through the file, I can't use
    #   another function that reads through the file in the same Open section
    with open(data_file) as data:
        reader = csv.reader(data)
        #Select a random row num, sum function returns total number of rows
        row_num = random.randint(1, sum(1 for line in data))

    with open(data_file) as data:
        reader = csv.reader(data)
        #Return a random noun from the data csv
        noun = [row[0] for idx, row in enumerate(reader) if idx == row_num]
        #Convert noun from a list object (['noun']) to a string object (noun)
        noun = "".join(noun)

    print(f"\nWhy not draw... {noun}?")
    error = True
    while error:
        u_input = input("\nWant to draw something esle? (y/n)\n")
        if u_input == "y":
            more = u_input
            error = False
        elif u_input == "n":
            print("\nCool, good luck with your art :)")
            more = u_input
            error = False
        else:
            print(f"\nSorry, {u_input} isn't a valid input")
        