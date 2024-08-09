# Financial Budgeting Application

# TODO: Work on View entry module
# TODO: Work on importing entries module

# import packages
import sys
import time
import zmq
import json # for Ryans program

# maintain individual record of each entry
class Record:
    # individual record fields - constructor
    def __init__(self, date, description, amount, category):
        self.date = date                # store date of entry
        self.description = description  # store description of entry
        self.amount = amount            # store amount of entry
        self.category = category        # store category of entry

    # set Date
    def setDate(self, date):
        self.date = date
    
    # set Description
    def setDescription(self, description):
        self.description = description

    # set Amount
    def setAmount(self, amount):
        self.amount = amount

    # set Category
    def setCategory(self, category):
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

    # Add entry to GL
    def AddEntryToGL(self, date, description, amount, category):
        self.entryNumber += 1       # maintain unique entry numbers for each record
        self.general_ledger[self.entryNumber] = Record(date, description, amount, category)


    # General Ledger write to file
    def write_to_file(self, filename="generalLedger.txt"):
        with open(filename, "w") as file:
            for entry_num, record in self.general_ledger.items():
                # write to file using entry number and record containing multiple fields
                file.write(f"{entry_num}\t{record}\n")

    # General Ledger read from file
    def read_from_file(self, filename="generalLedger.txt"):
        with open(filename, "r") as file:
            # iterate over file contents
            for line in file:
                # parse read in records
                entry_num, date, description, amount, category = line.strip().split('\t')
                # prevents overwriting data
                if entry_num == self.entryNumber:
                    print("Entry was not included:")
                    print(entry_num, ", ", date, ", ", description, ", ", amount, ", ", category)
                    continue
                # add entry to general ledger
                self.general_ledger[int(entry_num)] = Record(date, description, amount, category)
                self.entryNumber += 1       # increment read in record 

    # Import entries
    def ImportEntryModule(self):
        print("You've selected to import entries")
        importFileName = input("Enter the name of the file you are trying to import: ")
        with open(importFileName, "r") as file:
            # iterate over file contents
            for line in file:
                # parse read in records
                date, description, amount, category = line.strip().split('\t')
                # add entry to general ledger
                self.entryNumber += 1       # increment read in record 
                self.general_ledger[int(self.entryNumber)] = Record(date, description, amount, category)
        print("All records have been imported successfully!")

    # Edit entry
    def EditEntryModule(self):
        print("You've selected to Edit an entry")
        entrySelection = input("Enter Entry # you would like to edit: ")    # choose entry by number
        print("Entry Selected: ", self.general_ledger[int(entrySelection)])
        record = self.general_ledger[int(entrySelection)]                   # store record from general ledger
        print("\nSelect which field you would like you choose: ")
        print(" 1 = Date, 2 = Description, 3 = Amount, 4 = Category, 5 = exit")
        fieldSelection = input("Enter your field choice: ")                 # capture user choice
        # update field selected by user
        match int(fieldSelection):
            case 1:
                date = input("Input new date (eg. YYYY-MM-DD): ")
                record.setDate(date)                                        # update date
                print("updated: ", record)
            case 2:
                description = input("Input new description: ")
                record.setDescription(description)                          # update description
                print("updated: ", record)
            case 3:
                amount = input("Input new amount: ")
                record.setAmount(amount)                                    # update amount
                print("updated: ", record)
            case 4:
                category = input("Input new category: ")
                record.setCategory(category)                                # update category
                print("updated: ", record)
            case 5:
                print("Exited editing entry")
                return
        
    # remove entry
    def RemoveEntryModule(self):
        print("You've selected to Remove an entry")
        entrySelection = input("Enter Entry # you would like to remove: ")    # choose entry by number
        print("Entry Selected: ", self.general_ledger[int(entrySelection)])
        confirmation = input("Please confirm you want to delete entry Y/N: ")
        if confirmation == "Y":
            del self.general_ledger[int(entrySelection)]
            print("Entry deleted!")
        else:
            print("Action cancelled!")
            return

    # view entries
    # *** premiumUser added to determine if certain views are unlocked ***
