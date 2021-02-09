
<img src="/static/assets/img/logo_2.png" alt="drawing" width="200"/>



## Stream Three Project: Python and Data Centric Development - Code Institute

This is the third milestone project of my journey as a Software Developer in Code Institute.
 The goal of this project is to build a full-stack web application that allows
  users to manage a common dataset about a particular domain.
As the ultimate goal, **JournalClub** aims to be an online journal club platform for 
collaboration and discussion for research minds of academia. Journal Clubs 
are essential research & academic activity at academic organizations. Therefore, **JournalClub** will provide
an organization solution to a real world need. The main feature will be the
journal club organisation. It will provide literature reading and mining tool.
The Journal Club cycle would ideally include the following stages:

1. Schedule
2. Critical reading
3. Critical appraise
4. Live online presentation
5. Broadcasting
6. Realtime discussion
7. Archive

As the first stage release of this application, the minimal features to include will the CRUD (Create, Read, Update and Delete) 
operations on a back-end database.

## Live website

The deployed website can be found [here](https://journalclub.herokuapp.com/).

![responsive mockups](/static/assets/img/demo.png)

## User Experience Design (UXD)
 
## User stories:

Before starting the planning of the project I started by identifying initial
need that will cover the minimal features of the first release of the application.
In the following the user stories are presented, and in each case the corresponding CRUD
operation is highlighted.

#### As a user:

- I want to signup to JournalClub so that I can contribute journal articles of my interest (**CREATE**)
- I want to be able to modify my personal information on my profile (**UPDATE**)
- I want to view all journal articles suggested by other fellow researchers.
(**INDEX**)
- I want to create a journal list to be shared with my fellows. (**CREATE**)
- I want to access all details of the article journal (full citation reference).
(**READ**)
- I want to delete a journal club event created by me. (**DESTROY**)
- I want to edit a journal club event created by me. (**EDIT/UPDATE**)
- I want to comment on a particular journal article suggested by me or
other fellows.(**COMMENTS/CREATE**)
- I want to delete my comments on a particular journal articule.
(**DESTROY/DELETE**)


Beside the provided solution to the user of the application, it will also provide
a value to the owner of the application:

#### As a site owner:

-  I want to be contacted by users in order to organise meet-ups and
networking activities (**VALUE PROVIDED**).

## Strategy:

The goal of this project is to get the attention of fellows researchers,
and encourage discussions and collaboration (networking).


### Strategy Table

The strategy table illustrates the trade-off between importance and viability.
 As we move onto Scope soon, it is clear that this project requires different 
 phases to implement the exhaustive list of features - it is an on-going process! 

Opportunity/Problem/Feature| Importance| Viability
------------ | -------------------------|---------
Create/Schedule a Journal Club | 5|5
Add comments/description to Journal Club event | 5 | 5
Delete a Journal Club event | 5 | 5
Sign Up/ Sign In | 5 | 5
Live Online Presentation | 4 | 2
Broadcasting | 4 | 1
Real time discussion | 5 | 1
User comments/reviews | 5 | 5
Total| 38 | 29

## Scope:

As derived from the strategy table (Importance < Viability), I am unable to put in place everything. As a result, I identified what a minimum viable product is. This means **Stage** 1 should be enough to satisfy users. I will then have the opportunity to get feedback for future developments.

Please find below the planned releases:

## Stage 1 (current release)

As the initial stage of this project:

- Sign Up and Sign In functionalities.

- Create Journal Club event.

- Edit and Delete Journal Club functionalities.

- Subcription for newsletters.

- Call on Google maps API.

- Journal Club Blog (all users contributions).



## Stage 2 (Future release)

As future capabilities:

- Live online presentation.

- Broadcasting.

- Realtime discussion.

- Archive.

## Structure:

As it can be noticed in the initial wireframes, I decided 
to organize the website in different pages. The number of pages available will vary dependending
on whether the user is Logged In or not.

- **Base template**: I used a base template (**base.html**) what serves a the main structure of
all pages. Regardless the location on the page users will be able to see the following features:

    - **Navegation bar and Logo on the top of the page**, it will collapse to a dropdown menu in tablet and 
      mobile phones sizes.

    - **About Section before footer**, it will contain a description of the website (purpose), Contact Info and Google Map with locations.

    - **Footer** indicating copyrights.

- **Home Page** organized in Sections: calls to actions, features highlights and subscription to newsletters.

- **Sign In/Sign Up/Create/Edit pages** will contains a main division with a form.

- **Dashboard** will be organized in cards containing different user information and 
  call to actions.

- **Events page** will be displayed once the user signed in, and it will contain a 
  accordion with list of all journal arcticles. Edit/Delete buttons will be available 
  for those articles belonging to the current user.


## Skeleton:

I used **Balsamiq** software to create my initial wireframes, starting with the mobile and desktop design as an overall idea and helping me to make the design responsive afterwards.
The deployed application slightly differs from the initial
wireframes as some of the features were evolving as I was working on the development.

[Desktop wireframe](/static/assets/wireframes/MS3_desktop.pdf)

[Tablet wireframe](/static/assets/wireframes/MS3_tablet.pdf)

[Mobile wireframe](/static/assets/wireframes/MS3_mobile.pdf)


## Surface:

- Appealing pictures were chosen for backgrounds, in order to make compatible with the purpose of the website (obtained from [Pixabay](https://pixabay.com)).

- Google font "Lato" is used throughout the site. 

- The CSS Family Grey   (#606060) color Scheme was chosen dashboard card background.

- The CSS Family White  color Scheme was chosen dashboard card text.

- In Sections were a background image was not set, the CSS family background-color #fff was used.

- Buttons in SignUp/SignIn forms were consistently set in Blue.

- Buttons in call for action in home page forms were consistently set in Green.

- Navegation bar item are in Orange (#f4623a), while a Grey background is presented in dropdown menu in mobile devices sizes.

- All remaining text is constantly in CSS family #6c757d.

## Data Modeling (MongoDB Atlas)

Keeping in mind that the main challenge in data modeling is balancing the needs
of the application, the performance characteristics of the database engine, 
and the data retrieval patterns. I adopted the the philosophy that
while designing my data model I would consider the application usage of the data
(i.e. queries, updates, and processing of the data) as well as the inherent 
structure of the data itself. The database engine used in this project is MongoBD Atlas.
MongoDB is a source-available cross-platform document-oriented database program. Classified as a NoSQL database program, 
MongoDB uses JSON-like documents with optional schemas. 

The **JournalClub** single collection hosted in MongoDB is conformed by
four documents: **users**, **add_article**, **field_reasearch** and **subscribers**. Each of
these documents contains unique attributes, and relationships between 
documents are also present. In the following diagram my data model is shown. Note
that relationships between 3 of the documents are exist, while the **subscribers**
document is not related to the others.


![data model](/static/assets/img/datamodel.png)

## Code style and reusability (Object-oriented Programming in Python)

During the writing and development of the Python code in this project, I adopted
the object oriented programming (OOP) paradigm. Using OOP improves 
software-development productivity as it is
modular by providing separation of duties in object-based program development.
It is also extensible, as objects can be extended to include new attributes and
behaviors. Objects can also be reused within an across applications. Because of
these three factors – modularity, extensibility, and reusability – OOP provides
improved software-development productivity over traditional
procedure-based programming techniques. OOP also improves software 
maintainability.

The **app.py** file contains the following classes and methods:


Class | Methods
------------ | -------------------------
User | start_session, signup, signout, login, update
CreateNewJC | submission, delete, edition
Subscription | subscriber

## Defensive programming

Given the nature of this application, in which users will be constantly adding
and deleting information. I have implemented defensive programming throughout
the site. In the following screenshots of selected different situations are shown. 

- All input data in forms is validated (e.g. presence check, format check, range check)

Presence check:
![Empty field](/static/assets/code_validation/validation1.png)

Format validation:
![Incorrect format](/static/assets/code_validation/validation2.png)


- All internal errors are handled gracefully and users are notified of the problem where
appropriate.

Incorrect user credentials:
![Incorrect format](/static/assets/code_validation/validation2.png)

Check for existing user:
![Incorrect format](/static/assets/code_validation/validation2.png)


- Before any modification of data modal are displayed in order to the user to confirm or cancel 
the action.

Ask for confirmation:
![Incorrect format](/static/assets/code_validation/validation5.png)

## Encountered bugs (fixed)

Throughout the development process I encountered different bugs/issues. The main 
tools that helped me discover and explore them was the command line interface and the
Google Development Tool. In the following I will discribe some of the most important bugs
I found and the corresponding solution I implemented:

- **SignIn Failed because of case sensitive authentication**: After implementing
the SignIn features I found a problem related with the case sensitivity of the form 
field. I have fixed by using the lowercase method on username field before searching for it
the database: **"username": request.form.get('username').lower()**.

- **Responsiveness of height of section with dynamic content**: In the website there are few section in which 
the content increase depending on the number of entries in the database. For instance the carousel in **events.html**,
for which the more articles are available the section height should increase. I have fixed that issue by setting **min-height** css property
instead of a fixed **height**. That will able the section to adjust to its inner content.

- **Subscription to newsletter form**: after implementing the Subscription form in **home.html**, I found that
empty field were allowed to be submitted. It should not happen!.  I fixed it by setting presence check and required validation in the 
corresponding form.

- **Lastest added article in home.html**: I found that Jinja was given errors when trying to render
journal articles in home.html in the case that the corresponding list was empty. I fixed that problem by setting 
the statement: **{% if journals is defined and journals[0] is defined %}** so that, the html block would be ignored 
in case of not articles available in the database.

- **Logo image and google map not shown in dynamic pages**: I found that images and google maps in base.html template were not being
in dynamic pages like **/edit/<event_id>**. It had to be fixed my making sure that logo image and javascript maps script were defined as static file
and using the **url_for** jinja convention.

- **Google maps not shown in Heroku**: After deploying the app to Heroku I found out that Google Maps were not displayed. By inspecting the Google Dev Tool Console,
I noticed that they were blocked. I figured out that I had to load the map script in the same page were it was called (**base.html**).
Now, it is working but I would like to be able to include the maps JS file in static/assets/js folder!.

- **Security breaches in connection/authentication**: Initially I used the email account and password as authentication 
field in SignIn form, and I kept getting the message "A data breach on a site or app exposed your password" on Chrome and Firefox browsers.
The fix for that was using **username/password** combination instead.


## Testing

## Manual testing of the deployed product
The testing of the website, both in development and as a 
finished product has been done through manual testing. 
I have decided to present the manual tests conducted in a separated
file [Manual Tests](/ManualTesting/testing.md).


## Responsive design

The deployed application is fully responsive. I tested 
my site on Safari, Firefox, Opera and Google Chrome. The
 mobile and desktop version of the website looks very good and it is working as desired.

I used the chrome DevTools to test that the website is fully responsive. I tested the following
devices (mobile and tablet sizes):

- Moto G4.

- Galaxy S5.

- Galaxy S9 (my own device).

- iPhone 5/SE, iPhone 6/7/8, iPhone 6/7/8 Plus and  iPhone X.

- iPad and iPad Pro.

- Surface Duo.

I also used **Am I Responsive?** to check my responsive design and to create the final product screenshots presented at the beginning.


## Code validation

I used **W3C** to check my HTML and CSS files. I used JSHint validator to check my Javascript files. I used **PEP8online** to validate Python files.
Below screenshots of the validation results are exhibited.

## HMTL validation 
All html pages passed the **W3C** validator, except for warnings/errors related to the Jinja templating formatting. A selection of validation outputs is shown as follows.
A complete selection of screenshots for every html page can be found at [HTML validation](/static/assets/code_validation/)

Base template:

![Base template validation](/static/assets/code_validation/base.png)


Home page:

![Home page validation](/static/assets/code_validation/home.png)

Signin page:

![Signin page validation](/static/assets/code_validation/signin.png)

Signup page:

![Signout page validation](/static/assets/code_validation/signup.png)



## CSS validation
![python validation](/static/assets/code_validation/css_w3c.png)

## JavaScript validation
![jquery validation](/static/assets/code_validation/JQuery_JSHint.png)

## Python validation
![python validation](/static/assets/code_validation/python_pep8.png)

## Technologies Used

- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
    - The project uses **HTML** as building block.
- [CSS3](https://www.w3.org/Style/CSS/Overview.en.html)
    - The project uses **Cascading Style Sheets (CSS)** for adding style to the website.
- [JS](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
    - The project uses **JavaScript (JS)** for adding interactivity to the website.
- [Python](https://www.python.org/)
    -  The project uses **Python3** for adding developing the backend functionality of this project.
- [Flask](https://www.python.org/)
    -  I used **Flask** micro web Python framework.
- [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)
    - I used **Jinja2** as the HTML templating language for Python.

## Libraries and Tools Used 

- [Bootstrap (4.5.2)](https://getbootstrap.com/)
    - The project uses **Bootstrap** to design and customize responsive mobile-first sites.
- [JQuery (3.5.1)](https://jquery.com/)
    - This project uses **JQuery** JavaScript library, to manupulate 
    the HTML document (DOM API) and add interactivity in a much simpler way. 
- [Google Maps JavaScript](https://developers.google.com/maps/documentation/javascript/overview)
    - This project uses the Google Maps JavaScript API.
- [Balsamiq](https://balsamiq.com/wireframes/)
    - The project uses **Balsamiq** as wireframing tool.
- [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools/)
    - I use **Chrome DevTools** to inspect and test styling and responsive desing during my development process.
- [W3C](https://validator.w3.org)
    - I use **W3C** to check the HTML and CSS files.
- [JSHint](https://jshint.com/)
    - I use **JSHint** to check the JS files.
- [PEP8](http://pep8online.com/)
    - I use **PEP8 online** to check and validate the Python script files.
- [AmIResponsive](http://ami.responsivedesign.is)
    - I use **Am I Responsive?** to check my responsive design and take screenshots of the deployed website.
- [Fontawesome](https://fontawesome.com)
    - This project uses **FontAwesome** for including vector icons and social logos.
- [GoogleFonts](https://fonts.google.com)
    - This project uses **GoogleFonts** to import the font styles.
- [GitHub](https://github.com)
    - I used **GitHub** as my project repository.
- [GitPod](https://www.gitpod.io)
    - I used **GitPod** as the cloud-based development environment to write my code.
- [Heroku](https://www.heroku.com)
    - I used **Heroku** to deploy my project.
- [MongoDB](https://www.mongodb.com/2)
    - I used **MongoDB Atlas** to create and manage the non-relational database in this project.

## Deployment

**This procedure was followed to deploy Journal Club**
For step 1 and 2, make sure you are in the root directory of your project. Don't forget to push the two new files to github before proceeding with the deployment.

1. Create a requirements file. In the command line interface (cli)  it can be done by running the following command:
`pip3 freeze --local > requirements.txt`
2. Create a Procfile. In the cli it can be done by running the following command: `echo web: python app.py > Procfile` "Note: make sure you have an empty new line after app.py"
3. Log in to Heroku, click "New" > "Create new app"
4. Give the project a unique name, choose region and click "Create app".
5. Scroll down to "deployment method"-section. Choose "Github" for automatic deployment.
6. From the inputs below, make sure your github user is selected, and then enter the name for your repo. Click "search". When it finds the repo, click the "connect" button. 
7. Scroll back up and click "settings". Scroll down and click "Reveal config vars". Set up your variables for IP, PORT, SECRET_KEY, MONGO_URI and MONGODB_NAME.
8. Scroll back up and click "Deploy". Scroll down and click "Enable automatic deployment". 
9. Just beneath, click "Deploy branch". Heroku will now start building the app. When the build is complete, click "view app" to open it.

**To clone the repository, follow these instructions:**

1. Navigate to the [repository](https://github.com/jdquerales/MilestoneProject_3)
2. Click **Clone or download**
3. Copy the url from the **Clone or download** dropdown.
4. In cli, navigate to the folder where you want to clone the repository.
5. Type *git clone*, and then paste the URL you copied in Step 3.
6. Press Enter

*Note: You will have to install all the dependencies from [requirements](https://github.com/jdquerales/MilestoneProject_3/blob/master/requirements.txt) for the app to work. In the cli, you can run the command* 

`pip install -r requirements.txt`

*You will also have to set up an* `env.py` *file in the root directory of your project, and set up variables for IP, PORT, SECRET_KEY, MONGU_URI and MONGODB_NAME. In addition, you will have to setup a new collection and databases for the project in mongoDB.*

For more information, visit [Cloning a repository](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/cloning-a-repository)
on github.

## Credits

### Authentication features
- I used the authentication features from Code Institute walkthrough TaskManager project.
My own implementation can be found at: (https://github.com/jdquerales/flask-task-manager-project).

- For implementing the authentication features (SigIn/SignUp forms) I followed along tutorials 
by Luke Peters at Youtube (https://www.youtube.com/watch?v=w1STSSumoVk&t=153s).

### Bootstrap CSS template
- I used a Bootstrap template from (https://startbootstrap.com/themes).
I used the **creative** template, which can be found at (https://github.com/startbootstrap/startbootstrap-creative)

### Media
- The photos used in portfolio section were obtained from [Pixabay](https://pixabay.com).
- The logo of this project was created on (https://hatchful.shopify.com/).


### Acknowledgements

- I would like to thank my mentor Dick Vlaanderen for his support and helpful suggestions.

- I would like to thank my friends Juan V. Guerrero and Manuel Odelli for testing my app and providing 
useful feedback on encountered bugs/issues.