# MP3-Climbing-Log


![Screenshot of game on different devices](/climbing_log/static/images/climbing_log.jpg)

Climbing log is an activity tracker site for climbing. It allows users to track their climbs through sessions and view past session information and stats through interactive charts/graphs. 

Live version of site hosted on Heroku [here](https://climbing-log-c3c4ad26055c.herokuapp.com/)

You can view an account which already has some logged activities by Logging in with:

 Username: ian

 Password: password

 

***

## Contents

1 [User Experience (UX)](#UX)

  * [Project Goals](#project-goals)
  * [User Stories](#user-stories)
  * [Database schema](#database-schema)
  * [Wireframes](#wireframes)
  * [Colour Scheme and Font](#styles)


2 [Features](#features)

 * [Database](#database)
 * [NavBar](#navbar)
 * [Footer](#footer)
 * [Flash Messages](#flash-messages)
 * [Page Features](#page-features)
 * [404 page](#404-page)


3 [Technologies Used](#technologies-used)

4 [Credits](#credits)

4 [Testing](#testing)

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

<br>

* As a user of the site, I want to keep a log of my climbing sessions so that I can track my progress over time.

* As a user of the site, I want each log to contain details about the different climbs I did in that session so that I can review the information when I choose.

* As a user of the site, I want to store information such as the difficulty, length, name, and whether I completed each climb so that I can have a comprehensive record of my activities.

* As a user of the site, I want to visualize data about my sessions and climbs using visually pleasing graphs and charts so that I can better understand my progress.

* As a user of the site, I want to use the information from my logs to guide my future climbing activities so that I can improve and set new goals.

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

#### The color scheme for the site

#### The font used for the site

***

## Features <a name="features"></a>

***

### Database <a name="database"></a>

#### Relational vs Non-Relational Databases

For this project I was required to use a database and implement CRUD functionality.

- Create: Adding new data or records to the database.

- Read: Retrieving or querying data from the database.

- Update: Modifying or editing existing data or records.

- Delete: Removing data or records from the database.

#### CRUD Functionality 

My app demonstrates CRUD functionality as outlined below:

#### Create:

- Creating user account
- Creating climbing sessions
- Creating individual climbs

#### Read:

- Reading from Sessions table to display recent sessions on homepage and sessions page
- Reading from Users table for logging in
- Reading from Climbs table for displaying climb information on sessions page and for creating interactive graphs/charts on sessions info page
- Reading from Climbs table to populate form on edit climb page

#### Update:

- Edit climb form allows users to edit the details of previously logged climbs
- Removing climbs from sessions updates Sessions table and updated session can be viewed

#### Delete:

- Deleting climbs from sessions using the delete climb button on sessions page
- Deleting whole Sessions on the session page
- Deleteing User account

***

### Database types

There are two types of database structures relational and non-relational, i decided a relational database was the best choice for my project, as the primary key/ foreign key features would be useful in the relationships between my users, their sessions and climbs from these sessions

Below is a summary of the two types: 

#### 1. Relational Databases

Structured Model: Utilize a table-based format, organizing data into rows and columns.

Data Organization: Manage structured data efficiently with well-defined relationships.

Complex Relationships: Ideal for applications that require handling intricate 
relationships between data.

Consistency: Ensure strong data consistency and integrity.

#### 2. Non-Relational Databases

Flexible Models: Offer various data models like documents, key-value pairs, or graphs.

Scalability: Designed to scale horizontally and handle dynamic, unstructured data.

Adaptability: Well-suited for applications with rapidly changing data requirements and unstructured content.

***

### NavBar <a name="navbar"></a>

Navbar for mobile screensizes, contains a button to expand and show available pages, site title is in top left which links back to home page.

![NavBar mobile](/climbing_log/static/images/navbar_mobile.jpg)

Navbar for mobile screensizes when expanded shows current page options depending on user login status.

![NavBar mobile expanded](/climbing_log/static/images/navbar_mobile_expanded.jpg)

Larger screen size navbar displays all available pages, site title is in top left which links back to home page. Current page is highlighted.

![NavBar](/climbing_log/static/images/navbar_logged_out.jpg)

Larger screen size navbar for when users are logged in, displaying the pages available when a user is authenticated.

![NavBar logged in](/climbing_log/static/images/navbar_logged_in.jpg)

- the logout button appears in the navbar on the homepage and all pages visible when the user is logged in, it allows the user to logout

- logout confirmation modal, when user is logged in and clicks the logout button in the navbar, this confirmation appears, this prevents the user logging out accidentally

  ![Logout Modal](/climbing_log/static/images/logout_modal.jpg)

***

### Footer  <a name="footer"></a>

Footer contains icons for social media, which are clickable links opening up these pages in new tabs

![Footer](/climbing_log/static/images/footer.jpg)

***

### Flash Messages <a name="flash-messages"></a>

The site contains a number of flash messages which diplay as a banner under the navbar, these provide feedback to the user to let them know that operations have been performed succesfully when they interact with the page

- flash message for when user logs out of their profile

![logged out flash message](/climbing_log/static/images/flash_message_logout.jpg)

- flash message for when the user logs into their profile

![logged out flash message](/climbing_log/static/images/flash_message_logged_in.jpg)

- flash message for when the user attempts to login with a username which is not present in the database

![no username flash message](/climbing_log/static/images/flash_message_no_username.jpg)

- flash message for when the user enters an incorrect password

![incorrect password flash message](/climbing_log/static/images/flash_message_incorrect_password.jpg)

- flash message for when the user starts logging a new climbing session

![session created flash message](/climbing_log/static/images/flash_new_session_created.jpg)

- flash message for when the user finishes logging their current climbing session

![session logged flash message](/climbing_log/static/images/flash_message_session_logged.jpg)

- flash message for when the user attempts to create a user profile with a username which is already taken

![duplicate user flash message](/climbing_log/static/images/flash_duplicate_user.jpg)

***

### Page Features <a name="page-features"></a>

***

#### Homepage

The homepage features the hero image, this is present accross the whole site.

The homepage is the first page the user is presented with when visiting the site, it contains three cards, one has a short explaination of the site, one prompts them to create a user profile and the other to log in if they already have an account.
Both of these options are also displayed for quick access on the navbar.

Once the user is logged in the cards then change one for creating a new session, one for viewing all their sessions and one contains a list of up to 10 of their recent sessions with a link to view the session charts/graphs.

##### Home page when user not logged in

![Home page not logged in](/climbing_log/static/images/homepage_not_logged_in.jpg)

##### Homepage when user logged in

![Home page logged in](/climbing_log/static/images/homepage_logged_in.jpg)


##### Page purpose card

  ![Details of page purpose](/climbing_log/static/images/page_purpose.jpg)

##### Link to create account card

  ![Home page link to create account](/climbing_log/static/images/home_page_create_account.jpg)

##### Link to login card

  ![Home page link to login](/climbing_log/static/images/home_page_login.jpg)

##### Most recent session cards

  ![Home page recent sessions link](/climbing_log/static/images/home_page_recent_sessions.jpg)


##### Link to log a new climbing session card

  ![link to log a new climbing session](/climbing_log/static/images/home_page_new_session.jpg)

##### Link to view all sessions card

  ![link to view all sessions](/climbing_log/static/images/home_page_view_sessions.jpg)

***

#### Create user page

The create user page contains a form which gathers information required to set up an account, the page layout revolves around the hero image.
It has features which ensure the password must be entered twice and match before the form can be submitted. The date of birth field can utalise a calendar to enter the users DOB. There is also user feedback through flash messages discussed above, these ensure already existing usernames/emails cannot be used again. There is alsoe feedback when to tell the user when they have successfully created an account. 

##### Create userpage 

![create user page form](/climbing_log/static/images/add_user_page.jpg)

![create user page form 2](/climbing_log/static/images/add_user_page2.jpg)

***

#### Login Page 


The login page allows user to enter their login details to access the site features which require login.
It has flash messages, discussed in details above, which appear to provide feedback to the user. To notify them of using an incorrect password, using and incorrect username and when they succesfully log in.

##### Login page

![Login page](/climbing_log/static/images/login_page.jpg)

***

#### Delete Account Page

The delete user account page allows user to delete their account removing all their information from the database
It also contains explanation that doing so will be permenant and that logged data will not be able to be retreived and password confirmation is required for this step to protect the user.


##### Delete account page

![Delete account page](/climbing_log/static/images/delete_account_page.jpg)

Upon submitting the form a modal appears and requires confirmation, this ensures it is clear to the user the action they are about to take. 

The form also contains flash messages, as discussed above in detail, which will show if the user was to enter an incorrect password into the form, or if the passwords entered do not match.

##### Delete account page modal

![Delete account confirmation modal](/climbing_log/static/images/delete_account_modal.jpg)

***

#### View Sessions Page

The view sessions page allows users to view their logged sessions, each session displays the basic information of session date, session length and number of climbs in the session.

Depending upon screen size the climbs from the session are viewed in different ways, on large screen sizes all the climbs are visible in a table, but on smaller screen sizes these are moved into accordians which can be collapsed or expanded to view the climb information.

There are buttons available to the user which allow them to edit/delete climbs and delete sessions. There is also a button for each session which takes them the the session info page which contains charts/graphs with details on that session.

There are also modals which launch when the user clicks the delete session or climb buttons, which require confirmation of deletion. This protects the user from mistakenly deleting information.

##### View sessions page large screen sizes

![View session page on large screens](/climbing_log/static/images/view_sessions_large_page.jpg)

##### View sessions page small screen sizes

![View session page on small screens](/climbing_log/static/images/view_sessions_small_page.jpg)


##### Small screen accordian 

![View session small screen accordian](/climbing_log/static/images/view_sessions_small_page_accordian.jpg)

##### Delete climb modal

![View session delete climb modal](/climbing_log/static/images/session_delete_climb_modal.jpg)

##### Delete session modal

![View session delete climb modal](/climbing_log/static/images/delete_session_modal.jpg)

***

#### Edit Climb Page

The edit climb page is accessible from the sessions page, if the user clicks the button next to a climb it loads the edit climb page for that specific climb.

The existing climb details are loaded from the database into the form, and can be changed by the user. There is a help button present which launches a modal which explains to the user the function of the edit climb page.

##### Edit climb page

![Edit climb page](/climbing_log/static/images/edit_climb_page.jpg)

##### Edit climb help modal

![Edit climb help modal](/climbing_log/static/images/edit_climb_help_modal.jpg)

***

#### Record Session Page

The record session page is the first page a user is presented with when they want to start a new session. It contains a form which collects the location of the session, this will be used in future version when I would like to add features to compare sessions from different locations.

It also contains a help button which launches a modal which provides more details to the user on how logging a session works and the start session button which takes them to the climb logging page and creates the session in the database. 

The start session button has a flash message to alert the user that they have successfully started a new session.

##### Record session page

![Record session page](/climbing_log/static/images/record_session_page.jpg)

##### Record session page help modal

![Record session help modal](/climbing_log/static/images/record_session_help_modal.jpg)

*** 

#### Add climb Page

The add climb page contains a form which the user can fill in with details of the climb they are attempting, it collects the climb name (which is an optional field), difficulty which is collected by a drop down, length of climb and radio buttons for either completed or not completed.

Once the user has attempted their climb they add the climb to the session by clicking the add climb button, the form reloads and they can log the next climb. This action has feedback via a flash message.

Upon completion of session they can click the end session button which will complete the session, provide them with feedback via a flash message and take them to the sessions page where details of that and their other sessions can be viewed.

The add climb page also has a help button which launches a modal to provide more details on how to user the page.

##### Add climb page

![Add climb page](/climbing_log/static/images/add_climb_page.jpg)

##### Add clmb help modal

![Add climb help modal](/climbing_log/static/images/add_climb_help_modal.jpg)

***

#### Session Info Page

The session info page allows users to look in more details at how they performed in the chosen session, it contains a number of graphs and charts. These are interactive with the legends being clickable to remove or add features from them.

The user can view a pie chart showing the ratio of completed to none completed climbs. A scatter showing the range of difficulty of climbs from the session, with the plots being different colors depending on whether they were completed or not. And two bar charts one showing the grade and number of climbs completed and one showing the same for the none completed climbs.

##### Session info pie chart

![session_info page](/climbing_log/static/images/session_info_page.jpg)

##### Session info scatter plot

![session_info page](/climbing_log/static/images/session_info_page1.jpg)

##### Session info bar chart

![session_info page](/climbing_log/static/images/session_info_page2.jpg)

##### Session info bar chart

![session_info page](/climbing_log/static/images/session_info_page3.jpg)

***

#### 404 page

The 404 page is designed to show when the page the user is trying to view can't be returned, for example if they enter an incorrect URL, the page has been moved or deleted, or there is a broken link. The 404 page contains the navbar, some simple text and a button to return the user to the homepage. 

##### 404 page

![404 page](/climbing_log/static/images/404_page.jpg)


#### Page design without background image

The site is designed so that all content is still visible if there is issues with loading the background image

##### Site with no background image example 1
![site without background image](/climbing_log/static/images/background_image_not_load.jpg)

##### Site with no background image example 2

![site without background image](/climbing_log/static/images/background_image_not_load1.jpg)

***

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

[Jinja](https://jinja.palletsprojects.com/en/3.1.x/) templating was used to add templates in my HTML files

[Plotly Express](https://plotly.com/python/plotly-express/) was used to created the graphs and charts to display user information on logged activities.

[Bootstrap](https://getbootstrap.com/) was used to assist in creating a responive layout and for prebuilt components such as the accordians and header/footer.

[Git](https://git-scm.com/) and [GitHub](https://github.com/) for version control and as a repository.

[Google Fonts](https://fonts.google.com/) was used to browse, select and as a source of the font I used on this site.

[FontAwesome](https://fontawesome.com/) was used for social media icons in the footer.


***

## Credits <a name="credits"></a>

When creating my project I frequently used the docs for
- [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- [Flask](https://flask.palletsprojects.com/en/3.0.x/)
- [Plotly](https://plotly.com/python/)

in addition to these the following sites/tutorials/blogs were useful:

I used [this blog post](https://vertabelo.com/blog/schema-diagram/)
to learn more about database schemas and [this blog post](https://www.gleek.io/blog/crows-foot-notation.html#google_vignette) to better understand crows foot notation schema drawings.

I used [this stackoverflow](https://stackoverflow.com/questions/70997771/is-there-a-way-to-use-python-flask-to-receive-a-unique-input-from-the-user) when looking for a solution for stopping duplicate enteries into database for unique fields.

[This tutorial](https://www.geeksforgeeks.org/how-to-add-authentication-to-your-app-with-flask-login/) was where i learned about and how to use flask-login.

[This tutorial](https://www.geeksforgeeks.org/password-hashing-with-bcrypt-in-flask/) was where i learned aboutusing bcrypt for hashing passwords to store in the database using flask.

After making some changes to my database after it was created I used [this tutorial](https://www.digitalocean.com/community/tutorials/how-to-perform-flask-sqlalchemy-migrations-using-flask-migrate) for learning how to use flask-migrate to apply changes to the database.

When I wanted to learn about how to use plotly charts with flask i used [this tutorial](https://www.geeksforgeeks.org/create-a-bar-chart-from-a-dataframe-with-plotly-and-flask/) and [this stackoverflow question](https://stackoverflow.com/questions/63616028/how-to-integrate-plotly-express-chart-to-flask-app) to help, create my charts and include them in my routes.py file.

When it came to editing my plotly charts I used [this question](https://community.plotly.com/t/how-can-i-adjust-the-whitespace-around-go-pie-chart/78584) on a plotly forum to help understand how.

When it came to creating the database queries I used the SQLAlchemy docs to better understand the ORM, particulaly [this page](https://docs.sqlalchemy.org/en/20/orm/queryguide/relationships.html) and [this one](https://docs.sqlalchemy.org/en/20/tutorial/orm_data_manipulation.html#tutorial-orm-data-manipulation).

For learning how to correctly implement a 404 page in flask I used [this site](https://flask.palletsprojects.com/en/1.1.x/patterns/errorpages/).

When i was having trouble with managing the sizing of my back ground image [this blog post](https://www.webfx.com/blog/web-design/responsive-background-image/) helped resloving it.


***

## Testing  <a name="testing"></a>

Testing was performed and documented in detail in a seperate file.

The testing documentation can be viewed [here](/TESTING.md)


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



