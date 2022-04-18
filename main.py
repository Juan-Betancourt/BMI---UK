# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: \n"))
weight = float(input("enter your weight in kg: \n"))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi_cal = round(weight / (height ** 2))

if bmi_cal < 18.5:
  print(f"Your BMI is {bmi_cal}, you are " '\033[1m' + 'Underweight' + '\033[0m'".")
elif bmi_cal < 25:
  print(f"Your BMI is {bmi_cal}, you are " '\033[1m' + 'Normal Weight' + '\033[0m'".")
elif bmi_cal < 30:
  print(f"Your BMI is {bmi_cal}, you are " '\033[1m' + 'Overweight' + '\033[0m'".")
elif bmi_cal < 35:
  print(f"Your BMI is {bmi_cal}, you are " '\033[1m' + 'Obese' + '\033[0m'".")
else: 
  print(f"Your BMI is {bmi_cal}, you are " '\033[1m' + 'Clinically Obese' + '\033[0m'".")

  
  


