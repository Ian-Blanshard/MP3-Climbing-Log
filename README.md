# MP3-Climbing-Log
***

## Contents

1 [User Experience (UX)](#UX)

  * [Project Goals](#project-goals)
  * [User Stories](#user-stories)
  * [Database schema](#database-schema)
  * [Wireframes](#wireframes)
  * [Colour Scheme and Font](#styles)

2 [Features](#features)

3 [Technologies Used](#technologies-used)

4 [Credits](#credits)

5 [Testing](#testing)

  * [Bugs](#bugs)
  * [Code Validation](#code-validation)
    * [CSS code validation](#css-code-validation)
    * [HTML code validation](#html-code-validation)
  * [Lighthouse Testing](#lighthouse-testing)
  * [Manual Testing](#manual-testing)
    * [Testing across different devices and browsers](#testing-across-different-devices-and-browsers)
  * [Testing Stories](#testing-stories)
  

6 [Deployment](#deployment)

7 [Finished Site](#finished-site)

***
## User Experience (UX) <a name="UX"></a>
### Project Goals <a name="project-goals"></a>

 * Create a activity tracker for indoor climbing

 * Have users log climbs, collect this information and store it in a database

 * Retreive this information and display it in a variety of graphical representations, to allow users to guide future training/ activities.

 * Responsive design so it can be used across different devices

 * Have clear instructions and user interface

 * Initially focussed on a single user but I would like to eventually intergrate authentication add a feature for mutliple users to log in with a user name and password

<br>

***

### User stories <a name="user-stories"></a>

A user of the site wants to:

* Keep a log of their climbing sessions

* The logs to contain the different climbs they did in that session

* Information on difficulty, length name and whether they completed the climb to be stored

* To be able to visualise the data about the sessions and climbs in visually pleasing graphs and charts

* To be able to use this information to guide there future activities

<br>

***

### Database schema <a name="database-schema"></a>

[Figma](www.figma.com) was used to create a database schema and wireframes for the project. This ensured I had a clear vision for the project before beginning to write code.

![Screenshot database schema](/climbing_log/static/images/database_schema.jpg)

The database is a simple design with a single user having one or more sessions and each session containing one or more climbs. An email and password are included for users to allow scope for adding user logins further in development.

***

### Wireframes <a name="wireframes"></a>

### Mobile wireframes

### Homepage

![Screenshot of mobile wireframe 1](/climbing_log/static/images/mobile_wireframe_1.jpg)

![Screenshot of mobile wireframe 2](/climbing_log/static/images/mobile_wireframe_2.jpg)

### Sessions home page

![Screenshot of mobile wireframe 3](/climbing_log/static/images/mobile_wireframe_3.jpg)

### New session page

![Screenshot of mobile wireframe 4](/climbing_log/static/images/mobile_wireframe_4.jpg)

### Logging climbs to session page

![Screenshot of mobile wireframe 5](/climbing_log/static/images/mobile_wireframe_5.jpg)

### Individual session information

![Screenshot of mobile wireframe 6](/climbing_log/static/images/mobile_wireframe_6.jpg)

***


### Tablet/ Desktop wireframes

The layout and design for tablet/desktop will be the same with desktop having larger borders to the side of the cards. This provides consistency across devices.The site is desinged mobile first, with the idea being it will primarily be used on a mobile in a situtaion you are performing the activities.

### Homepage

![Screenshot of tablet/desktop wireframe 1](/climbing_log/static/images/tablet_wireframe_1.jpg)

![Screenshot of tablet/desktop wireframe 2](/climbing_log/static/images/tablet_wireframe_2.jpg)

### Sessions home page

![Screenshot of tablet/desktop wireframe 3](/climbing_log/static/images/tablet_wireframe_3.jpg)

### New session page

![Screenshot of tablet/desktop wireframe 4](/climbing_log/static/images/tablet_wireframe_4.jpg)

### Logging climbs to session page

![Screenshot of tablet/desktop wireframe 5](/climbing_log/static/images/tablet_wireframe_5.jpg)

### Individual session information

![Screenshot of tablet/desktop wireframe 6](/climbing_log/static/images/tablet_wireframe_6.jpg)


 ***


### Colour Scheme and Font <a name="styles"></a>

## Credits <a name="credits"></a>
for learning about database schemas
https://vertabelo.com/blog/schema-diagram/
https://www.gleek.io/blog/crows-foot-notation.html#google_vignette

for stopping duplicate enteries into database for unique fields
https://stackoverflow.com/questions/70997771/is-there-a-way-to-use-python-flask-to-receive-a-unique-input-from-the-user

basic tutorial for flask-login
https://www.geeksforgeeks.org/how-to-add-authentication-to-your-app-with-flask-login/

tutorial for hashing passwrod using flask
https://www.geeksforgeeks.org/password-hashing-with-bcrypt-in-flask/

for learning how to user flask-migrate to apply changes to the database
https://www.digitalocean.com/community/tutorials/how-to-perform-flask-sqlalchemy-migrations-using-flask-migrate

for learning how to create plotly charts and place into html
https://stackoverflow.com/questions/63616028/how-to-integrate-plotly-express-chart-to-flask-app
https://www.geeksforgeeks.org/create-a-bar-chart-from-a-dataframe-with-plotly-and-flask/

for pie chart borders 
https://community.plotly.com/t/how-can-i-adjust-the-whitespace-around-go-pie-chart/78584

https://docs.sqlalchemy.org/en/20/tutorial/orm_data_manipulation.html#tutorial-orm-data-manipulation

I'd hugely overcomplicated my sessions() route, doing multiple queries to build nested dictionaries so that i could use those relationships to display all the climbs for each session in a list using jinja. I realised the code was very confusing and there surely must be a better way. i used the following resources to learn that i should be using the existing relationships from my database and there was a far simpler way of doing it. this led to refactoring and producing a much better route.
(code to show how messy things can get)
# get session ids
        session_ids = db.session.query(Sessions.session_id).filter_by(
            user_id=current_user.user_id).order_by(Sessions.session_id.desc()).all()
        # turn this into a list of integers - rather than tuples
        session_ids = [session_id[0] for session_id in session_ids]
        # create a dictionary to store the climbs/session in
        climb_details = {}
        # loop through the sessions and query the database for climbs
        for session_id in session_ids:
            # get climbs for that session
            climbs = db.session.query(Climb).filter_by(
                session_id=session_id).all()
            # Initialize the session_id key if it doesn't already exist
            if session_id not in climb_details:
                climb_details[session_id] = {}
            # loop through climbs and add them to dictionary
            for climb in climbs:
                # store data in nested dictionaries
                climb_details[climb.session_id][climb.climb_id] = {
                    'name': climb.name,
                    'difficulty': climb.difficulty,
                    'length': climb.length,
                    'completed': climb.completed
                }

https://www.golinuxcloud.com/flask-sqlalchemy/#Querying_Data
https://medium.com/@vickypalaniappan12/relationship-loading-techniques-in-sqlalchemy-4e7d1ff96f75
https://docs.sqlalchemy.org/en/20/orm/queryguide/relationships.html




## Testing  <a name="testing"></a>

### Bugs <a name="bugs"></a>

#### Bug fix

Fix the bug throws error when trying to log in with a username that doesn't exist in database