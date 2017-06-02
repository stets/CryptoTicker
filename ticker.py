from flask import Flask, render_template
import ether

app = Flask(__name__)



@app.route('/')
def hello_world():
	author = "Stetson"
	name = "Stetson"
	price = ether.getPrice()
	return render_template('index.html', author=author, name=name, price=price)


if __name__ == '__main__':
	app.run()


