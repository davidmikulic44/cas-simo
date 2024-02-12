**IEEE 830-1998 Software Requirements Specification „Cas-Simo: A casino simulator“**

Lea Gregurić David Mikulić

Faculty of Electrical Engineering, Computer Science and Information Technology

Osijek, 2024.

1. [**Introduction.................................................................................2**](#_page2_x127.56_y103.84)
1. [Purpose.................................................................................. 2](#_page2_x127.56_y127.68)
1. [Document Conventions......................................................... 3](#_page2_x127.56_y303.95)
1. [Intended Audience and Reading Suggestions......................3](#_page2_x127.56_y415.14)
1. [Product Scope........................................................................ 3](#_page2_x127.56_y540.59)
1. [References..............................................................................3](#_page2_x127.56_y680.32)
1. [Overview................................................................................3](#_page3_x127.56_y72.00)
2. [**Overall Description....................................................................4**](#_page3_x127.56_y150.65)
1. [Product Perspective...............................................................4](#_page3_x127.56_y174.48)
1. [Product Functions................................................................. 4](#_page3_x127.56_y365.02)
1. [User Classes and Characteristics.........................................4](#_page3_x127.56_y543.02)
4. [Operating Environment........................................................5](#_page4_x127.56_y150.65)
4. [Design and Implementation Constraints.............................5](#_page4_x127.56_y255.56)
4. [User Documentation............................................................. 5](#_page4_x127.56_y389.02)
3. [**Specific Requirements.............................................................. 5**](#_page4_x127.56_y633.67)
1. [Functional Requirements: User Requirements...................5](#_page4_x127.56_y657.50)
1. [User Registration......................................................... 5](#_page4_x127.56_y689.34)
1. [User Login.....................................................................6](#_page5_x127.56_y145.08)
1. [User Logout...................................................................6](#_page5_x127.56_y284.81)
1. [User Dashboard............................................................6](#_page5_x127.56_y410.27)
1. [User Profile...................................................................6](#_page5_x127.56_y624.81)
1. [Bet Placing....................................................................7](#_page6_x127.56_y138.81)
1. [Bet History....................................................................7](#_page6_x127.56_y278.54)
2. [Functional Requirements: Admin Requirements................7](#_page6_x127.56_y375.46)
1. [Admin Dashboard.........................................................7](#_page6_x127.56_y399.29)
1. [Apply a Token Balance to a User.................................7](#_page6_x127.56_y599.56)
3. [Functional Requirements: Game Requirements................. 9](#_page8_x127.56_y72.00)
1. [Game Playing: Roulette............................................... 9](#_page8_x127.56_y91.84)
1. [Game Playing: Coin flip............................................... 9](#_page8_x127.56_y175.34)
1. [Betting and Winning Calculation................................9](#_page8_x127.56_y239.01)
4. [Usability Requirements......................................................10](#_page9_x127.56_y91.84)
4. [Reliability Requirements....................................................10](#_page9_x127.56_y196.75)
4. [Performance Requirements................................................ 10](#_page9_x127.56_y265.13)
7. [Supportability Requirements............................................. 10](#_page9_x127.56_y333.51)
7. [Design Constraints..............................................................10](#_page9_x127.56_y401.88)
4. [**System Interfaces..................................................................... 11**](#_page10_x127.56_y94.27)
1. [User Interfaces.................................................................... 11](#_page10_x127.56_y118.11)
1. [Hardware Interfaces............................................................11](#_page10_x127.56_y481.62)
1. [Software Interfaces..............................................................11](#_page10_x127.56_y564.27)
4. [Communications Interfaces................................................ 11](#_page10_x127.56_y646.92)
5. [**Other Nonfunctional Requirements....................................12**](#_page11_x127.56_y72.00)
1. [Security Requirements........................................................12](#_page11_x127.56_y91.84)
1. [Safety Requirements...........................................................12](#_page11_x127.56_y203.02)
1. [Business Rules.....................................................................12](#_page11_x127.56_y263.40)
1. [Quality Attributes...............................................................12](#_page11_x127.56_y323.78)
6. [**Other Requirements................................................................ 12**](#_page11_x127.56_y415.12)
1. [Business Requirements.......................................................12](#_page11_x127.56_y438.95)
1. [Regulatory Requirements...................................................12](#_page11_x127.56_y498.63)

<a name="_page2_x127.56_y103.84"></a>**1. Introduction**

1. **Purpose**

<a name="_page2_x127.56_y127.68"></a>The purpose of this document is to define the Software Requirements Specification (SRS) for the development of "Cas-Simo", a web application created to provide users with an immersive platform for participating in games of chance and engaging in online betting. This document outlines the functional and non-functional requirements, ensuring a clear understanding of the project's scope, objectives, and constraints.

2. **Document<a name="_page2_x127.56_y303.95"></a> Conventions**

This document is written using the IEEE 830-1998 standard for software requirements specifications. It will include user, system, and customer requirements for the completion of the project.

3. **Intended<a name="_page2_x127.56_y415.14"></a> Audience and Reading Suggestions**

This document is intended for the developers and designers working on the ”Cas-Simo” project. It is recommended that readers start from the beginning and read the document from start to finish to get a complete picture of the project requirements.

4. **Product<a name="_page2_x127.56_y540.59"></a> Scope**

"Cas-Simo" aims to offer users a dynamic and secure online environment for participating in various games of chance, including casino games and other wagering activities. The scope of this project encompasses user interactions, system functionalities, and customer expectations related to the online gambling platform.

5. **References**
1. <a name="_page2_x127.56_y680.32"></a>IEEE 830-1998: IEEE Standard for Software Requirements

Specifications (IEEE, 1998).

2. Django 4.1. documentation
6. **Overview**

<a name="_page3_x127.56_y72.00"></a>The “Cas-Simo” web application is a casino simulator for users to try out their luck. In this version, real currency won’t be used.

2. **Overall<a name="_page3_x127.56_y150.65"></a> Description**
1. **Product<a name="_page3_x127.56_y174.48"></a> Perspective**

“Cas-Simo” is a standalone web application that allows users to play games of chance. Admins have control over the system and can monitor all activities. The user interface is designed to be intuitive and easy to use, a homepage with all available games to be played. Users will also be able to see their bet history and their current balance. “Cas-Simo” is a self-contained web application that will be hosted on a web server. It will be accessible through a web browser.

2. **Product<a name="_page3_x127.56_y365.02"></a> Functions**

User Interface: Users can access the platform, view available games, and place bets.

Gameplay: Users can play roulette or coin flip games by placing bets. The outcomes are determined randomly.

Admin Dashboard: Admins can oversee all games, monitor user activities, and manage the system.

3. **User<a name="_page3_x127.56_y543.02"></a> Classes and Characteristics**

The product will have two logical user classes: Admin and User. Admin is a user class with a superuser status and can access the Admin dashboard. Admin users can create, edit, and delete users, and user’s balance. Users can place bets on different games.

1. **Admin**

Admin users manage and monitor the web application, including managing users. Admin users will be able to see every user’s bet history and their balance.

2. **User**

Users will be able to play different games, place bets and see their own bet history and balance.

4. **Operating<a name="_page4_x127.56_y150.65"></a> Environment**

The web application will be hosted on a web server. It will be accessible through a web browser.

5. **Design<a name="_page4_x127.56_y255.56"></a> and Implementation Constraints**

The web application will be written in Python using the Django framework. It will be hosted on a web server. The data will be stored in a SQLite database. No further design and implementation constraints are known at this time.

6. **User<a name="_page4_x127.56_y389.02"></a> Documentation**

No documentation will be provided to users.

7. **Assumptions and Dependencies**

The application will use a cryptocurrency token to handle payments. For the first version of the application, the amounts of tokens each user has will be recorded as a field in the database and will be managed by admin users. The token deposit and withdrawal functionality will not be implemented in this version of the application. The application will not have an automated quality assurance process.

3. **Specific<a name="_page4_x127.56_y633.67"></a> Requirements**
1. **Functional<a name="_page4_x127.56_y657.50"></a> Requirements: User Requirements**
1. **User<a name="_page4_x127.56_y689.34"></a> Registration**

Req U1 - The web application will allow users to register for an account. The web application will allow users to register for an account. Users will provide their username and password. 

2. **User<a name="_page5_x127.56_y145.08"></a> Login**

Req U2 - The web application will allow users to log in to their account. The web application will allow users to log in to their account. Users will provide their username and password. The web application will verify that the username and password match the information in the database.

3. **User<a name="_page5_x127.56_y284.81"></a> Logout**

Req U3 - The web application will allow users to log out of their account. The web application will allow users to log out of their account. Users will click on a ”LogOut” button in the Navigation. The web application will terminate the user’s session.

4. **User<a name="_page5_x127.56_y410.27"></a> Dashboard**

Req U4 - The web application will provide a dashboard for users to view their account information. The web application will provide a dashboard for users to view their account information. The dashboard will include the following information:

- User’s username
- User’s token balance
- List of previous bets

5. **Bet<a name="_page6_x127.56_y138.81"></a> Placing**

Req U5 - The player will be able to bet if there is enough money on the account. If there is not enough money, the system shall notify the player and take him/her to the account recharge page. Upon successful betting, the system will confirm to the user details of the game. The player shall be able to check the details in the Bet History.

6. **Bet<a name="_page6_x127.56_y278.54"></a> History**

Req U6 - The user can see their own bet history of all games that they’ve played. Admin users can see every user’s bet history.

2. **Functional<a name="_page6_x127.56_y375.46"></a> Requirements: Admin Requirements**
1. **Admin<a name="_page6_x127.56_y399.29"></a> Dashboard**

Req A1 - The web application will provide a dashboard for admins to manage the system. The web application will provide a dashboard for admins to manage the system. The dashboard will use the Django Admin interface. The dashboard will allow admins to manage the following:

- Users (create, edit, delete)
- Bet History (create, edit, delete)
- Apply a token balance to a user
2. **Apply<a name="_page6_x127.56_y599.56"></a> a Token Balance to a User**

Req A2 - The web application will allow admins to apply a token balance to a user. The web application will allow the admins to find a user in the Admin dashboard and to change the user’s token balance. The web application will update the user’s token balance in the database. The web application will display the new token balance on the user’s dashboard.

**Constraints and considerations:** The token balance is used for payments in the system. The token balance is applied to the user’s account when the user wins a bet. The deposit and withdrawal of the tokens is outside the scope of this application. In this version of the application there won’t be any real currency involved.

Note: The token balance is not a currency (yet). The token balance is a number that represents the number of tokens that the user has in their account. The token balance is used for payments in the system.

3. **Functional<a name="_page8_x127.56_y72.00"></a> Requirements: Game Requirements**
1. **Game<a name="_page8_x127.56_y91.84"></a> Playing: Roulette**

Req G1 - Users can place bets on specific colors, numbers or both in the roulette game.

2. **Game<a name="_page8_x127.56_y175.34"></a> Playing: Coin flip**

Req G2 - Users can place bets on either heads or tails.

3. **Betting<a name="_page8_x127.56_y239.01"></a> and Winning Calculation**

Req G3 - The system will deduct the betting amount from the user's account, and winnings will be credited based on the game outcome.

4. **Usability<a name="_page9_x127.56_y91.84"></a> Requirements**

The web application will be designed to be easy to use.The web application will be designed to be intuitive and easy to learn.

5. **Reliability<a name="_page9_x127.56_y196.75"></a> Requirements** None at this time.
5. **Performance<a name="_page9_x127.56_y265.13"></a> Requirements** None at this time.
5. **Supportability<a name="_page9_x127.56_y333.51"></a> Requirements** None at this time.
5. **Design<a name="_page9_x127.56_y401.88"></a> Constraints** None at this time.
4. **System<a name="_page10_x127.56_y94.27"></a> Interfaces**
1. **User<a name="_page10_x127.56_y118.11"></a> Interfaces**

The application will have a user interface that is accessible via a web browser. The interface will be designed to be intuitive and user-friendly, optimized for mobile and desktop devices. The web application will use a standard web interface with a top navigation bar and a main content area. The web application will be primarily used on a desktop computer and a responsive design is not required.

The top navigation bar will have the following links:

- On the left side:
  - Logo
- On the right side:
- Login (a link to the Login page) if the user is not logged in
- Profile (a link to the Bet history page) if the user is logged in
- Add funds (a link to the Add funds page) if the user is an admin
- User balance
- Logout (a link to the Logout page) if the user is logged in
2. **Hardware<a name="_page10_x127.56_y481.62"></a> Interfaces**

The application will be hosted on a secure web server running on Linux or Windows.

3. **Software<a name="_page10_x127.56_y564.27"></a> Interfaces**

The application will use Django 4.1, the database will be SQLite, and the frontend will be written with SCSS and jQuery.

4. **Communications<a name="_page10_x127.56_y646.92"></a> Interfaces**

The application will have a secure communication interface for secure data transfer.

5. **Other<a name="_page11_x127.56_y72.00"></a> Nonfunctional Requirements**
1. **Security<a name="_page11_x127.56_y91.84"></a> Requirements**

The application will use the Django's default User management system. The application will use Django’s default authentication system. The application will use Django’s default authorization system. The application will use Django’s default password reset system.

2. **Safety<a name="_page11_x127.56_y203.02"></a> Requirements**

The application must be designed to prevent the user from performing any unsafe actions or operations.

3. **Business<a name="_page11_x127.56_y263.40"></a> Rules**

The application will have business rules in place to ensure the safety and security of user data.

4. **Quality<a name="_page11_x127.56_y323.78"></a> Attributes**

The application must have a high-quality user interface with good usability and responsiveness. The application must also have an uptime of at least 99.

6. **Other<a name="_page11_x127.56_y415.12"></a> Requirements**
1. **Business<a name="_page11_x127.56_y438.95"></a> Requirements** None at this time.
1. **Regulatory<a name="_page11_x127.56_y498.63"></a> Requirements** None at this time.
