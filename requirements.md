## Functional Requirements

1. Login (Haomiao)
2. Logout (Navdip)
3. Create new account (Haomiao)
4. Delete Account (Joshua)
5. User Home Page (Joshua)
6. Send message to followers (Ekansh)
7. User Profiles (Navdip)
8.  Follow user  (Navdip)
9. Search user profiles (Ekansh)
10. View follower count (Ekansh)
11. Post a tweet (Joshua)
12. Reply to a post (Haomiao)

## Non-functional Requirements

1. Passwords should be at least 8 characters long with at least 1 number and 1 special character
2. Should be easy to use
3. The website should load in less than 5 seconds
4. Should resize window on different devices

## Use Cases
1. User Profiles
    - **Pre-conditions:** The user has made an account and is logged in
    - **Trigger:** Selects create profile
    - **Primary Sequence:**
        1. System prompts user to enter their username
        2. User inputs an available name
        3. System prompts user to enter their password
        4. User inputs a password
        5. System prompts user to submit a profile picture
        6. User selects a photo to be their profile picture
        7. After confirming, the system creates the user profile with the given username and photo
        8. The profile is added to the database and registered and the name can not be used again
    - **Primary Postcondition:** User is able to make a unique user profile that they can use to post and follow users
    - **Alternative Sequence:**
        1. The username inputted by the user is unavailable
        2. The system prompts the user to choose a diffrent username that is not taken

2. Follow User
    - **Pre-conditions:** User is logged into account
    - **Trigger:** User puts the name of other user into search bar
    - **Primary Sequence:**
        1. User goes to search bar and enters other user profile name
        2. User can click the follow button in order to follow the other user
        3. The user that received the follow will receive a follow requeust that shows who is trying to follow them
    - **Primary Postcondition:** User is able to follow others and keep a track of their messages and pictures
    - **Alternative Sequence:**
        1. The user enters a profile name that does not exist
        2. The system prompts them that there is no profile name that matches and they can search again for another name


3. Search User Profiles
    - **Pre-conditions:** The user has made an account and is logged in
    - **Trigger:** User uses the search bar to search for another user
    - **Primary Sequence:**
        1. User uses the search bar to search for another user
        2. User selects the profile that the user searched for
        3. User can now view the profile of searched user
        4. User will be able to comment on the searched user posts and message
    - **Primary Postcondition:** The user is now able to see the searched user profile
    - **Alternative Sequence:**
        1. The user searches for a user that is not in the system
        2. The system does not display a user for the user to view and prompts the user to search for a different user

4. View follower count
   - **Pre-conditions:** The user has made an account and is logged in
   - **Trigger:** Selects the view profile option
   - **Primary sequence:**
        1. User is logged into their account and selects the view profile option
        2. User can now see a numeric value that displays the number of followers they have
        3. User can also see a numeric value that displays the number of people that they follow
        4. Users can view the profiles of the people that they follow and their followers
    - **Primary Postcondition:** The user is able to see their follower account
    - **Alternative Sequence:**
        1. The user does not have an account or is not logged in
        2. The system prompts the user to make an account or login

5. Post a tweet
   - **Pre-condition:** The user has made an account and is logged in
   - **Trigger:** The user clicks the post button
   - **Primary Sequence:**
        1. User who is logged in selects the post button
        2. A text box appears on the screen
        3. The user can type the message they would like to post
        4. Clicking the post button posts the message
   - **Primary Postcondition:** Other users can now see the posted message when viewing the user's account
   - **Alternative Sequence:**
        1. The user does not have an account or is not logged in
        2. The system prompts the user to make an account or login

6. Reply to a post
   - **Pre-conditions:** The user has made an account and is logged in
   - **Trigger:** User selects and views a post
   - **Primary Sequence:**
        1. User is logged into their account and selects the view post option
        2. The user enters the keyword of the post to be searched in the search box
        3. Users can now see the post they selected
        4. Users can choose to comment on a post of their choice
        5. Users can also see other users' comments on this post and the post's author's reply
   - **Primary Postcondition:** Users can browse all viewable posts and the posts they want to search
   - **Alternative Sequence:**
        1. The user does not have an account or is not logged in
        2. The post searched by the user does not exist, the system prompts the user to search again
