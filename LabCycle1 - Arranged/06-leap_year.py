current_year=2022
target_year=int(input("Enter A Year (After 2022) : "))

while current_year < target_year:
    if current_year % 4==0 and current_year % 100!=0:
        print(current_year)
    if current_year % 100==0 and current_year %400==0:
        print(current_year)
    current_year += 1
			
