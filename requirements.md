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

1. ui interactive interface
2. usability- should be easy to use
3. maintainability- shouldn't crash, code should be well-documented
4. Should work on different kinds of devices

## Use Cases
1. User profiles
    **preconditions: The user has made an account and logged into it
    **trigger: Selects create profile
    **primary sequence:
	1. system ask for profile name
	2. User selects a name not taken
	3. System asks for profile picture
	4. user selects a phtot to be user profile picture
	5. using the name and photo system create the profile
	6. the profile is added to the database and registered and the name can not be used again
     **primary postcondition: the User is able to make a unique user profile they can
     **alternative sequence:
	1. the user selects a name unavible
	2. system prompts the user to choose a diffrent name and one that is not taken

2. Follow User
    **precondition: user is logged into account
    **trigger: user puts the name of other user into search bar
    **primary sequence:
	1. User goes to search bar and enters other user profile name
	2. system checks in the database for a user name that matches the one put in
	3. System responds back with user that is matches the profile
	4. User can click the follow button inorder to follow the other user
	5. system makes a note of which user is following and puts any message form them into the feed of the other

    **primary postcondition: User is able to fllow other and keep a track of their messages and picture
    **alternative sequence:
	1. the user enters a profile name that does not exist
	2. the system prompts them that there is no profile name that matches and they can search again for another name

3. Search User Profiles
    **preconditions: The user has made an account and is logged in
    **trigger: User uses the search bar to search for another user
    **primary sequence:
        1. User uses the search bar to search for another user
        2. User selects the profile that the user searched for
        3. User can now view the profile of searched user
        4. User will be able to comment on the searched user posts and message
     **primary postcondition: The user is now able to see the searched user profile
     **alternative sequence:
        1. The user searches for a user that is not in the system
        2. The system does not display a user for the user to view and prompts the user to search for a different user

4. View follower count
    **preconditions: The user has made an account and is logged in
    **trigger: Selects the view profile option
    **primary sequence:
        1. User is logged into their account and selects the view profile option
        2. User can now see a numeric value that displays the number of followers they have
        3. User can also see a numeric value that displays the number of people that they follow
        4. Users can view the profiles of the people that they follow and their followers
     **primary postcondition: The user is able to see their follower account
     **alternative sequence:
        1. The user does not have an account or is not logged in
        2. The system prompts the user to make an account or login

5. Post a tweet
    **preconditions: The user has made an account and is logged in
    **trigger: The user clicks the post button
    **primary sequence:
	1. User who is logged in selects the post button
	2. A text box appears on the screen
	3. The user can type the message they would like to post
	4. Clicking the post button posts the message
    **primary postcondition: Other users can now see the posted message when viewing the user's account
    **alternative sequence:
	1. The user does not have an account or is not logged in
	2. The system prompts the user to make an account or login

6. Reply to a post
    **preconditions: The user has made an account and is logged in
    **trigger: User selects and views a post
    **primary sequence:
        1. User is logged into their account and selects the view post option
        2. The user enters the keyword of the post to be searched in the search box
        3. Users can now see the post they selected
        4. Users can choose to comment on a post of their choice
        5. Users can also see other users' comments on this post and the post's author's reply
    **primary postcondition: Users can browse all viewable posts and the posts they want to search
    **alternative sequence:
        1. The user does not have an account or is not logged in
        2. The post searched by the user does not exist, the system prompts the user to search again
