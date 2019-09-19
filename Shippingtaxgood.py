tax_1 = 1.05
tax_2 = 1.13
tax_3 = 1.11
totalCharge = float( input("Please enter your total price: "))
country = input ("Are you buying from Canada or Other?: ")
if country == "Canada" :
    province = input("Please enter your province: ")

if country == "Other" :
    totalPrice = totalCharge *1
    print ("You don't have any tax")
    print ("Total cost is %.2f dollars" % totalPrice)

if province == "Alberta" :
    totalPrice = totalCharge *tax_1
    print ("Total cost is %.2f dollars" % totalPrice)

if province == "Onraio" or province == "New Brunswick" \
   or province == "Nova Scotia" :
    totalPrice = totalCharge *tax_2
    print ("Total cost is %.2f dollars" % totalPrice)

if province == "British Columbia" or province == "Saskatchewan" \
   or province == "Manitoba" or province == "Quebec" \
   or province == "Prince Edward Island" \
   or province == "Yukon" or province == "Nunavut" \
   or province == "Northwest Territories" :
    totalPrice = totalCharge *tax_3
    print ("Total cost is %.2f dollars" % totalPrice)
