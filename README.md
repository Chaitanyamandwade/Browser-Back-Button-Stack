
# Browser Back Button Using Stack

## Aim
To implement a basic web browser back button using the Stack data structure in Python.

## Description
This mini project demonstrates how a browser's Back button works using a stack.

Whenever a user visits a new page, the previous page is stored in the stack. When the Back button is pressed, the most recently visited page is retrieved using the pop operation.

## Data Structure Used
Stack (LIFO - Last In, First Out)

## Operations
- Visit a new web page
- Store the previous page in the stack
- Navigate back to the previous page
- Display the current page

## Technologies Used
- Python 3

## How to Run
1. Install Python 3.
2. Run the following command:

   python main.py

## Sample Output
Visited: www.google.com
Visited: www.youtube.com
Visited: www.github.com
Back to: www.youtube.com
Back to: www.google.com
Current Page: www.google.com

## Time Complexity
- Visit Page: O(1)
- Back Button: O(1)
- Display Current Page: O(1)

## Conclusion
This project demonstrates the use of a Stack to implement basic browser back button functionality.
