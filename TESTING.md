  
  
  * [Bugs](#bugs)
  * [Code Validation](#code-validation)
    * [CSS code validation](#css-code-validation)
    * [HTML code validation](#html-code-validation)
  * [Lighthouse Testing](#lighthouse-testing)
  * [Manual Testing](#manual-testing)
    * [Testing across different devices and browsers](#testing-across-different-devices-and-browsers)
  * [Testing Stories](#testing-stories)



#### html validation

![](/climbing_log/static/images/html_validation.jpg)

![](/climbing_log/static/images/html_validation1.jpg)

![](/climbing_log/static/images/html_validation2.jpg)

![](/climbing_log/static/images/html_validation_pass.jpg)

#### JavaScript validation

JSHint JavaScript validator highlighted a number of unnecessary semicolons in my javscript

![JavaScript validation](/climbing_log/static/images/javascript_validation.jpg)

After removing this my script.js file passed valiation with no errors.

![JavaScript validation pass](/climbing_log/static/images/javascript_validation_pass.jpg)

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



#### Testing   <a name='testing-'></a>

Feature | Outcome | Pass/Fail  
--- | --- | ---






### Bugs <a name="bugs"></a>

#### Bug fix

Fix the bug throws error when trying to log in with a username that doesn't exist in database

incorrect button styling delete climb modal sessions page



url(/static/images/climbing.jpg)