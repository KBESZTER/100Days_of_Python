bid = {}
bidding_finished = False

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner=""
  for bidder in bidding_record:
    bid_amount=bidding_record[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winnwer is {winner} with a bid of {highest_bid}")
  

while not bidding_finished:
 name = input("What is your name")
 price = int(input("Type your bid"))
 bid[name] = price
 should_countinue=input("Are there any bidders? Type 'yes' or 'no'")
 if should_countinue == "no" :
   
   bidding_finished = True
   find_highest_bidder(bid)

 elif should_countinue == "yes":
   clear()
