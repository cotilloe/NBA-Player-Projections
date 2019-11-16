# NBA-Player-Projections
An app to project users stats in their next game for use in fantasy sports and sports wagering.

<h3>Application Flow:</h3>
<p>
  <ol>
    <li>User enters player names into text boxes</li>
    <li>Upon clicking button, we generate a url to basketball-reference.com for that player's specific  game log table</li> 
    <li>Using Beautiful soup, the html table is parsed and saved as a csv file</li>
    <li>The data from the csv file is then used to make a projection on the needed statistics and then the projection is made</li>
    <li>The projected stats are displayed in a second Tkinter window</li>
  </ol>
</p>
<h3>Current Known Issues:</h3>
<p>
  Currently, the biggest issue we face is in the URL building. The format for the URL is fairly simple and follows the same method for all players. the only exception is if there is a player whose URL ends up pointing to another players game logs. This happens due to the method of forming the url:</p>
  
  <blockquote>The base url/Player_Directory/Player's Initial (Last Name) /<u><strong><em>Player ID</em></strong></u> + File extension</blockquote>
  
 <p> The normal way the player ID is built is to take the first 5 letters of the last name (or all letters if shorter than 5) and then the the first 2 letters of the first name (ignoring punctuation. i.e. J.J. Reddick is simply JJ Reddick) and then add '01' to it. So, Lebron James ends up with a player ID of 'jamesle01', James Harden is 'hardeja01' and Russell Westbrook is 'westbru01'. 
<br /><br />
Fairly simple and easy to implement via code.
<br /><br />
However, when a player's first 5 characters of their last name and two characters of their first name are the same as a player that is/was in the league longer than them, then we need to change the '01' to '02'. When you try and enter a player who this happens with, Anthony Davis for example, you get a TypeError because the game log that is retrieved is for "Antonio Davis", who played from 1994-2006. So what happens is the 2019-2020 season gamelog table for Antonio Davis does not exist and there is nothing for thye csv module to read. </p>
<p>
Currently, it is being handled with a Try/Except that attempts to read the contents of the parsed csv file and if empty simply assigns a value of '0' to all stats. When this happens, it then causes a ValueError to be thrown, which is excepted in the same block as the TypeError, again, simply assigning '0' as a value.
  <br /><br />
I have also added in the function that a file is created, if it does not exist already, that contains the names of all known players this happens too. I am now checking this file first and if the player name entered in the text box matches a name in the file, then it automatically assigns '02' instead. It is initially created and saved with 'Anthony Davis' as the only entry, with new names being added as the error occurs. <br /><br />
  
Currently, the name will be added, the file saved and then the program will be restarted, which is not optimal. </p>

<h3>Coding Format/Style</h3>
<p> Currently, everything resides in one file, which needs to be broken up into multiple files really.</p>
<p>Some of the code is sloppy at the moment as this is the first draft really. I will be cleaning it up and would love some suggestions to cut some of the code down a bit</p>

<h3>Projection Algorithm</h3>
It is not much of an Algorithm. It takes the player's seaso average, average of last game they played, average of last 5 games and then last 10 games and then gets the average of those. I am still developing a better way to get more accurate numbers returned.</p>

<h3>Helping/Pull Requests</p>
Just submit them, alll help is appreciated!</p>
