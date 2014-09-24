# InsightFL
A basic template for building minimal web applications.

### Introduction
InsightFL is a basic [Flask](http://flask.pocoo.org/) template created specifically to help budding
data scientists in the [Insight Data Science](http://insightdatascience.com/) program get their web applications
off the ground quickly. As a former Insight fellow, I spent too much time troubleshooting the ins and outs of
web development instead of focusing on extracting insight from my data.

To get started building your web app, follow the instructions below to setup your development environment.

### Getting Started <a name="getting-started"></a>
#### System Requirements <a name="system-requirements"></a>
1. [Python](https://www.python.org/downloads/)(v2.7+) with [pip](http://pip.readthedocs.org/en/latest/installing.html) installed.

#### Setup <a name="environment-setup"></a>
1. Fork the [project](https://github.com/stormpython/insightfl/fork) and clone the repository.

  **Note:** It is helpful to change the repository name **before** cloning. In Github, click on `Settings` on the right-hand
  side of your screen. Within the Settings box at the top of the screen, rename the repository and click `Rename`.

  ```
  git clone git@github.com:<username>/<project>.git
  ```

2. **Recommended:** Install virtualenv and fire up a virtual environment.

  ```
  # Install virtualenv
  sudo pip install virtualenv

  # Create virtualenv folder `venv`
  virtualenv venv

  # Activate the virtual environment
  source venv/bin/activate
  ```

3. Install Python project dependencies.

  ```
  pip install -r requirements.txt
  ```

4. To test your application, run the manage.py file: `python manage.py runserver`, and open your web browser to
`localhost:5000`.

That's it! You are ready to start coding your project.

### Application Structure
#### Philosophy
InsightFL's project layout mimics that of large Flask applications. This is done intentionally. Despite the
fact that most Insight projects are small applications, utilizing this structure allows you to separate your development 
concerns more effectively. Instead of having all your web app code in one file, it can be broken up into separate, 
smaller chunks, which makes for cleaner code and easier debugging.

#### Project Layout
- **app** - Where your Flask web application lives. This is where you'll spend the majority of your time
- **docs** - Project documentation
- **.gitignore** - [Git ignore file](https://help.github.com/articles/ignoring-files)
- **config.py** - Project configuration file for storing sensitive or dynamic settings, e.g. database passwords
- **LICENSE.md** - Project license
- **manage.py** - Entry point to running your Flask application, click [here](http://flask-script.readthedocs.org/en/latest/) for more info.
- **README.md** - You're looking at it! :)
- **requirements.txt** - Tracks all your Python dependencies using [pip](http://pip.readthedocs.org/en/latest/user_guide.html#requirements-files)
- **schema.sql** - Your database schemas
