  # Testing Climbing Log
  ***
  ## Contents
  
  * [Code Validation](#code-validation)
    * [CSS code validation](#css-validation)
    * [HTML code validation](#html-validation)
    * [JavaScript validation](#javascript-validation)
    * [python code validation](#python-validation)

  * [Lighthouse Testing](#lighthouse-testing)

  * [Manual Testing](#manual-testing)
    * [Testing across different devices and browsers](#testing-across-different-devices-and-browsers)
    * [Testing Navbar](#testing-navbar-page)
    * [Testing Homepage](#testing-home-page)
    * [Testing Add User Page](#testing-add-user-page)
    * [Testing Login Page](#testing-login-page)
    * [Testing Delete Account Page](#testing-delete-account-page)
    * [Testing View Sessions Page](#testing-view-sessions-page)
    * [Testing Edit Climb Page](#testing-edit-climb-page)
    * [Testing Record Session Page](#testing-record-session-page)
    * [Testing Add Climb Page](#testing-add-climb-page)
    * [Testing Session Info Page](#testing-session-info-page)
    * [Testing 404 page](#testing-404-page)
    
  * [Bugs](#bugs)

  * [Testing Stories](#testing-user-stories)

***

### Code validation <a name="code-validation"></a>

#### CSS validation <a name="css-validation"></a>

My CSS code passed validation with no errors

![CSS validation](/climbing_log/static/images/css_validation.jpg)

#### HTML validation <a name="html-validation"></a>

My HTML code has a number of errors as seen below, these were due to a number of trailing slashes, br elements being used in lists and an unclosed div.

![HTML validation before 1](/climbing_log/static/images/html_validation.jpg)

![HTML validation before 2](/climbing_log/static/images/html_validation1.jpg)

![HTML validation before 3](/climbing_log/static/images/html_validation2.jpg)

I rectified all these issues and my code passed as can be seen below

![HTML validation after](/climbing_log/static/images/html_validation_pass.jpg)


#### JavaScript validation <a name="javascript-validation"></a>

JSHint JavaScript validator highlighted a number of unnecessary semicolons in my javaScript

![JavaScript validation](/climbing_log/static/images/javascript_validation.jpg)

After removing this my script.js file passed valiation with no errors.

![JavaScript validation pass](/climbing_log/static/images/javascript_validation_pass.jpg)

#### Python validation

The [Code Institute](https://pep8ci.herokuapp.com/#) python linter was used to ensure my
python code was PEP8 compliant

This highlighted a number of issues with trailing whitespace and lines being greater than 79 characters long

![python validation](/climbing_log/static/images/python_validation.jpg)

These were rectified and my code passed with no errors.

![python validation pass](/climbing_log/static/images/python_validation_passed.jpg)

***

### Lighthouse testing <a name="lighthouse-testing"></a>

Lighthouse testing was good scores for all apart from my SEO, I altered some of the elements used for heading and included a meta description in the head, this rectified the issues and I also achieved a high score for SEO.

Initial score

![lighthouse score before](/climbing_log/static/images/lighthouse_before.jpg)

Lighthouse score following changes

![lighthouse score after](/climbing_log/static/images/lighthouse_after.jpg)



***

### Manual testing <a name="manual-testing"></a>

#### Testing across different devices and browsers  <a name="testing-devices-browsers"></a>

Browser | Outcome | Pass/Fail  
--- | --- | ---
Google Chrome | Site functioned as expected, design appearance correct and responsive across different screen sizes | Pass
Microsoft Edge | Site functioned as expected, design appearance correct and responsive across different screen sizes | Pass
Mozilla Firefox | Site functioned as expected, design appearance correct and responsive across different screen sizes | Pass
Apple Safari | Site functioned as expected, design appearance correct and responsive across different screen sizes, tested only on mobile screen size (iphone 12) | Pass

#### Testing site features  <a name="testing-site-features"></a>

#### Testing Navbar Page  <a name='testing-home-page'></a>

##### User not logged in Navbar

Feature | Outcome | Pass/Fail  
--- | --- | ---
Climbing logo brand link | clicking brand link reloaded homepage | Pass
Home page link | clicking link reloaded homepage | Pass
Create account page link | clicking link loaded create account form | Pass
Login link | clicking link loaded user login form | Pass

##### User logged in Navbar

Feature | Outcome | Pass/Fail  
--- | --- | ---
Climbing logo brand link | clicking brand link reloaded homepage | Pass
View sessions link | clicking link loaded sessions page | Pass
Record sessions link | clicking link loaded new session page | Pass
Logout link | clicking link launched confirmation of logging out modal, both modal buttons functioned correctly | Pass
Delete account link | clicking link loaded delete account page | Pass


#### Testing Home Page  <a name='testing-home-page'></a>

##### Not logged in:

Feature | Outcome | Pass/Fail  
--- | --- | ---
Page content | All page content loaded correctly and visible to user | Pass
Sign up here button | clicking button loaded create account form | Pass
Login to your account button | clicking button loaded user login form | Pass

##### Logged in:

Feature | Outcome | Pass/Fail  
--- | --- | ---
Page content | All page content loaded correctly and visible to user | Pass
Log a session button | clicking button loaded new session form | Pass
View sessions button | clicking button loaded view sessions page | Pass
Your recent sessions list | Recent sessions loaded with view session analysis charts button, if no session recorded correct text loaded | Pass
View sessions analysis charts button | Loaded session info page for correct session | Pass

#### Testing Add User Page  <a name='testing-add-user-page'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---
Page content | All page content loaded correctly and visible to user | Pass
Add user form | Form submitted correctly created user in database | Pass
Password check | Password must be correctly entered twice, two different passwords flash error message, length must be greater than 8 | Pass
Username check | Flashed error when tried to use a username which already existed in database | Pass
Date of birth check | Couldn't submit for with date of birth in future | Pass
Height check | Couldn't submit form with unrealistic height like 1cm | Pass
Weight check | Couldn't submit form with unrealistic weight like 1kg | Pass
Complete form | Couldn't submit incomplete form | Pass


#### Testing Login Page  <a name='testing-login-page'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---
Page content | All page content loaded correctly and visible to user | Pass
Login form | Successfully logged user into site | Pass
username field | Incorrect username entered flashed correct error message | Pass
Password field | Incorrect password entered flashed correct error message | Pass


#### Testing Delete Account page   <a name='testing-delete-account-page'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | All page content loaded correctly and visible to user | Pass  
Delete account button | clicking button deleted the user account and logged the user out | Pass  
Confirmation modal | When user clicks delete account confirmation modal launches, no button closes with no action, yes button submits form | Pass
Incorrect password | If incorrect password entered account not deleted and correct flash message displayed | Pass


#### Testing View Sessions Page <a name='testing-view-sessions-page'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | All page content loaded correctly and visible to user | Pass  
View session details link | clicking link loaded correct session details page | Pass  
Delete session button | clicking button deleted the selected session from the session list | Pass  
Delete climb button | Clicking button deleted correct climb | Pass
Edit climb button | Clicking button loaded edit climb page with correct climb details | Pass
View session analysis charts button | Clicking button loaded session info page for correct session | Pass

#### Testing Edit Climb Page  <a name='testing-edit-climb-page'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | All page content loaded correctly and visible to user | Pass  
Get climb details from database | All climb details correctly retrieved from database and filled into form | Pass
Edit climb form submission | correctly updated climb information upon submission | Pass  
Cancel button | clicking button returned user to view sessions page without saving changes | Pass  

#### Testing Record Session Page  <a name='testing-record-session-page'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | All page content loaded correctly and visible to user | Pass  
Record session form submission | correctly recorded new session upon submission | Pass  
Cancel button | clicking button returned user to homepage without saving session | Pass  
Help modal | Modal launched correctly, displayed correct text and close button closed modal | Pass

#### Testing Add Climb Page <a name='testing-add-climb-page'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | All page content loaded correctly and visible to user | Pass  
Add climb form submission | correctly added a new climb upon submission | Pass  
End session button | clicking button took user to view sessions page | Pass  
Help modal | Modal launched correctly, displayed correct text and close button closed modal | Pass
From checks | Couldn't enter negative number for climb length, couldn't submit form without required fields | Pass

#### Testing Session Info Page   <a name='testing-session-info-page'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | All page content loaded correctly and visible to user | Pass  
View climb details link | clicking link displayed correct climb details | Pass  
Back to view sessions button | clicking button returned user to view sessions page | Pass  
Pie chart | Displayed correctly and all interactive features worked as intended | Pass
Scatter chart | Displayed correctly and all interactive features worked as intended | Pass
Climbs completed graph | Displayed correctly and all interactive features worked as intended, didn't display in no climbs completed in session | Pass
Climbs not completed graph | Displayed correctly and all interactive features worked as intended, didn't display in no climbs not completed in session | Pass

#### Testing 404 page   <a name='testing-404-page'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | Custom 404 error page loaded correctly when navigating to a non-existent URL | Pass  
Home page link on 404 page | clicking link successfully redirected user to homepage | Pass  

#### Testing 401 page   <a name='testing-404-page'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | Custom 401 error page loaded correctly when attempting to view page which requires login when user not logged in | Pass  
Home page link on 401 page | clicking link successfully redirected user to homepage | Pass 


### Bugs <a name="bugs"></a>

#### Bug fixes

Fixed bug in which the page would show an error if the user attempted to login with a username not in the database.

Fixed bug in which the confirmation modal buttons did not display the correct styling.

Fixed a bug for deleting climb, the button would always delete the most recent climb not the correct one which the button was loaded next to.

Fixed a bug in which when the edit climb form loaded it did not display the correct grade in the dropdown.

Fixed a bug where users could enter a negative number for the length of climb.

Fixed bug where user could enter a DOB in the future in create user form.

Fixed bug in which if the user had no recent sessions this wasn't communicated to them under the recent session header on homepage.

Fixed bug where if a user tried to create and account and it failed due to duplicate user and/ or email it would still load the login page after form submission, even though it flashed the correct error message and did not create account.

***

### Testing User Stories <a name="testing-user-stories"></a>

#### User Story 1: Logging Climbing Sessions  
*As a user of the site, I want to keep a log of my climbing sessions so that I can track my progress over time.*

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Create new session | User can create and log new climbing sessions via the record Session page | Pass 
Save session data | Session data is saved in the database and is retrievable and can be view in the view sessions and session info pages | Pass
Session info charts | Session info charts allow me to track my performance and compare it to previous levels with the interactive charts | Pass
Display recent sessions | Recent session displays on homepage after logging in | Pass 

#### User Story 2: Climbing Log Details  
*As a user of the site, I want each log to contain details about the different climbs I did in that session so that I can review the information when I choose.*

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Log individual climbs | User can log individual climbs for each session, including difficulty, length, and completion status on log climbs page | Pass 
View logged climbs | All climbs within a session are viewable from the view Sessions page | Pass 
Edit climb details | User can edit logged climbs from the edit climb page | Pass 
Delete climb | User can delete a climb from the session, and confirmation is required to ensure they don't accidentally do so | Pass 

#### User Story 3: Comprehensive Climb Information  
*As a user of the site, I want to store information such as the difficulty, length, name, and whether I completed each climb so that I can have a comprehensive record of my activities.*

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Record climb details | User can log details like difficulty, length, name, and completion status | Pass 
Store climb data | Climb data is saved to the database and retrievable | Pass 
View climb summary | Logged climbs are summarized in both table format for large screens and expandable accordions on small screen sizes | Pass 

#### User Story 4: Visualize Session Data  
*As a user of the site, I want to visualize data about my sessions and climbs using visually pleasing graphs and charts so that I can better understand my progress.*

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Visual charts for sessions | User can view pie chart, bar charts and scatter plot which provide information on different parts of performance | Pass 
Charts design| Visually pleasing charts | Pass 
Interactive graphs | Charts are interactive, allowing the user to toggle climb data visibility in the legends | Pass 

#### User Story 5: Guide Future Climbing  
*As a user of the site, I want to use the information from my logs to guide my future climbing activities so that I can improve and set new goals.*

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Track climb progress  | Users can track session and climb history via graphs to identify improvement areas | Pass 
View past performance | User can analyze past climbs and sessions to guide future climbs and goals | Pass
Decide future training | User can use information to guide future training decisions | Pass

