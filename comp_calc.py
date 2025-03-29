def main():
    print("Compound Interest Calc")
    year = int(input("Year -> "))
    rate = float(input("Rate -> "))
    principle_amt = float(input("Principle -> "))  # Use float for decimal amounts

    rate_decimal = rate / 100  # Convert percentage rate to decimal

    for i in range(1, year + 1):  # Loop through each year (inclusive)
        temp_rate = 1 + rate_decimal
        temp_base = pow(temp_rate, i)  # Use the current year in the power
        total_amt = principle_amt * temp_base
        interest_amt = total_amt - principle_amt
        print(f"Year: {i}")
        print(f"Interest Amt at end of year -> {interest_amt:.2f}")
        print(f"Total Amt at end of year -> {total_amt:.2f}")
        print("-" * 30)

if __name__ == "__main__":
    main()
