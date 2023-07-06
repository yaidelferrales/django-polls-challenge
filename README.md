# Interview instructions

This is a simple but realistic Django project, which allows people to vote on polls.

You have the following tasks to perform on this project:

- Correct any issues you find in the code.
- Add a database migration to populate the database with a poll of your choice.
- Edit the source code so that people can vote for multiple options instead of just one.
- Add a UI framework to style the frontend.
- Remove the few instances of inline styles.
- Secure the UI so you require username and password to see the polls.
- Submit the code as a PR in a branch called 'your-name-challenge-date'

Feel free to take some time to familiarize yourself with the environment before starting the assignment.




# General instructions

## Running Django + PostgreSQL on CoderPad

This pad is running a Django application, with a built-in connection to a PostgreSQL database orchestrated with docker compose. Changes are automatically applied as you type them, and you can add as many files to the project as you need.

### Django admin

The Django admin is served on the default path `/admin` and a super user has to be created using the command `docker-compose run --rm web python manage.py createsuperuser`
