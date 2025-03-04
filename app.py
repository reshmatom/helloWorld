from flask import Flask

# Create a Flask instance
app = Flask(__name__)

# Define the route for the homepage
@app.route('/')
def hello_world():
    return "Hello, World!"

# Check if the script is being run directly
if __name__ == '__main__':
    app.run(debug=True)
