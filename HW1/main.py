# 1. Возвращать содержимое файла с пайтон пакетами (requirements.txt)
# PATH: /requirements/ открыть файл requirements.txt и вернуть его содержимое
# 2. Вывести 100 случайно сгенерированных юзеров (почта + имя) 'Dmytro aasdasda@mail.com'
# PATH: /generate-users/ ( https://pypi.org/project/Faker/ )
# + параметр который регулирует количество юзеров
# 3. Считать файл hw.csv и посчитать средний рост, средний вес в см и кг соответственно
# PATH: /mean/
# 4. Вывести количество космонавтов в настоящий момент (http://api.open-notify.org/astros.json) (https://pypi.org/project/requests/)
# PATH: /space/


from flask import Flask, request
from utils import read_requirements, generate_emails_and_names, read_and_count_file, count_spacemen


app = Flask(__name__)


@app.route("/")
def welcome_user():
    return """
    <p>Click the links below to get more information:</p>
    <a href='/requirements/'>/requirements/</a><br>
    <a href='/generate-users/'>/generate-users/</a><br>
    <a href='/mean/'>/mean/</a><br>
    <a href='/space/'>/space/</a>
    """


@app.route('/requirements/')
def get_requirements():
    return read_requirements()


@app.route('/generate-users/')
def get_users():
    query_params = request.args
    default_count_users = 100
    min_count_users = 1
    max_count_users = 150
    count_users = query_params.get('count_users') or ''
    if count_users.isdigit():
        count_users = int(count_users)
        if count_users < min_count_users or count_users > max_count_users:
            count_users = default_count_users
    else:
        count_users = default_count_users
    return generate_emails_and_names(count_users)


@app.route('/mean/')
def get_average_height_and_weight():
    return read_and_count_file()


@app.route('/space/')
def get_spacemen_count():
    return f'There are {count_spacemen()} spacemen.'


if __name__ == '__main__':
    app.run(debug=True)