PROBLEM STATEMENT :

We, the students of VIT often face difficulties in understanding and manually calculating our semester GPA and CGPA due to the complex relative grading system for theory courses and the different grading methodologies for laboratory and project-based courses. Without VTOP calculating our GPA and CGPA would be a tedious and error-prone job. Additionally, students need to track their academic progress across multiple semesters and understand how their current performance affects their cumulative CGPA. So I have created this "VIT'ian CGPA Calculator" as the solution for this trouble. The aim of this project is to create a calculator that accurately implements VIT's grading systems, takes into account both theory and laboratory courses, validates user inputs, and delivers instant and reliable results for both semester GPA and cumulative CGPA. 

Scope of the project :

1. Functional scope :

   The system allows the user to enter their marks, attendance percentage, class statistics and othercourse-related details for multiple semesters (up to 8 semesters). The system differentiates between two types of courses: Theory courses (LTP/LT) and Laboratory/Project-based courses (PJ). For Theory courses, the system takes the following inputs: CAT1 marks (out of 50), CAT2 marks (out of 50), Term-end examination marks (out of 100), Internal marks (out of 40), Attendance percentage, Class average (out of 100), and Standard deviation of the class. For Laboratory/Project courses, the system takes the following inputs: Term-end examination marks (out of 100), Internal marks (out of 10), and Lab assignment marks (out of 60). The system validates all inputs entered by the user to ensure they are within acceptable ranges. The valid inputs are processed and grades are calculated using the appropriate grading methodology. For theory courses, relative grading is applied using the formula: if marks > (Class average + 1.50 × SD), grade is 'S' (10 points), and this scaling continues down based on standard deviation ranges. For laboratory courses, absolute grading is applied with predefined grade boundaries. The GPA is calculated using the formula: GPA = (SUM(Course credits × Grade points)) / Total credits. The CGPA is calculated using the formula: CGPA =(SUM(GPA × Total credits for that semester)) / Total credits completed till date. The results (GPA and CGPA) are displayed finally along with their course credits, grades, and grade points for user verification.

2. Non-functional scope :

   The system is user-friendly with clear prompts and instructions to guide the user through the calculation process. The system performs all calculations in realtime and displays outputs within 1-2 seconds. The system can be executed on any platform that supports Python, making it available anywhere and anytime for users to calculate their GPA and CGPA. The system is designed to be robust and handle invalid inputs gracefully by displaying appropriate error messages.

 Target Audience :

   Students of VIT who need to track their academic progress, calculate their semester GPA and cumulative CGPA, and understand how the relative grading system impacts their grades. Teachers and academic advisors who may use this tool to help students understand their performance. Academic administrators who may need to verify student calculations.
