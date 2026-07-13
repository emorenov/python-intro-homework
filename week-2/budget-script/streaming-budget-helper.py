# ============================================================
# LIVE CODING PROMPT
# ============================================================
# Your friend has 3 streaming subscriptions and wants to know
# what they really cost over time. They'd like a report showing:
#   - the monthly cost of each service
#   - their total monthly cost
#   - their total cost over any number of months they choose
#   - whether that total goes over a $300 budget
#
# How would we write a script that collects this from the user
# and prints a clear report? Let's build it together.
# ============================================================

# Collect information for user
# Variables - store information

budget = 600.0

name = input("What's your name: ")
print(f"Hello! {name}")

streaming_service_name_1 = input("What is streaming service 1? ")
print(f"DEBUG - name: {streaming_service_name_1}, Type: {type(streaming_service_name_1)}")

streaming_service_price_1 = float(input(f"What is the price for {streaming_service_name_1}? "))
print(f"DEBUG - value: {streaming_service_price_1}, Type:{type(streaming_service_price_1)}")


streaming_service_name_2 = input("What is streaming service 2? ")
print(f"DEBUG - name: {streaming_service_name_2}, Type: {type(streaming_service_name_2)}")

streaming_service_price_2 = float(input(f"What is the price for {streaming_service_name_2}? "))
print(f"DEBUG - value: {streaming_service_price_2}, Type:{type(streaming_service_price_2)}")


streaming_service_name_3 = input("What is streaming service 3? ")
print(f"DEBUG - name: {streaming_service_name_3}, Type: {type(streaming_service_name_3)}")

streaming_service_price_3 = float(input(f"What is the price for {streaming_service_name_3}? "))
print(f"DEBUG - value: {streaming_service_price_3}, Type:{type(streaming_service_price_3)}")

months = input("How many months do you want to calculate? ")
print(f"DEBUG - value: {months}, Type:{type(months)}")

# Math
monthly_total = streaming_service_price_1 + streaming_service_price_2 + streaming_service_price_3
print(f"DEBUG - value: {monthly_total}, Type:{type(monthly_total)}")

grand_total = monthly_total * float(months)
print(f"DEBUG - value: {grand_total}, Type:{type(grand_total)}")

is_over_budget = grand_total > budget
print(f"DEBUG - value: {is_over_budget}, Type:{type(is_over_budget)}")


# Print a report
print()
print("=" * 40)
print(f"  {name}'s STREAMING BUDGET REPORT")
print("=" * 40)
print(f"{streaming_service_name_1}: ${streaming_service_price_1:.2f} / mo")
print(f"{streaming_service_name_2}: ${streaming_service_price_2:.2f} / mo")
print(f"{streaming_service_name_3}: ${streaming_service_price_3:.2f} / mo")
print("-" * 40)
print(f"Monthly Total: ${monthly_total:.2f} / mo")
print(f"Total over {months} months: ${grand_total:.2f}")
print(f"Over ${budget} budget? {is_over_budget}")
print("=" * 40)