VIT'ian CGPA Calculator 

Overview of the project :
The "VIT'ian CGPA Calculator" is a simple and effective tool for VIT students to calculate their Grade Point Average (GPA) and Cumulative Grade Point Average (CGPA) throughout their academic journey. Students at VIT often struggle with understanding and calculating their grades due to the unique 'Relative Grading System' implemented for theory courses. This calculator simplifies the process by automating GPA and CGPA calculations based on the VIT grading methodology. The system takes user inputs for course marks, attendance percentage, and class statistics, then returns accurate GPA for each semester and cumulative CGPA. Users can continue calculating GPAs for consecutive semesters or exit at any point with their current CGPA. This project applies fundamental programming concepts to solve a realworld problem faced by VIT students.

Features :
USER INPUTS : The system allows the user to input their marks, attendance percentage, class averageand standard deviation for multiple semesters and different types of courses.
THEORY COURSE GRADING : For theory courses, the system implements VIT's relative grading logic where grades are determined based on the student's marks relative to the class average and standard deviation, ensuring fair assessment. 
LABORATORY/PROJECT COURSE GRADING : For laboratory and project-based courses, the system uses an absolute grading scale with predefined grade boundaries based on total marks.
ATTENDANCE VALIDATION : The system calculates attendance marks based on the student's attendance percentage with specific grade cutoffs (96%, 91%, 86%, 81%, 75%) and sets the grade to 'F' if attendance falls below 75%.
VALIDATION : The system validates all user inputs to ensure they are within acceptable ranges before performing calculations, providing error messages for invalid entries.
OUTPUT : The system displays the course credits, grades, grade points, GPA for the current semester, and the cumulative CGPA with proper formatting.
MULTIPLE SEMESTER SUPPORT : The system supports up to 8 semesters of data entry, allowingstudents to calculate their entire academic record or stop at any point based on their preference.
DUAL COURSE TYPE SUPPORT : The system differentiates between theory courses (LTP/LT) and laboratory/project-based courses (PJ) and applies the appropriate grading methodology for each.

Tools used :

Language : Python 
Development environment : Jupyter Notebook / Python IDE 
Output User Interface : Console-based (Jupyter Notebook, Spyder, VS Code, etc.) 
Concepts used : Functions, Conditional statements (if, elif, else, nested if), Iterative statements (for loops), Data types (lists, floats, integers), Input validation, Mathematical calculations, Relative grading algorithms.

Steps to run the program : 

1. Download the source code file named "gov.py" from the repository.
2. The source code can be executed on any platform that supports Python execution (Windows, Mac,Linux).
3. Open the file in any Python code executing platform such as Jupyter Notebook, Spyder, VS Code, or any Python IDE.
4. Run the program and follow the on-screen prompts and guidelines to enter your course and semester details.
5.The system will guide you through each semester's data entry and will ask if you want to continue calculating the next semester's GPA or exit the program.
6. The system allows up to 8 semesters of calculation, and you can terminate at any point after completing a semester's calculation.

Instructions to test :

1. The system can be tested with various inputs entered by the user to verify its accuracy and functionality.
2. Test with valid inputs to ensure correct GPA and CGPA calculations.
3. Test with invalid inputs (marks exceeding the specified limits, invalid course types, etc.) to verify that the system properly handles errors and displays appropriate error messages.
4. Test the attendance marking system by entering different attendance percentages to ensure correct attendance marks are awarded.
5. Verify the relative grading calculation for theory courses by comparing calculated grades with expected results using different class averages and standard deviations. 6
6. Test the laboratory course grading by entering various mark combinations and verifying the assigned grades match the expected scale.

 Conclusion :

 This project is designed to simplify the GPA and CGPA calculation process for VIT students, helping them track their academic progress effectively. The calculator implements VIT's unique relative grading system for theory courses and provides accurate calculations for both theory and laboratory-based courses. This project was completed using the concepts and skills learnt during the course and does not contain any LLM-generated content. Through this project, I have gained practical experience in applying theoretical programming knowledge to solve realworld problems that students face daily. The calculator demonstrates the effective use of conditional logic, loops, and data structures to createa functional solution for academic grade calculation and tracking.
