


<img src="../static/assets/img/logo_2.png" alt="drawing" width="200"/>

## Manual testing

## User Stories Testing

#### As a user:

- I want to signup to JournalClub so that I can contribute journal articles of my interest (**CREATE**)
    
    - **Action**: I created a new user in SignUp page.
     ![responsive mockups](../static/assets/US_testing/us1.png)
    - **Expected**: User succesfully created.
     ![responsive mockups](../static/assets/US_testing/us2.png)
    - **Result**: Pass
     SignIn:

     ![responsive mockups](../static/assets/US_testing/us3.png)

     Dashboard:
     
     ![responsive mockups](../static/assets/US_testing/us4.png)

- I want to be able to modify my personal information on my profile (**UPDATE**)
    - **Action**: I clicked on **Edit Profile**.
     ![responsive mockups](../static/assets/US_testing/us5.png)
    - **Expected**: User succesfully updated.
    - **Result**: Failed
     ![responsive mockups](../static/assets/US_testing/us6.png)
    - **Fix Action Taken**: I inspect the source code, and enable debug feature
      to find source of error. I had deleted password from session, and I had to put it back.
    - **Result**: Pass
     ![responsive mockups](../static/assets/US_testing/us7.png)
       

- I want to view all journal articles suggested by other fellow researchers.
(**INDEX**)
- I want to create a journal list to be shared with my fellows. (**CREATE**)
- I want to access all details of the article journal (full citation reference).
(**READ**)
- I want to delete a journal club event created by me. (**DESTROY**)
- I want to edit a journal club event created by me. (**EDIT/UPDATE**)
- I want to comment on a particular journal article suggested by me or
other fellows.(**COMMENTS/CREATE**)
- I want to delete my comments on a particular journal articule.
(**DESTROY/DELETE**)


Beside the provided solution to the user of the application, it will also provide
a value to the owner of the application:

#### As a site owner:

-  I want to be contacted by users in order to organise meet-ups and
networking activities (**VALUE PROVIDED**).