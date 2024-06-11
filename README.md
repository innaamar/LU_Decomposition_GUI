#Project Topic: LU Decomposition Solver Application

This project creates a GUI application to solve systems of linear equations using LU decomposition, built with the customtkinter library.


Key Features:
1.	Matrix and Vector Input:
	Users can input matrix A and vector b directly or load them from a text file.

3.	Method Selection:
	Users can select between Doolittle and Crout LU decomposition methods via radio buttons.

5.	Solve Button:
	Parses inputs, performs LU decomposition, solves the system, and displays the solution.

6.	Intermediate Steps Display:
	Shows the steps of the LU decomposition process in a text box.

7.	Error Handling:
	Displays error messages for invalid inputs and computational issues.
Detailed Code Explanation:

	Class Initialization:
 Sets up the GUI with labels, entry fields, radio buttons, and buttons.

	File Handling:
	The open_file method loads matrix AAA and vector bbb from a text file.

	Input Parsing:
	Methods parse_matrix and parse_vector convert string inputs into numpy arrays.

	Solving the System:
	The solve method coordinates parsing inputs, performing LU decomposition, and solving the equations.
	Implements Doolittle and Crout LU decomposition algorithms, recording steps.

	Displaying Results:
Results and steps are shown in a text box.

Running the Application:
	Initializes the main window, sets appearance, and starts the event loop.
This application provides an accessible tool for solving linear equations using LU decomposition, suitable for educational and practical purposes.

Error Handling:

The application includes error handling for invalid inputs, singular matrices, and other potential issues during computation, displaying appropriate error messages to the user.


---This project was make by Nanu Iustina-Stefania, Bohotineanu Amalia and Ciobanu Andrei. We each contributed a large amount in this project. Amalia  and I did the GUI inteface using Tkinter, she came with this toolkit of widgets to use that was different from what we used during the laboratories, and i implemented them and upgraded it with custom tkinter for a better looking GUI. Andrei did the math part, the problem solving and the implementation of it in our project.---
