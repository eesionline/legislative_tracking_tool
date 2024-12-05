from flask import Flask, render_template, request
import getBills as gb

api_key = 'J0jKbtfI0cbPa6tbAwlnW7gmcYGealzZRhY48hQH'
date = '2024-09-25'

app = Flask(__name__)

# Example data to display
bills = gb.get_bills_details(api_key,date)

@app.route("/", methods=["GET", "POST"])
def index():
    selected_bills = []
    
    if request.method == "POST":
        # Collect selected bills based on checkboxes
        selected_ids = request.form.getlist("selected_bills")
        selected_bills = [bill for bill in bills if bill["bill_number"] in selected_ids]
    
    return render_template("index.html", bills=bills, selected_bills=selected_bills)

if __name__ == "__main__":
    app.run(debug=True)