# KayTea Art

## Full Stack Development - Milestone Project

[View the Live Site here.](https://katie-harte-art.herokuapp.com/)

<div align="center">
    <a href="https://katie-harte-art.herokuapp.com/" target="_blank">
      <img src="https://i.ibb.co/t4wz8DR/logo.png" alt="Katie Harte Art webshop">
    </a>
</div>

![Generated from Am I Responsive](https://i.ibb.co/WDmNFFv/amiresponsive.png)


The Kaytea Art webshop was designed, built and deployed by Emma Harte. The project was undertaken as the final milestone project for the Code Institute Full Stack; Web Development diploma.
The webstore was created to replace an existing Etsy account, allowing for a fully customizated shopping experience.

----------------------------

## Contents
1. [UX](#ux)
      - [Goals](#goals)
      - [User Stories](#user-stories)
        - [Visitor Stories](#visitor-stories)
        - [Business Stories](#business-stories)
    - [Project Scope](#project-scope)
      - [In Scope](#in-scope)
      - [Out of Scope](#out-of-scope)
    - [Wireframes](#wireframes)
    - [Design](#design)
      - [Color Scheme](#color-scheme)
      - [Typography](#typography)

2. [Features](#features)
    - [Existing Features](#existing-features)
    - [Future Features](#future-features)

3. [Information Architecture](#information-architecture)

4. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries and Programs](#frameworks-libraries-and-programs)
    - [Dependencies](#dependencies)

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

### Goals

**Target Audience:**
* People who are interested in realistic wildlife and animal art.
* Pet owners, interested in pet comissions.
* People looking for unique art at an affordable price.
* People looking for unique gift ideas.


### User Stories

#### Visitor stories:
**As a visitor of the website I expect/want/need:**

**Browsing**
1. To be able to browse the website easily without feeling confused or overwhelmed. It should have a easy-to-follow layout on all device sizes.
2. To be able to search for products by text, so that I can find something specific.
3. To browse orginal artwork and prints, as these are the main categories of an artshop which I would expect to see. 
4. To be able to filter by price within category pages so that I can find a product to suit my budget.
5. To see the image, media used and canvas size of each product. This information is vital to me.
6. To be able to read product reviews as this helps me to decide on the quality and level of service delivered by the company.
7. To request a quote for a pet commission so that I can decide myself whether this is something I would like to purchase.
8. To receive feedback after I interact with the website so that I am aware if the interaction has or has not been a success.
9. To learn more about the artist and the process behind the creations. As a supporter of small businessess, I like to feel a connection to the business owner.

**Shopping**
1. To know that the payment process is secure as I only shop on trustworthy sites.
2. To be able to navigate to my shopping cart easily so that I can quickly checkout.
3. To be able to add, edit or delete items or item quantities from my shopping cart so that I can easily modify my choices.
4. To know that the stock levels on products are accurate so that I know shipping delays won't occur. 
5. To receive an email after I submit an order so that I am aware the interaction had been a success.
6. My shipping details should autofill if I am logged in so that I can quickly checkout.

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
2. To be able to add/edit and delete blog content on the website so that I can keep the page fresh.

**Online shop admin**
1. To receive order notifications so that I begin preparing these.
2. To be able to provide a commision quote based on canvas size and number of pets. This would help to inform the user of the price before purchasing. 

### Project Scope

The following is a statement of the defined scope:

#### In scope

* User feedback
  - If a user interacts with a website feature, user feedback will be shared.
  - This will be in the form of either a pop-up modal or email.
  - Warning, error and success colors will be used for easy recognition.

* Text search
  - keywords can be used to search the site for a product at a very deep level.

* User acount registration with verification
  - A user will be asked to verify their email address before setup is complete. Email verification is designed to check accounts to make sure they are real.
  - A user will be able to input personal details such as contact and shipping details. This will be stored in the database.
  - if the user forgets their password, they will have the choice to reset it via an email link.

* A website contact form

* An online store selling original artwork, prints and gifts
  - The categories will be:
    - original artwork, 
    - prints
    - greeting cards. 
  - Within each category the user will be able to sort by price or easily switch categories.
  - Adding/editing and removing items from the shopping cart will be possible.
  - If the user is logged in, any saved shipping details will autofill at the checkout.
  - A fully secure checkout process will be in place, using Stripe.
  - Orders above €50 will inlude free shipping.

* Descriptive product pages
  - The template will include the following information:
    - Images
    - Canvas size
    - Media
    - Out of stock message (if applicable)
  - Product reviews

* An about page
  - This will be focused on introducing the artist and their work.
  - As the focus will be on promoting contact, a 'contact me' button will be added to this page.

* A Blog
  - The business owner will be able to upload new content, edit and/or delete existing content.
  - Logged in users will be able to add comments.

* A Pet commision contact service
  - The user can fill out the form and the admin will be in contact.

#### Out of scope

The following features have not been included in the first rollout of this project. At this time, the focus will be on launching the webshop with the most fundamental features covered.

* Online payment for commissions
* Product filtering by rating
* Discount code and voucher capabilities
* functionality to add a keyword from the site.
* Cart counter - showing number of items in cart instead of the cart cost
* Automatic deduction of product stock (upon sale)
* Automatic quote generation for pet commissions
* Abandoned cart recovery
* multiple media for products
* Integrated Social media share buttons on product pages
* Personalised product recommendations for users

### Wireframes
All wireframes were created using the software [Balsamiq](https://balsamiq.com/). 
These layouts were created following research on the five planes of UX, and before coding.\
\
<strong>
Please note, the final website layout contains slight variations to the original wireframes.
Each of the following files contain wireframes for desktop, tablet, and mobile devices.
</strong>
 
- [Homepage](https://i.ibb.co/QYHKLWC/Home.png)
- [Search results](https://i.ibb.co/YjGDyfM/Search-results.png)
- [About](https://i.ibb.co/vdwGFnF/About.png)
- [Blog](https://i.ibb.co/bLfcX9k/Blog.png)
- [Blog inner page](https://i.ibb.co/tcZ5YXV/Blog-inner-page.png)
- [Login](https://i.ibb.co/1Zzt9Fp/Login.png)
- [My profile](https://i.ibb.co/55H1gV7/My-account.png)
- [Register](https://i.ibb.co/yq92r4Z/Register.png)
- [Get in touch](https://i.ibb.co/MpvvwVr/Connect.png)
- [Shop - Categories](https://i.ibb.co/M9tDYLN/Shop-Categories.png)
- [Shop - Commissions](https://i.ibb.co/BtXZRD8/Shop-Pet-Commission.png)
- [Product page](https://i.ibb.co/CW02BCw/Product-page.png)
- [Shopping bag](https://i.ibb.co/5KBJLWy/Shopping-bag.png)
- [Checkout - Information + Payment](https://i.ibb.co/HnsrbMX/Checkout-Info.png)
- [Checkout - Complete](https://i.ibb.co/FbkNqCP/Checkout-Complete.png)

### Design
#### Colour Palette

- ![Color Palette](https://i.ibb.co/HNzkKYt/Color-Palette.png) 
  - #D4D3FF (Lavender Blue)
  - #FFCD69 (Maize Crayolla)
  - #2AA6B3 (Pacific Blue)
  - #F9CFE4 (Mini Pink)
  - #0095FF (Dodger Blue)

- Katie really wanted to acheive a playful, colour-rich website. The above color palette was chosen to create this, with the intention of using alot of whitespace inbetween. 


#### Typography
- All fonts used in this project derive from [Google Fonts](https://fonts.google.com/). 

- Fonts used include:
  - ['Roboto Mono'](https://fonts.google.com/specimen/Roboto+Mono#about) with a fallback of monospace, is used for h1 - h4
  - ['Montserrat'](https://fonts.google.com/specimen/Montserrat) with a fallback of sans-serif, is used for h5 - h6 and all other body text

--------------------------------------------------------------------------------------------

## Features

### Existing Features 

#### Elements on all pages

- Navigation
  - The navigation features The logo which is present on both mobile and desktop screen sizes.
  - Links to the blog, shop, about and contact pages are featured on the navbar. These are contained within the hamburger menu on mobile devices.
  - A search bar based on title and description allows for text searches. 
  - A shopping cart showing it's total cost is shown on the navbar. This is available across all pages. 

- Footer
  - The footer contains quick links, copyright information and social media icons.

- Toast messages
  - These notifications are available across the site, showing information, success and error messages.
  - The messages are triggered by CRUD operations. I.e., adding, editing or deleting a product.

- Custom 404, 403 and 500 pages
  - These error pages have been customised to fit the brand, ensuring that the user does not run into a dead end.

#### Home Page

The homepage features snippets of various pages, driving traffic to the about, shop and commissions page.
Cards are used to create visual cues and lead to the user to the next page. 

#### About Page

The about page simply features some text about Katie, images from her personal life and a link to the contact page.
The contact page acts as the CTA for this page.

#### Blog Page
The blog page contains an overview of the blog collection, showing the title, teaser, date and image of each. Pagination shows 3 blogs per page, organised by date.
The user can click into either the image or 'read more' link of any blog to reach the inner page.  

#### Blog Details Page
The blog details page contains the image, author, date, keywords and body of text content.
For superusers, an edit and delete button are visible.
Beneath the blog, lives a comment section. Only logged in users are permitted to post a comment and their username will be added to this.

#### Products Page
The products page an overview of products within the selected cateogry. 
These are presented on cards, which feature information such as the title, price and category name. Clicking on a card brings the user straight to the product details page.
Category buttons at the top of the page allow the user to switch easy between sub-sections.
Furthermore, 'sort by' functionality allows the user to sort by price or name.
Lastly, a 'back to top' button allows the user to quicky navigate back up the page. Pagination was not included on this template as it is unlikely product number will exceed 50. 

#### Product Details Page
The product details page contains the title, image, description, media, size and product price.
If an average star rating exists, this is also presented.
Quantity available is displayed in a dropdown menu. The user selected the desired quanity and add it to their shopping bag.
For superusers, an edit and delete button are visible.
Beneath the product section, lives a review section. Only logged in users are permitted to post a review and their username will be added to this. 

#### Product Admin Page
The product admin page is accessible to superusers only. The page link is located under the user icon on the navbar.
The page includes a form, from which a new product can be added.
As well as the product title, description, media, size, SKU and price, the user can select which category the product will live in. 
Furthermore, an image can be selected which will be displayed on the front-end.
If an image is not added, a default picture will be showm. 


#### Pet Commissions Page
The pet commissions page contains information about the service as well as a contact form.
The user can submit the form, stating their preferences for media type, canvas size and the number of pets per commission.

#### Contact Page
The contact page contains an enquiry form and lottie file animation.
This can be used for all general queries from users. 

#### Bag Page
he bag page displays every product and their quantity, which the user has added. 
Here, shoppers can update the quantities or remove products from their basket.
A bag summary shows the subtotal, delivery cost and the grand total. If a shopper us under the free shipping bag total, a message is displayed. This communicates the total extra cost required to avail of free delivery. A button with the summary box leads the shopper to the checkout page.
A second link allows the shopper to navigate back to the shop.

#### Checkout page
The checkout page contains an order form that shoppers must fill out to complete the checkout process.
If a user is logged in, they are promted to tick a checkbox in order to save their default information. 
If a user is not logged in, they are prompted to sign in to save their details.
An order summary reminds the shopper of their bag contents and cost.  
Payments are handled by Stripe. If card details are incorrect, an error message is triggered. If payement is successful, a confirmation email is sent. 
**Please note**: The website currently uses Stripe's test functionality as opposed to live payments.

#### Checkout success page
The checkout success page provides a summary of the order, stating that it was successful.
The summary includes the order number, order date, the products ordered as well as delivery and billing information. 
A link directing users back to the shop is provided underneath.

#### Additional Pages
The django-allauth library is used to manage user registeation and authentication on the site. The allauth templates inluding login, register, forgotten password etc hae been customised to suit the brand styling.


### Future Features
The following are Features that were not included in this release. Once adequate time is available, these points will be revisited.

* Sort by - average rating functionality
* Structure change to allow multiple picture uploads for products
* Development of the pet commissions app, to generate an automatic quote based on form field selection
* Social media sign up and login with allauth
* Paypal integration for checkout
* Allow users to set seperate billing and delivery addresses
* Replace the cart total with an item counter, on the navigation link
* Add user's name and email address to profile page

## Information Architecture

SQLite was used in the development of this project as it is the default database used with Django. On deployment with Heroku, a Postgres database is used.

### Data Models

**Profiles App**

`User` model

Django's default [User](https://docs.djangoproject.com/en/3.2/ref/contrib/auth/) model is used for this project. 

`UserProfile` model 

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| User | user | OneToOneField 'User' | on_delete=models.CASCADE |
| First Name | Default_first_name | CharField | max_length=40 |
| Last Name | Default_last_name | CharField | max_length=40 |
| Default Mobile Number | default_mobile_number | CharField | max_length=20, null=True, blank=True |
| Default Address Line 1 | default_address_line_1 | CharField | max_length=80, null=True, blank=True |
| Default Address Line 2 | default_address_line_2 | CharField | max_length=80, null=True, blank=True |
| Default Town or City | default_town_or_city | CharField | max_length=40, null=True, blank=True |
| Default County | default_county | CharField | max_length=80, null=True, blank=True |
| Default Postcode | default_postcode | CharField | max_length=20, null=True, blank=True |
| Default Country | default_country | CountryField | blank_label='Country', null=True, blank=True |

**Products App**

`Category` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Name | name | CharField | max_length=254 |
| Friendly Name | friendly_name | CharField | max_length=254, null=True, blank=True |

`Product` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Category | category | ForeignKey 'Category' | null=True, blank=True, on_delete=models.SET_NULL |
| Date Added | date_added | DateTimeField | auto_now_add=True, null=True |
| SKU | sku | CharField | max_length=200, null=True, blank=True |
| Name | name | CharField | max_length=200 |
| Description | description | TextField |
| Size | size | CharField | max_length=200 |
| Media | media | CharField | max_length=200 |
| Price | price | DecimalField | max_digits=6, decimal_places=2 |
| Image | image | ImageField | null=True, blank=True |

`ProductReview` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Author | author | ForeignKey 'User' | null=True, blank=True, on_delete=models.CASCADE |
| Date | date | DateTimeField | auto_now_add=True |
| Product | product | ForeignKey 'Product' | related_name='reviews', on_delete=models.CASCADE |
| Review Text | review_text | TextField | max_length=500 |
| Rating | review_rating | CharField | max_length=1, choices=RATING, default='2' |

**Checkout App**

`Order` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Order Number | order_number | CharField | max_length=32, null=False, editable=False |
| User Profile | user_profile | ForeignKey 'UserProfile' | on_delete=models.SET_NULL, null=True, blank=True, related_name='orders' |
| Date | date | DateTimeField | auto_now_add=True |
| First Name | first_name | CharField | max_length=50, null=False, blank=False |
| Last Name | last_name | CharField | max_length=50, null=False, blank=False |
| Email | email | EmailField | max_length=254, null=False, blank=False |
| Mobile Number | mobile_number | CharField | max_length=20, null=False, blank=False |
| Address Line 1 | address_line_1 | CharField | max_length=80, null=True, blank=True |
| Address Line 2 | address_line_2 | CharField | max_length=80, null=True, blank=True |
| Town or City | town_or_city | CharField | max_length=40, null=True, blank=True |
| County | county | CharField | max_length=80, null=True, blank=True |
| Postcode | postcode | CharField | max_length=20, null=True, blank=True |
| Country | country | CountryField | blank_label='Country *', null=True, blank=True |
| Delivery Cost | delivery_cost | DecimalField | max_digits=6, decimal_places=2, null=False, default=0 |
| Order Total | order_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0 |
| Grand Total | grand_total | DecimalField | max_digits=10, decimal_places=2, null=False, default=0 |
| Original Basket | original_basket | TextField | null=False, blank=False, default='' |
| Stripe PID | stripe_pid | CharField | max_length=254, null=False, blank=False |

`OrderLineItem` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Order | order | ForeignKey 'Order' | null=False, blank=False, on_delete=models.CASCADE, related_name='lineitems' |
| Product | product | ForeignKey 'Product' | null=False, blank=False, on_delete=models.CASCADE |
| Quantity | quantity | IntegerField | null=False, blank=False, default=0 |
| Line Item Total | lineitem_total | DecimalField | max_digits=6, decimal_places=2, null=False, blank=False, editable=False |

**Blog App**

`Keyword` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Name | name | CharField | max_length=20 |
| Friendly Name | friendly_name | CharField | max_length=20 |

`Blog` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Date | date | DateTimeField | auto_now_add=True |
| Keywords | keywords | ManyToManyField 'Keyword' | blank=True |
| Title | title | CharField | max_length=80 |
| Author | author | ForeginKey 'User' | null=True, blank=True, on_delete=models.CASCADE |
| Teaser | teaser | RichTextField | validators=[MinLengthValidator(70)] |
| Body Text | body | RichTextField | validators=[MinLengthValidator(70)] |
| Image | image | ImageField | null=True, blank=True |


`Reply` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Blog | blog | ForeignKey 'Blog' | related_name='replies', on_delete=models.CASCADE |
| Author | author | ForeignKey 'User' | null=True, blank=True, on_delete=models.CASCADE |
| Date | date | DateTimeField | auto_now_add=True |
| Body Text | body | TextField | max_length=600 | 


**Commissions App**

`Commissions` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Date | date | DateTimeField | auto_now_add=True, null=True, blank=True |
| Name | name | CharField | max_length=255 |
| Email | email | EmailField | max_length=254, null=False, blank=False |
| Size | size | CharField | max_length=30, choices=SIZE_CHOICES, default='Canvas size *'|
| Number of Pets | pet_num | CharField | max_length=30, choices=PET_NUM_CHOICES, default='Number of Pets *'|
| Media | media | CharField | max_length=30, choices=MEDIA_CHOICES, default='Media Preference *'|
| Message | message | TextField | null=True, blank=True |
| Image | image | ImageField | null=True, blank=True |

**Contact App**

`Contact` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Date | date | DateTimeField | auto_now_add=True, null=True, blank=True |
| Name | name | CharField | max_length=255 |
| Email | email | EmailField | max_length=254, null=False, blank=False |
| Message | message | TextField | max_length=1000 |


----------------------------

## Technologies Used

### Languages

* [HTML5](https://www.w3schools.com/html/)

* [CSS](https://www.w3schools.com/css/)

* [Javascript](https://www.w3schools.com/js/DEFAULT.asp)

* [Python](https://www.python.org/)

### Frameworks, Libraries and Programs

* [Django](https://www.djangoproject.com/) - A Python-based free and open-source web framework that follows the model–template–views architectural pattern.

* [jQuery](https://jquery.com/) - Used for website interactivity.

* [Heroku](https://www.heroku.com/) - Heroku is used to deploy this website.

* [Bootstrap 4](https://getbootstrap.com/) - Used in creating the responsiveness and styling of the website.

* [Font Awesome](https://fontawesome.com/) - All icons used derive from here.

* [AWS](https://aws.amazon.com/) - AWS Simple Cloud Storage S3 is used for storing static and media files.

* [Stripe](https://stripe.com/en-de) - The platfrom used for online payment and credit card processing.

* [SQLite](https://www.sqlite.org/index.html) - The default database used with Django. Used throughout the development phase of this project.

* [PostgreSQL](https://www.postgresql.org/) - The database used, upon project deployment with Heroku.

* [Git](https://www.gitpod.io/docs/) - Used to handle version control.

* [Gitpod](https://www.gitpod.io/docs/) - The IDE used for this project.

* [Github](https://github.com/) - Used for repository hosting.

* [Balsamiq](https://balsamiq.com/) - Used to create the wireframes during the design process.

* [Google Fonts](https://fonts.google.com/) - Usedd to obtain the website font.

* [Favicon.io](https://favicon.io/) - Used to generate the favicons.

* [IMgBB](https://imgbb.com/) - Used to store images.

* [Am I Responsive](http://ami.responsivedesign.is/) - Used to create responsive images for different devices.

* [LottieFiles](https://lottiefiles.com/) - All free animations are sourced from here.

* [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - Used for monitoring the responsiveness of the website.

### Dependencies

* [asgiref](https://pypi.org/project/asgiref/) - ASGI is a standard for Python asynchronous web apps and servers to communicate with each other, and is positioned as an asynchronous successor to WSGI.

* [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - Used to create, configure, and manage AWS S3.

* [botocore](https://botocore.amazonaws.com/v1/documentation/api/latest/index.html) - Botocore provides the low level clients, session, and credential & configuration data.

* [dj-database-url](https://pypi.org/project/dj-database-url/) - A Django utility that allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.

* [Django](https://www.djangoproject.com/) - A Python-based free and open-source web framework that follows the model–template–views architectural pattern.

* [django-allauth](https://django-allauth.readthedocs.io/en/latest/) - An integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.

* [django-ckeditor](https://django-ckeditor.readthedocs.io/en/latest/) - A rich text WYSIWYG editor used within the 'Add a Blog' page.

* [django-countries](https://pypi.org/project/django-countries/) - A Django application that provides country choices for use with forms, flag icons static files, and a country field for models.

* [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Provides a |crispy filter and {% crispy %} tag that allows for control over the rendering behaviour of Django forms in a very elegant and DRY way.

* [django-js-asset](https://pypi.org/project/django-js-asset/) - Provides a way of inserting script tags into Django templates that provide extra attributes such as `id` and `data-*` for CSP-compatible data injection.

* [django-storages](https://pypi.org/project/django-storages/) - Provides a variety of storage backends in a single library.

* [gunicorn](https://docs.gunicorn.org/en/stable/) - The Gunicorn "Green Unicorn" is a Python Web Server Gateway Interface HTTP server.

* [jmespath](https://pypi.org/project/jmespath/) - JMESPath allows declaratively specify how to extract elements from a JSON document.

* [oauthlib](https://oauthlib.readthedocs.io/en/latest/) - A framework that implements the logic of OAuth1 or OAuth2 without assuming a specific HTTP request object or web framework.

* [Pillow](https://pypi.org/project/Pillow/) - A Python Imaging Library adds image processing capabilities to your Python interpreter.

* [psycopg2-binary](https://pypi.org/project/psycopg2-binary/) -  A popular PostgreSQL database adapter for the Python programming language.

* [python3-openid](https://pypi.org/project/python3-openid/) - A set of Python packages to support the use of the OpenID decentralized identity system in applications.

* [pytz](https://pypi.org/project/pytz/) - Brings the Olson tz database into Python. This library allows accurate and cross platform timezone calculations using Python 2.4 or higher.

* [requests-oauthlib](https://pypi.org/project/requests-oauthlib/) - Uses the Python Requests and OAuthlib libraries to provide an easy-to-use Python interface for building OAuth1 and OAuth2 clients. 

* [s3transfer](https://pypi.org/project/s3transfer/) - A Python library for managing Amazon S3 transfers.

* [sqlparse](https://pypi.org/project/sqlparse/) - A non-validating SQL parser for Python. It provides support for parsing, splitting and formatting SQL statements.

* [stripe](https://pypi.org/project/stripe/) - A Python library for Stripe’s API.


## Testing
All testing documentation for this project is stored in a separate [TESTING.md](https://github.com/emmahartedev/testing.md) file.

----------------------------

## Deployment

To run this project on your own IDE, ensure that the following are installed on your machine:

  * [Python 3](https://www.python.org/download/releases/3.0/)
  * [PIP](https://pypi.org/project/pip/)
  * [Git](https://git-scm.com/)

Additionally, make sure that you also have the following set up: 
  * [Heroku](https://www.heroku.com/)
  * [Stripe](https://stripe.com/)
  * [Gmail](https://www.google.com/gmail/) with 2 step verification
  * [AWS S3 bucket](https://aws.amazon.com/s3/)

### Local Deployment

1. Clone the GitHub Repository

* Login to GitHub and Navigate to the [project repository](https://github.com/emmahartedev/kaytea_art.).

* Click 'Code' and in the Clone with HTTPS window, copy the provided repository URL. 

* Open a terminal in your IDE.

* Change the current working directory to the location you wish to generate the cloned directory.

* Type ```git clone```, and then paste the URL from step 2. 

```
git clone https://github.com/emmahartedev/kaytea_art.git
```

2. Create a Virtual Environment

  * cd into the project directory and create a new virtual environment by typing:
  ```
  python -m .venv venv
  ```
  * Activate the virtual environment byt typing:
  ```
  .venv\Scripts\activate.bat
  ```

3. Install the project requirements by typing:
  ```
  pip install -r requirements.txt
  ```

4. Set up the environment variables.

  * Create an env.py file in the root directory, adding it to the .gitignore file.

  * Add the following import and variables to the file.
    ```
    import os
    os.environ["DEVELOPMENT"] = "True"
    os.environ["SECRET_KEY"] = "<Your Key>"
    os.environ["STRIPE_PUBLIC_KEY"] = "<Your Key>"
    os.environ["STRIPE_SECRET_KEY"] = "<Your Key>"
    os.environ["STRIPE_WH_SECRET"] = "<Your Key>"
    ```
5. Migrate the models to create your database by typing:

  ```
  python manage.py migrate
  ```
6. Load the products & category data by typing

  ```
  python3 manage.py loaddata categories

  python3 manage.py loaddata products
  ```

7. Create a superuser account by typing:

  ```
  python manage.py createsuperuser
  ```

8. You should now be able to run the project locally by typing:
  ```
  python manage.py runserver
  ```

6. Create an [env.py](https://pypi.org/project/env.py/) file to store environmental variables. Add this to the [.gitignore](https://git-scm.com/docs/gitignore/en) to ensure it is not uploaded.

7. Run the application using the command: ```python3 app.py```

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

https://www.toptal.com/designers/subtlepatterns/ - pattern overlay
bird singing animation - https://lottiefiles.com/23100-happy-bird
bag
https://lottiefiles.com/web-player?lottie_url=https%3A%2F%2Fassets8.lottiefiles.com%2Fprivate_files%2Flf30_94juvpzy.json

### Acknowledgments
* 