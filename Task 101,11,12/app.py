from flask import Flask, render_template, request
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load("/home/hackerali/Desktop/Ali Husnain/Laptop_price_model.pkl")
brands = ['ASUS', 'Lenovo', 'HP', 'Dell', 'Acer']
processor_brands = ['Intel', 'AMD']
processor_names = ['i5', 'i7', 'i9', 'Ryzen 5', 'Ryzen 7', 'Ryzen 9']
ram_types = ['DDR3', 'DDR4', 'DDR5']
oss = ['Windows', 'DOS', 'Linux']
os_bits = ['64', '32']
weights = ['Light', 'Medium', 'Heavy']
touchscreen = ['Yes', 'No']
msoffice = ['Yes', 'No']
ratings = ['1', '2', '3', '4', '5']

@app.route("/", methods=['GET', 'POST'])
def index():
    price = None
    if request.method == "POST":
        # Collect input data
        data = {
            'brand': request.form.get('brand'),
            'processor_brand': request.form.get('processor_brand'),
            'processor_name': request.form.get('processor_name'),
            'ram_type': request.form.get('ram_type'),
            'os': request.form.get('os'),
            'os_bit': int(request.form.get('os_bit')),
            'weight': request.form.get('weight'),
            'Touchscreen': 1 if request.form.get('Touchscreen') == 'Yes' else 0,
            'msoffice': 1 if request.form.get('msoffice') == 'Yes' else 0,
            'ram_gb': int(request.form.get('ram_gb')),
            'ssd': int(request.form.get('ssd')),
            'hdd': int(request.form.get('hdd')),
            'graphic_card_gb': int(request.form.get('graphic_card_gb')),
            'processor_gnrtn': int(request.form.get('processor_gnrtn')),
            'warranty': int(request.form.get('warranty')),
            'rating': float(request.form.get('rating')),
            'total_storage': int(request.form.get('ssd')) + int(request.form.get('hdd'))
        }

        df = pd.DataFrame([data])
        # Predict price
        price = model.predict(df)[0]

    return render_template("index.html",
                           price=price,
                           brands=brands,
                           processor_brands=processor_brands,
                           processor_names=processor_names,
                           ram_types=ram_types,
                           oss=oss,
                           os_bits=os_bits,
                           weights=weights,
                           touchscreen=touchscreen,
                           msoffice=msoffice,
                           ratings=ratings)

if __name__ == "__main__":
    app.run(debug=True)
