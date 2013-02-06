tweecli
=======

Command line python tweet machine, uses tweepy.
Pronounced Twee-klee.

To get working you first need to set up the app under your twitter account.
To do this you'll need to log in to http://dev.twitter.com. Then under your
name in the top right select My Applications and create a new application,
call it what you like.
Once create you will see the details on screen, you now need to create an
access token. Click the button at the bottom of the page.

Now, you will need to create a file in your home folder called .tweeclirc
Include the details from your newly created twitter app in the rc file.

It should look like the following.


[tweecli]
token: insert-access-token-here
secret: insert-access-token-secret-here 

consumer_key: insert-consumer-key-here
consumer_secret: insert-consumer-secret-here 

Finally go to the settings tab for your application and change the
Application Type to 'Read and Write', note this change may take a minute
or two to take effect. You'll get an error about the application being
read-only until it does take effect. 
