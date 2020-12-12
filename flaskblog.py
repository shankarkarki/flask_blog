from flask import Flask,render_template,url_for
from forms import RegistrationForm,LoginForm
app = Flask(__name__)

app.config['SECRET_KEY']='32c049e7e582f7de8d02d7a2b846c8ee'

posts=[
    {
        'author':'Shankar Karki',
        'title':'Blog Post 1',
        'content':'First post content',
        'date_posted':'April 20,2020'
    },{
        'author':'Hera Karki',
        'title':'Blog Post 2',
        'content':'Second post content',
        'date_posted':'April 21,2020'
    }

]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html',posts=posts)

@app.route("/about")
def about():
    return render_template('about.html',title='About')

@app.route("/register")
def register():
    form=RegistrationForm()
    return render_template('register.html',title='Register',form=form)   

@app.route("/login")
def login():
    form=LoginForm()
    return render_template('login.html',title='Login',form=form) 



if __name__=='__main__':
    app.run(debug=True)