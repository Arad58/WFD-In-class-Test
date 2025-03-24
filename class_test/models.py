class Car:

    def __init__(self, car_id, serial_number, make, model, color, year, for_sale):
        self.car_id = car_id
        self.serial_number = serial_number
        self.make = make
        self.model = model
        self.color = color
        self.year = year
        self.for_sale = for_sale

    def __str__(self):
        return f"Car({self.car_id}, {self.make}, {self.model}, {self.color}, {self.year}, For Sale: {self.for_sale})"


class Customer:
    def __init__(self, customer_id, last_name, first_name, phone, address, city, state, country, postal_code):
        self.customer_id = customer_id
        self.last_name = last_name
        self.first_name = first_name
        self.phone = phone
        self.address = address
        self.city = city
        self.state = state
        self.country = country
        self.postal_code = postal_code

    def __str__(self):
        return f"Customer({self.customer_id}, {self.first_name} {self.last_name}, {self.city}, {self.country})"


class Parts:
    def __init__(self, part_id, part_number, description, purchase_price, retail_price):
        self.part_id = part_id
        self.part_number = part_number
        self.description = description
        self.purchase_price = purchase_price
        self.retail_price = retail_price

    def __str__(self):
        return f"Part({self.part_id}, {self.description}, Retail Price: €{self.retail_price})"


class PartsUsed:
    def __init__(self, parts_used_id, part_id, service_ticket_id, number_used, price):
        self.parts_used_id = parts_used_id
        self.part_id = part_id
        self.service_ticket_id = service_ticket_id
        self.number_used = number_used
        self.price = price

    def __str__(self):
        return f"PartsUsed({self.parts_used_id}, Part ID: {self.part_id}, Service Ticket ID: {self.service_ticket_id}, Number Used: {self.number_used})"


class Mechanic:
    def __init__(self, mechanic_id, last_name, first_name):
        self.mechanic_id = mechanic_id
        self.last_name = last_name
        self.first_name = first_name

    def __str__(self):
        return f"Mechanic({self.mechanic_id}, {self.first_name} {self.last_name})"


class Salesperson:
    def __init__(self, salesperson_id, last_name, first_name):
        self.salesperson_id = salesperson_id
        self.last_name = last_name
        self.first_name = first_name

    def __str__(self):
        return f"Salesperson({self.salesperson_id}, {self.first_name} {self.last_name})"


class ServiceMechanic:
    def __init__(self, service_mechanic_id, service_ticket_id, service_id, mechanic_id, hours, comment, rate):
        self.service_mechanic_id = service_mechanic_id
        self.service_ticket_id = service_ticket_id
        self.service_id = service_id
        self.mechanic_id = mechanic_id
        self.hours = hours
        self.comment = comment
        self.rate = rate

    def __str__(self):
        return (
            f"ServiceMechanic({self.service_mechanic_id}, "
            f"Service Ticket ID: {self.service_ticket_id}, Service ID: {self.service_id}, "
            f"Mechanic ID: {self.mechanic_id}, Hours: {self.hours}, Rate: €{self.rate}/hr)"
        )


class Service:
    def __init__(self, service_id, service_name, hourly_rate):
        self.service_id = service_id
        self.service_name = service_name
        self.hourly_rate = hourly_rate

    def __str__(self):
        return f"Service({self.service_id}, {self.service_name}, Hourly Rate: €{self.hourly_rate})"


class SalesInvoice:
    def __init__(self, invoice_id, invoice_number, date, car_id, customer_id, salesperson_id):
        self.invoice_id = invoice_id
        self.invoice_number = invoice_number
        self.date = date
        self.car_id = car_id
        self.customer_id = customer_id
        self.salesperson_id = salesperson_id

    def __str__(self):
        return f"SalesInvoice({self.invoice_id}, Invoice Number: {self.invoice_number}, Date: {self.date})"

class ServiceTicket:
    def __init__(self, service_ticket_id, service_ticket_number, car_id, customer_id, date_received, comments, date_returned=None):
        self.service_ticket_id = service_ticket_id
        self.service_ticket_number = service_ticket_number
        self.car_id = car_id
        self.customer_id = customer_id
        self.date_received = date_received
        self.comments = comments
        self.date_returned = date_returned

    def __str__(self):
        return f"ServiceTicket({self.service_ticket_id}, Ticket Number: {self.service_ticket_number}, Date Received: {self.date_received})"