# The Notice Board

Click this link to view the live App - [The Notice Board](https://the-notice-board.herokuapp.com/)

Celebrating the best of the UK, with blog posts covering everything from Sport to History, Geography to the Arts.

Welcome to The Notice Board, a platform for people to come together and discuss all things UK. The App allows users to create their own profiles and interact with the community. Whether you're here to share some interesting facts or looking to learn, the App is a great way to discover things that you may not have known about...

## Contents
+ [Project Aims](#project-aims "Project Aims")
+ [How to Use](#how-to-use "How to Use")
+ [User Stories & Epics](#user-stories--epics "User Stories & Epics")
    + [Epic: Content Management & Interaction](#epic-content-management--interaction "Epic: Content Management & Interaction")
    + [Epic: User Profiles & Account Management](#epic-user-profiles--account-management "Epic: User Profiles & Account Management")
    + [Epic: Post Navigation & Discovery](#epic-post-navigation--discovery "Epic: Post Navigation & Discovery")
+ [Design](#design "Design")
    + [Features](#features "Features")
        + [Navbar](#navbar "Navbar")
        + [My Profile](#my-profile "My Profile")
        + [Footer](#footer "Footer")
        + [Index](#index "Index")
        + [Posts](#posts "Posts")
            + [Post Messages](#post-messages "Post Messages")
        + [About](#about "About")
        + [Create Post](#create-post "Create Post")
            + [Create Post Messages](#create-post-messages "Create Post Messages")
        + [Sign Up, Login & Sign Out](#sign-up-login-and-sign-out "Sign Up, Login & Sign Out")
    + [Future Features](#future-features "Future Features")
        + [Profile Images](#profile-images "Profile Images")
        + [Notifications](#notifications "Notifications")
+ [Technologies Used](#technologies-used "Technologies User")
+ [Testing](#testing "Testing")
    + [Fixed Bugs](#fixed-bugs "Fixed Bugs")
        + [Downvote counter](#1-downvote-counter "Downvote counter")
        + [Non registered users accessing profiles](#2-non-registered-users-accessing-profiles "Non registered users accessing profiles")
+ [Deployment](#deployment "Deployment")
    + [Local Deployment](#local-deployment "Local Deployment")
    + [Remote Deployment](#remote-deployment "Remote Deployment")
+ [Credits](#credits "Credits")
+ [Acknowledgments](#acknowledgments "Acknowledgments")

## Project Aims

Provide a platform for people to post interesting content relating to the UK
Allow users to create posts
Encourage community engagement by allowing users to comment and vote on posts
Provide a simple, visually pleasing layout that ensures users can consume the information easily
Ensure that the App can be scaled up and handle a larger number of posts over time
Offer security features to protect user data
Ensure administrators can easily moderate content and prevent misuse

## How to Use

Steps to use The Notice Board:

1. Create an account - You can do this by entering an email address and creating a password.
2. Update your profile - Add your personal information and a biography to help others get to know you.
3. Browse posts - Browse the website looking for interesting posts to engage with.
4. Comment/vote on posts - Let other users know what you think of their content and vote to inform potential readers.
5. Create posts - Contribute to the site and create posts for other users/site visitors to view an interact with.

## User Stories & Epics

All of my user stories were entered in a GitHub project - [Link](https://github.com/users/DanFNKD/projects/2)

### Epic: Content Management & Interaction

- [10]([#10])(https://github.com/DanFNKD/the-notice-board/issues/10) - As a site user, I can view a limited number of posts per page so that I can browse content easily without being overwhelmed.
- [2]([#2])(https://github.com/DanFNKD/the-notice-board/issues/2) - As a site user I can create posts so that I can contribute to the site.
- [11]([#11])(https://github.com/DanFNKD/the-notice-board/issues/11) - As a site user I can edit and update my posts so that I can correct any errors and refresh content where necessary.
- [7]([#7])(https://github.com/DanFNKD/the-notice-board/issues/7) - As a site admin, I can approve, edit or delete any post so that I can ensure all content meets site standards.
- [8]([#8])(https://github.com/DanFNKD/the-notice-board/issues/8) - As a site user, I can add tags to my posts so that I can categorise content and make it easier for others to find.
- [3]([#3])(https://github.com/DanFNKD/the-notice-board/issues/3) - As a registered user, I can leave comments on posts so that I can engage with other users and participate in discussions.
- [12]([#12])(https://github.com/DanFNKD/the-notice-board/issues/12) - As a site admin I can approve, edit or delete comments so that I can ensure all content meets site standards.
- [13]([#13])(https://github.com/DanFNKD/the-notice-board/issues/13) - As a site admin, I can create and set Tags so that site users can assign them to their posts.
- [4]([#4])(https://github.com/DanFNKD/the-notice-board/issues/4) - As a registered user, I can upvote or downvote posts so that I can express my opinion on content and help highlight popular posts.
- [18]([#18])(https://github.com/DanFNKD/the-notice-board/issues/18) - As a site user, I can upload images when creating posts, so that I can make my content more engaging.
- [19]([#19])(https://github.com/DanFNKD/the-notice-board/issues/19) - As a site admin, I want to manage images within posts so that I can remove or replace images to maintain site standards where necessary.
- [17]([#17])(https://github.com/DanFNKD/the-notice-board/issues/17) - As a registered user, I can be notified if my comment is awaiting approval so that I can understand why it is not immediately visible on the site.

### Epic: User Profiles & Account Management

- [1]([#1])(https://github.com/DanFNKD/the-notice-board/issues/1) - As a site user, I can register for an account and login so that I can access additional features and interact with the site.
- [6]([#6])(https://github.com/DanFNKD/the-notice-board/issues/6) - As a registered user, I can view and edit my profile so that I can share relevant information about myself with others.
- [14]([#14])(https://github.com/DanFNKD/the-notice-board/issues/14) - As a registered user, I can view other users' profiles so that I can learn more about the authors of posts I read.

### Epic: Post Navigation & Discovery

- [15]([#15])(https://github.com/DanFNKD/the-notice-board/issues/15) - As a site user, I can search for posts so that I can find specific content.
- [16]([#16])(https://github.com/DanFNKD/the-notice-board/issues/16) - As a site user, I can sort and filter posts so that I can quickly find tailored content to suit my interests.
- [20]([#20])(https://github.com/DanFNKD/the-notice-board/issues/20) - As a site user, I want to filter posts by tags so that I can quickly find content relevant to specific topics.

## Design

### ERD
![erd](readme-media/erd.png)

### Features

Below are the core features of The Notice Board. 

#### Navbar

The site name is written and links to the home page. Navlinks are stored next to the logo and login/logout functionality sits to the right to separate the features.
A responsive toggle button to expand/collapse the navigation links.
Conditional links for user authentication - Create post and my profile are not visible to non-members.

![nav 1](readme-media/site_images/navbar/navbar.png)
![nav 2](readme-media/site_images/navbar/navbar-hover.png)
![nav 3](readme-media/site_images/navbar/navbar-collapse.png)

#### My Profile

A profile that is only accessible when the user is logged in.
It provides an overview of the user and provides links to their posts as well as displaying the votes.

![prof 1](readme-media/site_images/profile/profile.png)
![prof 2](readme-media/site_images/profile/edit-profile.png)

#### Footer

The footer contains two paragraphs. The first displays a link to the author's GitHub and the second shows social media icons from FontAwesome.

![foot 1](readme-media/site_images/footer/footer.png)
![foot 2](readme-media/site_images/footer/footer-responsive.png)

#### Index

This page displays posts from users and is limited to 6 posts per page.
Users can search for posts.
Users can sort or filter posts.
Cards display an overview of the posts, including name, excerpt and date/time/author information.
Users can view the total page numbers at the bottom of the page.
There is pagination, allowing users to navigate between pages to view posts.

![ind 1](readme-media/site_images/index/index.png)

#### Posts

This page displays the selected post.
It has a title, confirms the author and when it was created.
There posts upvotes/downvotes are displayed with FontAwesome Icons.
Users can leave a comment.

![post 1](readme-media/site_images/post/post1.png)
![post 2](readme-media/site_images/post/post2.png)

##### Post Messages

Messages are displayed when a user votes on a post.
Messages are displayed when a user submits a comment, confirming that it has been sent for approval.

![post 3](readme-media/site_images/post/vote-feedback-message.png)
![post 4](readme-media/site_images/post/comment-feedback-message.png)

#### About

This page provides site users with an overview of the goals for the site.
Users can see when the content was last updated.

![ab 1](readme-media/site_images/about/about1.png)
![ab 2](readme-media/site_images/about/about2.png)

#### Create Post

This page allows an admin or user to create a post.

![cp 1](readme-media/site_images/create-post/create-post.png)
![cp 2](readme-media/site_images/create-post/create-post-verification1.png)
![cp 3](readme-media/site_images/create-post/create-post-verification2.png)

##### Create Post Messages

The admin and user will see a message when the post has been created/sent for approval.

![cp 4](readme-media/site_images/create-post/create-post-acceptance.png)

#### Sign Up, Login and Sign Out

Users can sign up and create a new account.
When creating a new account, they can see the criteria for passwords.
Users can log in to their account.
Allauth was implemented to handle account creation and verification.

![acc 1](readme-media/site_images/sign-up/sign-up.png)
![acc 2](readme-media/site_images/sign-up/sign-up-verification1.png)
![acc 3](readme-media/site_images/sign-up/sign-up-verification2.png)
![acc 4](readme-media/site_images/sign-up/sign-up-verification3.png)
![acc 5](readme-media/site_images/sign-in/sign-in.png)
![acc 6](readme-media/site_images/sign-in/sign-in-verification.png)
![acc 7](readme-media/site_images/sign-out/sign-out.png)

### Future Features

#### Profile Images:

Allow registered users to upload images to their profiles.

#### Notifications:

Provide registered users with notifications when someone either votes or comments on a post of theirs.

## Technologies Used

- HTML
- CSS
- Python
- Javascript
- django-allauth
- django-crispy-forms
- django-summernote
- Google Fonts
- Bootstrap
- Postgres

## Testing

### Fixed Bugs

#### 1. Downvote counter

When initially testing my vote counter, I noticed that a downvote would reduce the total counter by -1. To combat this, I removed the total vount counter as it was not necessary to be displayed to the user.

#### 2. Non registered users accessing profiles

For the project, I ensured that non registered users could not view certain pages. They could however click the hyperlink on the post card and be directed to the user's profile. I implemented the following code to prevent this behaviour.

## Deployment

### Local Deployment

1. Sign up to code-institute-ide.net.
2. On Github.com, navigate to the DanFNKD/the-notice-board repository
3. Click the code button.
4. Copy the https link.
5. Navigate to code-institute-ide.net and select new workspace.
6. Paste the https link.
7. Click Continue.

### Remote Deployment

1. Log in to Heroku.
2. Click 'Create new app'.
3. Give the application a unique name, select the correct region and click the 'Create App' button.
4. Configure the external Postgres database.
5. Go to settings are click 'Reveal Config Vars' in the Config Vars section.
6. Add ALLOWED_HOSTS and the value as the project name with '.herokuapp.com' appended at the end.
7. Add SECRET_KEY and the value of the complex string.
8. Add DATABASE_URL as I am using a different database for the project.
9. Navigate to the 'Deploy' page.
10. Select 'GitHub' from the 'Deployment method' section.
11. Enter the GitHub account details and the correct repository.
12. Select 'Manual Deploy'.
13. Select the 'main branch'.
14. Click 'Deploy'.
15. Click the 'View' button once the project is built to load the URL.

## Credits

- Django Documentation - Django - [Django](https://docs.djangoproject.com/en/5.1/)
- Bootstrap Documentation - Bootstrap - [Bootstrap](https://getbootstrap.com/docs/5.3/getting-started/introduction/)
- Stack Overflow - [Stack Overflow](https://stackoverflow.com/)
- Lucid Chart - Used to design the Entity Relationship Diagram - [Lucid Chart](https://lucid.app/)
- Icons - Font Awesome - [Font Awesome](https://fontawesome.com/)
- Google Fonts - [Google Fonts](https://fonts.google.com/)

## Acknowledgments

I'd like to thank my tutor Daniel Hamilton. He taught me many new things that were included in the project and helped throughout.


