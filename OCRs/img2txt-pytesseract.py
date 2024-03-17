import pytesseract
from PIL import Image
import csv
import time

# Define the number of iterations
total_iterations = 1000

# Get the start time
start_time = time.time()

def print_loading_bar(progress, total, now, sum, bar_length=50):
    filled_length = int(bar_length * progress / total)
    bar = "#" * filled_length + "-" * (bar_length - filled_length)
    percentage = progress / total * 100

    progress_text = f"Progress: [{bar}] {percentage:.2f}% [{now}/{sum}]"
    return progress_text


# Define the whitelist of characters you want to allow in the OCR result
whitelist = "0123456789."  


# Open a CSV file for writing
with open("output-pytesseract.csv", "w", newline="", encoding="utf-8") as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write the header row
    csv_writer.writerow(["ID", "Price"])

# Loop through items
for i in range(1, total_iterations):
    price = Image.open(f"crops/price/{i}.jpg")

    # Perform OCR on preprocessed images
    price_text = pytesseract.image_to_string(price, config=f"--oem 3 --psm 6 -c tessedit_char_whitelist={whitelist}")

    # Remove unwanted characters and whitespace
    price_text = "".join(filter(lambda char: char.isdigit() or char == ".", price_text.strip()))

    # Add all the extracted text to the row_data list (one item per cell)
    row_data = [i, price_text]

    # Append the row data to the CSV file
    with open("output-pytesseract.csv", "a", newline="", encoding="utf-8") as csv_file:
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(row_data)

    print(print_loading_bar(i, total_iterations, i, total_iterations), end="\r")

# Get the end time
end_time = time.time()

# Calculate the total time taken
total_time = end_time - start_time

# Calculate the average time per iteration
average_time_per_iteration = total_time / total_iterations

# Print the results
print(f"Total time taken: {round(total_time,4)} seconds")
print(f"Average time per iteration: {round(average_time_per_iteration,4)} seconds")


