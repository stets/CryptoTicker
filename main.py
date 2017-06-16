from flask import Flask, render_template
import ticker

app = Flask(__name__)


@app.route('/')
def root():
    price, symbol = ticker.getPrice() 
    return render_template('index.html', price=price, symbol=symbol)

if __name__ == '__main__':
    app.run()

