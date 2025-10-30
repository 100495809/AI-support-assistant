def classify_message(message: str) -> str:
    """Classifies message in one of the categories: Shipment Status, Delivery Issue, or Payment / Invoice."""

    if not isinstance(message, str):
        return "Unknown"

    message = message.lower()

    if any(
        word in message
        for word in ["shipment", "tracking", "transit", "status", "order"]
    ):
        return "Shipment Status"
    elif any(
        word in message for word in ["delay", "damaged", "late", "address", "delivery"]
    ):
        return "Delivery Issue"
    elif any(word in message for word in ["payment", "invoice", "paid", "charge"]):
        return "Payment / Invoice"
    else:
        return "Other"
