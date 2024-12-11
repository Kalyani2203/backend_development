class MenuItem:
    def __init__(self, name, description, price, category):
        self.name = name
        self.description = description
        self.price = price
        self.category = category

    def __str__(self):
        return f"{self.name} - {self.description} (${self.price})"


class Reservation:
    def __init__(self, name, email, phone, date, time, party_size, notes=""):
        self.name = name
        self.email = email
        self.phone = phone
        self.date = date
        self.time = time
        self.party_size = party_size
        self.notes = notes

    def __str__(self):
        return f"Reservation for {self.name} on {self.date} at {self.time} for {self.party_size} people."


class Order:
    def __init__(self, table_number):
        self.table_number = table_number
        self.items = []
        self.completed = False

    def add_item(self, menu_item, quantity):
        self.items.append((menu_item, quantity))

    def complete_order(self):
        self.completed = True

    def __str__(self):
        items_str = ', '.join([f"{quantity} x {item.name}" for item, quantity in self.items])
        return f"Order for Table {self.table_number}: {items_str} (Completed: {self.completed})"


# Example usage
if __name__ == "__main__":
    # Create some menu items
    pizza = MenuItem("Pizza", "Delicious cheese pizza", 12.99, "Main Course")
    salad = MenuItem("Salad", "Fresh garden salad", 7.99, "Appetizer")
    burger = MenuItem("Burger", "Juicy beef burger with fries", 10.99, "Main Course")
    pasta = MenuItem("Pasta", "Creamy Alfredo pasta", 11.99, "Main Course")

    # Print menu items
    print("Menu Items:")
    for item in [pizza, salad, burger, pasta]:
        print(item)
    print()

    # Create a reservation
    reservation1 = Reservation("John Doe", "john@example.com", "123-456-7890", "2023-10-15", "19:00", 4)
    reservation2 = Reservation("Jane Smith", "jane@example.com", "987-654-3210", "2023-10-16", "20:00", 2)
    
    # Print reservations
    print("Reservations:")
    print(reservation1)
    print(reservation2)
    print()

    # Create an order for the first reservation
    order1 = Order(table_number=5)
    order1.add_item(pizza, 2)
    order1.add_item(salad, 1)
    print("Order for John Doe:")
    print(order1)

    # Complete the order
    order1.complete_order()
    print(order1)
    print()

    # Create an order for the second reservation
    order2 = Order(table_number=3)
    order2.add_item(burger, 1)
    order2.add_item(pasta, 1)
    print("Order for Jane Smith:")
    print(order2)

    # Complete the order
    order2.complete_order()
    print(order2)
