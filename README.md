# To-Do List

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Windows OS
- Python installed

### Installation

***1. Create a virtual environment & activate it:***

```sh
python -m venv venv
venv\Scripts\activate
```
   
***2. Install project dependencies from requirements.txt:***
```sh
pip install -r requirements.txt
```

***3. Make necessary migrations:***
```sh
python manage.py makemigrations
python manage.py migrate
```

***4. Run the local server:***
```sh
python manage.py runserver
```

# Preview of specific pages

**Homepage:** 
<br><br>
![todo_homepage](https://github.com/dawidkaplon/Django_To-Do-List/assets/97986683/d4519fb3-7798-4a26-a8c5-ac6b67ff6ca5)

**A list of tasks inside a specified list:**
<br><br>
![todo_tasklist](https://github.com/dawidkaplon/Django_To-Do-List/assets/97986683/610f3c7d-c1be-4014-8cdb-0bd840bb71c1)

**Selecting a specific list if the user has previously created one:**
<br><br>
![todo_chooselist](https://github.com/dawidkaplon/Django_To-Do-List/assets/97986683/353a6cc3-1eec-4375-84d8-9ca9af567dff)

