# Financial Budgeting Application

# TODO: Determine which data structure works best for storing journal entries = Dictionary

# maintain individual record of each entry
class Record:
    # constructor
    def __init__(self, date, description, amount, category):
        self.date = date
        self.description = description
        self.amount = amount
        self.category = category

    # output record
    def __str__(self):
        return f"{self.date}\t{self.description}\t{self.amount}\t{self.category}"

# maintain general ledger which encapsulates records
class GeneralLedger:
    # constructor
    def __init__(self):
        self.general_ledger = {}    # dictionary to store individual records
        self.entryNumber = 0        # maintain rolling entry number


def introduction():
    print("Welcome to Financial Budgeting")
    print("Journey towards reaching your financial goals!")
    print("\n\n*Premium financial reports will be marked with a cost.")
    print("\tsuch as: Cash Flow statement - Premium feature [$4.99].")
    print("\n\nRecord your transactions with us through our series of options.")

def UiModule():
    print("Enter the numeric option you would like to choose:")
    print("[1] Add entry")
    print("[2] Edit entry")
    print("[3] Remove entry")
    print("[4] View entries")
    print("[5] Import entries")
    print("[6] Exit")

# Add entry to General Ledger
def AddEntryModule():
    # Into prompts
    print("You've selected to Add an entry")
    print("Please enter the following items:")
    print("Date, description, amount, and category of entry")
    # Date
    date = AddDate()
    # Description
    description = AddDescription()
    # Amount
    amount = AddAmount()
    # Category
    category = AddCategory()
    # Completion prompt
    print("Entry has been recorded")
    # Add entry to General Ledger
    GeneralLedger(date, description, amount, category)

# Add date to entry
def AddDate():
    date_entry = input("Enter Date with format YYYY-MM-DD format: ")
    return date_entry

# Add description to entry
def AddDescription():
    description_entry = input("Enter entry description (eg. Purchased Chipote): ")
    return description_entry

# Add amount to entry
def AddAmount():
    amount_entry = input("Enter amount of entry (eg. 10.00): ")
    return amount_entry

# Add category to entry
def AddCategory():
    category_entry = input("Enter category of entry (eg. Food): ")
    return category_entry

# General Ledger write to file
def GeneralLedgerWrite(entryNumber, dateGL, descriptionGL, amountGL, categoryGL):
    file = open("generalLedger.txt", "a")
    file.writelines('\n' + entryNumber + '\t')
    file.writelines(dateGL + '\t')
    file.writelines(descriptionGL + '\t')
    file.writelines(amountGL + '\t')
    file.writelines(categoryGL)
    file.close()

# General Ledger read from file
def GeneralLedgerRead():
    print("Date\t\tDescription\tAmount\tCategory")
    file = open("generalLedger.txt", "r")
    print(file.read())


# Edit entry
def EditEntryModule():
    print("You've selected to Edit an entry")
    print("Enter Entry # you would like to edit")


# Main UI
def main():
    introduction()

# Main program
if __name__ == "__main__":
    main()
#    AddEntryModule()
    GeneralLedgerRead()

