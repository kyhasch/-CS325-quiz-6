# s.py

class Order:
    def __init__(self, customer, items, shipping_address):
        self.customer = customer
        self.items = items
        self.shipping_address = shipping_address

class OrderCostCalculator:
    @staticmethod
    def calculate_total_order_cost(order):
        total_cost = 0
        
        for item in order.items:
            total_cost += item.price * item.quantity
        
        total_cost += total_cost * 0.1  # Assuming 10% tax
        
        if order.customer.is_premium:
            total_cost *= 0.9  # 10% discount for premium customers
        
        return total_cost

class OrderValidator:
    @staticmethod
    def validate_order(order):
        for item in order.items:
            if not item.is_available_in_inventory():
                return False
        
        if not order.shipping_address.is_valid():
            return False
        
        return True

class EmailSender:
    @staticmethod
    def send_order_confirmation_email(order):
        # Send order confirmation email to customer
        print(f"Order confirmation email sent to {order.customer.email}")

class InventoryManager:
    @staticmethod
    def update_inventory(order):
        for item in order.items:
            item.update_inventory()
        print("Inventory updated successfully.")

class Customer:
    def __init__(self, email, is_premium=False):
        self.email = email
        self.is_premium = is_premium

class Item:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity
    
    def is_available_in_inventory(self):
        # Placeholder logic to check item availability in inventory
        return True  # Placeholder implementation
    
    def update_inventory(self):
        # Placeholder logic to update inventory after item is purchased
        print(f"Updating inventory for {self.name} - Quantity: {self.quantity}")

class Address:
    def __init__(self, street, city, state, zip_code):
        self.street = street
        self.city = city
        self.state = state
        self.zip_code = zip_code
    
    def is_valid(self):
        # Placeholder logic to check if address is valid
        return True  # Placeholder implementation

if __name__ == "__main__":
    customer = Customer("kyhasch@example.com", is_premium=True)
    items = [Item("Bannana", 20.0, 2), Item("Apple", 30.0, 1)]
    shipping_address = Address("123 Street", "Springfield", "Illinois", "12345")
    
    order = Order(customer, items, shipping_address)
    
    if OrderValidator.validate_order(order):
        total_cost = OrderCostCalculator.calculate_total_order_cost(order)
        print(f"Total cost of the order: ${total_cost}")
        EmailSender.send_order_confirmation_email(order)
        InventoryManager.update_inventory(order)
    else:
        print("Order validation failed. Please check your order details.")
