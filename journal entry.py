entry_count = 0

def save_entry(entry):
    global entry_count

    try:

        file = open("journal.txt", "a")
        file.write(entry + "\n")
        file.close()

        entry_count += 1
        print("Entries saved this run:", entry_count)

    except OSError:
        print("Sorry, there was a problem opening the journal file.")



journal_entry = input(
    "Enter your journal entry (Example: Today I have basketball practice.): "
)


save_entry(journal_entry)