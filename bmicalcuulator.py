def calculate_bmi(weight, height):
    height_m = height / 100  # Convert cm to meters
    bmi = weight / (height_m ** 2)
    return bmi

def classify_bmi(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 24.9:
        return "Normal weight"
    elif 25 <= bmi < 29.9:
        return "Overweight"
    else:
        return "Obese"

def main():
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in cm: "))
        
        if weight <= 0 or height <= 0:
            print("Weight and height must be positive values.")
            return
        
        bmi = calculate_bmi(weight, height)
        category = classify_bmi(bmi)
        
        print(f"Your BMI is: {bmi:.2f}")
        print(f"Category: {category}")
    except ValueError:
        print("Please enter valid numerical values for weight and height.")

if __name__ == "__main__":
    main()
