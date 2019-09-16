Item_1 = float(input("How much does item one cost?: "))
Item_2 = float(input("How much does item two cost?: "))
Item_3 = float(input("How much does item three cost?: "))
No_Tax = Item_1 + Item_2 + Item_3
print("Price Before Tax %.2f" %No_Tax)
Cost = No_Tax * 1.12
print ("The total price will be {0:.2f} dollars". format(Cost))
