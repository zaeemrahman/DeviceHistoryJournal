from datetime import datetime # Import the datetime module so I can work with dates and times

def main():
    now = datetime.now() # get the current date and times

    # Format the date and time using Windows-friendly format:
    #   %#d - Day of the month without a leading zero (e.g., "4")
    #   %B  - Full month name (e.g., "March")
    #   %Y  - Four-digit year (e.g., "2025")
    #   %#I - Hour on a 12-hour clock without a leading zero (e.g., "4")
    #   %M  - Minutes with leading zero if needed (e.g., "25")
    #   %p  - AM or PM designation

    formatted_date = now.strftime("%#d %B %Y, %#I:%M %p")   #On some systems (especially Windows), the - flag might not work as expected. You might need to use %#d and %#I instead, which achieve a similar result (displaying numbers without a leading zero).

    #Ask Question 1
    print("How did you get here?")
    answer1 = input("> ").strip()   # Read and store the user's first input (Removes all the spaces)

    #Ask Question 2
    print("What are you planning to do next?")
    answer2 = input("> ").strip() #read and store user's second input

    #Build the journal entry with just formatted date and answers (no questions)
    entry = f"{formatted_date}:\n{answer1}\n{answer2}\n" + "-" * 30 + "\n"   #check this again

    #Open or create a file named "entries.txt" in append mode ("a")
    with open("entries.txt", "a") as file:
        file.write(entry) # Write the journal entry to the file

     #notify the user that the entry is saved.
    print("\nEntry saved. Good Luck!")

# This condition makes sure the main() function runs when the script is executed
if __name__ == "__main__":
    main()