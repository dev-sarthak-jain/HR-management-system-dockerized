To start the server you first have to install the dependencies. You can do so in a virtual environment or to save yourself some headache directly do so in your computer.

Install dependencies

pip install -r requirements.txt

to run the backend
cd backend

python manage.py migrate

python manage.py runserver

to run the frontend
cd frontend
(from the main directory)

To start the frontend server

streamlit run app.py
