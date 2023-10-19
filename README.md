# Prototype
This is the Monarch Course Explorer Prototype
Cs 411W Team Silver 

Django notes:
- HTML files are loaded from the templates folder
- CSS and JavaScript files are loaded from the static folder

Working with local Docker container (Make sure your terminal is in the folder where local.yml is located):
- Run server: docker-compose -f local.yml up
    - When running, you should be able to see the server in Docker Desktop and at 127.0.0.1:8000 in your browser
- Stop server: Ctrl+C in terminal or user Docker Desktop to stop the server