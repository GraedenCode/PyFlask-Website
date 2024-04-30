from flask import Blueprint, render_template, request, flash

auth = Blueprint('auth', __name__)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    data = request.form
    print(data)
    return render_template("login.html")

@auth.route('/logout')
def logout():
    return render_template("home.html")

@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    if request.method == 'POST':
        email = request.form.get('email')
        firstName = request.form.get('firstName')
        password1 = request.form.get('password1')
        password2 = request.form.get('password2')

        # sign-up authentication
        if len(email) < 4:
            flash("email must @", category='fail')
        elif len(firstName) < 2:
            flash("name must be longer than 1 character", category='fail')
        elif password1 != password2:
            flash("Passwords do not match", category='fail')
        elif password1 < 7:
            flash("Password is too short", category='fail')
        else:
            flash("Account Created!", category='success')

    return render_template("sign-up.html")