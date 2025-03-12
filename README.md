![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

# Naveena's Store

![Naveena'sStore_ResponsiveImg]()

## Description

Welcome to Naveena's Store, your one-stop destination for premium, handmade scented candles and reed diffusers. We specialize in creating products infused with natural essences, designed to enhance your home with delightful fragrances. Although we’re a new and growing brand in the candle and diffuser market, we are committed to offering high-quality, eco-friendly products that bring warmth, relaxation, and a touch of elegance to any space.

This project was developed as part of Code Institute's Full Stack Software Developer program.

#### - By Priyanka Dhanabal

The live version of the project can be viewed [here]()

You can check out my Repository [here]()

## Table of contents



# Project Research and Preparation

For the development of this project, I adopted **Agile development** methodologies to ensure a flexible and iterative approach.

To manage and track the progress of user stories during the project, I created a Kanban Board board. The board was divided into four columns: **Epics**, **To Do**, **In Progress**, and **Done**.

- Epics: This column contained overarching goals that grouped related user stories together.
- To Do: At the start of each iteration, user stories to be completed were moved here.
- In Progress: As work began on a user story, it was moved to this column.
- Done: Completed user stories were moved to this column to indicate they were finished.

This setup provided a clear and simple way to track the status of tasks throughout the project, ensuring that progress was organised and transparent.

## Naveena's Store User Stories

#### EPICS

### Admin

- As an admin, I can assign products to specific categories so that users can find them more easily during browsing.
- As an admin, I can upload, update, or delete product images so that products are visually appealing and well-represented.
- As an admin, I can edit existing product details (e.g., name, price, description, stock) so that the catalogue stays accurate and up-to-date.
- As an admin, I can add new products to the catalogue so that users can see and purchase the latest items available.
- As an admin, I can delete products from the catalogue so that unavailable items no longer appear on the site.
- As an admin, I can sort products in the admin panel by various criteria (e.g., name, price,) so that I can manage the catalogue more efficiently.
- As an admin, I can view all messages submitted by users in a structured format so that I can respond to inquiries efficiently.
- As an admin, I can process payments using Stripe so that I can handle transactions securely and reliably.

### User

- As a user, I can fill out a contact form on the website so that I can send inquiries or feedback to the company.
- As a user, I can see a detailed breakdown of my order total, including discounts and shipping, so that I understand the final price I am paying.
- As a user, I can receive an email confirmation after completing my order so that I know my transaction was successful.
- As a user, I can view a summary of the products in my cart so that I can confirm my order is correct before checkout.
- As a user, I can experience a clean and professional design so that I feel confident shopping on a high-quality website.
- As a user, I can access a clear and well-organised navigation menu so that I can find the information or products I need without frustration.
- As a user, I can access the website on my mobile device so that I can browse and shop seamlessly on the go.
- As a user, I can see visual or textual feedback when interacting with elements (e.g., buttons or forms) so that I know my actions have been registered.
- As a user with disabilities, I can use assistive technologies (e.g., screen readers) to navigate the site so that I can access the same features as any other user.
- As a user, I can experience minimal load times on every page so that I don't lose interest or abandon the site.
- As a user, I can access a secure checkout process so that I feel confident that my payment details are safe.

### Returning Visitor Goals
- As a returning user, I can securely save my payment details so that future purchases are faster and easier.
- As a returning user, I can review my previous purchases so that I can reorder or track my past orders.
- As a returning user, I can leave reviews for products I’ve purchased so that I can share feedback with other users.

### Landing page on desktop 

![Home Landing Page of site]()

### Landing page on mobile

![Home Landing page mobile]()

## E-Commerce Business Model

Naveena's Store operates on a B2C (Business-to-Consumer) model, offering high-quality, handmade scented candles and reed diffusers directly to our valued customers. Through our easy-to-navigate e-commerce platform, we ensure a seamless shopping experience, where individual consumers can explore, select, and purchase our products with convenience. Our focus is on providing exceptional products that enhance your home environment, all while maintaining a personal touch and commitment to customer satisfaction.

## Marketing Strategies

Search Engine Optimization (SEO)
Optimize for Relevant Keywords: Focusing on keywords related to scented candles, reed diffusers, and natural home fragrance products. Use these keywords throughout your website and blog to improve your search engine rankings and visibility.

Marketing is done on customer satisfaction where they would use word of mouth to spread the word about our products. At Fitness Fanatic a Facebook webpage was also setup to spread the word about our products that we offer [Facebook Page]()

[Goto Top](#Table of contents)

## Planning 

## Entity Relationship Diagram
The entity relationship diagram for this project can be seen below.

1. The profiles_userprofile model has a one-to-one relationship with the auth_user model, as each user can have only one profile.

2. The products_product model has a one-to-many (Foreign Key) relationship with the products_category model, as each product belongs to one category, but a category can have many products.

3. The products_review model has:
   - A one-to-many (Foreign Key) relationship with the auth_user model, as one user can post many reviews.
   - A one-to-many (Foreign Key) relationship with the products_product model, as one product can have many reviews.

4. The account_emailaddress model has a one-to-one relationship with the auth_user model, as each user can have one primary email address.

5. The account_emailconfirmation model has a one-to-many (Foreign Key) relationship with the account_emailaddress model, as one email address can have multiple confirmations.

6. The checkout_order model has a one-to-many (Foreign Key) relationship with the profiles_userprofile model, as one user profile can have many orders.

7. The checkout_orderlineitem model has:
   - A one-to-many (Foreign Key) relationship with the checkout_order model, as one order can have many line items.
   - A one-to-many (Foreign Key) relationship with the products_product model, as many line items can represent one product.

8. The contact_contactmessage model has a one-to-many (Foreign Key) relationship with the auth_user model, as one user can send many contact messages.

Below is the Entity Relationship Diagram (ERD) for the Maison Lavaux project, which visualises the relationships between the various models in the database.

![Naveena's Store ERD]()

[Goto Top](#Table of contents)

## Wireframes

### About

![About]()

[Goto Top](#Table of contents)

### Contact

![Contact]()

[Goto Top](#Table of contents)

### Bag

![bag]()

[Goto Top](#Table of contents)

### Checkout

![Checkout]()

[Goto Top](#Table of contents)

### Home Page/ Landing Page

![Home Page]()

[Goto Top](#Table of contents)

### Product new arrivals

![Product new arrivals]()

[Goto Top](#Table of contents)

### Products

![Products]()

[Goto Top](#Table of contents)

### User Profile

![User Profile]()

[Goto Top](#Table of contents)

### Product Management for Admin

![Product Management for Admin]()

[Goto Top](#Table of contents)

### Design

Color Palette: 
-   The color scheme is kept simple by opting mainly for a combination of Black/marroon text set against the light backgrounds and White text against the dark backgrounds.  Throughout the site, the user will see light and calming, welcoming colors like this when hovering over certain sections as well as colorful buttons on each page.

Color Scheme:
- Text: #000 / rgb(82, 0, 0)
- Body Background: Image taken from google images

Typography:
- Imported Lato from Google fonts user as the primary font, and Sans-Serif used as the secondary font.

[Goto Top](#Table of contents)

## Technologies Used
  - HTML
  - Python
  - CSS
  - JavaScript
  - Django used as the Python framework for the site
  - AWS S3 used for online static and media file storage
  - PostgresSQL used as the relational database management
  - Heroku used for hosting the site
  - GitHub for storing repository of development
  - GitPod used for cloud IDE
  - Balsamiq used for wireframing
  - Bootstrap 4 used for frontend framework
  - favicon.io used to make favicon for the site

#### dependencies 

app | version
--- | ---
django-storages | 1.14.5
gunicorn | 23.0.0
jmespath | 1.0.1
oauthlib | 3.2.2
pillow | 10.3.0
psycopg2 | 2.9.10
PyJWT | 2.10.1
python3-openid | 3.2.0
pytz | 2025.1
requests-oauthlib | 2.0.0
s3transfer | 0.11.4
sqlparse | 0.5.3
stripe | 11.6.0

[Goto Top](#Table of contents)

## Deployment
  This project was developed using GitPod. The web application is deployed on Heroku. All Static and media files are stored via Amazon AWS S3. The repository is hosted on GitHub.

[Goto Top](#Table of contents)

### Clone GitHub Repository

  By Cloning a GitHub repository you can create a local copy of a GitHub remote repository.
  Cloning is done via the following steps

  - 1. Login to GitHub
  - 2. Navigate to the main GitHub repository that you want to clone
  - 3. Click on the green dropdown button Code
  - 4. To clone the repository using HTTPS under HTTPS copy the link
  - 5. Open command prompt
  - 6. Change to the directory you want to create the repository in
  - 7. Type git clone and paste the URL you copied in step 4.
    ``` $ git clone https://github.com/your-username/your-repository```
  - 8. Press enter. Your local copy of the repository will be created

For this project GitPod IDE was used so I just had to create a workspace and connect to GitHub by choosing the repository.
Once the workspace opened in GitPod 

To install the dependencies from the command line in GitPod
pip3 install -r requirements.txt


## Deployment
  This project was developed using GitPod. The web application is deployed on Heroku. All Static and media files are stored via Amazon AWS S3. The repository is hosted on GitHub.

[Goto Top](#Table of contents)

### Clone GitHub Repository

  By Cloning a GitHub repository you can create a local copy of a GitHub remote repository.
  Cloning is done via the following steps

  - 1. Login to GitHub
  - 2. Navigate to the main GitHub repository that you want to clone
  - 3. Click on the green dropdown button Code
  - 4. To clone the repository using HTTPS under HTTPS copy the link
  - 5. Open command prompt
  - 6. Change to the directory you want to create the repository in
  - 7. Type git clone and paste the URL you copied in step 4.
    ``` $ git clone https://github.com/your-username/your-repository```
  - 8. Press enter. Your local copy of the repository will be created

For this project GitPod IDE was used so I just had to create a workspace and connect to GitHub by choosing the repository.
Once the workspace opened in GitPod 

To install the dependencies from the command line in GitPod
pip3 install -r requirements.txt

Make migrations and setup initial database operations
on the CLI in GitPod enter python3 manage.py makemigrations
then
python3 manage.py migrate

To setup the categories and products copy over the media file and run
python3 manage.py loaddata categories
python3 manage.py loaddata products

Then I created a superuser by entering
python3 manage.py createsupreruser

### Deployment on Heroku

This project uses Heroku for production and static and media files are stored via a bucket on Amazon AWS S3. To deploy on Heroku

  - 1. Naviage to heroku.com and login and create new app for your project and set the region and click on create app.
  - 2. Connect Heroku app to github repository 
  - 3. Configure variables on Heroku by navigating to settings and click on Revela Config Vars 

Variable | Key
--- | ---
AWS_ACCESS_KEY_ID | Access key for AWS 
AWS_SECRET_ACCESS_KEY | secret key for AWS 
DATABASE_URL | database url got from code institute 
EMAIL_HOST_PASS | password for email sender 
EMAIL_HOST_USER | email address used 
PORT | 8000 
SECRET_KEY | Django secrey key 
STRIPE_PUBLIC_KEY | stripe public key 
STRIPE_SECRET_KEY | stripe secret key 
STRIPE_WH_SECRET | stripe webhook secret key 
USE_AWS | True 

  - 4. Then create a Procfile with contents - web: gunicorn naveena_store.wsgi:application

  - 5. add hostname of heroku app to allowed hosts in settings.py

  I have setup the debug to be true if the DEVELOPMENT is found in the environment variables which will be true for localhost.

  - 6. on Heroku under deploy for your app click Deploy Branch to deploy your app