#Creating calculate function
def calculate_discount(price, discount_percent):
  
  if discount_percent <=20:
     discount_amount= (price*discount_percent)/100
     final_price= price-discount_amount
     return final_price
  else:
      return price 

#Promting user to enter origianal price and discount percentage
try:
    original_price= float(input('Enter the original price before discount:'))
    discount_percentage= float(input('Enter the discount percentage:'))

#Calling for calculate discount function
    final_price = calculate_discount(original_price, discount_percentage)

#Printing final price
    print(f"The final price after applying the discount is: ${final_price:.2f}")

except ValueError:
    print("Please enter valid numerical values for the price and discount percentage.")
