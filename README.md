<h3>Version Control</h3>
Available in VERSION.md file

<h3>Project Info</h3>
<p>Pixel Studio is a fully functional business site that enables user to browse through our offer regarding, web, design, print, programming and other IT related businesses.
It enables user ability to login and eventually buy some services (just like any popular webstore). It also provides order history for user.</p>

<h3>UX</h3>
Page is divided into 3 subsections<br>
1: Top Navigation Bar - > contain search bar, my account info and shopping cart.<br>
1.1 -Pixel Studio with a link to homepage<br>
1.2 - Services which gives a list of all services (Web development, Graphic Desig, Print, Hosting & Domains)<br>
1.3 - Web development (Starter, Functional, Blog, E-commerce)
1.4 - Graphic Design (Logo & Logotypes, Business Cards, Posters, Flyers & Leaflets, Signs & Banners, Invitationas, Labels & Stickers)
1.5 - Print<br>
1.6 - Hosting & Domains <br>
1.7 - About - short description about the business<br>
1.8 - Frequently Asking Questions - help about most of the things<br>
<br><br>
2. Footer - at the bottom of the page containing info with address and ><br>
2.1 - Privacy Policy -standard procedure how do We handling your data<br>
2.2 - Testimonials - some information about recent jobs<br>
2.3 - Directions - google map with location of our office<br>
2.4 - Contact Us - form provided to make it easier contacting with us <br>
2.5 - Social Media Links - Instagram, LinkedIn, Facebook<br>

<h3>User Stories</h3>

<p>As a <strong>Customer</strong> I would like to search through available product so I can find what I desire.<br>
As a <strong>Customer</strong> I would like to see each individual service so I can identify price.<br>
As a <strong>Customer</strong> I would like to see my shopping cart so I can track my potential expenses<br>
As a <strong>Customer</strong> I would like to specify a category for desired service so I can find perfect match<br>
As a <strong>Customer</strong> I would like to have a help link available with answers to the most commons sections<br>
As a <strong>Customer</strong> I would like to see what I have searched for and the number of results so I can quickly decide if any product suits me <br>
As a <strong>Customer</strong> I would like to have a order history so I can track my spendings<br>
</p><br>
<p>As a <strong>Site User</strong> I would like to have an option to login in order to have my details saved<br>
As a <strong>Site User</strong> I would like to have all information presented nicely so I can easily find what I am looking for<br>
</p><br>
<p>
As a <strong>Site Owner</strong> I would like to have ability to login so I can see all technical website info<br>
As a <strong>Site Owner</strong> I would like to have ability to add services into my collection so I can expand my bussiness<br>
As a <strong>Site Owner</strong> I would like to add more information for FAQ section so the users can find easier what they are looking for<br>
As a <strong>Site Owner</strong> I would like to see the users order history so I can track it and see for any possible failures<br>
<br>


<h3>Testing</h3>
<p>Website was tested using 3 devices: Desktop PC, Tablet (Samsung a300) and smartphone (Samsung s8+ EDGE).<br>
Website was also tested using Inspect function in Google Chrome.<br> 
HTML and CSS Validator were also used in place.<br></p>

<h3>Testing write-up</h3>
 

<h3>Deployement</h3>
<p>Using Git Command Line to upload to a repository
Type in terminal these commands:<br>
git init to initialize a new repository<br>
git add README.md to add README.md file to repository<br>
git commit -m "Initial commit" to add a message for first commitement<br>
. git remote add origin https://github.com/bloobsky/your_repository_name.git to assign repository<br>
git push -u origin master to upload files to the repository</p>


<h4>For heroku development type in terminal these commands</h4>

<p>heroku login "then entry your login and password"
pip3 freeze --local > requirements.txt "these is essential for heroku to work"
echo web: python app.py > Procfilecreate a Procfile with "web: python app.py"
heroku git:clone -a [repository_name]
git push heroku master</p>

<h4>Your website is available now @ https://repository_name.herokuapp.com</h4>

<h3>Project is deployed @ GitHub and Heroku</h3>
Github was used in deployement process as it is integrated, simple and ther is no need to use additional services. It also containt Version Control and everything is uploaded using terminal commands (git)
How it is done ?
Open www.github.com. Login with your credentials On the Navigation Bar in the repository you would like to deploy look for 'settings' link. Scroll down the page and look for 'GitHub Pages' Under the source section select 'master branch' option Message should appear 'Your site is ready to be published at https://$YourLogin.github.io/$RepositoryName/ Your website is deployed now.

<h3>Technologies,Programming Languages and APIs</h3>
<ul>
<li>HTML5</li>
<li>CSS</li>
<li>Bootstrap4</li>
<li>JavaScript</li>
<li>jQuery</li>
<li>Python3</li>
<li>Django with (Allauth, CookieLaw, CrispyForms, ClassyTags, Pillow, Stripe)</li>
<li>GoogleFonts</li>
<li>Google Maps API</li>
</ul>

<h3>Features to be implemented</h3>
<p>No features planned to be implemented at this stage. If you have any ideas how the project can be expanded feel free to contribute</p>

<h3>Media</h3>
Screenshots for testing were done by using SnippingTool @ MS Windows<br>
PixelStudio logo was created in Adobe Illustrator. <br>
Icons used in Project are part of FontAwesome (www.fontawesome.com) <br>

<h3>Acknowledgements</h3>
I received inspiration from CodeInstitute (www.codeinstitute.net) <br>
Privacy Policy was generated using www.iubenda.com<br> 
Gitpod was used to entirely written all the code for the proposed project.<br>