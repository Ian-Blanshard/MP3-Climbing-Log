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

#### html validation <a name="css-validation"></a>

![](/climbing_log/static/images/html_validation.jpg)

![](/climbing_log/static/images/html_validation1.jpg)

![](/climbing_log/static/images/html_validation2.jpg)

![](/climbing_log/static/images/html_validation_pass.jpg)

#### html validation <a name="html-validation"></a>

#### JavaScript validation <a name="javascript-validation"></a>

JSHint JavaScript validator highlighted a number of unnecessary semicolons in my javscript

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

***

### Manual testing <a name="manual-testing"></a>

#### Testing across different devices and browsers  <a name="testing-devices-browsers"></a>

Browser | Outcome | Pass/Fail  
--- | --- | ---
Google Chrome | - | -
Microsoft Edge | - | -
Mozilla Firefox | - | -
Apple Safari | - | -

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
Your recent sessions list | Recent sessions loaded with view session analysis charts button | Pass
View sessions analysis charts button | Loaded session info page for correct session | Pass

#### Testing Add User Page  <a name='testing-add-user-page'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---
Page content | All page content loaded correctly and visible to user | Pass

#### Testing Login Page  <a name='testing-login-page'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---
Page content | All page content loaded correctly and visible to user | Pass

#### Testing Delete Account page   <a name='testing-delete-account-page'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | All page content loaded correctly and visible to user | Pass  
Delete account button | clicking button deleted the user account and logged the user out | Pass  

#### Testing View Sessions Page <a name='testing-view-sessions-page'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | All page content loaded correctly and visible to user | Pass  
View session details link | clicking link loaded correct session details page | Pass  
Delete session button | clicking button deleted the selected session from the session list | Pass  

#### Testing Edit Climb Page  <a name='testing-edit-climb-page'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | All page content loaded correctly and visible to user | Pass  
Edit climb form submission | correctly updated climb information upon submission | Pass  
Cancel button | clicking button returned user to view sessions page without saving changes | Pass  

#### Testing Record Session Page  <a name='testing-record-session-page'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | All page content loaded correctly and visible to user | Pass  
Record session form submission | correctly recorded new session upon submission | Pass  
Cancel button | clicking button returned user to homepage without saving session | Pass  

#### Testing Add Climb Page <a name='testing-add-climb-page'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | All page content loaded correctly and visible to user | Pass  
Add climb form submission | correctly added a new climb upon submission | Pass  
Cancel button | clicking button returned user to view sessions page without saving climb | Pass  

#### Testing Session Info Page   <a name='testing-session-info-page'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | All page content loaded correctly and visible to user | Pass  
View climb details link | clicking link displayed correct climb details | Pass  
Back to view sessions button | clicking button returned user to view sessions page | Pass  

#### Testing 404 page   <a name='testing-404-page'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---  
Page content | Custom 404 error page loaded correctly when navigating to a non-existent URL | Pass  
Home page link on 404 page | clicking link successfully redirected user to homepage | Pass  


### Bugs <a name="bugs"></a>

#### Bug fix

Fix the bug throws error when trying to log in with a username that doesn't exist in database

incorrect button styling delete climb modal sessions page

bug fix delete mst recent session/ climb insteasd of one that butti was for

***

### Testing User Stories <a name="testing-user-stories"></a>

#### User Story 1: Logging Climbing Sessions  
*As a user of the site, I want to keep a log of my climbing sessions so that I can track my progress over time.*

| Feature              | Outcome                                                                            | Pass/Fail |
|----------------------|------------------------------------------------------------------------------------|-----------|
| Create new session    | User can create and log new climbing sessions via the "Record Session Page"        | Pass      |
| Save session data     | Session data is saved in the database and is retrievable from the "View Sessions Page" | Pass      |
| End session           | User can end session and receive a flash message indicating the session has been logged | Pass      |
| Display recent sessions | Recent session displays on homepage after logging in                             | Pass      |

#### User Story 2: Climbing Log Details  
*As a user of the site, I want each log to contain details about the different climbs I did in that session so that I can review my performance for each climb.*

| Feature              | Outcome                                                                            | Pass/Fail |
|----------------------|------------------------------------------------------------------------------------|-----------|
| Log individual climbs | User can log individual climbs for each session, including difficulty, length, and completion status | Pass      |
| View logged climbs    | All climbs within a session are viewable from the "View Sessions Page"             | Pass      |
| Edit climb details    | User can edit logged climbs from the "Edit Climb Page"                             | Pass      |
| Delete climb          | User can delete a climb from the session, and confirmation is required             | Pass      |

#### User Story 3: Comprehensive Climb Information  
*As a user of the site, I want to store information such as the difficulty, length, name, and whether I completed each climb so that I can have a comprehensive record of my activities.*

| Feature              | Outcome                                                                            | Pass/Fail |
|----------------------|------------------------------------------------------------------------------------|-----------|
| Record climb details  | User can log details like difficulty, length, name, and completion status on the "Add Climb Page" | Pass      |
| Store climb data      | Climb data is saved to the database and retrievable via session overview            | Pass      |
| View climb summary    | Logged climbs are summarized in both table format and expandable accordions on small screen sizes | Pass      |

#### User Story 4: Visualize Session Data  
*As a user of the site, I want to visualize data about my sessions and climbs using visually pleasing graphs and charts so that I can better understand my progress.*

| Feature              | Outcome                                                                            | Pass/Fail |
|----------------------|------------------------------------------------------------------------------------|-----------|
| Visual charts for sessions | User can view pie chart and scatter plot for climb completions and difficulties | Pass      |
| Bar charts for climbs | Bar charts display climb performance by difficulty and completion status on the "Session Info Page" | Pass      |
| Interactive graphs    | Charts are interactive, allowing the user to toggle climb data visibility in the legends | Pass      |

#### User Story 5: Guide Future Climbing  
*As a user of the site, I want to use the information from my logs to guide my future climbing activities so that I can improve and set new goals.*

| Feature              | Outcome                                                                            | Pass/Fail |
|----------------------|------------------------------------------------------------------------------------|-----------|
| Track climb progress  | Users can track session and climb history via graphs to identify improvement areas | Pass      |
| View past performance | User can analyze past climbs and sessions to guide future climbs and goals         | Pass      |
| Session comparison    | Future feature planned to compare sessions by location, visible on "Record Session Page" | Planned   |
