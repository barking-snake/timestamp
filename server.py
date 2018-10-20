from flask import render_template
import connexion

# Create the application instance
app = connexion.App(__name__, specification_dir="./")

app.add_api('swagger.yml')

# Create "/" route
@app.route('/')
def home():
    """
    """
    return render_template('home.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
