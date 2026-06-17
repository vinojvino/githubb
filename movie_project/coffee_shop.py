# ==========================================
# TOPIC: Comments & Global Lambda Functions
# ==========================================

# Custom lambdas to replace built-in math functions for tax and discounts
# TOPIC: Lambda functions & Operators
calc_tax = lambda subtotal: subtotal * 0.05       # 5% flat tax rate
calc_discount = lambda subtotal: subtotal * 0.10  # 10% loyalty discount


def launch_billing():
    """
    Main controller for the billing system interface.
    Demonstrates: Simultaneous assignments, Data types, Input/Print, and Loops.
    """
    # TOPIC: Simultaneous Assignment & Data Types (String and Float)
    cafe_name, version = "Retro Byte Cafe", 2.1
    coffee_price, sandwich_price, pastry_price = 3.50, 5.00, 4.00
    
    print("========================================")
    print("WELCOME TO:", cafe_name, "| Version:", version)
    print("========================================")
    
    # TOPIC: While Loop (Keeps the cash register software running)
    system_active = True
    while system_active:
        print("\n--- REGISTER MENU ---")
        print("1. Start New Customer Order (Recursion & Operators)")
        print("2. Print Decorative Divider Pattern (Pattern Printing)")
        print("3. Shut Down Register")
        
        # TOPIC: Input & Type Casting (String to Int)
        menu_choice = int(input("\nSelect system action (1-3): "))
        
        # TOPIC: Control Statements (if, elif, else)
        if menu_choice == 1:
            print("\n--- MENU PRICE SHEET ---")
            print("Item 1 - Hot Coffee: $", coffee_price)
            print("Item 2 - Club Sandwich: $", sandwich_price)
            print("Item 3 - Fresh Pastry: $", pastry_price)
            
            # Start the order balance at 0.0 and pass to the recursive ordering machine
            starting_bill = 0.0
            take_order(starting_bill, coffee_price, sandwich_price, pastry_price)
            
        elif menu_choice == 2:
            run_pattern_divider()
        elif menu_choice == 3:
            print("\nClosing cash register. Balancing daily ledger... Goodbye!")
            system_active = False
        else:
            print("System Error: Invalid access code. Select 1, 2, or 3.")


# ==========================================
# TOPIC: Recursion & Control Statements
# ==========================================
def take_order(current_subtotal, p1, p2, p3):
    """
    Recursively builds up the user's running bill balance without using lists or lists loops.
    """
    print("\nRunning Subtotal: $", current_subtotal)
    item_choice = int(input("Enter Item Number to add (1-3) or '0' to Checkout/Finish: "))
    
    # Base Case: Customer is ready to checkout
    if item_choice == 0:
        # Pass final accumulated total over to processing checkout function
        process_checkout(current_subtotal)
        return  # Stops the recursion cleanly
        
    # Recursive Cases: Items matched to math configurations
    elif item_choice == 1:
        # TOPIC: Arithmetic Operators
        new_subtotal = current_subtotal + p1
        print("Added Hot Coffee to bill.")
        take_order(new_subtotal, p1, p2, p3)  # Loop back via recursion
        
    elif item_choice == 2:
        new_subtotal = current_subtotal + p2
        print("Added Club Sandwich to bill.")
        take_order(new_subtotal, p1, p2, p3)
        
    elif item_choice == 3:
        new_subtotal = current_subtotal + p3
        print("Added Fresh Pastry to bill.")
        take_order(new_subtotal, p1, p2, p3)
        
    else:
        print("Invalid item index selection! Try adding again.")
        take_order(current_subtotal, p1, p2, p3)


# ==========================================
# TOPIC: Operators & Type Casting Logic
# ==========================================
def process_checkout(subtotal):
    print("\n--- FINALIZING BILL MATRIX ---")
    
    # TOPIC: Control Statements & Relational/Logical Operators
    # Give a special discount only if they spent over $15.00
    if subtotal >= 15.00:
        discount_amount = calc_discount(subtotal)
        print("Loyalty status detected! Discount Applied: -$", discount_amount)
    else:
        discount_amount = 0.0
        
    # Calculate taxes using our lambda functions
    tax_amount = calc_tax(subtotal - discount_amount)
    
    # Final total calculation utilizing core operators
    grand_total = (subtotal - discount_amount) + tax_amount
    
    print("\n================================")
    print("       OFFICIAL RECEIPT        ")
    print("================================")
    print("Subtotal:        $", subtotal)
    print("Discount:       -$", discount_amount)
    print("Tax (5%):        +$", tax_amount)
    print("--------------------------------")
    print("GRAND TOTAL:     $", grand_total)
    print("================================")
    
    # Handling raw cash payment calculation
    cash_paid = float(input("\nEnter cash amount received from customer: "))
    
    if cash_paid >= grand_total:
        change_due = cash_paid - grand_total
        print("Change to return to customer: $", change_due)
    else:
        shortage = grand_total - cash_paid
        print("[ALERT] Insufficient Payment! Customer is short by: $", shortage)


# ==========================================
# TOPIC: Pattern Printing, For Loops & Range
# ==========================================
def run_pattern_divider():
    print("\n--- Decorative Divider Design Matrix ---")
    size = int(input("Enter size of design line block (e.g. 5): "))
    
    print("\nGenerated Ribbon Pattern Output:\n")
    # Prints a grid layout step pattern representing a structural graphic design choice
    for i in range(1, size + 1):
        for j in range(1, i + 1):
            print("#", end=" ")
        print()


# Execution Trigger
if __name__ == "__main__":
    launch_billing()