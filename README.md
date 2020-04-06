# DailySnaps
DailySnaps is a Django based News website , as of now there are going to be 5 news channels to get news from.

## Features
This is a **Django-based website** that displays top news and using **GoogleNews API** and **NewsAPI**.

1. User preferred news sections
2. Categorical search of news
3. Top news
4. News viewing of various websites
5. Filter by keyword
6. Save user's loved articles.
7. Tokenized Signup with confirmation in console(on local machine) or email.

## Getting Started
Follow these instructions to get a copy running on your local machine for
development and testing purposes

### Prerequisites.
Anaconda, Python 3.6, git and Virtual Environment (Conda environment of Anaconda preferred)

### Installing

1. Open up Terminal, and go into the directory where you want your local copy,
e.g.
```
cd projects
```

2. Download a copy
```
git clone https://github.com/RITIKHARIANI/DailySnaps.git
```

3. Install a virtual environment
```
conda create --name djangoenv
```

4. Start the environment in the projects folder.
```
conda activate djangoenv
```

5. Install Django using pip (pip is inbuilt in python when Anaconda is installed) (Django 3.0 and above )
```
pip install django
```

6. Install GoogleNews, NewsApi and six
```
pip install GoogleNews
pip install newsapi-python
pip install six
pip install django-widget-tweaks
```

7. Generate a secret key for your django app using
```
python
```
  **then run python and type**
```
from django.utils.crypto import get_random_string
```
  **then**
```
chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
```
  **then**
```
get_random_string(50, chars)
```
  **and lastly**
```
quit()
```

8. Copy this result and in your website/website/settings.py file replace
```
SECRET_KEY = os.environ.get('DAILYSNAPS')
```
  **with**
```
SECRET_KEY = 'your newly generated secret key here'
```

9. In the directory that contains 'manage.py' file, run the following to set up the database
```
python manage.py makemigrations news
```

10. When this has completed, run these migrations
```
python manage.py migrate
```

11. Create a user profile to login with
```
python manage.py createsuperuser
```

12. Once you have followed the instructions to create a user, then run the server
```
python manage.py runserver
```

13. If there were no errors anywhere, you can now go to http://localhost:8000/
in your browser to view a local copy of DailySnaps

### Signup Usage

Once you fill in the details and click Signup button, look inside your terminal/console. There will be a uniquely generated link. Copy paste that onto your broswer's address bar and press enter. You will automatically be redirected to the website with you logged in.
