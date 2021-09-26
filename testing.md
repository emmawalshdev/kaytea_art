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

#### Product Detail Page
* Product section
    - Click on the product image, confirm that the image in a new tab.
    - Click on the product category, confirm redirect to correct category page.
    - Login as a superuser, confirm that the edit and delete buttons are visible. Click on each button, confirm that the correct template/popup is rendered.
    - Delete the product, confirm that it is removed from the store.
    - Choose a quantity and 'Add to Bad'. 'Confirm that the navbar bag quantity and total updates.
    - Click the 'Keep Shopping' button, confirm redirect to the all products category page.
    - Confirm that the average rating is correct based on the existing product reviews.

* Reviews section
    - Confirm the message 'No reviews yet!' is displayed for a product that has no reviews. 
    - Logout. Confirm that the 'Please Login' message is displayed.
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


### Mobile and Tablet Manual Testing


## Bugs

### Solved Bugs

1. When attempting to add a new image to a blog/product and remove an existing image at the same time, an error occured.



### Unresolved Bugs



> [Back to Top](#table-of-contents)
