import random
import string


def get_email():
    letters = string.ascii_lowercase
    random_word = ''.join(random.choice(letters) for _ in range(random.randint(5, 7)))
    random_email = f'{random_word + str(random.randint(0, 1000)) + "@mail.com"}'
    return random_email

def show_table_view(data):
    html_view = '<table border="1">'
    for row in data:
        html_view += '<tr>'
        for i in row:
            html_view += '<td>%s</td>' % i
        html_view += '</tr>'
    return html_view