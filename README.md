# KayTea Art

## Full Stack Development - Milestone Project

[View the Live Site here.](https://the-book-bar.herokuapp.com/)

![logo](assets/images/readmeFiles/readmeLogo.png) 

![Generated from Am I Responsive](assets/images/readmeFiles/TheBookbar.jpg)


The Kaytea Art webshop was designed, built and deployed by Emma Harte as her final milestone project for the Code Institute Full Stack Web Development diploma.
The webstore was created to replace an existing Etsy account, allowing for a fully customizated shopping experience. 
This space is all about art. Enter the home of the artist, browse her online portfolio or even order your own customised piece. 

In this project, full CRUD functionality is present. 
Security features are also present. Such include user permissions for the 'admin' user and safe storage of passwords and sensitive-security information.

----------------------------

## Contents
1. [UX](#ux)
      - [Strategy](#strategy)
      - [User Stories](#user-stories)
        - [Visitor Stories](#visitor-stories)
        - [Business Stories](#business-stories)
    - [Project Scope](#project-scope)
      - [In Scope](#in-scope)
      - [Out of Scope](#out-of-scope)
    - [Wireframes](#wireframes)
    - [Design](#design)
      - [User journey](#user-journey)
      - [Typography](#typography)
      - [Color Scheme](#color-scheme)

2. [Features](#features)
    - [Existing Features](#existing-features)
    - [Features Left to Implement](#features-left-to-implement)

3. [Information Architecture](#information-architecture)
    - [Database information](#database-information)
    - [Datatypes](#datatypes)
    - [Collections information](#collections-information)

4. [Technologies Used](#technologies-used)
    - [Database](#database) 
    - [Languages](#languages)
    - [Libraries](#libraries)
    - [Tools](#tools)
    - [Deployment](#deployment-heroku)

5. [Testing](https://github.com/emmahartedev/The-Book-bar/blob/master/testing.md)
    
6. [Deployment](#deployment)
    - [Local Deployment](#local-deployment)
    - [Heroku Deployment](#heroku-deployment)

7. [Credits](#credits "goto credits")
    - [Content](#content "goto Content")
    - [Code](#code "goto code")
    - [Media](#media "goto media")
    - [Acknowledgments](#acknowledgments "goto acknowledgments")

----------------------------

## UX

### Strategy

**Target Audience:**
* People who are interested in wildlife, plant and animal art.
* Pet owners, interested in pet comissions.
* People looking for unique art at an affordable price.
* People looking for unique gift ideas.

**Importance v Feasability**
* This study was carried out to investigating the in-scope features for this release. 
* The graphic below showcases the results.

![ivf](assets/images/readmeFiles/ivf.jpg) 

### User Stories

#### Visitor stories:
**As a visitor of the website I expect/want/need:**

**Browsing**
1. To be able to browse the website easily without feeling confused or overwhelmed. It should have a easy-to-follow layout on all device sizes.
2. To be able to search for products by text, so that I can find something specific.
3. To browse orginal artwork, prints and gifts, as these are the main categories of an artshop which I would expect to see. 
4. To be able to filter by price within cargeory pages so that I can find a product to suit my budget.
5. To see the image, media used and canvas size of each product. This information is vital to me.
6. To be able to read product reviews as this helps me to decide on the quality and level of service delivered by the company.
7. To request a quote for a pet commission so that I can decide myself whether this is something I would like to purchase.
8. To receive feedback after I interact with the website so that I am aware if the interaction has or has not been a success.
9. To learn more about the artist and the process behind the creations. As a supporter of small businessess, I like to feel a connection to the business owner.

**Shopping**
1. To know that the payment process is secure as I only shop on trustworthy sites.
2. To be able to navigate to my shopping card easily so that I can quickly checkout.
3. To be able to add, edit or delete items or item quantities from my shopping cart so that I can easily modify my choices.
4. To know that the stock levels on products are accurate so that I know shipping delays won't occur. 
5. To receive an email after I submit an order so that I am aware the interaction had been a success.
6. my shipping details should autofill if I am logged in so that I can quickly checkout.

**Customer care**
1. To be able to set up an account, so that I can login on return and view my data.
2. To be able to contact the shop owner easily in case I have a question related to my order.
3. To see a summary of my order after I make a purchase so that I can review the details.
4. To see a list of my order history so that I can check up on my recent activity. 
5. To have the choice to reset my account password in case I forget it.
6. To be able to update my account details in case a change is required.
7. To be able to connect to the company owner on social media channels so that I can keep up-to-date. 


#### Business stories:
**As the website owner**:
**As a superuser of the website I expect/want/need:**

**General**
1. Build a beautiful, easy-to-use, trustworthy website so that I can build brand awareness and sell artwork.
2. To be able to view customer/order/product data so that I easily pull up information if required. 

**Website admin**
1. To be able to add/edit and delete products on the website so that I can keep the information up-to-date.
2. To be able to add/edit and delete gallery images on the website so that I can keep the page fresh.

**Online shop admin**
1. To receive order notifications so that I begin preparing these.
2. To be able to issue refunds in case required.
3. To be able to provide a commision quote based on canvas size and number of pets. This would help to inform the user of the price before purchasing. 
4. To have the choice to accept or decline a comission request. I would need to access each request to see if it is feasible. 

### Project Scope
As part of the 5 plane investigation, the project scope was defined.
During this process, the functional and content requirements were examined.
In considering the functional requirements, each problem was examined to find a best-fit solution.
In considering the content requirements, the following were questioned: 
  1. What type of content would fulfill the need (image, video, text, mixed)
  2. Whether or not adequate resources were available to produce the content.

The following is a statement of the defined scope:

#### In scope

* User feedback
  - If a user interacts with a website feature, user feedback will be shared.
  - This will be in the form of either a pop-up modal or email.
  - Warning, error and success colors will be used for easy recognition.

* User acount registration with verification
  - A user will be asked to verify their email address before setup is complete. Email verification is designed to check accounts to make sure they are real.
  - A user will be able to input personal details such as contact and shipping details. This will be stored in the database.
  - if the user forgets their password, they will have the choice to reset it via an email link.

* A webiste contact form
  - This will allow users to contact the business owner. A message subject can be selected on the form, which lets the receiver know the topic of contact.
  - The form will include a dropdown field called 'subject of message'.

* An online store selling original artwork, prints and gifts
  - Within each cateogry the user will be able to sort by price and filter by subcategory.
  - Adding/editing and removing items from the shopping cart will be possible.
  - If the user is logged in, any saved shipping details will autofill at the checkout.
  - A fully secure checkout process will be in place, using Stripe.
  - Shipping will be at the standard fee of €4.99. Orders above €50 will inlude free shipping.

* Descriptive product pages
  - The template will include the following information:
    - Images
    - canvas size
    - media
    - Stock level
  - A section for customer reviews will be included at the bottom of each page. 

* An about page
  - This will be focused on introducing the artist and their work.
  - As the focus will be on promoting the online shop, both this and a 'contact us' block will be incoporated into this page.

* A gallery
  - The business owner will be able to uplaod new content, edit and/or delete existing content.
  - A hover effect will be present on each image revealing the tite, canvas size and media used.

Time permitting - full task description
* A Pet commision service that generates a quote which the user can review
  - The user can upload an image and must then select the desired canvas size, media and confirm the number of pets in the picture. Based on the selection, a custom quote is generated.  
  - The quote would be calculated based on the number of pets (max 3 pets) in an image and the canvas size.
  - The request can then be accepted by the user. If submitted, it will be sent to the shop owner for review.
  - The shop owner retains the right to accept or decline the quote. (The request may be declined due to poor image quality).

#### Out of scope

* A sophisticated recommendation algorithm
  - Not possible due to the project time frame

### Wireframes
All wireframes were created using the software [Balsamiq](https://balsamiq.com/). 
These layouts were created following research on the five planes of UX, and before coding.\
\
<strong>
Please note, the final website layout contains slight variations to the original wireframes.
Each of the following files contain wireframes for desktop, tablet, and mobile devices.
</strong>
 
**Users: non-admin**
- [Homepage](assets/images/readmeFiles/wireframes/home.png)
- [Login](assets/images/readmeFiles/wireframes/login.png)
- [Register](assets/images/readmeFiles/wireframes/register.png)
- [Profile](assets/images/readmeFiles/wireframes/profile.png)
- [](assets/images/readmeFiles/wireframes/addABook.png)
  - The edit book page will be a direct copy of the Add a book page. The fields will be pre-selected.
- [](assets/images/readmeFiles/wireframes/bookPage.png)

**User: admin only**
- [](assets/images/readmeFiles/wireframes/manageGenresAdmin.png)
  - The 'add genre' book page will be a direct copy of the Add a book page.
    - It will contain two fields: a genre title and an icon name.
  - The Edit genre page will be a direct copy of the Add genre page. The fields will be pre-selected.

### Design

#### User journey
- The website structure was designed to be consistent, predictable, learnable, visible, and provide user feedback.
- A user journey for non-admin users was created to aid the structural design.

![user journey](assets/images/readmeFiles/userjourney.jpg) 


#### Typography
- All fonts used in this project derive from [Google Fonts](https://fonts.google.com/). 

- Fonts used include:
  - [Raleway](https://fonts.google.com/specimen/Raleway?query=raleway) - used for h1 - h4
  - [Lato](https://fonts.google.com/specimen/Lato?query=lato) - used for h5 - h6 and all other body text


#### Color scheme
- A ..

![colour palette](assets/images/readmeFiles/example.jpg)

--------------------------------------------------------------------------------------------

## Features

### Existing Features 

#### Elements on all pages

- NavBar
  - The navigation features The logo in the top left corner in desktop view. This switches to a center position on smaller screen sizes.

  - Access rights:
    - Certain links are viewable only to a logged-in user...

    - Below is a full list of navbar links shown for each user type.

      - For **all users** who **are not logged in**, the following links are viewable:
        1. Home 

      - For **non-admin users** who **are logged in**, the following links are viewable:
        1. 

      - For an **admin user** who **is logged in**, the following links are viewable:
        1. 


- Footer
  - The footer includes the following:
    - ..

#### Homepage


### Features Left to Implement
The following are features that were not included in this release. Once adequate time and a developed skillset are available, these points will be revisited.

* name
  - Implement ...



## Information Architecture

### Database information
- MongoDB (a project requirement):
  - This project utilizes MongoDB; a NoSQL database.

- Take-away thoughts:
  - A pre-defined schema would have simplified the development of the overall project.


### Datatypes
  - The datatypes utilized in this project include the following:
    - ObjectId
    - String
    - Boolean
    - DateTime
    - Array
    - Object

### Collections information
The website involves .. database collections. The details of each collection are detailed below.

  #### Users collection

| Title | Key in db | form validation type | Data type |
--- | --- | --- | --- 
Account Id | _id | None | ObjectId
Username | created_by | Text, `maxlength="15"` |string
Password | password | Text, `maxlength="15"` | string
Books Added by User | books_added | None | array
Reviews Added by User | reviews_added | None | array



----------------------------

## Technologies Used

### Database

* [MongoDB Atlas](https://www.mongodb.com/) - Used as the primary database for storing and retrieving the information in the website.

### Languages

* [HTML5](https://www.w3schools.com/html/) - Used for structuring the site pages.

* [CSS](https://www.w3schools.com/css/) - Used for styling the site pages.

* [Javascript](https://www.w3schools.com/js/DEFAULT.asp) - Used to make the website interactive.

* [Python](https://www.python.org/) - Used to create database-driven functionalities.

### Libraries

* [jQuery](https://jquery.com/) - Used to make the website interactive.

* [PyMongo](https://pypi.org/project/pymongo/) - Used to establish communication between MongoDB and Python.

* [Flask](https://flask.palletsprojects.com/en/2.0.x/) - Used to construct and render pages.

* [Jinja](https://jinja.palletsprojects.com/en/3.0.x/) - used in conjunction with flask to display data from the backend.

### Tools

* [Gitpod](https://www.gitpod.io/docs/) - Used as a development environment.

* [PIP](https://pip.pypa.io/en/stable/installing/) - Used for tool installations.

* [Git](https://www.gitpod.io/docs/) - Used to handle version control.

* [Github](https://github.com/) - Used for repository hosting.

* [Materialize](https://materializecss.com/about.html) - Used to develop the website design system.

* [Canva](https://www.canva.com/) - Used to create the brand logo.

* [IMgBB](https://imgbb.com/) - Used to store images.

* [Adobe Photoshop](https://www.adobe.com/products/photoshop.html) - Used to resize and edit images.

* [Favicon.io](https://favicon.io/favicon-converter/) - Used for favicon creation.

* [Am I Responsive](http://ami.responsivedesign.is/) - Used to create responsive images for different devices.

* [Google Fonts](https://fonts.google.com/) - Used for typography.

* [Font Awesome](https://fontawesome.com/) - Used for footer Icons.

* [Google Icons](https://fonts.google.com/icons) - Used for all Icons (bar footer icons).

* [LottieFiles](https://lottiefiles.com/) - All free animations are sourced from here.

* [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - Used for monitoring the responsiveness of the website.

* [LamdaTest](https://www.lambdatest.com/) - Used for monitoring the responsiveness of the website.
### Deployment (Heroku)

* [Heroku](https://id.heroku.com/login) - The cloud platform used to deploy the website.
----------------------------
## Testing
All testing documentation is stored in a separate testing file, which can be accessed [here](https://github.com/emmahartedev/..).

----------------------------

## Deployment

### Local Deployment
To run this project on your own IDE, ensure that the following are installed on your machine:

  * [Python 3](https://www.python.org/download/releases/3.0/)
  * [PIP](https://pypi.org/project/pip/)
  * [Git](https://git-scm.com/)

Additionally, make sure that you also have the following set up: 
  * [A MongoDB Atlas account](https://www.mongodb.com/)

#### Forking the repository
To fork the repository, the following steps must be followed:
1. Navigate to the [project repository](https://github.com/emmahartedev/The-Book-bar).

2. Click "Fork", located on the top right of the screen.

3. You have successfully forked the repository. A copy of the original project will now be copied to your account.

4. Create an [env.py](https://pypi.org/project/env.py/) file to store environmental variables. Add this to the [.gitignore](https://git-scm.com/docs/gitignore/en) file to ensure it is not uploaded.

5. Run the application using the command: ```python3 app.py```

#### Cloning the repository
To clone the repository, the following steps must be followed:

1. Navigate to the [project repository](https://github.com/emmahartedev/..).

2. Click 'Code' and in the Clone with HTTPS window, copy the provided repository URL. 

3. Open a terminal in your IDE.

4. Change the current working directory to the location you wish to generate the cloned directory.

5. Type ```git clone```, and then paste the URL from step 2. 

```
git clone https:..
```
6. Create an [env.py](https://pypi.org/project/env.py/) file to store environmental variables. Add this to the [.gitignore](https://git-scm.com/docs/gitignore/en) to ensure it is not uploaded.

7. Run the application using the command: ```python3 app.py```

### Heroku Deployment
To deploy 'The Book bar' to Heroku, the following steps must be followed:
  1. Create a [requirements.txt](https://blog.usejournal.com/why-and-how-to-make-a-requirements-txt-f329c685181e) file using the command ```pip freeze > requirements.txt```.

  2. Create a [Procfile](https://devcenter.heroku.com/articles/procfile) using the command ```echo web: python app.py > Procfile```.

  3. Add both files to Github by using ```git add```, then ```git commit -m "Add a relevant git message here"``` and finally ```git push```.

  4. Navigate to the [Heroku](https://id.heroku.com/login) website. On the dashboard page, click "New", then click "Create new app". Add a name and a region.

  5. Connect the Heroku app to the Github repository. On the Heroku app dashboard, select the "Deploy" tab. Under "Deployment method", select "Github" and confirm.

  6. Navigate to the "Settings" tab in the app dashboard. Under "Config Vars" click "Reveal Config Vars".

  7. Set the following config vars:

  | Key | Value |
 --- | ---
DEBUG | FALSE
IP | 0.0.0.0
MONGO_URI | `mongodb+srv://<username>:<password>@<cluster_name>-qtxun.mongodb.net/<database_name>?retryWrites=true&w=majority`
PORT | 5000
SECRET_KEY | `<your_secret_key>`
 
8. In the Heroku app click on the "Deploy" tab and navigate to the "Manual Deployment" section. Confirm that the "master" branch is selected and click "Deploy Branch".

9. The website is now successfully deployed.

----------------------------

## Credits 
The following material is not my own. Sources have been listed alongside a description of the content used. 

### Content

* [name of source](link) - Used for ...


### Code
The following code was used directly in this project:
  * [name of source](link) - used to create ...

The following code has been modified in this project:
  * [Stack Overflow - dippas](https://stackoverflow.com/questions/37127123/change-color-of-underline-input-and-label-in-materialize-css-framework/37127156) - used to change the color of the materialize input fields.


###  Media
The images used on this website were obtained from the following sources:

README.md:
* image desc - [Source](link)

### Acknowledgments
* 