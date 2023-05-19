import datetime

# Create a dictionary to store the reservations
reservations = {}

def make_reservation():
    # Get input from the user
    date = input("Enter the reservation date (YYYY-MM-DD): ")
    number_of_guests = int(input("Enter the number of guests: "))
    price = float(input("Enter the price: "))
    special_arrangements = input("Enter any special arrangements: ")
    phone_number = input("Enter the phone number: ")

    # Store the reservation data in a dictionary
    reservation_data = {
        "date": date,
        "number_of_guests": number_of_guests,
        "price": price,
        "special_arrangements": special_arrangements,
        "phone_number": phone_number
    }

    # Generate a unique reservation ID
    reservation_id = len(reservations) + 1

    # Store the reservation data in the reservations dictionary using the ID as key
    reservations[reservation_id] = reservation_data

    # Print a confirmation message
    print("Reservation successfully made!")

def display_reservation(reservation_id):
    # Check if the reservation ID exists
    if reservation_id in reservations:
        reservation_data = reservations[reservation_id]

        # Print the reservation details
        print("Reservation Details:")
        print("Date:", reservation_data["date"])
        print("Number of Guests:", reservation_data["number_of_guests"])
        print("Price:", reservation_data["price"])
        print("Special Arrangements:", reservation_data["special_arrangements"])
        print("Phone Number:", reservation_data["phone_number"])
    else:
        print("Reservation not found.")

def schedule_call(reservation_id):
    # Check if the reservation ID exists
    if reservation_id in reservations:
        reservation_data = reservations[reservation_id]

        # Calculate the reminder date (7 days before the reservation date)
        reservation_date = datetime.datetime.strptime(reservation_data["date"], "%Y-%m-%d").date()
        reminder_date = reservation_date - datetime.timedelta(days=7)

        # Print the reminder
        print("Reminder: Call", reservation_data["phone_number"], "on", reminder_date)
    else:
        print("Reservation not found.")

# Example usage
make_reservation()
display_reservation(1)
schedule_call(1)