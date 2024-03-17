import csv
import pygetwindow as gw
import pyautogui
import pyperclip
import time

# Define the number of iterations
total_iterations = 10

# Get the start time
start_time = time.time()

def copy_selected_text_home():
    # Press Shift + Home to select text from current cursor position to the beginning
    pyautogui.keyDown('shiftleft')
    pyautogui.keyDown('shiftright')
    pyautogui.hotkey('home')
    pyautogui.keyUp('shiftleft')
    pyautogui.keyUp('shiftright')

    # Copy the selected text
    pyautogui.hotkey('ctrl', 'c')
    
    # Return the copied text
    copied_text = pyperclip.paste()

    # Clear the clipboard
    pyperclip.copy('')

    return copied_text



def copy_selected_text_end():
    # Press Shift + End to select text from current cursor position to the end
    pyautogui.keyDown('shiftleft')
    pyautogui.keyDown('shiftright')
    pyautogui.hotkey('end')
    pyautogui.keyUp('shiftleft')
    pyautogui.keyUp('shiftright')

    # Copy the selected text
    pyautogui.hotkey('ctrl', 'c')
    
    # Return the copied text
    copied_text = pyperclip.paste()

    # Clear the clipboard
    pyperclip.copy('')

    return copied_text



def click_tab(num_clicks):
    for _ in range(num_clicks):
        pyautogui.press('tab')



# Activate the target application window
app_window = gw.getWindowsWithTitle("بيانات الادوية")[0]
app_window.activate()



# Open the file for writing in append mode
with open('output.csv', 'w', newline='', encoding='utf-8') as csvfile:
    csv_writer = csv.writer(csvfile)

    # Write the header row if the file is empty
    csv_writer.writerow(['name_c', 'price', 'mid_unit', 'min_unit', 'name_sc', 'company', 'name_ar', 'farma', 'licence', 'pharma_form', 'bar1', 'bar2', 'bar3', 'bar4', 'bar5'])

    # Loop for 3 iterations
    for i in range(10):
        # Click buttons and copy selected text
        pyautogui.click(-300, 160)
        time.sleep(0.1)
        pyautogui.click(-430, 190)
        name_c = copy_selected_text_home()

        pyautogui.click(-620, 220)
        price = copy_selected_text_home()

        pyautogui.click(-900, 260)
        mid_unit = copy_selected_text_home()

        pyautogui.click(-620, 260)
        min_unit = copy_selected_text_home()

        pyautogui.click(-430, 310)
        name_sc = copy_selected_text_home()

        pyautogui.click(-430, 350)
        company = copy_selected_text_home()

        pyautogui.click(-430, 390)
        name_ar = copy_selected_text_home()

        pyautogui.click(-430, 415)
        farma = copy_selected_text_home()

        pyautogui.click(-710, 555)
        click_tab(3)
        licence = copy_selected_text_end()

        pyautogui.click(-975, 590)
        pharma_form = copy_selected_text_home()

        pyautogui.click(-275, 480)
        bar1 = copy_selected_text_home()

        pyautogui.click(-510, 480)
        bar2 = copy_selected_text_home()

        pyautogui.click(-750, 480)
        bar3 = copy_selected_text_home()

        pyautogui.click(-980, 480)
        bar4 = copy_selected_text_home()

        pyautogui.click(-1220, 480)
        bar5 = copy_selected_text_home()

        # Write the data to the CSV file
        csv_writer.writerow([name_c, price, mid_unit, min_unit, name_sc, company, name_ar, farma, licence, pharma_form, bar1, bar2, bar3, bar4, bar5])

        # Print a progress message
        print(f'Progress: {i+1}/10')

print("Data saved to output.csv")
# Get the end time
end_time = time.time()

# Calculate the total time taken
total_time = end_time - start_time

# Calculate the average time per iteration
average_time_per_iteration = total_time / total_iterations

# Print the results
print(f"Total time taken: {round(total_time,4)} seconds")
print(f"Average time per iteration: {round(average_time_per_iteration,4)} seconds")
