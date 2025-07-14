logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
other_bids = True
bidders = {"Name": [], "Bid": []}

while other_bids:
    name = input("What is your name? ")
    bid = int(input("What is your bid? $"))

    bidders["Name"].append(name)
    bidders["Bid"].append(bid)

    more_bids = input("Any other bidders? Type 'no' to exit. ")
    if more_bids == "no":
        other_bids = False
    else:
        other_bids = True
        print("\n" * 20)

top_bidder = max(bidders["Bid"])
winner = bidders["Bid"].index(top_bidder)
print("\n" * 20)
print(
    f"The winner is {bidders['Name'][winner]} with \
a bid of {bidders['Bid'][winner]}"
)