#    def ViewEntryModule(self, isPremiumUser):
    def ViewEntryModule(self):
        print("You've selected to View your entries")
        print("Which entries would you like to view:")
        print("1 = View entries for a category")
        print("2 = View entries by Date")
        print("3 = View entries by Amount")
        print("4 = View all entries")
        print("5 = Cash Flow statement [Premium feature]")
        entrySelection = input("Please select a view: ")
        if int(entrySelection) == 1:
            categorySelection = input("Which category would you like to view: ")
            print("\nEntries to view:")
            print("Entry #\t Date\t\tDescription\tAmount\tCategory")
            # unpack dictionary to isolate category selection
            for entryNum, records in self.general_ledger.items():
                if records.category == categorySelection:
                    print(entryNum, ")\t", records)
                else:
                    continue
        # Date view
        elif int(entrySelection) == 2:
            dateSelection = input("Which date would you like to view: ")
            print("\nEntries to view:")
            print("Entry #\t Date\t\tDescription\tAmount\tCategory")
            # unpack dictionary to isolate date selection
            for entryNum, records in self.general_ledger.items():
                if records.date == dateSelection:
                    print(entryNum, ")\t", records)
                else:
                    continue
        # Amount view
        elif int(entrySelection) == 3:
            amountSelection = input("Which amount would you like to view: ")
            print("\nEntries to view:")
            print("Entry #\t Date\t\tDescription\tAmount\tCategory")
            # unpack dictionary to isolate date selection
            for entryNum, records in self.general_ledger.items():
                if records.amount == amountSelection:
                    print(entryNum, ")\t", records)
                else:
                    continue
        # View all entries
        elif int(entrySelection) == 4:
            print("\nEntries to view:")
            print("Entry #\t Date\t\tDescription\tAmount\tCategory")
            # unpack dictionary to isolate date selection
            for entryNum, records in self.general_ledger.items():
                    print(entryNum, ")\t", records)

        # Cash Flow statement view 
        # *** Premium User Microservice added here ***
        elif int(entrySelection) == 5:
#            yesOrNo = input("Would you like to purchase this report? Enter: Y/N ")
#            if yesOrNo == "Y":
            # premiumUser check
            if isPremiumUser:
#                print("You've selected a premium feature which is still being developed based on your business.")
                print("Welcome premium member.")
                print("Your premium features are in development.")
            else:
#                print("You've selected No.")
                print("You've selected a Premium feature which costs $4.99")
                print("You are not a premium member, please speak with a representative to unlock.")

# introduction prompt
def introduction():
    print("Welcome to Financial Budgeting")
    print("Journey towards reaching your financial goals!")
    print("\n\n*Premium financial reports will be marked with a cost.")
    print("\tsuch as: Cash Flow statement - Premium feature [$4.99].")
    print("\n\nRecord your transactions with us through our series of options.")

# UI for entry decisions
def UiModule():
    print("Enter the option you would like to choose:")
    print("[1] Add entry")
    print("[2] Edit entry")
    print("[3] Remove entry")
    print("[4] View entries")
    print("[5] Import entries")
    print("[6] Exit")
    userSelection = input("Enter Selection: ")
    print("\n")
    return int(userSelection)


# Add entry to General Ledger
def AddEntryModule(generalLedger):
    # Into prompts
    print("You've selected to Add an entry")
    print("Please enter the following items:")
    print("Date, description, amount, and category of entry")
    # Date
    date = AddDate()
    # Description
    description = AddDescription()
    # 9 = character padding
    padding = 10
    if len(description) < padding:
        padding = padding - len(description)
        # adds padding to description for cosmetic purposes when viewing entries
        # padding does NOT persist once saved to an external file
        while padding > 0:
            description += ' '
            padding -= 1
    # Amount
    amount = AddAmount()
    # Category
    category = AddCategory()
    # Completion prompt
    print("Entry has been recorded")
    # Add entry to General Ledger
    generalLedger.AddEntryToGL(date, description, amount, category)

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

# Premium user verification - Microservice A inclusion
# Acts as the client
def PremiumUser(premiumUserName):
    # @Context(): sets up the environment so that we are able to begin creating sockets
    context = zmq.Context()
    
    # Connect to the server to send a message
    print("Client attempting to connect to server...")
    
    # @socket(socket_type): This is the type of socket we will be working with.
    # In this case REQ is the request socket
    socket = context.socket(zmq.REQ)
    
    # @connected(addr): This will connect to a remote socket
    # The format for this is: protocol://interface:port
    socket.connect("tcp://localhost:5555")
    
    # Request a value from the server. Sending a user specified string.
    #print(f"Sending a request...")

    # @send_string will send user provided login.
    socket.send_string(premiumUserName)
    
    # Get the reply.
    # @recv(flags=0, copy: bool=True, track: bool=False): will receive a message from the client.
    # Parameter will be blank for simplicity
    message = socket.recv()
        
    # Terminate connection to server
    socket.send_string("Q") # (Q)uit will ask server to stop

    # Return premium user validation
    return message

