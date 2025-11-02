# FastAPI - Tinker and Learn Features:

1. Parameter selection using Enums
2. Path and query parameters
3. Conditional logic based on query parameters

# Steps to run the application:


1. Clone this repository and install the required packages:
    `pip install -r requirements.txt`

2. Run the application using Uvicorn:

   `uvicorn lessons.lesson_1.main:app --reload` 
   
   or 
   
   `uvicorn <module_name>:<app_instance_name> --reload`

3. Access the application in your browser at:
   `http://localhost:8000`


> Create virtual environment before step 1 (optional but recommended):

   `python -m venv venv`

   - `source venv/bin/activate` -> on macOS/Linux use
   - `venv\Scripts\activate` -> on Windows use 