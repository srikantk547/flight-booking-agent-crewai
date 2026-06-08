from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from datetime import datetime
import os


def generate_ticket_pdf(booking):

    os.makedirs("tickets", exist_ok=True)

    filename = (
        f"tickets/{booking.transaction_id}_ticket.pdf"
    )

    c = canvas.Canvas(
        filename,
        pagesize=letter
    )

    width, height = letter

    y = height - 50

    c.setFont("Helvetica-Bold", 20)
    c.drawString(
        50,
        y,
        "AIRLINE E-TICKET"
    )

    y -= 40

    c.setFont("Helvetica", 12)

    fields = [
        f"PNR: {booking.pnr}",
        f"Transaction ID: {booking.transaction_id}",
        f"Source: {booking.source}",
        f"Destination: {booking.destination}",
        f"Journey Date: {booking.journey_date}",
        f"Flight Number: {booking.selected_flight}",
        f"Travel Class: {booking.travel_class}",
        f"Seat Number: {booking.selected_seat}",
        f"Meal Preference: {booking.selected_meal}",
        f"Flight Price: ${booking.flight_price}",
        f"Payment Status: {booking.payment_status}",
        f"Generated On: {datetime.now()}"
    ]

    for item in fields:
        c.drawString(50, y, item)
        y -= 25

    c.line(50, y, 550, y)

    y -= 40

    c.setFont("Helvetica-Bold", 14)
    c.drawString(
        50,
        y,
        "Thank you for choosing our service."
    )

    c.save()

    return filename