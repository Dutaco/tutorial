
from flask import Flask, render_template, url_for
from basic import app, db, Course
from forms import CourseForm

app.secret_key = 'mojtajnikljuc'


@app.route('/', methods=['GET', 'POST'])
def index():
    form2 = CourseForm()
    course_one = Course.query.get(1)
    course_two = Course.query.get(2)
    name1 = course_one.name
    name2 = course_two.name
    pers1 = course_one.progress
    pers2 = course_two.progress
    cont1 = course_one.content
    cont2 = course_two.content
    return render_template('front_page.html', name1=name1, name2=name2, pers1=pers1, pers2=pers2, cont1=cont1, cont2=cont2, form=form2)


@app.route('/dashboard')
def dashboard():
    return render_template('dashboard.html')


@app.route('/rearpage', methods=['GET', 'POST'])
def rearpage():
    course_one = Course.query.get(1)
    course_two = Course.query.get(2)
    form2 = CourseForm()
    if form2.submit1.data:
        cont = course_one.content
    elif form2.submit2.data:
        cont = course_two.content
    return render_template('rear_page.html', cont=cont)


if __name__ == '__main__':
    app.run(debug=True)
