
**DirectWindowInteraction** and **KeyboardControlTextExtraction**. These methods are employed to collect data from the application's user interface and store it in CSV format.



## DirectWindowInteraction

This method utilizes the `pywinauto` library to automate interactions with the window controls of the target application. By connecting to the window handle and accessing its descendant controls, this method extracts specific text data from the UI elements directly. It simulates user interactions to navigate through the app's interface and extract the required information.

![DirectWindowInteraction Sample](https://i.ibb.co/C8ftGq9/sample.gif)

## KeyboardControlTextExtraction

This method relies on simulating keyboard shortcuts and cursor movements to select and copy text data from the window app. By pressing specific keys such as Shift + Home or Shift + End, the method selects text within the window, copies it to the clipboard, and retrieves the copied text. This approach mimics manual text selection and copying actions performed by a user. It offers simplicity and ease of implementation.

![KeyboardControlTextExtraction Sample](https://i.ibb.co/KVJDXmy/sample-keyboard.gif)

## Performance Comparison

The performance of both methods was evaluated based on the time taken to complete a single iteration of data extraction. The results are as follows:

- **DirectWindowInteraction**: 0.5332 seconds per iteration
- **KeyboardControlTextExtraction**: 13.8062 seconds per iteration

## Conclusion

While **KeyboardControlTextExtraction** may be simpler to implement, its performance was significantly slower compared to **DirectWindowInteraction**. The latter method proved to be more efficient in extracting data from the Windows application.
