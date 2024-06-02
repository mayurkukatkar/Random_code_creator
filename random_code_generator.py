from flask import Flask, jsonify, render_template_string
import random
import string

app = Flask(__name__)

def generate_random_code(length=12):
    """Generate a random alphanumeric code of a given length."""
    characters = string.ascii_letters + string.digits
    random_code = ''.join(random.choice(characters) for _ in range(length))
    return random_code

@app.route('/')
def index():
    return render_template_string(template)

@app.route('/generate')
def generate():
    code = generate_random_code()
    return jsonify(code=code)

template = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Random Code Generator</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
            background-color: #f4f4f4;
        }
        .container {
            text-align: center;
            background-color: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        .code {
            font-size: 2em;
            margin: 20px 0;
            padding: 10px;
            background-color: #e8e8e8;
            border-radius: 4px;
            letter-spacing: 2px;
        }
        .button {
            padding: 10px 20px;
            font-size: 1em;
            color: #fff;
            background-color: #007BFF;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        .button:hover {
            background-color: #0056b3;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Random Code Generator</h1>
        <div id="code" class="code">Loading...</div>
        <button class="button" onclick="regenerateCode()">Regenerate</button>
    </div>

    <script>
        function regenerateCode() {
            fetch('/generate')
                .then(response => response.json())
                .then(data => {
                    document.getElementById('code').innerText = data.code;
                });
        }

        // Generate a code when the page loads
        document.addEventListener('DOMContentLoaded', regenerateCode);
    </script>
</body>
</html>
'''

if __name__ == '__main__':
    app.run(debug=True)
