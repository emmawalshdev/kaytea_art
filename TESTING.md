# Testing

## Table of Contents

1. [**Validation**](#validation)
    - [**HTML**](#html)
    - [**CSS**](#css)
    - [**JavaScript**](#javascript)
    - [**Python**](#python)
        - [**PEP8**](#pep8)
        - [**Unit Testing**](#unit-testing)
        - [**Coverage**](#coverage)
2. [**Testing User Stories**](#testing-user-stories)
3. [**Manual Testing on Live Site**](#manual-testing-on-live-site)
    - [**Desktop Manual Testing**](#desktop-manual-testing)
    - [**Mobile and Tablet Manual Testing**](#mobile-and-tablet-manual-testing)
4. [**Bugs**](#bugs)
    - [**Solved Bugs**](#solved-bugs)
    - [**Unresolved Bugs**](#unresolved-bugs)

## Validation

### HTML

The [W3C Markup Validator](https://validator.w3.org/#validate_by_input) service was used to validate all HTML code.

* All issues causing errors were rectified. Such errors included using multiple id attributes, missing closing tags and the misuse of tags.

* Issues resulting in a warning have not been rectified. These are not critical and will be dealt with in the future.

### CSS

The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) service was used to validate all CSS code.

* All issues casuing erros were rectified. Such errors inluced minor issues including invalid CSS properties.

* Issues resulting in a warning have not been rectified. These are not critical and will be dealt with in the future.

### JavaScript

[JSHint](https://jshint.com/) was used to validate all JavaScript code.

* All errors found, were concerend with missing semicolons. These were added to rectify the code.

* All warnings are not critical and have been safely ignored. The use of 'let' which is available in ES6 was flagged.

### Python

#### PEP8

The Flake8 Python library was used to check the project code base against coding style (PEP8).
The initial report can be found [here](https://www.dropbox.com/s/txpx7wyzxl74vck/flake8_results.txt?dl=0).

**General information**
* Errors generated were concerned with trailing whitepaces, libraries imported but never used, unnecessary blank lines, missing blank lines, lines which were too long and the innapropriate use of null=True on model fields. In rectifying these issues, the following files were ignored:

    * All Auto migration files were ignored. 
    * In settings.py,  auto-generated lines were ignored.
    * In all files, the Rule DJ01 - 'Avoid using null=True on string-based fields such as CharField and TextField' was ignored.

**Resolution**

After adjusting the code, all files passed with the following errors being safely ignored:

- ```./products/widgets.py:9:80: E501 line too long (87 > 79 characters) ```

    This was ignored as the URL cannot be split.

- ```./contact/forms.py:5:1: DJ07 Do not use __all__ with ModelForm, use fields instead```
    
    Not a critical error, ignored.

- ```./checkout/apps.py:8:9: F401 'checkout.signals' imported but unused```
    
    Not a critical error, ignored.

#### Unit Testing

Basic view and URL testing has been carried out on all apps within this project. In future releases,  more extensive automated tests would be advised to thoroughly test the code. 

**Information on TDD**

At this time, the project does not use a Test Driven Development.
As creating comprehensive texts can be a lengthy and complex process, TDD is something which will be attempted in the future. 

**How to run Python tests**

1. Activate your virtual environment.

2. To run all tests, enter the following command in your terminal:

    ```
    python3 manage.py test
    ```

3. To run tests for a specific app, enter the following command terminal:

    ```
    python3 manage.py test <app name>
    ```

3. Test results will be displayed in the terminal.

    ![Python test results](https://i.ibb.co/JHCgV4g/Python-Tests.jpg)

#### Coverage
[Coverage.py](https://coverage.readthedocs.io/en/coverage-5.5/) was used to measures the execution of Python files in this project.

**How to run coverage**

1. Activate your virtual environment.

2. Install coverage by runnning the following command:

    ```
    pip3 install coverage
    ```

2. To run all tests, enter the following command in your terminal:

    ```
    coverage run manage.py test -v 2 && coverage report
    ```

3. To run tests for a specific app, enter the following command terminal:

    ```
    coverage run --source "<app name>" manage.py test -v 2 && coverage report
    ```

3. Test results will be displayed in the terminal.

**Results**

- About app

    ![About app coverage results](https://i.ibb.co/k30s0x1/about.jpg)

- Bag app

    ![Bag app coverage results](https://i.ibb.co/p0nvbQQ/bag.jpg)

- Blog app

    ![Blog app coverage results](https://i.ibb.co/ZJ1ZPG0/blog.jpg)

- Checkout app

    ![Checkout app coverage results](https://i.ibb.co/QdJCJnb/checkout.jpg)

- Commissions app

    ![Commissions app coverage results](https://i.ibb.co/D1bzjsX/commissions.jpg)

- Contact app

    ![Contact app coverage results](https://i.ibb.co/j6V0JM4/contact.jpg)

- Home app

    ![Home app coverage results](https://i.ibb.co/3mFL51y/home.jpg)

- Products app

    ![Products app coverage results](https://i.ibb.co/tXDwqjK/products.jpg)

- Profiles app

    ![Profiles app coverage results](https://i.ibb.co/wCV0rSw/profiles.jpg)


## Testing User Stories
The following section revisits the previously outlined user stories. These have been listed in the UX section of [README.md](https://github.com/emmahartedev/kaytea_art/blob/main/README.md).

### Visitor stories:
**As a visitor of the website I expect/want/need:**

**Browsing**
1. To be able to browse the website easily without feeling confused or overwhelmed. It should have a easy-to-follow layout on all device sizes.
    * The placement of site elements including the navbar, search bar, footer, icons, products lists, and website forms have been designed and developed to satisfy this specific UX need. 
    * The site's key pages can be accessed from both the navigation bar and the footer, which are included on all site pages.

2. To be able to search for products by text, so that I can find something specific.
    * A search bar located on the navigation bar allows the user to search by product title or description. Additionally, the user can sort results to drill down their search even further.

3. To browse orginal artwork and prints, as these are the main categories of an artshop which I would expect to see. 
    * These categories, along with 'All Artwork' have been included in the current rollout.
    * Buttons for each category are also present within each individial page, allowing the user to easily switch views.

4. To be able to filter by price within category pages so that I can find a product to suit my budget.
    * A 'Sort by' dropdown field is presented on each cateogory page. This allows the user to sort by price and also my name.

5. To see the image, media used and canvas size of each product. This information is vital to me.
    * This information has been included in the product upload and the data is present on the product detail page.
    * The size and media field are required (upon upload). The image field is optional, and takes a default 'coming soon' image if no picture has been saved.

6. To be able to read product reviews as this helps me to decide on the quality and level of service delivered by the company.
    * A  reviews section has been added to the product details template, allowing users to leave a review (text and rating) and to view existing reviews.
    * To help fish out disingenuous submissions, the user must be logged in to submit a form. Alongside each review, the author's username is posted.
    * An average star rating, pinned to the product section, is calculated based on existing reviews.
    * The reviews are ordered by date. This makes sure that the most recent comments are shown first.

7. To request a quote for a pet commission so that I can decide myself whether this is something I would like to purchase. 
    * A form on the Pet Commissions page allows the user to make a service request. As stated in the page text, the Artist will then get in touch with the client to discuss a quote.
    * As well as contact information, the commission form indludes the following fields: 
        - Media preference
        - Canvas size preference
        - Number of pets
        - Textfield for extra comments
    
        This allows the artist to calculate a preliminary quote, before speaking to the client. 

8. To receive feedback after I interact with the website so that I am aware if the interaction has or has not been a success.
    * Toast messages provide user feedback about an operation in a small popup.
    In this release, Information, Error and Success Toast messages have been included. 

    * The user can quickly identify Success, information or error messages. Each Toast has been styled to clearly stand out with font colors and icons.

    * The message informs the user of failed or successful interaction. Examples include form submission and user login.

    * On success Toast messages, a summary of the user's bag contents is included (if items have been added). This keeps the user updated with their activity.
 
9. To learn more about the artist and the process behind the creations. As a supporter of small businessess, I like to feel a connection to the business owner.
    * An About page containing imagery and text, allows the user to gain a detailed insight into the Artist's life. 
    * Links to the about page are feautred on the navigation bar and footer as well as on the homepage.

**Shopping**
1. To be able to navigate to my shopping cart easily so that I can quickly checkout.
    * The shopping cart is featured on the navbar which makes it easily assessible from all pages.
    * The bag icon changes color and displays the cost total when items have been added to it. This gives the user a visual represntation of their active session. 

2. To be able to add, edit or delete items or item quantities from my shopping cart so that I can easily modify my choices.
    * Within the bag page, the user can easily update quantities or remove products entirely.
    * With every successful update or product removal, a toast message is triggered notifying the user of their action.

3. To know that the stock levels on products are accurate so that I know shipping delays won't occur. 
    * If the product is out of stock, the user will not be able to add the item to their shopping bag. An 'Out of Stock' message is instead displayed on the product page. In future rollouts, functionality to publish and unpublish the page will be investigated.

4. To receive an email after I submit an order so that I am aware the interaction had been a success.
    * Once an order is complete, an email confirmation is sent to the supplied email address.
    * A Toast message stating the transaction has been a success, is displayed.
    * The user is redirected to a 'Checkout Success' page. This contains a thank you message and a summary of the order.
    * If the user is registered, the order summary is stored on the user's profile page and can be accessed at any time in the future.

5. My shipping details should autofill if I am logged in so that I can quickly checkout.
    * The Profile page gives the logged in user the ability to update their personal and shipping information. This infomation is used to prefill the order form on the checkout page.
    * Shipping details can also be updated on the checkout page. If the user is logged in, a checkbox labelled 'Save this delivery information to my profile' handles the request. If the user is not logged in, the message 'Login or Register to save this information.' is displayed instead.

**Customer care**
1. To be able to set up an account, so that I can login on return and view my data.
    * Customised allauth Login and Register pages have been built, allowing the user to register and login to an account.
    * On the Profile page, the user is able to add and edit their personal and shipping information.
    * Setting up an account and logging in allows the user to review products and leave blog comments. 
       
2. To be able to contact the shop owner easily in case I have a question related to my order.
    * A Contact page is accessible from the navigation bar and footer,  which is visible on all website pages.
    * The contact form welcomes all general enquiries from users.

3. To see a summary of my order after I make a purchase so that I can review the details.
    * After an order has been submitted, an email confirmation is sent to the supplied email address. This can be kept by the customer for their own personal record.  
    * Upon order submission, the user is redirected to a 'Checkout Success' page. This contains a thank you message and a summary of the order.
    * If registered (and logged in), the order summary is stored on the user's profile page and can be accessed at any time in the future.


4. To see a list of my order history so that I can check up on my recent activity. 
    * If the user is registered (and logged in), the order summary is stored on the user's profile page and can be accessed at any time in the future.


5. To be able to update my account details in case a change is required.
    * The Account page gives the logged in user the ability to update their first name, last name and mobile number.
    At the moment the user cannot change their email address, username or password. This will be included in future releases. 


6. To be able to connect to the company owner on social media channels so that I can keep up-to-date. 
    * Social media links are located on the website footer, which is visible on all pages.


### Business stories:

**As a superuser of the website I expect/want/need:**

**General**
1. Build a beautiful, easy-to-use, trustworthy website so that I can build brand awareness and sell artwork.
    * The website has been designed in collaboration with Katie, who had a clear idea on color scheme and layout.
    * The placement of site elements including the navbar, search bar, footer, icons, products lists, and website forms have been designed and developed to satisfy this specific UX need. 
    * The site's key pages can be accessed from both the navigation bar and the footer, which are included on all site pages.

2. To be able to view customer/order/product data so that I easily pull up information if required. 
    * The admin site allows the superuser to view a host of information including form submissions, orders, products, customer and user data.
    * The supe user has full CRUD capabilities within the admin panel. E.g, adding, editing and removing a product.


**Website admin**
1. To be able to add/edit and delete products on the website so that I can keep the information up-to-date.
    * The 'Product Admin' link under 'Account' on the navigation bar allows the user to add a product to the store.
    * The 'Post Blog' button on the blog overview page allows the user to add a blog to the site.
    * Edit and delete buttons are visible within product pages only to the superuser. 
    * All CRUD operations can be easily executed from the Admin site.


2. To be able to add/edit and delete blog content on the website so that I can keep the page fresh.
    * The 'Post Blog' button on the blog overview page allows the user to add a blog to the site.
    * Edit and delete buttons are visible within blog detail pages, only to the superuser. 
    * All CRUD operations can be easily executed from the Admin site.


**Online shop admin**
1. To receive order notifications so that I begin preparing these.
    * The order will be saved to both stripe and the admin panel.
    * In a future release, a webhook will also be setup to notify the superuser by email.

2. To be able to provide a commision quote based on canvas size and number of pets. This would help me to better understand the user's needs before I contact them. 
    * 'Canvas size' and 'number of pets' fields have been included on the pet commissions form. This information, along with contact details for the user is designed to help the Artist calculate a rough quote.

## Manual Testing on Live Site

### Desktop Manual Testing

Manual testing was carried on a desktop computer using Google Chrome.

#### Navigation
- Click the navbar company logo, confirm redirect to home page.
- Click the 'About' link, confirm confirm redirect to About page.
- Click the 'Blog' link, confirm redirect to Blog page.
- Click the 'Shop' link, confirm that correct sub-links appear in dropdown menu.
- Click each link in the 'Shop' dropdown menu, confirm redirect to the correct page.
- While logged out, click the 'Account' link. Confirm that correct sub-links appear in dropdown menu (Login and Register).
- Login as a non-superuser, click on the 'Account' link. Confirm that the dropdown-menu displays 'My Profile' and 'Logout'.
- Login as a superuser, click on 'Account'. 
Confirm that the dropdown-menu displays 'Product Admin', 'My Profile' and 'Logout'.
- Click each link in the 'Account' dropdown menu. Confirm redirects to correct pages.
- Add an item to the user's bag, confirm that the bag total updates to the correct value and the icon color changes to blue.
- Delete all bag items, confirm that the bag total updates to €0.00 and the icon color changes to black.
- Search for a product within the search bar, confirm that the results of the search are displayed correctly.

#### Footer
- Click on footer links, confirm redirect to correct page.
- Click the company logo, confirm redirect to home page.
- Click on social media links, confirm redirect to correct site.

#### Homepage
- Click on the 'About' link, confirm redirect to about page.
- Hover over the category cards, confirm text color change to blue and hover effect.
- Click on each category card, confirm redirect to correct page.
- Click on the Pet Commision 'Read More' link, confirm redirect to Commissions page.

#### Products Page
- Click on each of the category buttons. Confirm redirect to correct page. 
- Click each option within the 'Sort by' dropdown menu, confirm that the expected result appears.
- Click on the card image for each product, confirm redirect to correct page.
- Click on each of the card category tags, confirm redirect to correct category page.  
- Hover over each product card, confirm that a shadow effect is applied.
- Click on the 'back to top' button. Confirm navigation back up to the top of the page.

#### Product Admin Page
- Attempt to access the 'Product Admin' page while logged in as a non superuser. Confirm redirect to homepage, along with the display of an Error toast message.
- Attempt to access the 'Product Admin' page while logged out. Confirm redirect to Login page.
* Form submission
    - Submit the form with incorrect data, confirm the relevant warning messages are displayed.
    - Submit a valid form, confirm redirect to the new product page.
    - Confirm that a default image is displayed for products which do not have a saved image.


#### Product Detail Page
* Product section
    - Click on the product image, confirm that the image opens in a new tab.
    - Click on the product category, confirm redirect to correct category page.
    - Login as a superuser, confirm that the edit and delete buttons are visible. Click on each button, confirm that the correct template/popup is rendered.
    - Delete the product, confirm that it is removed from the store.
    - Choose a quantity and click 'Add to Bag'. Confirm that the bag quantity and total updates on the navigation nag icon.
    - Click the 'Keep Shopping' button, confirm redirect to the 'All Artwork' category page.
    - Confirm that the average rating is correct, based on the existing product reviews.

* Reviews section
    - Confirm the message 'No reviews yet!' is displayed for a product that has no reviews. 
    - Logout. Confirm that the 'Please Login' to leave a review message is displayed.
    - Login, confirm that the review form is visible.
    - Attempt to submit the form with invalid data, confirm the relevant warning message is displayed.
    - Submit a valid form, confirm that the new review is added. Check that the reviews are ordered by date, showing the username, rating and comment.
    - Confirm that the product average rating updates, based on the new submitted rating.
 
#### Bag Page
- Click on the bag icon with no items added. Confirm that message 'Your bag is empty!' is displayed. Confirm that both the 'Login' and 'Continue Shopping' buttons are working.

- Click on the bag icon having added items. Confirm the correct products and quantities are present. Secondly, confirm that the subtotal, delivery and total figures are correct.

- Adjust the quantity of a product within the bag and click the update button. Confirm that the quantity, subtotal, delivery and total costs update.

- Click the 'Remove' button for a product, confirm that the product is deleted from the bag. Secondly, confirm that the bag quantity, subtotal, delivery and total costs update.

- Confirm that a bag total of less than €50 has a delivery charge of 20% the subtotal.

- Confirm that a bag total of more than €50 has no delivery charge.

- Click the 'Secure Checkout' button, confirm redirect to the Checkout page.

#### Checkout Page
- Attempt to access the Checkout page by URL with an empty bag, Confirm redirect to the homepage with an error message.

- Within the order summary box, confirm that the products in the are correct.

- Login to an account with saved delivery information, confirm that the order form is prepopulated with this delivery information.

- Confirm that a 'Save this delivery information' checkbox is shown for logged in users, under the checkout form. For logged out users, confirm that this is replaced by 'Login or Register' links. Confirm that each of these behaves correctly.

- Click the 'Adjust basket' button, confirm redirect to the Bag page.

- Attempt to submit the form with incorrect data, confirm the correct warning messages are displayed.

* Submitting a valid form
    - Confirm that the loading overlay is displayed followed by a redirect to the 'Checkout Success' page.  Confirm that a success toast message is shown, stating that a confirmation email has been sent. On the template page, confirm that the correct details are displayed in the 'Order summary box'.

    - Click on the 'Continue Shopping' link, confirm redirect to the 'All Artwork' products page.

    - Confirm that a confirmation email is sent to the user.

#### Profile Page
* Order history section
    - Confirm the order history correctly contains a list of past orders.
    - Click on an order number, confirm that the correct order details are rendered.
    Confirm that an information message is displayed, stating that this is a past order.
    - Click on the 'Back to Profile' button, confirm redirect to Profile page.

* Profile form
    - Add or edit default delivery information, click the 'Update Information' button. Confirm that the information correctly updates.
    - Click on the bag icon having added items. Confirm that the order form is pre-filled with the user's delivery details.

#### Blog Page

- Confirm the 'Post Blog' button is only visible to logged in superusers. Click button, confirm redirect to 'Add Blog' page.

- Click on a blog image, confirm redirect to the correct blog detail page.

- Click on the 'read more' link, confirm redirect to the correct blog detail page.

- Confirm pagination links are working correctly.

#### Add Blog Page
- Attempt to access the 'Add Blog' page while logged in as a non superuser by URL. Confirm redirect to homepage, along with the display of an Error toast message.

- Attempt to access the 'Add Blog' page while logged out. Confirm redirect to Login page.

* Form submission
    - Submit the form with incorrect data, confirm the relevant warning messages are displayed.
    - Submit a valid form, confirm redirect back to the blog overview page, with the new blog post appearing in the first position.
    - Confirm that a default image is displayed for blogs which do not have a saved image.

#### Blog Detail Page

* Blog section
    - Click on the blog image, confirm that the image opens in a new tab.
    - Login as a superuser, confirm that the edit and delete buttons are visible. Click on each button, confirm that the correct template/popup is rendered.
    - Delete the blog, confirm that it is removed from overview page.

* Comments section
    - Confirm the message 'No comments yet!' is displayed for a blog that has no comments. 
    - Logout. Confirm that the 'Please Login' to leave a comment message is displayed.
    - Login, confirm that the comment form is visible.
    - Attempt to submit the form with invalid data, confirm the relevant warning message is displayed.
    - Submit a valid form, confirm that new comment is added. Check that comments are ordered by date, showing the username and comment.

 
### Mobile and Tablet Manual Testing

The desktop tests listed above were repeated for mobile and tablet devices.

First, Chrome developer tools was used to test the site on the iPhone5/SE, iPhone 6/7/8, iPad and iPad Pro.

Secondly, the site was tested on physical devices. Specifically, the devices included a Samsung Galaxy s7, iPhone 11 and a Samsung Galaxy Tab A7.

Additional manual testing included the following:

* Navigation
    * Confirm that the navigation collapses into a hamburger icon.
    * Confirm that all links are located within the collapsed menu and work as expected.
    * Confirm that the main logo is displayed within the hamburger menu.
    * Click on the search icon, confirm that the search bar opens below the navbar and functions correctly.
    * Add a product to the bag, confirm the bag value updates and the icon changes color.

* Footer
    * Confirm that the mobile view behaves as expected. The logo should appear on top, with the links below.

* Toast message
    * Confirm that Toast message alignment is correct. This should appear below the navbar and to the far right.

## Bugs

### Solved Bugs

1. **Multiple image uploads**

    When attempting to add a new image to a blog/product and remove an existing image at the same time, a toast error message occured. I discovered this was caused by the image limitation of 1, set to this project. As allowing multiple images is not a feauture planned for this release, no changes were made to this setting. 
    A temporary fix to hide the 'select image' button (if an image already has been uploaded) was added instead. This forces the user to first remove the image before adding a new one. 

2. **Adding an item with zero stock disallowed.**

    Understandably, Django threw an error for products with stock level < 0 which were added to the bag. Preferably, I would like to add a boolean 'publish' feature which would unpublish the product when stock level is 0.
As a temporary fix, the 'Add to Bag' button was hidden and a short message shown.


3. **Model migrations not working on Heroku.**

    After deployement, I continued to alter and create models. While this worked locally, no changes were reflected on the deployed site.
    When attempting to access the models from the admin site, a 500 error was thrown. I discoved that the migrations had not successfully migrated to the live site and was able to resolve this by running ```python3 manage.py runserver``` directly on the heroku console.

### Unresolved Bugs

2. **DATABASES is improperly configured**

    After deploying to Heroku, issues were encountered on the locally site. The error message states that [settings.DATABASES is improperly configured](https://i.ibb.co/L85QJpQ/database-url-error.jpg).
    I discoved that this issue is casued by the CI template and how it has configured the database within the dockerfile. As a short term fix, the following command is run on startup: 
    ```
    unset DATABASE_URL
    ```  
    While this temporarily fixes the issue for the active session, I am yet to find a permanent solution.


> [Back to Top](#table-of-contents)
