# OAuth2.0

https://oauth-174216.appspot.com/

CS 496 - OAuth 2.0 Implementation

In this assignment you will implement a OAuth 2.0 Server Side flow without using a 3rd party OAuth library. The course materials demonstrate what all the requests look like, you will need to implement them in your application so that it can access protected resources on the users Google+ account.

To do so you will need to generally implement the following pieces of functionality:

A page that has a link a user clicks to visit the Google OAuth 2.0 endpoint
A page that handles the user getting redirect back to your website from Google's endpoint and handles the exchanging of the access code for a token
A page (which could use the same handler as the page they were redirected to) which uses that token to access and display  the following information: The users first and last name and the URL to access their Google Plus account. It should also print out the value of the state variable that was used to secure the original redirect.
The only scope you are allowed to request is "email". If your application requests additional permissions beyond that, we are not going to give them to you and your assignment will not be graded. So don't go asking for write permissions for the TAs Google Drive files. :)

You should implement a randomly generated state variable and display it along with the users name.
