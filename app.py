from flask import Flask, render_template_string, request, send_from_directory

app = Flask(__name__)

def generate_password(length, level, include_uppercase, include_lowercase, include_digits, include_special):
    import random
    import string

    # Define character sets for password
    lowercase = string.ascii_lowercase if include_lowercase else ''
    uppercase = string.ascii_uppercase if include_uppercase else ''
    digits = string.digits if include_digits else ''
    special_chars = string.punctuation if include_special else ''

    # Combine selected character sets based on level
    if level == 'easy':
        all_chars = lowercase + digits
    elif level == 'medium':
        all_chars = lowercase + uppercase + digits
    else:  # hard
        all_chars = lowercase + uppercase + digits + special_chars

    # Validate if the length is sufficient and all_chars is not empty
    if len(all_chars) == 0 or length < 8:
        return None, "Password must be at least 8 characters long and include selected character types."

    # Ensure the password contains at least one character from each selected set
    password = []
    if include_lowercase:
        password.append(random.choice(lowercase))
    if include_uppercase:
        password.append(random.choice(uppercase))
    if include_digits:
        password.append(random.choice(digits))
    if include_special:
        password.append(random.choice(special_chars))

    # Fill the rest of the password length with random choices from all selected sets
    password += random.choices(all_chars, k=length - len(password))

    # Shuffle the password list to ensure randomness
    random.shuffle(password)

    # Convert the list to a string
    return ''.join(password), None

@app.route('/', methods=['GET', 'POST'])
def home():
    password = None
    message = None

    # Handle POST request for password generation
    if request.method == 'POST':
        # Get user inputs from the form
        length = int(request.form.get('length', 12))
        level = request.form.get('level', 'medium')
        include_uppercase = 'uppercase' in request.form
        include_lowercase = 'lowercase' in request.form
        include_digits = 'digits' in request.form
        include_special = 'special' in request.form

        # Generate password based on user inputs
        password, message = generate_password(length, level, include_uppercase, include_lowercase, include_digits, include_special)

    # Read the contents of the HTML file
    with open("index.html", "r") as file:
        html_content = file.read()

    # Render the HTML with the password and message
    return render_template_string(html_content, password=password, message=message)

@app.route('/style.css')
def serve_css():
    return send_from_directory('.', 'style.css')

if __name__ == '__main__':
    app.run(debug=True)
