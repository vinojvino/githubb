calc_tax = lambda subtotal: subtotal*0.05
calc_discount = lambda subtotal: subtotal*0.10

def launch_billing():
    cafe_name = "retro_cafe"
    coffie_price,sandwhitch_price,cake_price=10.00,12.00,15.00
    print("========================================")
    print("WELCOME TO:", cafe_name, "|",)
    print("========================================")

    system_active=True
    while system_active:
        print("\n--- welcome to retro coffie ----")
        print("1.take order for coustomer")
        print("2.patern printing")
        print("3.shut down register")
        try:
            menu_choice=int(input("\nselect your choice (1/2/3):"))
        except ValueError:
            print("enter valid number")

        if menu_choice==1:
            print("----menu selection------")
            print("black coffie: $",coffie_price)
            print("chicken sandwhitch: $",sandwhitch_price)
            print("blueforest cake: $",cake_price)

            starting_bill=0.00
            take_order(starting_bill,coffie_price,sandwhitch_price,cake_price)


        elif menu_choice==2:
            run_pattern_divider()
        elif menu_choice==3:
            print("\nclosing cash register good bye....")
            system_active=False
        else:
            print("system error invalid command select 1|2|3")

        

def take_order(current_subtotal,p1,p2,p3):
    print("\nrunning subtotal: &",current_subtotal)
    item_choice=int(input("enter selection |1 |2 |3:"))

    if item_choice==0:
        process_checkout(current_subtotal)
        return
    elif item_choice==1:
        new_subtotal=current_subtotal+p1
        print("added coffie to bill.")
        take_order(new_subtotal,p1,p2,p3)
    elif item_choice==2:
        new_subtotal=current_subtotal+p2
        print("added sandwhitch to bill.")
        take_order(new_subtotal,p1,p2,p3)
    elif item_choice==3:
        new_subtotal=current_subtotal+p3
        print("added cake to bill.")
    else:
        print("invalid item selection,try again.")
        take_order(current_subtotal,p1,p2,p3)
def process_checkout(subtotal):
    print("\n---finalizing the bill---")
    if subtotal>=15.00:
        discount_amound=calc_discount(subtotal)
        print("\nloyality point detected discount applied: &",discount_amound)
    else:
        discount_amound=0.00
    tax_amount=calc_tax(subtotal-discount_amound)
    grand_total=(subtotal-discount_amound)+tax_amount

    print("\n=========================================")
    print("\n--------------retro cafe-----------------")
    print("\n=========================================")
    print("\nsubtotal:               &",subtotal)
    print("\ndiscount:              -&",discount_amound)
    print("\ntax amount:            +&",tax_amount) 
    print("\n-----------------------------------------")
    print("\ngrand total:            &",grand_total)
    print("\n=========================================")


    cash_paid=float(input("enter the amound given by coustomer:"))
    if cash_paid>=grand_total:
        cash_change=cash_paid-grand_total
        print("\namount to be return to coustomer: &",cash_change)
    else:
        shortage=grand_total-cash_paid
        print("\ncostomer is short in amount by: &",shortage) 

def run_pattern_divider():
    print("\n--- Decorative Divider Design Matrix ---")
    size = int(input("Enter size of design line block (e.g. 5): "))
    
    print("\nGenerated Ribbon Pattern Output:\n")
    # Prints a grid layout step pattern representing a structural graphic design choice
    for i in range(1, size + 1):
        for j in range(1, i + 1):
            print("#", end=" ")
        print()


if __name__ == "__main__":
    launch_billing()
    


