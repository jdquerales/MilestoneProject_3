
<img src="/static/assets/img/logo_2.png" alt="drawing" width="200"/>



## Stream Three Project: Python and Data Centric Development - Code Institute

This is the second milestone project of my journey as a Software Developer in Code Institute. The goal of this project is to build a full-stack web application that allows users to manage and common dataset about a particular domain.

## Data model

![data model](/static/assets/img/datamodel.png)

## Code validation
![python validation](/static/assets/code_validation/css_w3c.png)

![python validation](/static/assets/code_validation/python_pep8.png)


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