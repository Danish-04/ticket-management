TICKETLIST = []
TICKET_DICT = {}

class Ticket:
    Ticketid = 1000

    def __init__(self, origin, destination, date, name, age, price):
        self.origin = origin
        self.destination = destination
        self.date = date
        self.name = name
        self.age = age
        self.price = price  # Store the price when creating a Ticket object
        self.Ticketid = Ticket.Ticketid
        Ticket.Ticketid += 1

    def generate_ticket_booking_id(self):
        return f"{'FLN'}{self.Ticketid}"

    def __str__(self):
        booking_id = self.generate_ticket_booking_id()
        return f"""
Ticket ID     :{self.Ticketid}
Booking ID    :{booking_id}
Origin        :{self.origin}
Destination   :{self.destination}
Date          :{self.date}
Name          :{self.name}
Age           :{self.age}
Price         :Rs.{self.price}"""  # Include the price in the ticket details

def calculate_price(origin, destination):
    city_distances = {
        ("Nasik", "Mumbai"): 2000,
        ("Mumbai", "Nasik"): 2500,
        ("Nasik", "Pune"): 5000,
        ("Pune", "Nasik"): 5100,
        ("Mumbai", "Pune"): 4000,
        ("Pune", "Mumbai"): 4200,
    }

    if (origin, destination) in city_distances:
        distance = city_distances[(origin, destination)]
        
        price = distance
        return price
    else:
        return 

def add_tickets():
    origin = input("Enter Origin          : ")
    destination = input("Enter Destination: ")
    
    # Calculate the price using calculate_price function
    price = calculate_price(origin, destination)

    date = input("Enter Date              : ")
    name = input("Enter Your Name         : ")
    age = int(input("Enter your Age       : "))

    ticket = Ticket(origin, destination, date, name, age, price)

    ticket_details = (origin, destination, date, name, age, price)
    TICKETLIST.append(ticket_details)
    booking_id = ticket.generate_ticket_booking_id()
    TICKET_DICT[booking_id] = ticket

def show_tickets():
    for booking_id, ticket in TICKET_DICT.items():
        print(ticket)

def Update_Ticket():
    booking_id = input("Enter Booking ID to Update the Details: ")
    if booking_id in TICKET_DICT:
        print("What you want to Update..?")
        print("1. Origin")
        print("2. Destination")
        print("3. Date")
        print("4. Exit")
        
        choice = int(input("Enter your choice: "))
        if choice == 1:
            new_origin = input("Enter New Origin: ")
            ticket = TICKET_DICT[booking_id]
            ticket.origin = new_origin
            print("Origin Updated successfully...!")
        elif choice == 2:
            new_destination = input("Enter New destination: ")
            ticket = TICKET_DICT[booking_id]
            ticket.destination = new_destination
            print("Destination Updated successfully...!")
        elif choice == 3:
            new_date = input("Enter New Date: ")
            ticket = TICKET_DICT[booking_id]
            ticket.date = new_date
            print("Date Updated successfully...!")
        elif choice == 4:
            return
        else:
            print("Choose Correct Input")
    else:
        print("Booking ID not found.")

def main():
    while True:
        print("Choose the option")
        print("1. Book a new Ticket")
        print("2. Show a Ticket")
        print("3. Update Ticket")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_tickets()
            print("Ticket Booked Added Successfully..!")

        elif choice == 2:
            for booking_id, ticket in TICKET_DICT.items():
                print(ticket)

        elif choice == 3:
            Update_Ticket()

        elif choice == 4:
            print("---End of program---")
            break

        else:
            print("Choose the Correct Input")

if __name__ == "__main__":
    main()

