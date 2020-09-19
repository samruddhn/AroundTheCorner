# AroundTheCorner

Around the corner is a mean to meet the people, listen their stories, asking them to spread joy, happiness and knowledge.
Truth be told, building this app wasn't difficult, as I had great instructor, Corey Schafer.
He is a YouTuber and he makes awesome tutorials. Visit the channel for learning python concepts with his exceptional ability
to cultivate programming skills into newbies like me.

Necessary information for running this application :-
Confirm if Python is installed, by typing following in the terminal, otherwise install the latest version python3 :-

$ python

To Install necessary dependencies please run following commands in the terminal:

To install pip:-

$ python get-pip.py

To verify the version of pip :-

$ pip -V

To install other dependencies : -

$ pip install flask

$ pip install Flask-SQLAlchemy

$ pip install Flask-bcrypt

$ pip install Flask-login

$ pip install Flask-mail

$ pip install Flask-wtf

$ pip install email_validator

$ pip install Pillow


This web application runs at following address, which is your local host.

http://127.0.0.1:5000/

Also, you can find the image of this application at Docker hub.

This image can been used to create your container without installing any dependencies.

My docker id is :- samruddh


To pull the image, use following command

$ docker pull samruddh/samruddh_first

To create and run the container, use following command

(The docker is exposed at port 5000, and you can specify your desired port. Following command will enable the application to run at address

http://127.0.0.1:7000/ )

$ docker run -d -p 7000:5000 samruddh/samruddh_first:latest

For any suggestions, kindly reach me at samruddhtest@gmail.com

I am Samruddh and this is my first flask web application. We shall meet again, in near future, with new tasks and endeavors. Until then, sayonara friend !
