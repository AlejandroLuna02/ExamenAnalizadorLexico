from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def analyzer():
    if request.method == 'POST':
        input_text = request.form['input_text']
        items = process_input(input_text)
        return render_template('result.html', items=items)
    return render_template('index.html')

def process_input(input_text):
    items = []
    for item_text in input_text.split(','):
        item = item_text.strip().split()
        name = item[0]
        price = float(item[1])
        iva = price * 0.16
        total = price + iva
        items.append({'name': name, 'price': price, 'iva': iva, 'total': total})
    return items

if __name__ == '__main__':
    app.run(debug=True)