class Event:
    def __init__(self, name, description, date, location):
        self.name = name
        self.description = description
        self.date = date
        self.location = location
        self.registrations = []

    def register(self, user_name, user_email):
        self.registrations.append({'name': user_name, 'email': user_email})
        print(f"{user_name} has been registered for {self.name}.")

    def show_registrations(self):
        print(f"Registrations for {self.name}:")
        for reg in self.registrations:
            print(f"Name: {reg['name']}, Email: {reg['email']}")


def main():
    events = []

    # Sample events
    events.append(Event("Python Workshop", "Learn Python programming.", "2023-10-15", "Online"))
    events.append(Event("Data Science Seminar", "Introduction to Data Science.", "2023-10-20", "Conference Hall A"))

    while True:
        print("\nAvailable Events:")
        for i, event in enumerate(events):
            print(f"{i + 1}. {event.name} - {event.description} on {event.date} at {event.location}")

        choice = input("Select an event to register (or type 'exit' to quit): ")

        if choice.lower() == 'exit':
            break

        try:
            event_index = int(choice) - 1
            if event_index < 0 or event_index >= len(events):
                print("Invalid choice. Please try again.")
                continue

            user_name = input("Enter your name: ")
            user_email = input("Enter your email: ")
            events[event_index].register(user_name, user_email)

        except ValueError:
            print("Invalid input. Please enter a number.")

    print("\nThank you for using the Event Registration System!")


if __name__ == "__main__":
    main()
