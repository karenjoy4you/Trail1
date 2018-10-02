from flask import Flask,render_template		#render template HTML Code from another file
app = Flask(__name__, template_folder='templates')	 #templates and static files

posts = [	#dummy data
	{
		'author':"C SC",
		'title':'Bp 2',
		'content':'firdy post',
		'date_posted':'April 20'

	},
	{
		'author':"jane doe",
		'title':'Blog 2',
		'content':'dcc post',
		'date_posted':'April 21'

	}

]

@app.route("/")		#decorater and routes
@app.route("/home")
def home():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

@app.route("/login")
def login():
    return render_template('login.html')

if __name__=="__main__":		#changes with app = Flask(__name__)
   	app.run(debug=True)