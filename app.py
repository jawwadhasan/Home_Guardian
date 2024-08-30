from flask import Flask, render_template, request, redirect, url_for

# Create a Flask application instance
app = Flask(__name__)

# Route for the home page
@app.route('/')
def home():
    return render_template('Home_Guardian.html')

# Route to handle order placement
@app.route('/place_order', methods=['POST'])
def place_order():
    # Get form data from the POST request
    name = request.form.get('name')
    email = request.form.get('email')
    area = request.form.get('area')
    services = request.form.get('services')
    
    # Print order details to the console for debugging
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Area: {area}")
    print(f"Services: {services}")

    # Redirect to a thank you page
    return redirect(url_for('thank_you'))

# Route for the thank you page
@app.route('/thank_you')
def thank_you():
    return "Thank you for your order! We will contact you soon."

# Route for the services page
@app.route('/service')
def services():
    return render_template('service.html')

# Route to handle booking of services
@app.route('/book_service', methods=['POST'])
def book_service():
    # Get service details from the POST request
    service_name = request.form.get('service_name')
    service_price = request.form.get('service_price')
    
    # Print booking details to the console for debugging
    print(f"Service booked: {service_name} at Rs.{service_price}")
    
    # Return a message confirming the booking
    return f"Thank you for booking {service_name}! Kindly fill form; from the Home Page! We will contact you soon."

# Route for the about page
@app.route('/about')
def about():
    return render_template('about.html')

# Route for the contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# Route to handle form submission on the contact page
@app.route('/submit_contact', methods=['POST'])
def submit_contact():
    # Get contact form data from the POST request
    name = request.form['name']
    email = request.form['email']
    phone = request.form.get('phone')  
    message = request.form['message']
    
    # Print contact details to the console for debugging
    print(f"Name: {name}")
    print(f"Email: {email}")
    print(f"Phone: {phone}")
    print(f"Message: {message}")
    
    # Return the contact page with a success message
    return render_template('contact.html', success=True)

# Run the application in debug mode
if __name__ == '__main__':
    app.run(debug=True)
