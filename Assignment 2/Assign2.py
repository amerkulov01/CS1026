from code_check import*

# creating lists for the different types of code
basic_list = []
positional_list = []
upc_list = []
none_list = []

# start of loop
while True:
    # prompting user to input code
    user_code = int(input("Please enter code (digits only) (enter 0 to quit) "))
    if user_code == 0:
        break
    valid_basic_code = basic_code(user_code)
    valid_positional_code = positional_code(user_code)
    valid_upc_code = upc_code(user_code)
    if not valid_basic_code and not valid_basic_code and not valid_upc_code:    # if the inputted code is neither basic, positional or UPC
        print("-- code: " + str(user_code) + " not Basic, Position or UPC code.")
        none_list.append(user_code)                      # user inputted code is stored in "none"
    else:
        if valid_basic_code:                        # if it is a basic code
            print("-- code: " + str(user_code) + " valid Basic code.")
            basic_list.append(user_code)                 # user inputted code is stored in "basic"
        if valid_positional_code:
            print("-- code: " + str(user_code) + " valid Position code.")
            positional_list.append(user_code)            # user inputted code is stored in "positional"
        if valid_upc_code:
            print("-- code: " + str(user_code) + " valid UPC code.")
            upc_list.append(user_code)                   # user inputted code is stored in "UPC"
        # still stores in multiple code lists if the code applies to more than one locations

print("\nSummary")
if not basic_list:                                       # checks if the list is empty
    print("Basic: None")
else:
    print("Basic: " + str(basic_list)[1:-1])
if not positional_list:                                  # checks if the list is empty
    print("Position: None")
else:
    print("Position: " + str(positional_list)[1:-1])
if not upc_list:                                         # checks if the list is empty
    print("UPC: None")
else:
    print("UPC: " + str(upc_list)[1:-1])
if not none_list:                                        # checks if the list is empty
    print("None: None")
else:
    print("None: " + str(none_list)[1:-1])
