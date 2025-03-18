import datetime

class PaymentRefundSystem:
    def __init__(self):
        self.transactions = []  # Stores payment and refund history

    def process_payment(self, order_id, amount, payment_method):
        """
        Processes a payment request.
        """
        if amount <= 0:
            return "Invalid payment amount."
        
        payment_data = {
            "order_id": order_id,
            "amount": amount,
            "payment_method": payment_method,
            "type": "Payment",
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.transactions.append(payment_data)
        return f"Payment of {amount} received for Order {order_id} via {payment_method}."

    def process_refund(self, order_id, amount, payment_method):
        """
        Processes a refund request.
        """
        if amount <= 0:
            return "Invalid refund amount."
        
        refund_data = {
            "order_id": order_id,
            "amount": -amount,  # Negative amount for refunds
            "payment_method": payment_method,
            "type": "Refund",
            "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        
        self.transactions.append(refund_data)
        return f"Refund of {amount} processed for Order {order_id} via {payment_method}."

    def show_transactions(self):
        """Displays all processed payments and refunds."""
        return self.transactions if self.transactions else "No transactions recorded yet."


# Example usage
if __name__ == "__main__":
    system = PaymentRefundSystem()
    print(system.process_payment("ORD12345", 100.0, "POS"))
    print(system.process_refund("ORD12345", 50.0, "POS"))
    print(system.show_transactions())
