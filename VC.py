import re

phone_number_pattern = r"^\+233\d{9}$"  # Specific pattern for phone number input
FDA_pin_pattern = r"^FDA/[A-Z]{2}/\d{2,3}-\d{2,4}$"  # specific pattern to follow for FDA pin to follow

def get_user_input(pattern, message):  
    while True:
        user_input = input(message)
        if re.match(pattern, user_input):
            return user_input
        else:
            print("Invalid input. Please try again.")

def FDA_approval():
    print("This Product is approved by FDA")
    print("Expiry Date: 12/06/24")
    

def main_menu():
    while True:
        print("Welcome to Sunset Scan Center!")
        print("1. Verify Product")
        print("2. Report Drug")
        print("3. Talk to an agent")
        option = input("Select an option: ")

        if option == "1":
            print("Specify product:")
            print("1. Drugs")
            print("2. Sachet water")
            print("3. Can Foods")
            print("4. Bottle Water and Drinks")
            print("0. Go back")
            product_type = input("Select a product: ")

            if product_type == "1" or product_type == "2" or product_type == "3" or product_type == "4":
                phone_number = get_user_input(phone_number_pattern, "Enter your phone number (+233 and 10 numbers): ")
                product_fda_pin = get_user_input(FDA_pin_pattern, "Enter FDA PIN (format: FDA/XX/YY-NNN): ")
 

                # Assuming you want to proceed with FDA approval if the PIN is correct
                if re.match(FDA_pin_pattern, product_fda_pin):
                    FDA_approval()
                    break
                
                
                else:
                    print("Invalid FDA PIN.")
                    
                    
            elif product_type == "0":
                continue
                
            else:
                print("Invalid option.")
                
        elif option == "2":
            # Handle drug reporting logic
            break
        elif option == "3":
            # Handle agent interaction logic
            break
        else:
            print("Invalid option. Please try again.")

# Call the main menu function to start the program
main_menu()
