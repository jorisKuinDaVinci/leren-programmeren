from help import input_yes_no, input_int, get_vat_from_amount_incl, get_vat_perc

RECEIPT_TEXT = '***** SPEELHAL ENTREE VOOR {personen:2} PERSONEN *****'
RESTART_TEXT = '\nBestelprocedure gestopt door invoerfout!\nHerstart de bestelprocedure!'
MAX_TICKETS = 30
MAX_VR_VIP_SEAT_TIME = 45
VR_VIP_SEAT_PRICE_PERIOD = 5

TICKET_PRICE = 7.50
VR_VIP_SEAT_PERIOD_PRICE = 0.37
COLA_PRICE = 2.10
POPCORN_PRICE = 2.89
VAT_CODE_H = 'H'
VAT_CODE_L = 'L'

print("SPEELHAL-ENTREE-KASSA")

# Bestellen starten
if input_yes_no("Wilt u bestellen?") not in ('j', 'J'):
    print("Nu geen interesse? Tot ziens!")
    exit()

# Vraag tickets
nr_tickets = input_int("Hoeveel personen?", 1, MAX_TICKETS)

# Vraag VR-VIP seats
vr_vip_ordered = input_yes_no("Ook VR-VIP seats?") in ('j', 'J')
if vr_vip_ordered:
    nr_vr_vip_seats = input_int("Hoeveel VR-VIP seats?", 0, nr_tickets)
    vr_vip_seat_time = input_int("Hoeveel minuten in de VR-VIP-seats?", 5, MAX_VR_VIP_SEAT_TIME)
else:
    nr_vr_vip_seats = vr_vip_seat_time = 0

# Vraag drankjes en snacks
nr_cola = input_int("Hoeveel cola?", 0, nr_tickets)
nr_popcorn = input_int("Hoeveel popcorn?", 0, nr_tickets)

# Vraag factuur
vat_invoice = input_yes_no("Wilt u een factuur met BTW-specificatie?") in ('j', 'J')
company_name = None
if vat_invoice:
    company_name = input("Op welke naam komt de factuur? ")
    if len(company_name) == 0:
        company_name = "........... (zelf invullen)"

# Berekeningen
total_tickets = round(nr_tickets * TICKET_PRICE, 2)
vr_vip_seat_price = vr_vip_seat_time / VR_VIP_SEAT_PRICE_PERIOD * VR_VIP_SEAT_PERIOD_PRICE
total_vr_vip_seats = round(nr_vr_vip_seats * vr_vip_seat_price, 2)
total_cola = round(nr_cola * COLA_PRICE, 2)
total_popcorn = round(nr_popcorn * POPCORN_PRICE, 2)
total_all = total_tickets + total_vr_vip_seats + total_cola + total_popcorn

# BTW-berekeningen
total_vat_H = total_vat_L = 0
if vat_invoice:
    total_vat_H = (
        get_vat_from_amount_incl(total_tickets, VAT_CODE_H) +
        get_vat_from_amount_incl(total_vr_vip_seats, VAT_CODE_H)
    )
    total_vat_L = (
        get_vat_from_amount_incl(total_cola, VAT_CODE_L) +
        get_vat_from_amount_incl(total_popcorn, VAT_CODE_L)
    )

# Bon tonen
print("\n" + RECEIPT_TEXT.format(personen=nr_tickets))
if vat_invoice:
    print(f"Factuur voor: {company_name}")
else:
    print("Kassabon")

print("-" * len(RECEIPT_TEXT))
print(f"Tickets                  {nr_tickets:2} x €{TICKET_PRICE:5.2f} = €{total_tickets:6.2f}")
if vr_vip_ordered:
    print(f"VR-vip-seats  {vr_vip_seat_time:3} minuten {nr_vr_vip_seats:2} x €{vr_vip_seat_price:5.2f} = €{total_vr_vip_seats:6.2f}")
print(f"Cola                     {nr_cola:2} x €{COLA_PRICE:5.2f} = €{total_cola:6.2f}")
print(f"Popcorn                  {nr_popcorn:2} x €{POPCORN_PRICE:5.2f} = €{total_popcorn:6.2f}")
print("." * len(RECEIPT_TEXT))
print(f"Totaal:                      €{total_all:6.2f}")

if vat_invoice:
    print(f"BTW Hoog                 {get_vat_perc(VAT_CODE_H)}% = €{total_vat_H:6.2f}")
    print(f"BTW Laag                 {get_vat_perc(VAT_CODE_L)}% = €{total_vat_L:6.2f}")
print("=" * len(RECEIPT_TEXT))
print("Bedankt voor de bestelling, veel plezier!")