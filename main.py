TICKET_DICT = {}

class Ticket:
    Ticketid = 1000

    def __init__(self, origin, destination, date, name, age, price):
        self.origin = origin
        self.destination = destination
        self.date = date
        self.name = name
        self.age = age
        self.price = price  
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
Price         :Rs.{self.price}"""  

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
    
    price = calculate_price(origin, destination)

    date = input("Enter Date              : ")
    name = input("Enter Your Name         : ")
    age = int(input("Enter your Age       : "))

    ticket = Ticket(origin, destination, date, name, age, price)

    ticket_details = (origin, destination, date, name, age, price)
    TICKET_DICT[ticket.generate_ticket_booking_id()] = ticket
    print("Ticket Booked Added Successfully..!")

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

def cancel_ticket():
    booking_id = input("Enter Booking ID to Cancel the Ticket: ")
    if booking_id in TICKET_DICT:
        del TICKET_DICT[booking_id]
        print(f"Ticket {booking_id} has been canceled successfully.")
    else:
        print("Booking ID not found.")

def main():
    while True:
        print("Choose the option")
        print("1. Book a new Ticket")
        print("2. Show a Ticket")
        print("3. Update Ticket")
        print("4. Cancel Ticket")
        print("5. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            add_tickets()
        elif choice == 2:
            show_tickets()
        elif choice == 3:
            Update_Ticket()
        elif choice == 4:
            cancel_ticket()
        elif choice == 5:
            print("---End of program---")
            break
        else:
            print("Choose the Correct Input")

if __name__ == "__main__":
    main()
