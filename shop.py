from flask import Flask, session, redirect, url_for, request, render_template

app = Flask(__name__) # создание объекта приложения
app.secret_key = '76fa5b0ec1841105a24b3de3c66e3a49e26dea0a2bcedcff143fc7cc733d500f'


@app.route('/') # декоратор маршрутизации запросов
def index():
    _text_info = ('<h1 class="cool-12 text-monospace text-center">Это главная страница Интернет магазина</h1>'
                  '<p class="cool-12 text-monospace text-center">Здесь вы можете ознакомиться с нашими товарами</p>')
    context = {'text': _text_info, 'title': 'Главная страница'}
    return render_template('index.html', **context)

@app.route('/about/') # декоратор маршрутизации запросов
def about():
    _text_info = ('<h1 class="cool-12 text-monospace text-center">Это страница о нас</h1>'
                  '<p class="cool-12 text-monospace text-center">Здесь вы можете узнать о нас больше</p>')
    context = {'text': _text_info, 'title': 'О Нас'}
    return render_template('about.html', **context)

@app.route('/contacts/') # декоратор маршрутизации запросов
def contacts():
    _text_info = ('<h1 class="cool-12 text-monospace text-center">Это страница контактов</h1>'
                  '<p class="cool-12 text-monospace text-center">Здесь вы можете связаться с нами</p>')
    context = {'text': _text_info, 'title': 'Контакты'}
    return render_template('contacts.html', **context)







# Домашнее задание Урок 2. Погружение во Flask 28.03.24 начало:-------------------------------------

@app.route('/user_lk/')
def user_lk():
    if 'username' in session:
        context = {'title': 'Личный кабинет', 'text': 'Привет, ' + session['username'] + '!, <a href="/logout/">Выйти</a>'}
        return render_template('lk.html', **context)
    return redirect(url_for('login'))


@app.route('/login/', methods=['GET', 'POST'])
def login():
    # если метод запроса POST
    if request.method == 'POST':
        # устанавливаем значение в словаре session
        session['username'] = request.form.get('username') or 'Гость'
        # перенаправляем на странницу приветствия пользователя
        return redirect(url_for('user_lk'))
    # если метод запроса GET
    return render_template('form.html')

'''
Для выхода из сессии используется метод pop() объекта session.
Этот метод удаляет значение по ключу из словаря. 
Ключ — username. 
После удаления значения, пользователь перенаправляется на страницу ввода имени и электронной почты.
'''
@app.route('/logout/')
def logout():
    session.pop('username', None)
    return redirect(url_for('login'))

# Домашнее задание Урок 2. Погружение во Flask 28.03.24 конец:-------------------------------------






@app.route('/cloth/') # декоратор маршрутизации запросов
def cloth():
    _text_info = ('<h1 class="cool-12 text-monospace text-center">Это страница одежды</h1>'
                  '<p class="cool-12 text-monospace text-center">Здесь вы можете ознакомиться с нашей одеждой</p>')
    context = {'text': _text_info, 'title': 'Одежда'}
    return render_template('cloth.html', **context)

@app.route('/shoes/') # декоратор маршрутизации запросов
def shoes():
    _text_info = ('<h1 class="cool-12 text-monospace text-center">Это страница обуви</h1>'
                  '<p class="cool-12 text-monospace text-center">Здесь вы можете ознакомиться с нашей обувью</p>')
    context = {'text': _text_info, 'title': 'Обувь'}
    return render_template('shoes.html', **context)

@app.route('/jacket/') # декоратор маршрутизации запросов
def jacket():
    _text_info = ('<h1 class="cool-12 text-monospace text-center">Это страница курток</h1>'
                  '<p class="cool-12 text-monospace text-center">Здесь вы можете ознакомиться с нашими куртками</p>')
    context = {'text': _text_info, 'title': 'Куртки'}
    return render_template('jacket.html', **context)

if __name__ == '__main__':
    app.run(debug=True) # запуск приложения
