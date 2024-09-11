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

 * [CRUD functionality](#crud-functionality)
 * [NavBar](#navbar)
 * [Footer](#footer)
 * [Flash Messages](#flash-messages)
 * [Home Page](#home-page)
 * [Create Account Page](#create-account-page)
 * []()

3 [Technologies Used](#technologies-used)

4 [Credits](#credits)

5 [Deployment](#deployment)

6 [Finished Site](#finished-site)

***
## User Experience (UX) <a name="UX"></a>
### Project Goals <a name="project-goals"></a>

 * Create a activity tracker for climbing

 * Have users log climbs, collect this information and store it in a database

 * Retreive this information and display it in a variety of graphical representations, to allow users to guide future training/ activities.

 * Responsive design so it can be used across different devices

 * Have clear instructions and user interface

 * add a feature for mutliple users to log in securely with a username and password

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

The database is a simple design with a single user having one or more sessions and each session containing one or more climbs. An email and password are included for users to allow the user to login.

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

***

## Features <a name="features"></a>


### Relational vs Non-Relational Databases

For this project I was required to use a database and implement CRUD functionality.

- Create: Adding new data or records to the database.
- Read: Retrieving or querying data from the database.
- Update: Modifying or editing existing data or records.
- Delete: Removing data or records from the database.

There are two types of database structures relational and non-relational, i decided a relational database was the best choice for my project, as the primary key/ foreign key features would be useful in the relationships between my users, their sessions and climbs from these sessions

Below is a summary of the two types: 

1. Relational Databases

Structured Model: Utilize a table-based format, organizing data into rows and columns.

Data Organization: Manage structured data efficiently with well-defined relationships.

Complex Relationships: Ideal for applications that require handling intricate 
relationships between data.

Consistency: Ensure strong data consistency and integrity.

2. Non-Relational Databases

Flexible Models: Offer various data models like documents, key-value pairs, or graphs.

Scalability: Designed to scale horizontally and handle dynamic, unstructured data.

Adaptability: Well-suited for applications with rapidly changing data requirements and unstructured content.

### CRUD Functionality <a name="crud-functionality"></a>

My app demonstrates CRUD functionality as outlined below:

#### Create:
  
#### Read:

#### Update:

#### Delete:


### NavBar <a name="navbar"></a>

Navbar for mobile screensizes, contains a button to expand and show available pages, site title is in top left which links back to home page.

![NavBar mobile](/climbing_log/static/images/navbar_mobile.jpg)

Navbar for mobile screensizes when expanded shows current page options depending on user login status.

![NavBar mobile expanded](/climbing_log/static/images/navbar_mobile_expanded.jpg)

Larger screen size navbar displays all available pages, site title is in top left which links back to home page. Current page is highlighted.

![NavBar](/climbing_log/static/images/navbar_logged_out.jpg)

Larger screen size navbar for when users are logged in, displaying the pages available when a user is authenticated.

![NavBar logged in](/climbing_log/static/images/navbar_logged_in.jpg)

### Footer  <a name="footer"></a>

![Footer](/climbing_log/static/images/footer.jpg)

### Flash Messages <a name="flash-messages"></a>

![logged out flash message](/climbing_log/static/images/flash_message_logout.jpg)

![logged out flash message](/climbing_log/static/images/flash_message_logged_in.jpg)

![no username flash message](/climbing_log/static/images/flash_message_no_username.jpg)

![incorrect password flash message](/climbing_log/static/images/flash_message_incorrect_password.jpg)

![session created flash message](/climbing_log/static/images/flash_new_session_created.jpg)

![session logged flash message](/climbing_log/static/images/flash_message_session_logged.jpg)

![duplicate user flash message](/climbing_log/static/images/flash_duplicate_user.jpg)

### Home Page <a name="home-page"></a>

Home page when user not logged in

![Home page not logged in](/climbing_log/static/images/homepage_not_logged_in.jpg)

Homepage when user logged in

![Home page logged in](/climbing_log/static/images/homepage_logged_in.jpg)


### Home Page Features

The Home page contains the following:

#### Hero Image.

  - The main image used for the site.
  - navbar/footer discussed above

#### scrollable page when not logged in contains:

  - details on page purpose

  ![Details of page purpose](/climbing_log/static/images/page_purpose.jpg)

  - link to create account, also available in navbar

  ![Home page link to create account](/climbing_log/static/images/home_page_create_account.jpg)

  - link to login, also available in navbar

  ![Home page link to login](/climbing_log/static/images/home_page_login.jpg)

  - list of most recent sessions and links to view charts from these

  ![Home page recent sessions link](/climbing_log/static/images/home_page_recent_sessions.jpg)

#### scrollable page when logged in contains:

  - link to log a new climbing session

  ![link to log a new climbing session](/climbing_log/static/images/home_page_new_session.jpg)

  - link to view all sessions 

  ![link to view all sessions](/climbing_log/static/images/home_page_view_sessions.jpg)

#### logout button

- the logout button appears in the navbar on the homepage and all pages visible when the user is logged in, it allows the user to logout

- logout confirmation modal, when user is logged in and clicks the logout button in the navbar, this confirmation appears, this prevents the user logging out accidentally

  ![Logout Modal](/climbing_log/static/images/logout_modal.jpg)

### Create account Page <a name="create-account-page"></a>

#### Create user form

![](/climbing_log/static/images/add_user_page.jpg)

![](/climbing_log/static/images/add_user_page2.jpg)

### Login Page Features

#### Login form

- allows user to enter their login details to access the site features which require login

- has flash messages, discussed in details above, which appear to provide feedback to the user. To notify them of using an incorrect password, using and incorrect username and when they succesfully log in

![Login page](/climbing_log/static/images/login_page.jpg)

### Delete Account Page Features

- allows user to delete their account removing all their information from the database

- page contains explanation that doing so will be permenant and that logged data will not be able to be retreived

- password confirmation is required for this step to protect the user

![Delete account page](/climbing_log/static/images/delete_account_page.jpg)

- upon submitting the form a modal appears and requires confirmation, this ensures it is clear to the user the action they are about to take

- the form also contains flash messages, as discussed above in detail, if the user was to enter an incorrect password into the form, or if the passwords entered do not match.

![Delete account confirmation modal](/climbing_log/static/images/delete_account_modal.jpg)

### View Sessions Page Features

![View session page on large screens](/climbing_log/static/images/view_sessions_large_page.jpg)

![View session page on small screens](/climbing_log/static/images/view_sessions_small_page.jpg)

![View session small screen accordian](/climbing_log/static/images/view_sessions_small_page_accordian.jpg)

![View session delete climb modal](/climbing_log/static/images/session_delete_climb_modal.jpg)

![View session delete climb modal](/climbing_log/static/images/delete_session_modal.jpg)

### Edit Climb Page Features

![Edit climb page](/climbing_log/static/images/edit_climb_page.jpg)

![Edit climb help modal](/climbing_log/static/images/edit_climb_help_modal.jpg)

### Record Session Page Features

![Record session page](/climbing_log/static/images/record_session_page.jpg)

![Record session help modal](/climbing_log/static/images/record_session_help_modal.jpg)

flash new session created

### Add climb Page Features

![Add climb page](/climbing_log/static/images/add_climb_page.jpg)

![Add climb help modal](/climbing_log/static/images/add_climb_help_modal.jpg)

session logged flash message

### Session Info Page Features

![session_info page](/climbing_log/static/images/session_info_page.jpg)

![session_info page](/climbing_log/static/images/session_info_page1.jpg)

![session_info page](/climbing_log/static/images/session_info_page2.jpg)

![session_info page](/climbing_log/static/images/session_info_page3.jpg)

###  <a name=""></a>

###  <a name=""></a>

###  <a name=""></a>

###  <a name=""></a>

## Technologies used <a name="technologies-used"></a>

This Project uses the following languages:

* HTML
* CSS
* JavaScript
* Python

[Flask](https://flask.palletsprojects.com/en/3.0.x/) backend framework was used to build the back end for this project.

[Flask-Bcrypt](https://flask-bcrypt.readthedocs.io/en/1.0.1/) was used to hash user passwords prior to saving them to the database for security.

[Flask-login](https://readthedocs.org/projects/flask-login/downloads/pdf/0.3.1/) was used as a simple way to manage user logins and restricting certain pages to authenticated users.

[SQL Alchemy](https://www.sqlalchemy.org/) was used as an ORM to define models as python classes and map these to database tables.

[Plotly Express](https://plotly.com/python/plotly-express/) was used to created the graphs and charts to display user information on logged activities.

[Bootstrap](https://getbootstrap.com/) was used to assist in creating a responive layout and for prebuilt components such as the accordians and header/footer.

[Git](https://git-scm.com/) and [GitHub](https://github.com/) for version control and as a repository.

[Google Fonts](https://fonts.google.com/) was used to browse, select and as a source of the font I used on this site.

***

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

https://docs.sqlalchemy.org/en/20/orm/queryguide/index.html

https://docs.sqlalchemy.org/en/20/tutorial/orm_data_manipulation.html#tutorial-orm-data-manipulation

I'd hugely overcomplicated my sessions() route, doing multiple queries to build nested dictionaries so that i could use those relationships to display all the climbs for each session in a list using jinja. I realised the code was very confusing and there surely must be a better way. i used the following resources to learn that i should be using the existing relationships from my database and there was a far simpler way of doing it. this led to refactoring and producing a much better route.


https://www.golinuxcloud.com/flask-sqlalchemy/#Querying_Data
https://medium.com/@vickypalaniappan12/relationship-loading-techniques-in-sqlalchemy-4e7d1ff96f75
https://docs.sqlalchemy.org/en/20/orm/queryguide/relationships.html

for creating a 404 page in flask
https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/

plotly layouy/margin 
https://plot.ly/python/reference/#layout-margin


https://stackoverflow.com/questions/11178426/how-can-i-pass-data-from-flask-to-javascript-in-a-template

for deleteclimb/session buttons in sessions.html
https://developer.mozilla.org/en-US/docs/Learn/HTML/Howto/Use_data_attributes

https://www.webfx.com/blog/web-design/responsive-background-image/

***

## Testing  <a name="testing"></a>

Testing was performed and documented in a seperate file which can be viewed [here](/TESTING.md)


***

## Deployment

This project was developed using Microsoft Visual Studio Code, committed to Git and pushed to GitHub using the terminal with in VScode.

The final Live version of site is hosted on Heroku and can be found [here]()

###  Deploying to Heroku

The project was deployed to Heroku, below are the steps taken:

1. Create a requirements.txt file.
pip freeze --local > requirements.txt

2. Create a Procfile details on [heroku here](https://devcenter.heroku.com/articles/procfile#:~:text=The%20Procfile%201%20Procfile%20naming%20and%20location%20The,type%20examples%20...%207%20Procfile%20and%20heroku.yml%20).

3. Add and commit the changes with git, and push the project to GitHub.

4. Create a new app on the [Heroku website](https://dashboard.heroku.com/apps) by clicking the new button in your dashboard. 

5. Confirm the linking of the Heroku app to the correct GitHub repository.

6. In the Heroku dashboard for the application, click on settings then reveal config vars and set up the configs.

7. From the Heroku dashboard of your newly created application, click deploy then deployment Method and select GitHub.

8. In the manual deployment section of this page, make sure the master branch is selected and then click deploy branch.

9. On the Heroku dashboard, click deploy.

10. Open the console on heroku and run a python3 terminal, create the db using db.create_all()



