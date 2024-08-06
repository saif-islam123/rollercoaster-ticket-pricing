# Rollercoaster Ticket Pricing

Welcome to the Rollercoaster Ticket Pricing project! This Python script calculates the ticket price for a rollercoaster ride based on the rider's height and age. It also includes an option to add a photo for an additional charge.

## How It Works

1. Height Check:
   - The script first asks for the rider's height. To be eligible to ride, the rider must be at least 120 cm tall.

2. Age-Based Pricing:
   - If the rider's height meets the minimum requirement, the script then asks for the rider's age.
   - Ticket pricing is determined as follows:
     - Free Ticket: Riders aged between 45 and 55 years old receive a free ticket.
     - Adult Ticket: Riders aged 18 and over pay $18.
     - Youth Ticket: Riders aged between 12 and 17 pay $7.
     - Child Ticket: Riders under 12 pay $5.

3. Photo Option:
   - After determining the ticket price, the script asks if the rider wants a photo. If the rider wants a photo, an additional charge of $3 is added to the total bill.

4. Output:
   - The script displays the ticket price and the total bill (including photo charges if applicable).
   - If the rider does not meet the height requirement, the script informs them that they cannot ride.

## Usage

To run the script, make sure you have Python installed on your machine. Save the script as `rollercoaster_ticket_pricing.py` and execute it using the following command:

```bash
https://github.com/saif-islam123/rollercoaster-ticket-pricing
