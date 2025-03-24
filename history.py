import os   # For checking if file exists
from datetime import datetime # Import the datetime module so I can work with dates and times

def read_entries():
   #This function displays all entries from 'entries.txt'
   # Check if the entries file esxists
   if not os.path.exists("entries.txt"):
       print("No entries found.")
   
   #open the file in read mode and get its content
   with open("entries.txt", "r") as file:
      content = file.read()

      #Display the cointent to the user
      print ("\n--- Journal Entries ---")
      print(content)
   


   
   
def write_entry():
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

def search_entries():
    # Check if the entries file exists
    if not os.path.exists("entries.txt"):
        print("No entries found to search.")
        return
    # Ask the user for a search query (could be part of the date or any keyword)
    print("\nEnter your search query (e.g., a date like '4 March 2025' or any keyword):")
    query = input("> ").strip().lower()  # Convert to lowercase for case-insensitive search
     # Open and read all entries, then split them using the divider line as separator
    with open("entries.txt", "r") as file:
        # Each entry is separated by a line of 30 dashes and a newline
        entries = file.read().split("-" * 30 + "\n")
        # Filter the entries that contain the query string (case-insensitive search)
    matching_entries = [entry for entry in entries if query in entry.lower()]
    
    # If there are matching entries, display them
    if matching_entries:
        print("\n--- Matching Journal Entries ---")
        for entry in matching_entries:
            # Print each matching entry followed by a divider
            print(entry)
            print("-" * 30)
    else:
        print("No matching entries found.")



def main():
    # Display the menu for the user
    while True: 
        print("Welcome to your Device!")
        print("Choose an option:")
        print("1. Write a new entry")            # Option 1: Write mode
        print("2. Read existing entries")        # Option 2: Read mode
        print("3. Search entries")               # Option 3: Search mode
        print("4. Exit")                         # Option 4: Exit the program
        # Get the user's choice
        choice = input("Enter your choice (1, 2, 3 or 4): ").strip()
        
        # Call the function based on the user's choice
        if choice == "1":
            write_entry()
        elif choice == "2":
            read_entries()
        elif choice == "3":
            search_entries()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")

# This condition makes sure the main() function runs when the script is executed
if __name__ == "__main__":
    main()