# *** TESTING dictionary parsing for Ryans program ****
def programTesting(dict):
        # @Context(): sets up the environment so that we are able to begin creating sockets
    context = zmq.Context()
    
    # Connect to the server to send a message
    print("Client attempting to connect to server...")
    
    # @socket(socket_type): This is the type of socket we will be working with.
    # In this case REQ is the request socket
    socket = context.socket(zmq.REQ)
    
    # @connected(addr): This will connect to a remote socket
    # The format for this is: protocol://interface:port
    socket.connect("tcp://localhost:5555")
    
    # Request a value from the server. Sending a user specified string.
    #print(f"Sending a request...")

    # @send_string will send user provided login.
    socket.send(json.dumps(dict).encode())
    
    # Get the reply.
    # @recv(flags=0, copy: bool=True, track: bool=False): will receive a message from the client.
    # Parameter will be blank for simplicity
    message = socket.recv()

    print("json.loads(message): ", json.loads(message))
        
    # Terminate connection to server
    #socket.send_string("Q") # (Q)uit will ask server to stop

    # Return premium user validation
    return message

# *** TESTING dictionary parsing for Ryans program ****

# *** TESTING general ledger PDF output for provided program ****
def programTesting1():
        # @Context(): sets up the environment so that we are able to begin creating sockets
    context = zmq.Context()
    
    # Connect to the server to send a message
    print("Client attempting to connect to server...")
    
    # @socket(socket_type): This is the type of socket we will be working with.
    # In this case REQ is the request socket
    socket = context.socket(zmq.REQ)
    
    # @connected(addr): This will connect to a remote socket
    # The format for this is: protocol://interface:port
    socket.connect("tcp://localhost:5555")
    
    # Request a value from the server. Sending a user specified string.
    #print(f"Sending a request...")

    # @send_string will send name of file expected to create a PDF of
    socket.send_string('generalLedger.txt')
    
    # Get the reply.
    # @recv(flags=0, copy: bool=True, track: bool=False): will receive a message from the client.
    # Parameter will be blank for simplicity
    message = socket.recv()
        
    # Terminate connection to server
    #socket.send_string("Q") # (Q)uit will ask server to stop

    # Return premium user validation
    return

# *** TESTING general ledger PDF output for provided program ****

# *** TESTING networking login ****
def programTesting2(action, user_id="Aaron", hex_key="AXS", email="Aaron@yahoo.com", year=2024, role="user"):
    #establish the socket to the server
    context = zmq.Context()
    socket = context.socket(zmq.REQ)
    socket.connect("tcp://localhost:6666")

    #complete the payload with the provided parameters
    request_payload = {
        "action": action,
        "user_id": user_id,
        "hex_key": hex_key,
        "email": email,
        "year": year,
        "role": role
    }
    #send payload
    socket.send_string(json.dumps(request_payload))
    #receive payload
    response = socket.recv_string()
    #convert payload from json to parsable string
    response_data = json.loads(response)
    
    #context.destroy()
    return response_data

# *** TESTING general ledger PDF output for provided program ****


# Main UI
def main():
    introduction()
    generalLedger = GeneralLedger()
    # automatically read in general ledger history 
    #   or create a new file to store GL activity
    responseData = programTesting2("Login")
    
    print("\nLogin credential match: ", responseData)
    
    generalLedger.read_from_file()
    #programTesting1()
    while True:
        # capture user selection
        userSelection = UiModule()
        match int(userSelection):
            case 1:
                AddEntryModule(generalLedger)
                print("\n")
            case 2:
                generalLedger.EditEntryModule()
                print("\n")
            case 3:
                generalLedger.RemoveEntryModule()
                print("\n")
            case 4:
                generalLedger.ViewEntryModule()
                print("\n")
            case 5:
                generalLedger.ImportEntryModule()
                print("\n")
            case 6:
                print("\n")
                generalLedger.write_to_file()
                print("Thank you for tracking your finances with us!")
                sys.exit()

# Main program
if __name__ == "__main__":
    main()
