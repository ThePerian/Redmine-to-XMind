# Redmine-to-XMind

## How to use
You will require the following python modules to use this script:
```
https://github.com/maxtepkeev/python-redmine.git@master
https://github.com/xmindltd/xmind-sdk-python.git@master
```
Then edit these lines in script to fit your Redmine project:
```
rmUrl = 'http://rm.site.ru'
rmKey = 'herebethekey'
rmProjectName = 'trade'
```
After that just launch
```
python redmine-to-xmind.py
```
and `redmine.xmind` file will be created containing your diagram.
