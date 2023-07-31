from pywebio.input import input as pw_input
from pywebio.input import NUMBER, PASSWORD, DATETIME, COLOR
from pywebio.output import put_success, put_warning, put_code, popup, put_markdown, toast

user_password = pw_input('Enter your password', type=PASSWORD)
put_warning(user_password)

user_name = pw_input('Enter your name ').title()
put_success(user_name)

age = pw_input('Enter your age ', type=NUMBER)
put_warning(age)

date = pw_input('Enter your birthday ', type=DATETIME)
put_code(f'Your birthday is {date}\U0001F382')

color = pw_input('Enter your favorite color ', type=COLOR)
put_success(color)

# toast('Thank you for entering your details. Now we can hack you.')
popup('Thank you for entering your details. Now we can hack you.')
# put_markdown('put markdown')



