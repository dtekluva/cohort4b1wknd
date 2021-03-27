principal = float(input("PLease enter principal collected : "))
rate      = float(input("PLease enter rate : "))
time      = float(input("PLease enter duration : "))

interest = (principal * rate *  time) / 100

print(interest)

total_repayment = principal + interest

# print(f"Principal obtained : {principal}")
# # print(f"Repayment amount : {total_repayment}")
# # print(f"Interest accrued : {interest}")

print("Principal obtaned :", principal)
print("Repayment amount  :", total_repayment)
print("Interest accrued  :", interest)
input()