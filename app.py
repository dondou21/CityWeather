from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///weather.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Model creation

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(60), unique=True, nullable=False)
    email = db.Column(db.String(150), unique=True,nullable=False)
    password = db.Column(db.String(60), nullable=False)

    def __repr__(self):
        return f"User('{self.username}', '{self.email}')"
    
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/users')
def user_list():
    users = db.session.execute(db.select(User).order_by(User.username)).scalar()
    return render_template('user/list.html', users=users)

@app.route('/users/create', methods=['GET','POST'])
def user_create():
    if request.method == 'POST':
        user = User(
            username=request.form["username"],
            email=request.form['email'],
            password=request.form['password'],
        )
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("user_detail", id=user.id))
    
    return render_template('user/create.html')

@app.route('/user/<int:id>')
def user_detail(id):
    user = db.get_or_404(User, id)
    return render_template('user/detail.html', user=user)

@app.route('/user/<int:id>/delete', methods=['GET', 'POST'])
def user_delete(id):
    user = db.get_or_404(User,id)

    if request.method == 'POST':
        db.session.delete(user)
        db.session.commit()
        return redirect(url_for('user_list'))
    
    return render_template('user/delete.html', user=user)


if __name__ == '__main__':
    app.run(debug=True)