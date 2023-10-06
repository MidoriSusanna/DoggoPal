<h1>DoggoPal - Your Virtual Best Friend</h1>
<p>"DoggoPal: Your Virtual Best Friend" is an application inspired by the timeless Japanese Tamagotchi and the more sophisticated Nintendogs. DoggoPal offers users the joy of caring for their very own virtual pet, complete with simple yet engaging activities like playtime, bath time, and mealtime.<br>
Simplicity is an essential feature of DoggoPal, making it accessible to a wide range of
users, including the youngest children. This game's target audience is not
specific, catering to all age groups and even welcoming the youngest of players.</p><br>
<image src="./assets/images/readme-screen.png"><br>

<h1>Project Goals</h1>
<p>
-	Create a simple and intuitive application that could be also accessible to younger children. <br>
-	Create a friendly and relaxed atmosphere through an interface that visually expresses the presence of a virtual pet using backgrounds and emojis.<br>
-	Make the user able to choose name, breed, and age of the virtual dog through open questions which cannot have a blank answer.<br>
-	Create a straightforward interface where users can select actions for their virtual dog through numerical choices.<br>
-	Changing the dog's state (excitement, hunger, cleanliness) with the passage of time.<br>
-	Make the user able to teach the dog new words and commands.<br>
-	Create a dynamic in which the user must respond to the dog's inputs/statements to change its state.<br>
-	Have the possibility to exit or restart the game with another pet. <br>
-	Display the instructions in a slow manner (typing) to create a narrative effect.<br>
-	Keep the instructions and commands to access the game as simple and clear as possible.<br></p>

<h1>User Stories</h1>

<h1>Design</h1>
<p>The project relies on a pre-built terminal, limiting the design aspect.<br> Nonetheless, I aimed to enhance user engagement with a welcoming background featuring cute puppies. The central placement of the terminal adds visual balance to the page. 
To create a more welcoming atmosphere and remember the Japanese origins of this game genre (like the Tamagotchi and Nintendogs), Japanese emojis were incorporated into the text displayed in the terminal.<br></p>

<h1>Flowchart</h1>

<h1>Features</h1>

<h1>Technologies used</h1>
<p>Phyton: the application is entirely written in Phyton. <br>
HTML and CSS: HTML and CSS were used to style the layout of the page. <br>
Javascript: it was used by Code Institute to set up the terminal. <br>
Github: it was used to store the repository of the project (pushed from VSCode). <br>
VSCode: it was used for the coding process and to push the code to github. <br>
Heroku: it was used for deployment of the application. <br>
Git: version control.</p><br>

<h1>Modules imported</h1>
<p>from random import randrange <br>
from time import sleep <br>
import sys <br>
import time </p><br>

<h1>Bugs and Errors </h1>
| **Bug** | **Fix** |
| --- | --- |
| Background not showing when the app is deployed | I fixed this bug moving the CSS styiling inside the index.html file (between style tags) instead of having a separated stylesheet. The background pictures cannot be saved only locally, but needs to be stored online. Trying to save a picture for the backroung of the terminal in an asset folder will result in an error (file not found).|
| The dog learns the command after the 3rd time it is repeated, but the command was actually learnt after the 4th time.| The 3rd time the command was input by the user, the function was not increasing the integer before checking the count. By fixing this issue the bug was also fixed.|

<p>The project follows the PEP8 style guidelines and passes the CI Phyton Linter https://pep8ci.herokuapp.com with no errors or warnings.</p><br>

<h1>Deployment</h1>

<h1>Credits</h1>
<p>The initial part of the game was made through this game building video:
https://www.youtube.com/watch?v=7m6O9zqZFZ8 <br>
Empty and blank string in Phyton: https://www.scaler.com/topics/check-if-string-empty-python/#method3 <br>
About the sleep function: https://www.freecodecamp.org/news/the-python-sleep-function-how-to-make-python-wait-a-few-seconds-before-continuing-with-example-commands/#:~:text=You%20can%20use%20Python%27s%20sleep,pauses%20between%20words%20or%20graphics. <br>
Slow typing: https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing <br>
How to use Randome choice() method: https://www.w3schools.com/python/ref_random_choice.asp <br> 
Text by me and corrected (English mistakes, vocabulary) with DeepL and ChatGPT. <br>
Pictures from open source website: https://unsplash.com <br>
Japanese Emoji: http://kaomoji.ru/en/#hugging <br>
Font: https://fonts.google.com <br>
A big thank you to the Student Support of Code Institute and my facilitator who have been extremely helpful. <br>
A big thank you also to the Slack Community and particularly my brilliant classmates and their advice. </p><br>
