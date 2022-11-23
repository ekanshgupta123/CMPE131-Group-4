## Functional Requirements

1. Login
2. Logout
3. Create new account
4. Delete Account
5. User Home Page
6. Send message to followers
7. User Profiles
8.  Follow user
9. Search user profiles
10. View follower count
11. Post a tweet 
12. Reply to a post 

## Non-functional Requirements

1. ui interactive interface 
2. usability- should be easy to use
3. maintainability- shouldn't crash, code should be well-documented
4. Should work on different kinds of devices

## Use Cases

1. Use Case Name (Should match functional requirement name)
- **Pre-condition:** <can be a list or short description> Lorem ipsum dolor sit amet, consectetur adipisci elit, sed eiusmod tempor incidunt ut labore et dolore magna aliqua.

- **Trigger:** <can be a list or short description> Ut enim ad minim veniam, quis nostrum exercitationem ullam corporis suscipit laboriosam, nisi ut aliquid ex ea commodi consequatur. 

- **Primary Sequence:**
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Et sequi incidunt 
  3. Quis aute iure reprehenderit
  4. ... 
  5. ...
  6. ...
  7. ...
  8. ...
  9. ...
  10. <Try to stick to a max of 10 steps>

- **Primary Postconditions:** <can be a list or short description> 

- **Alternate Sequence:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Ut enim ad minim veniam, quis nostrum e
  3. ...

- **Alternate Sequence <optional>:** <you can have more than one alternate sequence to describe multiple issues that may arise>
  
  1. Ut enim ad minim veniam, quis nostrum e
  2. Ut enim ad minim veniam, quis nostrum e
  3. ...
2. Use Case Name (Should match functional requirement name)
   ...
1. User profiles
    **preconditions: The user has made an account and logged into it 
    **trigger: Selects create profile 
    **primary sequence:
	1.system ask for profile name 
	2. User selects a name not taken
	3.System asks for profile picture
	4. user selects a phtot to be user profile picture
	5. using the name and photo system create the profile 
	6. the profile is added to the database and registered and the name can not be used again
     **primary postcondition: the User is able to make a unique user profile they can 
     ** alternative sequence:
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
		5.system makes a note of which user is following and puts any message form them into the feed of the other

	**primary postcondition: User is able to fllow other and keep a track of their messages and picture
	** alternative sequence:
		1.the user enters a profile name that does not exist 
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
     ** alternative sequence:
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
     ** alternative sequence:
        1. The user does not have an account or is not logged in
        2. The system prompts the user to make an account or login


