#total working hrs =(x+y+z)/((x*y)+(x*z)+(y*z))
def calculate(x,y,z):
    # Validate inputs: x, y, and z must be positive numbers.
    if not (isinstance(x, (int, float)) and x > 0 and
            isinstance(y, (int, float)) and y > 0 and
            isinstance(z, (int, float)) and z > 0):
        return "Error: Please provide positive numbers for days."
    numerator =x+y+z
    denominator = x*y+x*z+y*z
    if denominator == 0:
        result ="Error: Denominator evaluates to zero, which means work cannot be completed"
        return result
    result =numerator/denominator
    return result

if __name__ == "__main__":
    print("Welcome to work hours calculator")
    print("\n-------------------------------------")
    try:
        x_days =float(input("\nenter x_days  for x worker"))
        y_days =float(input("\nenter y_days  for y worker"))
        z_days =float(input("\nenter z_days  for z worker"))
        result = calculate(x_days,y_days,z_days)
        if isinstance(result, str) and "Error" in result:
            print(result)
        else:
            print(f"\nIf A, B, and C work together, the job will be completed in: {result:.2f} days")
    except ValueError:
        print("Invalid input: Please enter numeric values for days.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
