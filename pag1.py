
#codigo de cobro de salario bruto

hrs = float(input("Enter Hours:"))
rt = float(input("Enter rate:"))
if hrs <= 40:
    pay = hrs * rt
else:
    hrs_ext: hrs - 40
    pay = (hrs * rt) + (hrs_ext * rt * 1.5)
print (pay)  