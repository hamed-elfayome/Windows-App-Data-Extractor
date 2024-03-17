import csv
import pyautogui
import pywinauto
import win32gui
import time

# Define the number of iterations
total_iterations = 1000

# Get the start time
start_time = time.time()

# Specify the handle of the window 
window_handle = 0x000B0F32 

# Activate the window using its handle
win32gui.SetForegroundWindow(window_handle)

# Open the file for writing in append mode
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write the header row if the file is empty
    csv_writer.writerow(['id', 'name_c', 'price', 'mid_unit', 'min_unit', 'name_sc', 'company', 'name_ar', 'farma', 'licence', 'pharma_form', 'bar1', 'bar2', 'bar3', 'bar4', 'bar5'])

    # Loop for 3 iterations
    for i in range(1000):
        # Click buttons and copy selected text
        pyautogui.click(-300, 160)
        time.sleep(0.4)

        # Connect to the window
        app = pywinauto.application.Application().connect(handle=window_handle)

        # Get all descendant controls of the window
        all_descendants = app.window(handle=window_handle).descendants()

        name_c = all_descendants[4].window_text()

        price = all_descendants[10].window_text()

        mid_unit = all_descendants[9].window_text()

        company = all_descendants[7].window_text()

        name_sc = all_descendants[6].window_text()

        farma = all_descendants[5].window_text()

        bar5 = all_descendants[35].window_text()

        bar4 = all_descendants[34].window_text()

        bar3 = all_descendants[33].window_text()

        bar2 = all_descendants[32].window_text()

        licence = all_descendants[20].window_text()

        pharma_form = all_descendants[18].window_text()

        bar1 = all_descendants[16].window_text()

        min_unit = all_descendants[12].window_text()

        name_ar = all_descendants[11].window_text()


        # Write the data to the CSV file
        csv_writer.writerow([i, name_c, price, mid_unit, min_unit, name_sc, company, name_ar, farma, licence, pharma_form, bar1, bar2, bar3, bar4, bar5])

        # Print a progress message
        print(f'Progress: {i+1}/1000', end='\r')

# Get the end time
end_time = time.time()

# Calculate the total time taken
total_time = end_time - start_time

# Calculate the average time per iteration
average_time_per_iteration = total_time / total_iterations

# Print the results
print(f"Total time taken: {round(total_time,4)} seconds")
print(f"Average time per iteration: {round(average_time_per_iteration,4)} seconds")
