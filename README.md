
<img src="/static/assets/img/logo_2.png" alt="drawing" width="200"/>



## Stream Three Project: Python and Data Centric Development - Code Institute

This is the second milestone project of my journey as a Software Developer in Code Institute. The goal of this project is to build a full-stack web application that allows users to manage and common dataset about a particular domain.

## Skeleton:

I used **Balsamiq** software to create my initial wireframes, starting with the mobile and desktop design as an overall idea and helping me to make the design responsive afterwards.


[Desktop wireframe](/static/assets/wireframes/MS3_desktop.pdf)

[Tablet wireframe](/static/assets/wireframes/MS3_tablet.pdf)

[Mobile wireframe](/static/assets/wireframes/MS3_mobile.pdf)


## Data model

![data model](/static/assets/img/datamodel.png)

## Code validation
![python validation](/static/assets/code_validation/css_w3c.png)

![jquery validation](/static/assets/code_validation/JQuery_JSHint.png)

![python validation](/static/assets/code_validation/python_pep8.png)

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