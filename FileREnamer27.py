# Rename's files in bulk, keeping the original filename intact, while adding whatever the user wants to the beginning.

import os


def main():
    path_exists()


# Check that file path exists
def path_exists():
    while True:
        # Ask user to enter the filepath of the files they want to rename
        filePath = raw_input("Enter directory of files you want to rename: ")
        if os.path.isdir(filePath):
            print("File path found...")
            print("")
            # Ask user to enter what text they want to pre-pend to the files in said path
            text = raw_input("Enter text to pre-pend: ")
            # Loop through files and pre-pend user's text to the files
            for filename in os.listdir(filePath):
                # pre-pend user text
                new_filename = text + filename
                print(new_filename)
                os.rename(os.path.join(filePath, filename), os.path.join(filePath, new_filename))
            print("Finished")
            break
        else:
            print("Invalid path; try again")
            continue  # restart loop


main()