destinations = ["Goa", "Manali", "Kerala"]
prices = [15000, 12000, 18000]

# Empty list to store bookings
bookings = []

# Show available destinations
def show_destinations():
    print("\nAvailable Destinations:")
    for i in range(len(destinations)):
        print(f"{i+1}. {destinations[i]} - ₹{prices[i]} per person")

# Book a trip
def book_trip():
    name = input("Enter your name: ")
    show_destinations()
    choice = int(input("Choose destination number (1-3): "))
    people = int(input("Enter number of people: "))

    # Calculate total cost
    destination = destinations[choice - 1]
    cost = prices[choice - 1] * people

    # Store booking info
    bookings.append([name, destination, people, cost])

    print(f"\n✅ Booking confirmed for {name} to {destination}!")
    print(f"Total Cost: ₹{cost}")

# Show all bookings
def show_bookings():
    if len(bookings) == 0:
        print("\nNo bookings yet.")
    else:
        print("\nAll Bookings:")
        for b in bookings:
            print(f"{b[0]} booked a trip to {b[1]} for {b[2]} people – Total ₹{b[3]}")

# Main Menu
def main():
    while True:
        print("\n--- Travel Agency ---")
        print("1. View Destinations")
        print("2. Book Trip")
        print("3. Show Bookings")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == "1":
            show_destinations()
        elif choice == "2":
            book_trip()
        elif choice == "3":
            show_bookings()
        elif choice == "4":
            print("Thank you for using our Travel Agency!")
            break
        else:
            print("Invalid choice. Try again.")

# Run the program
main()
