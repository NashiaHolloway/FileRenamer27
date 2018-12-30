# Rename's files in bulk, keeping the original filename intact, while adding whatever the user wants to the beginning.

import os


def main():
    file_exists()


# Check that file path exists
def file_exists():
    while True:
        # Ask user to enter the filepath of the files they want to rename
        file_path = raw_input("Enter directory of files you want to rename (q to quit): ").lower()
        if file_path != "q":
            if os.path.isdir(file_path):
                print("File path found...")
                print("")
                renamer(file_path)
            else:
                print("Invalid path; try again")
                continue  # restart loop
        else:
            break


def renamer(file_path):
    while True:
        # Ask user to enter what text they want to pre-pend to the files in said path
        text = raw_input("Enter text to pre-pend: ")
        # Make sure user input is what they want
        ans = raw_input("Are you sure you want to pre-pend '" + text.upper() + "'? (y/n) ").lower()
        if ans == "y":
            # Loop through files and pre-pend user's text to the files
            for filename in os.listdir(file_path):
                # pre-pend user text
                new_filename = text + filename
                print(new_filename)
                os.rename(os.path.join(file_path, filename), os.path.join(file_path, new_filename))
            print("Finished")
            break
        else:
            print("")
            renamer(file_path)
            break


main()
