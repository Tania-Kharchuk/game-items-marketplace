# Game items marketplace Project

Project for managing game items marketplace which provide the possibility to create, update and delete items with special types of interaction between their owners.


## Features
* Non-logged in user has access to pages with playable race and class lists
* Logged-in user can create, update and delete items, defining type (which can be created by user too) and interaction type (for example to sell or to exchange)
* Every logged-in user has own profile page with possibility to update or delete it. Also user's profile contain list of this user's items
* In general items list if user is owner of item, he can update or delete it, otherwise only see details
* User can search items by name, by type, order by creation date or see only his/her items


## DB-structure

![DB_structure](db_structure.png)


## Home-page example

![DB_structure](home_page1.png)
![DB_structure](home_page2.png)

## Installation

Python3 must be already installed

```shell
git clone https://github.com/Tania-Kharchuk/game-items-marketplace
cd game-items-marketplace
python -m venv venv
venv/Scripts/activate
pip install -r requirements.txt
python manage.py runserver
```


## Link to the Project

[Game items marketplace project deployed to Render](https://wow-items-marketplace.onrender.com/)

You may use such credentials:

Username: testuser

Password: testpass2103
