import pyautogui
import win32gui
import time
import mss
import mss.tools
import keyboard
from PIL import Image

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

def crop_image(img, coordinates): 
    # Crop the image using the provided coordinates
    cropped_img = img.crop(coordinates)
    return cropped_img

def relative_coordinates(outer, inner):
    # Calculate the difference in coordinates
    dx = inner[0] - outer[0]
    dy = inner[1] - outer[1]
    # Adjust the inner window coordinates
    relative_inner = (dx, dy, dx + (inner[2] - inner[0]), dy + (inner[3] - inner[1]))
    return relative_inner

# Outer window coordinates
outer_window = (-1161, 57, -205, 671)

# Specify the handle of the window 
window_handle = 0x000B0F32 

# Activate the window using its handle
win32gui.SetForegroundWindow(window_handle)

# Define the coordinates of the region to capture
monitor = {"left": -1161, "top": 57, "width": 956, "height": 614}

# Variable to track if the loop should continue
running = True

# Function to stop the loop when a key is pressed
def stop_loop(event):
    global running
    running = False

# Register the keyboard event to stop the loop
keyboard.on_press_key("q", stop_loop)

i = 0
while running and i < total_iterations:
    # Click buttons and copy selected text
    pyautogui.click(-300, 160)
    time.sleep(0.4)
    # Initialize the mss instance
    with mss.mss() as sct:
        # Capture the screen within the specified region
        img = sct.grab(monitor)

    # Save the screenshot to a file
    mss.tools.to_png(img.rgb, img.size, output=f"screenshots/{i}.png")

    img = Image.frombytes("RGB", img.size, img.rgb)

    name= img.crop(relative_coordinates(outer_window, (-802, 139, -330, 166)))
    price = img.crop(relative_coordinates(outer_window, (-577,167,-508,194)))
    strip = img.crop(relative_coordinates(outer_window, (-607,195,-473,222)))
    blt = img.crop(relative_coordinates(outer_window, (-802,195,-698,222)))
    name_s = img.crop(relative_coordinates(outer_window, (-802,237,-330,264)))
    comp = img.crop(relative_coordinates(outer_window, (-802,265,-330,292)))
    name_ar = img.crop(relative_coordinates(outer_window, (-802,293,-330,320)))
    pharma = img.crop(relative_coordinates(outer_window, (-802,321,-330,348)))
    bar1 = img.crop(relative_coordinates(outer_window, (-399,375,-213,402)))
    bar2 = img.crop(relative_coordinates(outer_window, (-587,375,-399,402)))
    bar3 = img.crop(relative_coordinates(outer_window, (-775,375,-587,402)))
    certificate = img.crop(relative_coordinates(outer_window, (-686,460,--549,487)))
    shape = img.crop(relative_coordinates(outer_window, (-912,460,-774,487)))

    # Save the cropped image to a new file
    name.save(f"crops/name/{i}.jpg")
    price.save(f"crops/price/{i}.jpg")
    strip.save(f"crops/strip/{i}.jpg")
    blt.save(f"crops/blt/{i}.jpg")
    name_s.save(f"crops/name_s/{i}.jpg")
    comp.save(f"crops/comp/{i}.jpg")
    name_ar.save(f"crops/name_ar/{i}.jpg")
    pharma.save(f"crops/pharma/{i}.jpg")
    bar1.save(f"crops/bar1/{i}.jpg")
    bar2.save(f"crops/bar2/{i}.jpg")
    bar3.save(f"crops/bar3/{i}.jpg")
    certificate.save(f"crops/certificate/{i}.jpg")
    shape.save(f"crops/shape/{i}.jpg")

    i += 1
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

# Unregister the keyboard event when the loop exits
keyboard.unhook_all()
