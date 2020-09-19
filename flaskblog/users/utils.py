import os
import secrets
from PIL import Image
from flask import url_for, current_app
from flaskblog import mail
from flask_mail import Message

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename) 
    picture_fn = random_hex + f_ext
    picture_path = os.path.join(current_app.root_path, 'static/profile_pics', picture_fn)
    
    output_size = (125, 125)
    i = Image.open(form_picture)
    rgb_i = i.convert('RGB')
    rgb_i.thumbnail(output_size)
    rgb_i.save(picture_path)

    return picture_fn

def send_reset_email(user):
    token = user.get_reset_token()
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    msg = Message('Password Reset Request', sender='MAIL_USERNAME', recipients=[user.email])
        
    msg.body = f''' To reset your password, visit the following link:

{url_for('users.reset_token', token= token, _external=True)}

If you have not requested to reset the password, kindly ignore the message.
    
    '''

    
    mail.send(msg)