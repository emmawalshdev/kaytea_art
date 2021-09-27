# Testing

## Table of Contents

1. [**Validation**](#validation)
    - [**HTML**](#html)
    - [**CSS**](#css)
    - [**JavaScript**](#javascript)
    - [**Python**](#python)
        - [**PEP8**](#pep8)
        - [**Unit Testing**](#unit-testing)
2. [**Testing User Stories**](#testing-user-stories)
3. [**Manual Testing on Live Site**](#manual-testing-on-live-site)
    - [**Desktop Manual Testing**](#desktop-manual-testing)
    - [**Mobile and Tablet Manual Testing**](#mobile-and-tablet-manual-testing)
4. [**Bugs**](#bugs)
    - [**Solved Bugs**](#solved-bugs)
    - [**Unresolved Bugs**](#unresolved-bugs)

## Validation

### HTML

The [W3C Markup Validator](https://validator.w3.org/#validate_by_input) service was used to validate the HTML code of this project.


- [page.html](pagelink) template errors:

    - **Error:** *error msg*

      **Fix:** txt.


### CSS

The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input) service was used to validate the CSS code.

- css file - errors found.

### JavaScript

[JSHint](https://jshint.com/) was used to validate the JavaScript code of the project.

warnings and fix

### Python

#### PEP8

The Flake8 Python library was used for checking the code base against the PEP8 coding style and for checking for programming errors.

All the files passed with the following errors ignored/fixed:

- ```error```

    ```error msg
    ```

    reason for ignoring/fix 



#### Unit Testing

Unit testing was carried out on all the apps in this project. The project did not use a test driven development process, the test cases were written after development.
which need more testing/which have been tested

To run these tests:

1. Clone this project from the project's [repository](repo) by following the steps in the [README.md](readme.md) under 'Clone the GitHub Repository' and run the project on your own IDE. 

2. To run all the project's tests, enter the following command in your terminal:

    ```
    python3 manage.py test
    ```

3. To run the tests for a specific app, enter the following command:

    ```
    python3 manage.py test <app name here>
    ```

4. To run the tests for a specific test file, enter the following command:

    ```
    python3 manage.py test <app name here>.<filename here>
    ``` 

    Note: do not add the extension to the filename.

5. Test results will be displayed in the terminal.


## Testing User Stories
The following section revisits the user stories identified in the UX section of README.md. The aim is to check that the site meets those needs.

### Visitor stories:
**As a visitor of the website I expect/want/need:**

**Browsing**
1. To be able to browse the website easily without feeling confused or overwhelmed. It should have a easy-to-follow layout on all device sizes.
    * The placement of site elements including the navbar, search, footer, icons, products lists, and website forms have been designed and developed to satisfy this specific UX need. 
    * The site's key pages can be accessed from both the navigation bar and the footer, which are included on all site pages.

2. To be able to search for products by text, so that I can find something specific.
    * A search bar located on the navigation bar allows the user to search by product title or description. Additionally, the user can sort the result to drill the search down even further.

3. To browse orginal artwork and prints, as these are the main categories of an artshop which I would expect to see. 
    * These categories, along with 'All Artwork' have been included in the current rollout.
    * Buttons for each category are also present within each individial page, allowing the user to easily switch views.

4. To be able to filter by price within category pages so that I can find a product to suit my budget.
    * A 'Sort by' dropdown field is presented on each cateogory page. This allows the user to sort by price and also my name.

5. To see the image, media used and canvas size of each product. This information is vital to me.
    * This information has been included in the product upload form assessible to superusers.
    * The size and media field are required. The image field is optional, and takes a default 'coming soon' image in case no picture has been saved.

6. To be able to read product reviews as this helps me to decide on the quality and level of service delivered by the company.
    * A  reviews section has been added to the product details template, allowing users to leave a review (text and rating ) and to view existing reviews.
    * To help fish out disingenuous submissions, the user must be logged in to submit a form. Alongside each review, the author's username is posted.
    * An average star rating, pinned to the product section, is calculated based on existing reviews.
    * The reviews are ordered by date. This makes sure that the most recent comments are shown first.

7. To request a quote for a pet commission so that I can decide myself whether this is something I would like to purchase. 
    * A form on the Pet Commissions page allows the user to make a service request. As stated in the page text, the Artist will then get in touch with the client to discuss a quote.
    * As well as contact information, the commission form fields include media and canvas size preference,  number of pets and a textfield for extra comments. This allows the artist to calculate a preliminary quote, before speaking to the client. 

8. To receive feedback after I interact with the website so that I am aware if the interaction has or has not been a success.
    * Toast messages provides user feedback about an operation in a small popup.
    In this release, Information, Error and Success Toast messages have been included. 

    * The user can quickly identify Success, information or error messages. Each Toast has been styled to clearly stand out with font color and icons.

    * These inform them of failed or successful interaction. Examples include form submission and user login. Toast messages also show Information and Success messages are triggered by user activity and inform the user if their interaction.
    * On success Toast messages, a summary of the user's bag contents is included (if items have been added). This keeps the user updated with their activity.
 
9. To learn more about the artist and the process behind the creations. As a supporter of small businessess, I like to feel a connection to the business owner.
    * An about page containing imagery and text, allows the user to gain a detailed insight into the Artist's life. 
    * links to the about page are feautred on the navigation bar and footer as well as on the homepage.

**Shopping**
1. To be able to navigate to my shopping cart easily so that I can quickly checkout.
    * The shopping cart is featured on the navbar which makes it easily assessible from all pages.
    * The bag icon changes color and displayed the cost total when items have been added to it. This gives the user a visual represntation of their active session. 
2. To be able to add, edit or delete items or item quantities from my shopping cart so that I can easily modify my choices.
    * Within the bag page, the user can easily update quantities or remove products entirely.
    * With every successful update or product removal, a toast message is triggered notifying the user of their action.

3. To know that the stock levels on products are accurate so that I know shipping delays won't occur. 
    * If the product is out of stock, the user will not be able to add the item to their shopping bag. An 'Out of Stock' message is instead displayed on the product page. In future rollouts, functionality to publish and unpublish the page will be investigated.

4. To receive an email after I submit an order so that I am aware the interaction had been a success.
    * Once an order is complete, an email confirmation is sent to the supplied email address.
    * A Toast message stating the transaction has been a success, is displayed.
    * The user is redirected to a 'Checkout Success' page. This contains a thank you message and a summary of the order.
    * If registered, the order summary is stored on the user's profile page and can be accessed at any time in the future.

5. My shipping details should autofill if I am logged in so that I can quickly checkout.
    * The Profile page gives the logged in user the ability to update their personal and shipping information. This infomation is used to prefill the order form on the checkout page.
    * Shipping details can also be updated on the checkout page. If the user is logged in, a checkbox labelled 'Save this delivery information to my profile' handles the request. If the user is not logged in, the message 'Login or Register to save this information.' is displayed instead.

**Customer care**
1. To be able to set up an account, so that I can login on return and view my data.
2. To be able to contact the shop owner easily in case I have a question related to my order.
3. To see a summary of my order after I make a purchase so that I can review the details.
4. To see a list of my order history so that I can check up on my recent activity. 
5. To have the choice to reset my account password in case I forget it.
6. To be able to update my account details in case a change is required.
7. To be able to connect to the company owner on social media channels so that I can keep up-to-date. 


### Business stories:
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


## Manual Testing on Live Site

### Desktop Manual Testing

Manual testing was carried on a desktop computer using Google Chrome.

#### Navigation
- Click the navbar company logo, confirm redirect to home page.
- Click the 'About' link, confirm confirm that redirect to About page.
- Click the 'Blog' link, confirm redirect to Blog page.
- Click the 'Shop' link, confirm that correct sub-links appear in dropdown menu.
- Click each link in the 'shop' dropdown menu, confirm redirect to the correct page.
- While logged out, click the 'Accoount' link. Confirm that correct sub-links appear in dropdown menu (Login and Register).
- Log in as a non-superuser, click on the 'Account' link. Confirm that the dropdown-menu displays 'My Profile' and 'Logout'.
- Log in as a superuser, click on 'Account'. 
Confirm that the dropdown-menu displays 'Product Admin', 'My Profile' and 'Logout'.
- Click each link in the 'Account' dropdown menu. Confirm redirects to correct pages.
- Add an item to the user's bag, confirm that the bag total updates to the correct value and the icon color changes to blue.
- Delete all bag items, confirm that the bag total updates to €0.00 and the icon color changes to black.
- Search for a product with in the search bar, confirm that the results of the search are displayed correctly.

#### Footer
- Click on footer links, confirm redirect to correct page.
- Click the company logo, confirm redirect to home page.
- Click on social media links, confirm redirect to correct site.

#### Homepage
- Click on the 'About' link, confirm redirect to about page.
- Hover over the category cards, confirm text color change to blue and hover effect.
- Click on each category card, confirm redirect to correct page.
- Click on the Pet Commision 'Read More' link, confirm redirect to commissions page.

#### Products Page
- Click on each of the category buttons. Confirm redirect to correct page. 
- Click each option within the 'Sort by' dropdown menu, confirm the the expected result appears.
- Click on the card image for each product, confirm redirect to correct page.
- Click on the each of the card category tags, confirm redirect to correct category page.  
- Hover over each product card, confirm that a shadow effect is applied.
- Click the category for each product, confirm each product for that category is displayed.
- Click on the 'back to top' button. Confirm navigation to the top of page.

#### Product Admin Page
- Attempt to access the 'Product Admin' page while logged in as a non superuser by URL. Confirm redirect to homepage, along with the display of an Error toast message.
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
    - Choose a quantity and 'Add to Bad'. 'Confirm that the navbar bag quantity and total updates.
    - Click the 'Keep Shopping' button, confirm redirect to the all products category page.
    - Confirm that the average rating is correct based on the existing product reviews.

* Reviews section
    - Confirm the message 'No reviews yet!' is displayed for a product that has no reviews. 
    - Logout. Confirm that the 'Please Login' to leave a review message is displayed.
    - Login, confirm that the review form is visible.
    - Attempt to submit the form with invalid data, confirm the relevant warning message is displayed.
    - Submit a valid form, confirm that new review is added. Check that reviews are ordered by date, showing the username, rating and comment.
    - Confirm that the product average rating updates, based on the new submitted rating.
 
#### Bag Page
- Click on the bag icon with no items added. Confirm that message 'Your bag is empty!' is displayed. Confirm that both the 'Login' and 'Continue Shopping' buttons are working.

- Click on the bag icon having added items. Confirm the correct products and quantities are present. Confirm secondly, confirm that the subtotal, delivery and total figures are correct.

- Adjust the quantity of a product within the bag and click the update button. Confirm that the quantity, subtotal, delivery and total costs update.

- Click the 'Remove' button for a product, confirm that the product is deleted from the bag and the basket and the quantity, subtotal, delivery and total costs update.

- Confirm that a bag total that is less than €50 has a delivery charge of 20% the subtotal.

- Confirm that a bag total that is more than €50 has no delivery charge.

- Click the 'Secure Checkout' button, confirm redirect to the checkout page.

#### Checkout Page
- Attempt to access the checkout page by URL with an empty bag, Confirm redirect to the homepage with an error message.

- Confirm that the products in the order summary box are correct.
    Secondly, confirm that the quantity, subtotal, delivery and total costs update.

- Login to an account with saved delivery information on their profile, confirm that the order form is prepopulated with this delivery information.

- Confirm that a 'Save this delivery information' checkbox is shown for logged in users, under the checkout form. For logged out users, confirm that this is replaced by 'Login or Register' links. Confirm that each of these behaves correctly.

- Click the 'Adjust basket' button, confirm redirect to the bag page.

- Attempt to submit the form with incorrect data, confirm the correct warning messages are displayed.

* Submitting a Valid form
    - Confirm that the loading overlay is displayed followed by a redirect to the 'Checkout Success' page.  Confirm that a success toast message is shown, stating that a confirmation email has been sent. On the template page, confirm that the correct details are displayed in the 'Order summary box'.

    - Click on the 'Continue Shopping' link, confirm redirect to the 'view all' products page.

    - Confirm that a confirmation email is sent to the user.

#### Profile Page
* Order history section
    - Confirm the order history correctly contains a list of past orders.
    - Click on an order number, confirm that the correct order details are rendered.
    Confirm that an information message is displayed, stating that this is a past order.
    - Click on the 'Back to Profile' button, confirm redirect to profile page.

* Profile form
    - Add or edit default delivery information, click the 'Update Information' button. Confirm that the information correctly updates.
    - Click on the bag icon having added items. Confirm that the order form is pre-filled with the users delivery details.

#### Blog Page

- Confirm the 'Blog Blog' button is only visible to logged in superusers. Click button. Confirm redirect to 'Add Blog' page.

- Click on a blog image, confirm it directs to the correct blog details page.

- Click on the 'read more' link and blog image, confirm redirect to the correct blog detail page.

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


## Bugs

### Solved Bugs

1. When attempting to add a new image to a blog/product and remove an existing image at the same time, an error occured.

2. Adding an item with zero stock dissallowed.



### Unresolved Bugs

2. After deploying to Heroku, Issues were encountered while working locally.
This has temporarily been fixed by running command on workspage setup
```
unset DATABASE_URL
```
To permanently fix this issue, futher investigation is required.


> [Back to Top](#table-of-contents)
