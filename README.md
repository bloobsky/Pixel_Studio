>Version Control
Available in VERSION.md file

Project Info

Pixel Studio is a fully functional business site that enables user to browse through our offer regarding, web, design, print, programming and other IT related businesses.
It enables user ability to login and eventually buy some services (just like any popular webstore)

UX


Testing
Website was tested using 3 devices: Desktop PC, Tablet (Samsung a300) and smartphone (Samsung s8+ EDGE). Website was also tested using Inspect function in Google Chrome HTML and CSS Validator were also used in place.
Testing write-up
 

Deployement
Using Git Command Line to upload to a repository
Type in terminal these commands:
git init to initialize a new repository
git add README.md to add README.md file to repository
git commit -m "Initial commit" to add a message for first commitement
. git remote add origin https://github.com/bloobsky/your_repository_name.git to assign repository
git push -u origin master to upload files to the repository


For heroku development type in terminal these commands

heroku login "then entry your login and password"
pip3 freeze --local > requirements.txt "these is essential for heroku to word"
echo web: python app.py > Procfilecreate a Procfile with "web: python app.py"
heroku git:clone -a [repository_name]
git push heroku master

Your website is available now @ https://repository_name.herokuapp.com

Project is deployed @ GitHub and Heroku
Github was used in deployement process as it is integrated, simple and ther is no need to use additional services. It also containt Version Control and everything is uploaded using terminal commands (git)
How it is done ?
Open www.github.com. Login with your credentials On the Navigation Bar in the repository you would like to deploy look for 'settings' link. Scroll down the page and look for 'GitHub Pages' Under the source section select 'master branch' option Message should appear 'Your site is ready to be published at https://$YourLogin.github.io/$RepositoryName/ Your website is deployed now.

Technologies,Programming Languages and APIs
HTML5, CSS, Materialize, JavaScript, jQuery, Python, Django, MongoDB, GoogleFonts API: emailJS and Google Maps API

Features to be implemented


Media
Screenshots for testing were done by using SnippingTool @ MS Windows<br>
PixelStudio logo was created in Adobe Illustrator. <br>
Icons used in Project are part of Materialize (www.materialize.com) <br>

Acknowledgements
I received inspiration from CodeInstitute (www.codeinstitute.net) <br>
Privacy Policy was generated using www.iubenda.com MongoDB Atlas - for possibility to create a free database Gitpod was used to entirely written all the code for the proposed project.