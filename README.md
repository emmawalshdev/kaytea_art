# KayTea Art

## Full Stack Development - Milestone Project

[View the Live Site here.](https://katie-harte-art.herokuapp.com/)

<div align="center">
    <a href="https://katie-harte-art.herokuapp.com/" target="_blank">
      <img src="https://i.ibb.co/t4wz8DR/logo.png" alt="Katie Harte Art webshop">
    </a>
</div>

![Generated from Am I Responsive](https://i.ibb.co/D1mn86w/responsiveimg.png)


The Kaytea Art ecommerce website was designed, built, and deployed by Emma Harte. This project completes her Diploma in Software Development, undertaken through the Code Institute. 

This website was built for Katie Harte, a wildlife and animal artist based in West Cork, Ireland.  Through the new Art store, Katie aims to connect with her clients, share her story, and offer her wonderful artwork and commission service. 

Previously, Katie has marketed her work through Etsy and social media.  In the future, the Art store aims to become Katie's primary sales channel. This is a long-term project, with many new exciting features planned for the future.

----------------------------

**Test card details**

Card number: 4242 4242 4242 4242

Expiry date: 04 / 24

CVC: 424

ZIP: 42424

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
    - [Data Models](#data-models)

4. [Technologies Used](#technologies-used)
    - [Languages](#languages)
    - [Frameworks, Libraries and Programs](#frameworks-libraries-and-programs)
    - [Dependencies](#dependencies)

5. [Testing](#testing)
    
6. [Deployment](#deployment)
    - [Local Deployment](#local-deployment)
    - [Heroku Deployment](#heroku-deployment)

7. [Credits](#credits)
    - [Code](#code)
    - [Media](#media)
    - [Content](#content)
    - [Acknowledgments](#acknowledgments)

----------------------------

## UX

### Goals

**Target Audience:**
* People who are interested in realistic wildlife and animal art.
* Pet owners, interested in pet commissions.
* People looking for unique art at an affordable price.
* People looking for unique gift ideas.


### User Stories

#### Visitor Stories:
**As a visitor of the website I expect/want/need:**

**Browsing**
1. To be able to browse the website easily without feeling confused or overwhelmed. It should have an easy-to-follow layout on all device sizes.
2. To be able to search for products by text, so that I can find something specific.
3. To browse original artwork and prints, as these are the main categories of an art shop which I would expect to see. 
4. To be able to filter by price within category pages so that I can find a product to suit my budget.
5. To see the image, media used, and canvas size of each product. This information is vital to me.
6. To be able to read product reviews. This helps me to decide on the quality and level of service delivered by the company.
7. To request a quote for a pet commission so that I can decide myself whether this is something I would like to purchase.
8. To receive feedback after I interact with the website so that I am aware if the interaction has or has not been a success.
9. To learn more about the artist and the process behind the creations. As a supporter of small usinesses, I like to feel a connection to the business owner.

**Shopping**
1. To be able to navigate to my shopping cart easily so that I can quickly checkout.
2. To be able to add, edit or delete items or item quantities from my shopping cart so that I can easily modify my choices.
3. To know that the stock levels on products are accurate so that I know shipping delays won't occur. 
4. To receive an email after I submit an order so that I am aware the interaction had been a success.
5. My shipping details should autofill if I am logged in so that I can quickly checkout.

**Customer care**
1. To be able to set up an account, so that I can log in on return, and view my data.
2. To be able to contact the shop owner easily in case I have a question related to my order.
3. To see a summary of my order after I make a purchase so that I can review the details.
4. To see a list of my order history so that I can check up on my recent activity. 
5. To be able to update my account details in case a change is required.
6. To be able to connect to the company owner on social media channels so that I can keep up-to-date. 


#### Business Stories:

**As a superuser of the website I expect/want/need:**

**General**
1. Build a beautiful, easy-to-use, trustworthy website so that I can build brand awareness and sell artwork.
2. To be able to view customer/order/product data so that I easily pull up information if required. 

**Website admin**
1. To be able to add/edit and delete products on the website so that I can keep the information up-to-date.
2. To be able to add/edit and delete blog content on the website so that I can keep the page fresh.

**Online shop admin**
1. To receive order notifications so that I begin preparing these.
2. To be able to provide a commission quote based on canvas size and number of pets. This would help me to better understand the user's needs before I contact them. 

### Project Scope

The following is a statement of the defined scope.

#### In Scope

* User feedback
  - If a user interacts with a website feature, user feedback will be shared.
  - This will be in the form of either a pop-up modal or email.
  - Success, error, and information messages will be included. These will be customized for easy recognition.

* Text search
  - keywords can be used to search the site for a product by title or description.

* User acount registration with verification
  - A user will be asked to verify their email address before setup is complete. Email verification is designed to check accounts & ensure authenticity.
  - A user will be able to input personal details such as contact and shipping details. This information will be stored in the database.
  - If the user forgets their password, they will have the choice to reset it via an email link.

* A website contact form
  - This form will live on a separate contact page and will handle all general inquiries from users.

* An online store selling original artwork, prints, and gifts
  - The art store categories will be:
    - original artwork 
    - prints
    - greeting cards
  - Within each category, the user will be able to sort by price & will easily be able to switch between categories.
  - Adding/editing and removing items from the shopping cart will be possible.
  - If the user is logged in, any saved shipping details will autofill at checkout.
  - A fully secure checkout process will be in place, using Stripe.
  - Orders above €50 will include free shipping.

* Descriptive product pages
  - The product page template will include the following information:
    - Product mage
    - Canvas size
    - Media
    - Out of stock message (if applicable)
    - Product reviews

* An About page
  - This will be focused on introducing the artist and their work.
  - As the focus will be on promoting contact, a 'contact me' button will be added to this page.

* A Blog
  - The business owner will be able to upload new content, edit and/or delete existing content.
  - Logged in users will be able to add comments.

* A Pet commission contact service
  - The user can fill out the form and the admin will be in contact.

#### Out of Scope

The following features have not been included in the first rollout of this project. At this time, the focus will be on launching the webshop with the most fundamental features covered.

* Online payment for commissions
* Product filtering by rating
* Discount code and voucher capabilities
* Functionality to add a blog keyword from the font-end site
* URL structure change for blog and product detail pages (slugs)
* Cart counter - showing the number of items in the cart instead of the cart cost
* Automatic deduction of product stock (upon sale)
* Automatic quote generation for pet commissions
* Ability to add multiple images to product uploads
* Integrated Social media share buttons on product pages
* Customized allauth emails
* Personalized product recommendations for users

### Wireframes
All wireframes were created using the software [Balsamiq](https://balsamiq.com/). 
These layouts were created in collaboration with Katie Harte and following research on the five planes of UX\
\
<strong>
Please note, the final website layout contains slight variations to the original wireframes.
Each of the following files contains wireframes for desktop, tablet, and mobile devices.
</strong>
 
- [Homepage](https://i.ibb.co/QYHKLWC/Home.png)
- [Search results](https://i.ibb.co/YjGDyfM/Search-results.png)
- [About](https://i.ibb.co/vdwGFnF/About.png)
- [Blog](https://i.ibb.co/bLfcX9k/Blog.png)
- [Blog inner page](https://i.ibb.co/3Y98Pxb/Blog-inner-page.png)
- [Login](https://i.ibb.co/1Zzt9Fp/Login.png)
- [My profile](https://i.ibb.co/55H1gV7/My-account.png)
- [Register](https://i.ibb.co/yq92r4Z/Register.png)
- [Get in touch](https://i.ibb.co/MpvvwVr/Connect.png)
- [Shop - Categories](https://i.ibb.co/M9tDYLN/Shop-Categories.png)
- [Shop - Commissions](https://i.ibb.co/jTmmDS1/Shop-Pet-Commission.png)
- [Product page](https://i.ibb.co/CW02BCw/Product-page.png)
- [Shopping bag](https://i.ibb.co/5KBJLWy/Shopping-bag.png)
- [Checkout - Information + Payment](https://i.ibb.co/HnsrbMX/Checkout-Info.png)
- [Checkout - Complete](https://i.ibb.co/FbkNqCP/Checkout-Complete.png)

### Design

#### Color Scheme

![Color Palette](https://i.ibb.co/HNzkKYt/Color-Palette.png) 
  - #D4D3FF (Lavender Blue)
  - #FFCD69 (Maize Crayolla)
  - #2AA6B3 (Pacific Blue)
  - #F9CFE4 (Mini Pink)
  - #0095FF (Dodger Blue)

 Katie wanted to achieve a playful, colorful website. The above color palette was chosen to create this, with the intention of using a lot of whitespace to prevent noise.


#### Typography

- All fonts used in this project derive from [Google Fonts](https://fonts.google.com/)
- Fonts used include:
  - ['Sniglet'](https://fonts.google.com/specimen/Sniglet?query=sniglet) with a fallback of cursive, is used for h1 - h6.
  - ['Roboto'](https://fonts.google.com/specimen/Roboto?query=roboto) with a fallback of sans-serif, is used and all other body text.

--------------------------------------------------------------------------------------------

## Features

### Existing Features 

#### Elements on all pages

- **Navigation**
  - The navigation features the company logo, which is present on both mobile and desktop screen sizes.
  - Links to the blog, shop, about, and contact pages are featured on the navbar. These are contained within the hamburger menu on the mobile view.
  - The search bar field, located on the navbar allows the user to search by title or description. 
  - A shopping cart icon changes color if the value is greater than 0. Underneath, the user's cart total is displayed.

  ![navigation](https://media.giphy.com/media/qcc0dtIYnXryZ3ovf5/giphy.gif)

- **Footer**
  - The footer contains the company logo, quick links, copyright information, and social media icons.

  ![footer](https://i.ibb.co/BNXXGBX/footer.jpg)


- **Toast messages**
  - These notifications are displayed across the site, showing information, success, and error messages.
  - The messages are triggered by CRUD operations. I.e., adding, editing or deleting a product.

  <img src="https://i.ibb.co/qCR5mZv/toastmessage.jpg" alt="toast message" width="400"/>
  

- **Custom 404, 403, and 500 pages**
  - These error pages have been customized to fit the brand. A button redirecting the user back to the main site is included on each page. This ensures that the user does not run into a dead end.
  
  ![404 page](https://i.ibb.co/1sWTkZN/404page.jpg)

#### Home Page
* The Home page features snippets of the about and shop pages. This helps to introduce the artist and her work.
Cards are used to display Artwork from each category, enticing the user to click into the page.
![category cards](https://i.ibb.co/mzSvjhn/homepage.jpg)

#### About Page
* The About page features descriptive text about Katie;  the artist behind the work, along with some personal imagery.
* This page aims to provide the user with more information and a way to connect with the artist.
* A link to the contact page is also provided, welcoming all inquiries.

![About page](https://i.ibb.co/nsYCX9M/aboutpage.jpg)

#### Blog Page
* The Blog page contains an overview of the blog collection. The title, teaser, date, author, and image of each blog are displayed.
* The title and teaser text are truncated to prevent large unslight strings. To view a specific blog, the user can click either the image or 'read more' teaser link.  
* Pagination restricts the number of blogs per page to 3.
  \
  \
  ![Blog page](https://media.giphy.com/media/x8nCTyEldV5NUCy1rQ/giphy.gif)


#### Blog Details Page
* The Blog Details page contains two sections: Blog content, and blog comments. 
* In the blog content section, the image, author, date, keywords and body of text are displayed. For superusers, edit and delete buttons are visible.

  ![Blog page - content](https://i.ibb.co/59BgsKX/blogdetail.jpg)

* In the comments section, a toggle link invites the user to join the conversation. Only logged-in users are permitted to submit a comment.
* Featured existing comments are ordered by date. If the user is the author or a superuser, edit and delete buttons are visible.

  ![Blog page - comments](https://i.ibb.co/Qk7q6C6/blogdetail-comments.jpg)

#### Products Page
* The Products page contains an overview of products within the selected category. 
* Category buttons at the top of the page allow the user to switch easily between categories.
* The product count for the selected category is displayed alongside a button to 'view all artwork'.
* A 'sort by' dropdown field allows the user to sort by price or name. 

  ![Products page - buttons](https://i.ibb.co/k3H0gsm/products-buttons.jpg)

* Each product's title, price, and category name is displayed on a card. Clicking on the product card leads the user to the product details page.
* A 'back to top' button allows the user to quickly navigate back up the page. Pagination was not included on this template as it is unlikely the product count will ever exceed 50. 

  ![Products page - cards](https://i.ibb.co/Ht99SN9/products-cards.jpg)

#### Product Details Page
* The Products Details page contains two sections: Product detail and product reviews.
* In the product detail section, the title, image, description, average rating, media, size and product price are displayed. For superusers, edit and delete button are visible.
*  Quantity available is displayed in a dropdown menu. This value derives from the stock available.
In selecting a quantity, the user can add the product to their bag. 

    ![product detail - content](https://i.ibb.co/z5BcvMW/product-details-page.jpg)

* In the product reviews section, a toggle link invites the user to leave a review. Only logged-in users are permitted to submit a review.
* Featured existing reviews are ordered by date. If the user is the author or a superuser, edit and delete buttons are visible.

  ![product detail - reviews](https://i.ibb.co/6PCqtPb/products-reviews.jpg)


#### Product Admin Page
* The Product Admin page is accessible to superusers only and is accessible through the 'Account' icon dropdown on the navbar.
* The page contains a form, from which a new product can be added to the store.
* As well as the product title, description, media, size, SKU, and price, the user can select which category the product will live in. 
Furthermore, an image can be selected which will be displayed on the front-end.
If an image is not added, a default picture will be shown. 


#### Pet Commissions Page
* The Pet Commissions page contains service information and a customer contact form.
* The user can submit a commission request, stating their preferences for media type, canvas size and the number of pets per commission.

#### Contact Page
* The Contact page contains an inquiry form, taking the user's name, email address, and message as required fields. 

#### Bag Page
* The Bag Page displays each product (plus the quantity), which the user has 'added to bag'.
* The user can update the quantities or entirely remove products from their basket.
* A bag summary shows the subtotal, delivery cost, and the order grand total. If a shopper does not currently qualify for free shipping, a message is displayed. This communicates the total extra cost required to avail of free delivery. 
* A 'Secure Checkout' button leads the shopper to the checkout page. A 'Continue Shopping' link allows the shopper to navigate back to the store.
* Progress steps at the top of the bag show the user where they stand on the checkout process.

  ![Bag](https://i.ibb.co/LzGCwBk/bag.jpg)

* A message notifying the user that their bag is empty is displayed, if no products have been added.

  ![Empty bag](https://i.ibb.co/gtKb0Bm/empty-bag.jpg)

#### Checkout Page
* The checkout page contains an order form that shoppers must fill out to complete the checkout process.
* If a user is logged in, they are prompted to tick a checkbox to save their default information. 
If a user is not logged in, they are prompted to 'Login or Register' to save their details.

  ![Checkout page - save info](https://i.ibb.co/FV0tK8N/save-address-checkout.jpg)

* An order summary reminds the shopper of their bag contents and the order total.  
* Payments are handled by Stripe. If card details are incorrect, an error message is triggered. If payment is successful, a confirmation email is sent. 
**Please note**: The website currently uses Stripe's test functionality as opposed to live payments.

  ![Checkout page - error payment](https://i.ibb.co/6W0k41v/checkout-invalid-payment.jpg)

#### Checkout Success Page
* The checkout success page provides a summary of the order, stating that it was successful.
* The summary includes the order number, order date, the products ordered as well as delivery and billing information. 

  ![Order history](https://i.ibb.co/54M1dzP/order-history.jpg)

* A link directing users back to the shop is provided underneath.

#### Additional Pages
* The django-allauth library is used to manage user registration and authentication on the site. The allauth templates; including login, register, forgotten password, etc have been customized to suit the brand styling.


### Future Features
The following features are not included in this release. These points will be revisited in future rollouts.

* Improve 'Sort by' functionality on Products page - add sort by 'average rating'.
* Build a structure on product details page to allow for multiple picture uploads.
* Further develop the Commissions app - build automatic quote feature.
* Add pagination to reviews/comments section on blog detail and product detail pages.
* Add a boolean 'published' value to product and blog detail records - This should control whether a product/blog is public or not.
* Add Privacy Policy and Terms & condition pages. 
* Add social media sign-up and login functionality using allauth.
* Integrate Paypal on the checkout page.
* Build functionality to allow users to set up separate billing and delivery addresses.
* Replace the bag total value with an item counter, on the navigation bar.
* Add functionality to allow users to update their username and email address.

## Information Architecture

* SQLite was used during the development phase of this project. This is the default database used with Django. On deployment with Heroku, a Postgres database is used.

### Data Models

**Profiles App**

`User` model

* Django's default [User](https://docs.djangoproject.com/en/3.2/ref/contrib/auth/) model is used for this project. 

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
| Name | name | CharField | max_length=200 |
| Friendly Name | friendly_name | CharField | max_length=200, null=True, blank=True |

`Product` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Category | category | ForeignKey 'Category' | null=True, blank=True, on_delete=models.SET_NULL |
| Date Added | date_added | DateTimeField | auto_now_add=True, null=True |
| SKU | sku | CharField | max_length=200, null=True, blank=True |
| Name | name | CharField | max_length=200 |
| Description | description | TextField | null=True, blank=True |
| Size | size | CharField | max_length=200 |
| Media | media | CharField | max_length=200 |
| Stock | stock | PositiveSmallIntegerField | MaxValueValidator(20) |
| Price | price | DecimalField | max_digits=6, decimal_places=2 |
| Image | image | ImageField | null=True, blank=True |

`ProductReview` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Author | author | ForeignKey 'User' | null=True, blank=True, on_delete=models.CASCADE |
| Date | date | DateTimeField | auto_now_add=True |
| Product | product | ForeignKey 'Product' | related_name='reviews', on_delete=models.CASCADE |
| Review Text | review_text | TextField | max_length=600 |
| Rating | review_rating | CharField | max_length=2, choices=RATING, default='Rating *' |

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
| Original Bag | original_bag | TextField | null=False, blank=False, default='' |
| Stripe PID | stripe_pid | CharField | max_length=254, null=False, blank=False, default='' |

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
| Name | name | CharField | max_length=80 |
| Friendly Name | friendly_name | CharField | max_length=80 |

`Blog` model

| **Name**   | **Database Key**   | **Field Type**   | **Type Validation**   |
| ---------- | ------------------ | ---------------- | --------------------- |
| Date | date | DateTimeField | auto_now_add=True |
| Keywords | keywords | ManyToManyField 'Keyword' | blank=True |
| Title | title | CharField | max_length=80 |
| Author | author | ForeginKey 'User' | null=True, blank=True, on_delete=models.CASCADE |
| Teaser | teaser | RichTextField | MinLengthValidator(70)|
| Body Text | body | RichTextField | MinLengthValidator(70) |
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
| Media | media | CharField | max_length=40, choices=MEDIA_CHOICES, default='Media Preference *'|
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

### Frameworks, Libraries, and Programs

* [Django](https://www.djangoproject.com/) - A Python-based free and open-source web framework that follows the model–template–views architectural pattern.

* [jQuery](https://jquery.com/) - Used for website interactivity.

* [Heroku](https://www.heroku.com/) - Heroku is used to deploy this website.

* [Bootstrap 4](https://getbootstrap.com/) - Used in creating the responsiveness and styling of the website.

* [Font Awesome](https://fontawesome.com/) - All icons used derive from here.

* [AWS](https://aws.amazon.com/) - AWS Simple Cloud Storage S3 is used for storing static and media files.

* [Stripe](https://stripe.com/en-de) - The platform used for online payment and credit card processing.

* [SQLite](https://www.sqlite.org/index.html) - The default database used with Django. Used throughout the development phase of this project.

* [PostgreSQL](https://www.postgresql.org/) - The database used, upon project deployment with Heroku.

* [Git](https://www.gitpod.io/docs/) - Used to handle version control.

* [Gitpod](https://git-scm.com/) - The IDE used for this project.

* [Github](https://github.com/) - Used for repository hosting.

* [Balsamiq](https://balsamiq.com/) - Used to create the wireframes during the design process.

* [Google Fonts](https://fonts.google.com/) - Used to obtain the website font.

* [Favicon.io](https://favicon.io/) - Used to generate the favicons.

* [ImgBB](https://imgbb.com/) - Used to store images.

* [GIPHY](https://giphy.com/) - Used to create GIF files for README.md.

* [Article Generator Online](http://articlecreator.fullcontentrss.com/) - Used to generate blog content for the purpose of this project.

* [Am I Responsive](http://ami.responsivedesign.is/) - Used to create responsive images for different devices.

* [LottieFiles](https://lottiefiles.com/) - All free animations are sourced from here.

* [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) - Used for monitoring the responsiveness of the website.

### Dependencies

* [asgiref](https://pypi.org/project/asgiref/) - ASGI is a standard for Python asynchronous web apps and servers to communicate with each other, and is positioned as an asynchronous successor to WSGI.

* [boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) - Used to create, configure, and manage AWS S3.

* [botocore](https://botocore.amazonaws.com/v1/documentation/api/latest/index.html) - Botocore provides the low-level clients, session, and credential & configuration data.

* [coverage](https://coverage.readthedocs.io/en/coverage-5.5/) - Used to measure the code coverage of Python programs.

* [dj-database-url](https://pypi.org/project/dj-database-url/) - A Django utility that allows you to utilize the 12factor inspired DATABASE_URL environment variable to configure your Django application.

* [Django](https://www.djangoproject.com/) - A Python-based free and open-source web framework that follows the model–template–views architectural pattern.

* [django-allauth](https://django-allauth.readthedocs.io/en/latest/) - An integrated set of Django applications addressing authentication, registration, account management as well as 3rd party (social) account authentication.

* [django-ckeditor](https://django-ckeditor.readthedocs.io/en/latest/) - A rich text WYSIWYG editor used within the 'Add a Blog' page.

* [django-countries](https://pypi.org/project/django-countries/) - A Django application that provides country choices for use with forms, flag icons static files, and a country field for models.

* [django-crispy-forms](https://django-crispy-forms.readthedocs.io/en/latest/) - Provides a |crispy filter and {% crispy %} tag that allows for control over the rendering behavior of Django forms in a very elegant and DRY way.

* [django-js-asset](https://pypi.org/project/django-js-asset/) - Provides a way of inserting script tags into Django templates that provide extra attributes such as `id` and `data-*` for CSP-compatible data injection.

* [django-storages](https://pypi.org/project/django-storages/) - Provides a variety of storage backends in a single library.

* [gunicorn](https://docs.gunicorn.org/en/stable/) - The Gunicorn "Green Unicorn" is a Python Web Server Gateway Interface HTTP server.

* [jmespath](https://pypi.org/project/jmespath/) - JMESPath allows declaratively specify how to extract elements from a JSON document.

* [oauthlib](https://oauthlib.readthedocs.io/en/latest/) - A framework that implements the logic of OAuth1 or OAuth2 without assuming a specific HTTP request object or web framework.

* [Pillow](https://pypi.org/project/Pillow/) - A Python Imaging Library adds image processing capabilities to your Python interpreter.

* [psycopg2-binary](https://pypi.org/project/psycopg2-binary/) -  A popular PostgreSQL database adapter for the Python programming language.

* [python3-openid](https://pypi.org/project/python3-openid/) - A set of Python packages to support the use of the OpenID decentralized identity system in applications.

* [pytz](https://pypi.org/project/pytz/) - Brings the Olson tz database into Python. This library allows accurate and cross-platform timezone calculations using Python 2.4 or higher.

* [requests-oauthlib](https://pypi.org/project/requests-oauthlib/) - Uses the Python Requests and OAuthlib libraries to provide an easy-to-use Python interface for building OAuth1 and OAuth2 clients. 

* [s3transfer](https://pypi.org/project/s3transfer/) - A Python library for managing Amazon S3 transfers.

* [sqlparse](https://pypi.org/project/sqlparse/) - A non-validating SQL parser for Python. It provides support for parsing, splitting, and formatting SQL statements.

* [stripe](https://pypi.org/project/stripe/) - A Python library for Stripe’s API.


## Testing
* All testing documentation for this project is stored in a separate [TESTING.md](https://github.com/emmahartedev/kaytea_art/blob/main/TESTING.md) file.

----------------------------

## Deployment

To run this project on your own IDE, the following must be installed on your machine:

  * [Python 3](https://www.python.org/download/releases/3.0/)
  * [PIP](https://pypi.org/project/pip/)
  * [Git](https://git-scm.com/)

Secondly, make sure that you also have set up the following: 
  * [Heroku](https://www.heroku.com/)
  * [Stripe](https://stripe.com/)
  * [Gmail](https://www.google.com/gmail/) (with 2 step verification)
  * [AWS S3 bucket](https://aws.amazon.com/s3/)

### Local Deployment

1. Clone the GitHub Repository

* Log in to GitHub and Navigate to the [project repository](https://github.com/emmahartedev/kaytea_art).

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
  * Activate the virtual environment by typing the following command:
    ```
    .venv\Scripts\activate.bat
    ```

3. Install the project requirements by typing the following command:
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
5. Migrate the models to create your database by typing the following command:

    ```
    python manage.py migrate
    ```
6. Load the products & category data by typing the following command:

    ```
    python3 manage.py loaddata categories

    python3 manage.py loaddata products
    ```

7. Create a superuser account by typing the following command:

    ```
    python manage.py createsuperuser
    ```

8. You should now be able to run the project locally by typing the following command:
    ```
    python manage.py runserver
    ```

6. Create an [env.py](https://pypi.org/project/env.py/) file to store environmental variables. Add this to the [.gitignore](https://git-scm.com/docs/gitignore/en) to ensure it is not uploaded.

7. Run the application by typing the following command: 
    ```
    python3 app.py
    ```

### Heroku Deployment
1. Set up the Heroku app.

* Login to Heroku. On the dashboard, click on the 'New' button, then click 'Create new app'.
* Name the app, pick your region and click 'Create app'.
* In the 'Add-ons' search bar; search for 'postgres', then choose 'Heroku Postgres'.
* Submit the form, choosing the free plan.
* In the deployment tab, choose GitHub as the deployment method. Link the repository you cloned by searching for it by name.
* Choose the master branch to deploy, then click 'Enable Automatic Deploys'.
* Navigate to the settings tab, click 'Reveal Config Vars' and add the following:


  | Key	| Value |
  | ------| ----------- | 
  | AWS_ACCESS_KEY_ID |	Your AWS access key ID |
  | AWS_SECRET_ACCESS_KEY	| Your AWS secret access key |
  | DATABASE_URL | Your postgres database URL |
  | EMAIL_HOST_PASS	| 16-character password from Gmail |
  | EMAIL_HOST_USER	| Your Gmail |
  | SECRET_KEY	| Your secret key |
  | STRIPE_PUBLIC_KEY	| Your stripe public key |
  | STRIPE_SECRET_KEY	| Your stripe secret key |
  | STRIPE_WH_SECRET	| Your stripe webhook key |
  | USE_AWS	| True |


2. Set up your Database
  * In your settings.py file import dj_database_url.
  * Comment out the default DATABASES configuration and add the following:

    ```
    DATABASES = {
        'default': dj_database_url.parse('DATABASE_URL')
    }
    ```
  * Set up the database through the terminal by typing:
    ```
    python manage.py migrate
    ```

  * Load the products & category data through the terminal by typing:
    ```
    python3 manage.py loaddata categories

    python3 manage.py loaddata products
    ```

  * Create a superuser account through the terminal by typing:

    ```
    python manage.py createsuperuser
    ```

  * Replace the DATABASES configuration with the following:

      ```
      if "DATABASE_URL" in os.environ:
          DATABASES = {
              "default": dj_database_url.parse(os.environ.get('DATABASE_URL'))
          }
      else:
          DATABASES = {
              'default': {
                  'ENGINE': 'django.db.backends.sqlite3',
                  'NAME': BASE_DIR / 'db.sqlite3',
              }
          }
      ```

3. Deploy the site

  * Create a Procfile in the root directory and add the following code:
      ```
      web: gunicorn <app name>.wsgi:application
      ```
  * Log into Heroku through your IDE terminal by typing:
    ```
    heroku login -i
    ```
  * Temporarily disable static file collection by typing the following:
    ```
    heroku config:set DISABLE_COLLECTSTATIC=1 --app <app name>
    ```
    This will be re-enabled once AWS is up and running.

  * In your settings.py file add the following:
    ```
    ALLOWED_HOSTS = ["<heroku app name>.herokuapp.com", "localhost"]
    ```
  * Git commit and Git push the changes to Github

  * Deploy to Heroku through the terminal by typing:
    ```
    heroku git:remote -a <heroku app name>
    git push heroku master
    ```
  * Your app should now be deployed to Heroku.

  * As a final step, The AWS bucket [can be linked to the project](https://docs.aws.amazon.com/AmazonS3/latest/userguide/UsingBucket.html) and COLLECTSTATIC can be re-enabled. This will gather all static files including media, CSS, and js files. 
 
9. The website has now been successfully deployed.

----------------------------

## Credits 
The following material is not my own. Sources are listing below:

### Code
  * The code for this project uses the Code Institute's; 'Boutique Ado' project as a base.
  * Icon Hover effect - [Hover.CSS](https://ianlunn.github.io/Hover/)
  * Responsive home page banner -  [Bill Raymond](https://dev.to/billraymond/creating-a-pure-responsive-css-grid-hero-image-or-banner-image-2pej)



###  Media
* HTML body overlay - [Toptal Subtle Pattern, Pete Fecteau](https://www.toptal.com/designers/subtlepatterns/?s=foggy)
* Contact page, bird animation - [Lottie files](https://lottiefiles.com/23100-happy-bird)
* Bag page, empty bag animation - [Lottie files](https://lottiefiles.com/web-player?lottie_url=https%3A%2F%2Fassets8.lottiefiles.com%2Fprivate_files%2Flf30_94juvpzy.json)
* Coming soon default image -  [Pixabay, RossMannYYC](https://pixabay.com/photos/coming-soon-chalk-board-blackboard-2550190/)
* Brid image, company logo - [flaticon](https://www.flaticon.com/free-icon/bird_3069186?term=bird&page=1&position=4&page=1&position=4&related_id=3069186&origin=tag)

### Content
* Blog content - [Article Generator Online](https://articlegenerator.org/)

### Acknowledgments
* Thank you to Gerard McBride for his guidance and support throughout this project. 
* Thank you to the Code Institute tutors for their help in debugging tricky issues.
* Thank you to friends and family for their help in testing the functionality and responsiveness of the site.