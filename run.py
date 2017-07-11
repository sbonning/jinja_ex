from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def template_test():
	return render_template('template.html', my_string="Go!",my_list=[0,1,1,2,3,5,8,13,21])

if __name__ == '__main__':
	app.run(debug=True, port=8080, host="0.0.0.0")
