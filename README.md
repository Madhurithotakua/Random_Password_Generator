# Random_Password_Generator


A simple password generator web application built using Flask. This application allows users to generate passwords of varying lengths and complexities based on their preferences.

## Features

- Generate passwords with customizable lengths.
- Choose the complexity level: Easy, Medium, or Hard.
- Include or exclude lowercase letters, uppercase letters, digits, and special characters.
- Simple and user-friendly web interface.

## Getting Started

Follow these instructions to set up the Flask Password Generator on your local machine for development and testing purposes.

### Prerequisites

- Python 3.7 or later
- Flask

### Installation

1. **Clone the repository**:

    ```bash
    git clone https://github.com/Madhurithotakua/Random_Password_Generator
    cd Random_Password_Generator
    ```

2. **Create a virtual environment** (recommended):

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the required packages**:

    ```bash
    pip install flask
    ```

### Libraries Used

- **Flask**: A lightweight WSGI web application framework in Python, used to handle the server-side logic and routing.
- **random**: A Python built-in library used to generate random characters for the password.
- **string**: A Python built-in library used to access different sets of characters like lowercase, uppercase, digits, and punctuation.

### Running the Application

1. **Run the Flask server**:

    ```bash
    python app.py
    ```

2. **Open your web browser** and navigate to `http://127.0.0.1:5000/` to access the password generator.

### Usage

1. Select the desired password length using the provided input field.
2. Choose the complexity level: **Easy**, **Medium**, or **Hard**.
3. Check the options to include or exclude:
   - Lowercase letters
   - Uppercase letters
   - Digits
   - Special characters
4. Click on the **"Generate Password"** button.
5. After the password is generated, it will be displayed on the screen.
6. **Copy the generated password** by selecting it and using your browser's copy function (Ctrl+C or right-click and choose "Copy").
7. **Use the copied password** wherever required, such as for account creation, authentication, or any other secure access.

### Output Page

The output page includes:

- **Generated Password**: The password based on the selected options will appear prominently on the screen.
  ![Screenshot 2024-09-02 224558](https://github.com/user-attachments/assets/ead13684-77ed-4446-a09d-b56731aaf431)

- **Copy Instructions**: A clear prompt to copy the password using the browser's copy functionality.
  ![Screenshot 2024-09-02 224722](https://github.com/user-attachments/assets/8175dff5-f8b6-4c22-82f6-ec2d53272244)

- **Error Messages**: If any validation errors occur (e.g., the password length is less than 8 characters or no character types are selected), an appropriate message will be displayed to guide the user to make necessary adjustments.
  
![Screenshot 2024-09-02 224639](https://github.com/user-attachments/assets/6175ac8d-f40b-4c7d-8066-a16d3bc3b7f5)


                                             *Happy password generating!*
