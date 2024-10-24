from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('form.html') 

@app.route('/submit', methods=['POST'])
def submit():
 
    name = request.form['name']
    contact = request.form['contact']
    food_type = request.form['foodType']
    quantity = request.form['quantity']
    location = request.form['location']
    
  
    print(f"Name: {name}, Contact: {contact}, Food Type: {food_type}, Quantity: {quantity}, Location: {location}")

    return redirect(url_for('index'))  

if __name__ == '__main__':
    app.run(debug=True)