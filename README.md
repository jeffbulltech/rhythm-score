# Rhythm Score

Rhythm Score is a simple Flask-based web application that allows users to track their activities and calculate a "rhythm score" to ensure a balanced life rhythm between work and personal life. It was created with the understanding that maintaining a healthy balance between work and life is important for overall wellness.

The application provides an intuitive interface where users can input their activities categorized as either 'Work' or 'Life' along with the duration in hours. It then calculates a rhythm score, which is a percentage indicating the proportion of time spent on life activities compared to the total time spent on both work and life activities. The rhythm score allows users to visualize the balance between work and personal life, encouraging them to achieve a more balanced lifestyle.

## Deployment

This application is built on Python and Flask, and utilizes SQLAlchemy for database operations. To deploy it:

- Ensure that Python and Flask are installed on your machine.
- Clone or download the project to your local machine.
- Navigate to the directory where you've saved the project.
- Run the application using the command python app.py. The Flask server will start, and the application will be accessible at http://127.0.0.1:5000 in your web browser.

## User Interaction

On accessing the web application, users will see a form where they can select an activity type (either 'Work' or 'Life') and input the duration of the activity in hours. After submitting the form, the application calculates the rhythm score, which is displayed as a percentage.

Additionally, a statement is provided indicating the current rhythm status. This statement will tell the user if their rhythm currently favors work, life, or if it's in harmony (indicating that the work and life hours are equal).

Users also have an option to clear all entries by clicking the 'Clear Entries' button, which deletes all the previous entries from the database, allowing users to start afresh.

Please note that while this application is primarily designed for local usage, it can also be adapted for deployment on a web server or a cloud-based platform.

## Development

Rhythm Score was developed using Python 3.8, Flask 1.1.2, and SQLAlchemy 1.3.23. The database used for storing entries is SQLite. Please note that these versions were current as of May 2023, and updates may have been released since.

Please feel free to clone or fork the repository for personal use or further development! Contributions are also welcome.