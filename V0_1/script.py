import csv, random, os
# set up directory
file_name = "data.csv"
dirname = os.path.dirname(__file__)
data_file = os.path.join(dirname, file_name)

#Set up variables
version = "0.1"
noun_types = {1: "object", 2: "scene", 3: "concept"}

#Start
print(f"WELCOME TO RANDOM ART PROMPTER {version}\n----------------------------------")
print("Be creative, interpret things however you want!")

more = "y"
while more == "y":
    n_type = ""
    error = True
    while error:
        try:
            n_type = noun_types[int(input(f"\nWhat would you like draw?\n\n1 - {noun_types[1]}\n2 - {noun_types[2]}\n3 - {noun_types[3]}\n\n"))]
            error = False
        except (KeyError, ValueError):
            print("\nSorry, that's not a valid input")

            
    # So apparantly because the code to create row_num reads through the file, I can't use
    #   another function that reads through the file in the same Open section
    ready = False
    while not ready:
        with open(data_file) as data:
            reader = csv.reader(data)
            #Select a random row num, sum function returns total number of rows
            row_num = random.randint(1, sum(1 for line in data))
        with open(data_file) as data:
            reader = csv.reader(data)
            #Return a random noun from the data csv
            row = [row for idx, row in enumerate(reader) if idx == row_num]
            #Confirm ready if the row is of the chosen noun type
            ready = row[0][2] == n_type
    
    article = row[0][0]
    noun = row[0][1]
    prompt = f"Why not draw {article} {noun}?"
    #Print prompt, removing extra whitespace from empty articles
    print("\n" + " ".join(prompt.split()))
    error = True
    #Loop continuation options, with validation
    while error:
        u_input = input("\nWant to draw something else? (y/n)\n\n")
        if u_input == "y":
            more = u_input
            error = False
        elif u_input == "n":
            print("\nCool, good luck with your art :)")
            more = u_input
            error = False
        else:
            print(f"\nSorry, that's not a valid input")
        