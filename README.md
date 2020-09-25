# MoodUpdater-Discord-
Pings your close friend(s) or loved one(s) on discord to tell them how you're feeling!

Future improvements I am working on or I will work on:  
<ol>
  <li> Cleaning up the GUI and making it more aesthetically pleasing (i.e. widgets for each emotion that contain an image and the mood associated, adding a better background color, better layout, etc.) </li>
  <li>Adding images + more information to the message in Discord </li>
  <li>Add something on the GUI that indicates that the user's name was successfully set + message was successfully sent (eliminate the pop-ups) </li>
  <li>Cross-platform compatability </li>
</ol>
  

</br> 

To run: 
  1. Create/Log-in to a Discord account: 
    <ul>  Navigate to a text channel that you'd like messages to be sent to (if you're new to Discord, you can create a server, and from there create a text channel) </ul> 
    <ul>  Click on the "Edit Channel" wheel next to the channel's name </ul> 
    <ul>  Go to "Integrations" --> "Webhooks" --> create a new webhook --> specify the channel you want from the  drop down --> Copy the Webhook URL </ul> 
  2. Create an app on Discord's Developer Portal 
    <ul> Click on your app --> click the "OAuth2" tab --> paste the Webhook URL you copied into the "Redirects"field --> specify the scope you want </ul> 
  3. Create a config.py file --> create webhook_url + auth_key variables (using respectively: the Redirect URL created in the OAuth2 tab and your client ID) 
  4. Run GUI.py  
