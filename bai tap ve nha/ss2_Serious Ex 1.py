cm = int(input("Hay cho toi biet chieu cao cua ban(cm)?"))
kg = int(input("Hay cho toi biet can nang cua ban(kg)?"))
m = cm/100
bmi = kg/(m**2)
if bmi < 16:
    print("Chi so BMI cua ban la: ",bmi,", rat tiec ban bi suy dinh duong.")
elif bmi > 16 and bmi < 18.5:
    print("Chi so BMI cua ban la: ",bmi," ban hoi gay do.")
elif bmi > 18.5 and bmi < 25:
    print("Chi so BMI cua ban la: ",bmi," ban rat can doi.")
elif bmi > 25 and bmi <30:
    print("Chi so BMI cua ban la: ",bmi," ban hoi beo roi")
else:
    print("Chi so BMI cua ban la: ",bmi," ban bi beo phi day")
