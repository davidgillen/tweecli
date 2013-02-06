tweecli
=======

Command line python tweet machine, uses tweepy.
Pronounced Twee-klee.

To get working you first need to set up the app under your twitter account.
To do this you'll need to log in to http://dev.twitter.com. Then under your
name in the top right select My Applications and create a new application,
call it what you like.
Next you need to go to the settings tab for your application and change the
Application Type to 'Read and Write'.
You now need to create an access token. Go back to the details page and
click the button at the bottom of the page.
Ensure under both the "OAuth Setting" and "Your access token" the access
level is listed as Read and write.

Now, you will need to create a file in your home folder called .tweeclirc
Include the details from your newly created twitter app in the rc file.

It should look like the following.


    [tweecli]
    token: insert-access-token-here
    secret: insert-access-token-secret-here 

    consumer_key: insert-consumer-key-here
    consumer_secret: insert-consumer-secret-here 

You should now be good to tweet away on the command line
e.g. python tweecli.py "Command line tweeting FTW!"
