

cart_items = ""
total_amount = 0
total_items = 0

while True:

    print("\n===================================")
    print("          WELCOME TO")
    print("         SAMSUNG STORE")
    print("===================================")

    print("\n1. Overall Items Detail")
    print("2. Mobiles")
    print("3. TVs")
    print("4. Accessories")
    print("5. Exit & Bill ")

    choice = int(input("\nEnter Your Choice : "))
    if choice == 1:

        print("\n========== OVERALL ITEMS ==========")

        print("\nMobiles Available :")
        print("1. Samsung Galaxy S24 Ultra - Rs 120000")
        print("2. Samsung Galaxy A55 - Rs 45000")
        print("3. Samsung Galaxy M14 - Rs 15000")

        print("\nTVs Available :")
        print("1. Samsung Smart TV 43 inch - Rs 40000")
        print("2. Samsung QLED TV 55 inch - Rs 85000")
        print("3. Samsung LED TV 32 inch - Rs 22000")


        print("\nAccessories Available :")
        print("1. Samsung Charger - Rs 1500")
        print("2. Samsung Power Bank - Rs 3000")
        print("3. Samsung Cover - Rs 1000")


    elif choice == 2:

        while True:

            print("\n========== MOBILES ==========")

            print("1. Samsung Galaxy S24 Ultra - Rs 120000")
            print("2. Samsung Galaxy A55 - Rs 45000")
            print("3. Samsung Galaxy M14 - Rs 15000")
            print("4. Back To Main Menu")

            mobile = int(input("\nSelect Mobile : "))

            if mobile == 1:

                print("\nSamsung Galaxy S24 Ultra")
                print("RAM : 12GB")
                print("Storage : 512GB")
                print("Camera : 200MP")
                print("Price : Rs 120000")

                add = input("Add To Cart ? (yes/no) : ")

                if add == "yes":
                    cart_items = cart_items + "\nSamsung Galaxy S24 Ultra"
                    total_amount = total_amount + 120000
                    total_items = total_items + 1
                    print("Item Added Successfully")

                else:
                    print("Item Not Added")

            elif mobile == 2:

                print("\nSamsung Galaxy A55")
                print("RAM : 8GB")
                print("Storage : 256GB")
                print("Camera : 50MP")
                print("Price : Rs 45000")

                add = input("Add To Cart ? (yes/no) : ")

                if add == "yes":
                    cart_items = cart_items + "\nSamsung Galaxy A55"
                    total_amount = total_amount + 45000
                    total_items = total_items + 1
                    print("Item Added Successfully")

                else:
                    print("Item Not Added")

            elif mobile == 3:

                print("\nSamsung Galaxy M14")
                print("RAM : 6GB")
                print("Storage : 128GB")
                print("Camera : 50MP")
                print("Price : Rs 15000")

                add = input("Add To Cart ? (yes/no) : ")

                if add == "yes":
                    cart_items = cart_items + "\nSamsung Galaxy M14"
                    total_amount = total_amount + 15000
                    total_items = total_items + 1
                    print("Item Added Successfully")

                else:
                    print("Item Not Added")

            elif mobile == 4:
                break

            else:
                print("Invalid Choice")


    elif choice == 3:

        while True:

            print("\n========== TVs ==========")

            print("1. Samsung Smart TV 43 inch - Rs 40000")
            print("2. Samsung QLED TV 55 inch - Rs 85000")
            print("3. Samsung LED TV 32 inch - Rs 22000")
            print("4. Back To Main Menu")

            tv = int(input("\nSelect TV : "))

            if tv == 1:

                print("\nSamsung Smart TV 43 inch")
                print("Resolution : Full HD")
                print("Smart Features : Yes")
                print("Price : Rs 40000")

                add = input("Add To Cart ? (yes/no) : ")

                if add == "yes":
                    cart_items = cart_items + "\nSamsung Smart TV 43 inch"
                    total_amount = total_amount + 40000
                    total_items = total_items + 1
                    print("Item Added Successfully")

                else:
                    print("Item Not Added")

            elif tv == 2:

                print("\nSamsung QLED TV 55 inch")
                print("Resolution : 4K")
                print("Smart Features : Yes")
                print("Price : Rs 85000")

                add = input("Add To Cart ? (yes/no) : ")

                if add == "yes":
                    cart_items = cart_items + "\nSamsung QLED TV 55 inch"
                    total_amount = total_amount + 85000
                    total_items = total_items + 1
                    print("Item Added Successfully")

                else:
                    print("Item Not Added")

            elif tv == 3:

                print("\nSamsung LED TV 32 inch")
                print("Resolution : HD")
                print("Smart Features : No")
                print("Price : Rs 22000")

                add = input("Add To Cart ? (yes/no) : ")

                if add == "yes":
                    cart_items = cart_items + "\nSamsung LED TV 32 inch"
                    total_amount = total_amount + 22000
                    total_items = total_items + 1
                    print("Item Added Successfully")

                else:
                    print("Item Not Added")

            elif tv == 4:
                break

            else:
                print("Invalid Choice")



    elif choice == 4:

        while True:

            print("\n========== ACCESSORIES ==========")

            print("1. Samsung Charger - Rs 1500")
            print("2. Samsung Power Bank - Rs 3000")
            print("3. Samsung Cover - Rs 1000")
            print("4. Back To Main Menu")

            acc = int(input("\nSelect Accessory : "))

            if acc == 1:

                print("\nSamsung Charger")
                print("Fast Charging Supported")
                print("Price : Rs 1500")

                add = input("Add To Cart ? (yes/no) : ")

                if add == "yes":
                    cart_items = cart_items + "\nSamsung Charger"
                    total_amount = total_amount + 1500
                    total_items = total_items + 1
                    print("Item Added Successfully")

                else:
                    print("Item Not Added")

            elif acc == 2:

                print("\nSamsung Power Bank")
                print("Battery : 20000mAh")
                print("Price : Rs 3000")

                add = input("Add To Cart ? (yes/no) : ")

                if add == "yes":
                    cart_items = cart_items + "\nSamsung Power Bank"
                    total_amount = total_amount + 3000
                    total_items = total_items + 1
                    print("Item Added Successfully")

                else:
                    print("Item Not Added")

            elif acc == 3:

                print("\nSamsung Cover")
                print("Premium Protection")
                print("Price : Rs 1000")

                add = input("Add To Cart ? (yes/no) : ")

                if add == "yes":
                    cart_items = cart_items + "\nSamsung Cover"
                    total_amount = total_amount + 1000
                    total_items = total_items + 1
                    print("Item Added Successfully")

                else:
                    print("Item Not Added")

            elif acc == 4:
                break

            else:
                print("Invalid Choice")

    
    elif choice == 5:

        print("\n========== BILL SUMMARY ==========")

        print("\nSelected Items : ")
        print(cart_items)

        print("\nTotal Items :", total_items)
        print("Total Amount : Rs", total_amount)

        if total_amount > 0:

            print("\nPayment Options")
            print("1. Online Payment")
            print("2. Offline Payment")

            payment = int(input("Select Payment Method : "))

            if payment == 1:

                online = input("Do You Want To Pay Online ? (yes/no) : ")

                if online == "yes":
                    print("\nPayment Successful")
                    print("Items Booked Successfully")
                    print("Product Will Arrive Soon")

                else:
                    print("Payment Cancelled")

            elif payment == 2:

                offline = input("Cash On Delivery Confirm ? (yes/no) : ")

                if offline == "yes":
                    print("\nOrder Confirmed")
                    print("Product Will Arrive Soon")

                else:
                    print("Order Cancelled")

            else:
                print("Invalid Payment Choice")

        else:
            print("No Items Purchased")

        print("\nThank You For Visiting Samsung Store")
        break

    else:
        print("Invalid Choice Please Try Again")