# keep a seperate list of duplicate colors and print it at the end
# make sure the duplicate list does not contain duplicates itself
# print the color list and duplicate list at the end of the program

QUIT_CLAUSE = "quit"

colors = []
duplicates = []
while True:
    color_input = input("Enter a color to add to the list (or 'quit' to exit): ")
    if color_input.lower() == QUIT_CLAUSE:
        break
    if color_input not in colors:
        colors.append(color_input)
        print(f"you entered: {color_input}. The list is now: {colors}")
    else:
        if color_input not in duplicates:
            duplicates.append(color_input)
        print(f"{color_input} is already in the list.")
print(f"The list of colors is: {colors}")
print(f"The list of duplicates is: {duplicates}")
