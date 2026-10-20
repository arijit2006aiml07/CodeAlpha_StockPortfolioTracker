total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")

while True:
    stock_name = input("Enter stock name: ").upper()
    stock_price = float(input("Enter price per share: ₹"))
    quantity = int(input("Enter quantity of shares: "))

    if stock_price <= 0 or quantity <= 0:
        print("Price and quantity must be greater than zero.")
        continue

    investment = stock_price * quantity
    total_investment += investment

    print("Stock Name:", stock_name)
    print("Investment in", stock_name, "= ₹", investment)

    choice = input("Add another stock? (yes/no): ").lower()

    if choice != "yes":
        break

print("\n===== PORTFOLIO SUMMARY =====")
print("Total investment = ₹", total_investment)

with open("portfolio_result.txt", "w", encoding="utf-8") as file:
    file.write("STOCK PORTFOLIO TRACKER\n")
    file.write("Total investment = ₹" + str(total_investment))

print("Result saved successfully!")
