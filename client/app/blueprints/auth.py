from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, login_required, logout_user

from app.forms import LoginForm
from app.utils import logout_required

blueprint = Blueprint("auth", __name__, url_prefix='/auth')

@blueprint.route("/login/", methods=['get'])
@logout_required
def login():
    form = LoginForm()
    return render_template('auth/login.html', form=form)

@blueprint.route("/login/", methods=['post'])
@logout_required
def login_post():
    form = LoginForm(request.form)
    if form.validate_on_submit():
        login_user(form.user, remember=form.remember.data)
        return redirect(url_for('manage.manage_index'))

    return render_template('auth/login.html', form=form)

@blueprint.route("/logout/")
@login_required
def logout():
    logout_user()
    flash('You are logged out.', 'info')
    return redirect(url_for('auth.login'))
