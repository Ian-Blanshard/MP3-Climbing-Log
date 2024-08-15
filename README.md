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

https://vertabelo.com/blog/schema-diagram/
https://www.gleek.io/blog/crows-foot-notation.html#google_vignette

for stopping duplicate enteries into database for unique fields
https://stackoverflow.com/questions/70997771/is-there-a-way-to-use-python-flask-to-receive-a-unique-input-from-the-user