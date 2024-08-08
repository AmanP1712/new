# Function to calculate the area of a rectangle
def calculate_area(width, height):
    return width * height

# Main program
def main():
    # Prompt user for the width of the rectangle
    width = float(input("Enter the width of the rectangle: "))
    
    # Prompt user for the height of the rectangle
    height = float(input("Enter the height of the rectangle: "))
    
    # Calculate the area
    area = calculate_area(width, height)
    
    # Display the result
    print(f"The area of the rectangle is: {area}")

# Run the main program
if __name__ == "__main__":
    main()
