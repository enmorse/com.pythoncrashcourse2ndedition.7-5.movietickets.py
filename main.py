# A movie theater charges different ticket prices
# depending on a person's age. If a person is under
# the age of 3, the ticket is free; if they are between
# 3 and 12, the ticket is $10; and if they are over 12,
# the ticket is $15. Write a loop in which you ask
# users their age, and tell them the cost of their
# movie ticket.
prompt = int(input("\nHow old are you?: "))

while True:
    if prompt <= 3:
        print("Your ticket is free.")
        break
    if prompt > 3 and prompt < 12:
        print("Your ticket will cost 10 dollars.")
        break
    if prompt > 12:
        print("Your ticket will cost 15 dollars.")
        break
