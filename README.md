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
- As a user I can personalize the virtual pet with name, breed and age group, so that I can have a customised game experience. <br>
- As a user I can access a simple menu of actions (defined by numbers), so that I can simply navigate the game and choose the game development. <br>
- As a user I need to understand the pet feedback, so that I can respond with an appropriate action. <br>
- As a user, I want to be able to feed, play and clean the dog. <br>
- As a user, I want to be able to teach my dog a word or a command. <br>
- As a user, I want to be able to go for a walk with the pet dog. <br>
- As a user, I want to be able to exit or restart the game whenever I wish. <br>


<h1>Design</h1>
<p>The project relies on a pre-built terminal, limiting the design aspect.<br> Nonetheless, I aimed to enhance user engagement with a welcoming background featuring cute puppies. The central placement of the terminal adds visual balance to the page. 
To create a more welcoming atmosphere and remember the Japanese origins of this game genre (like the Tamagotchi and Nintendogs), Japanese emojis were incorporated into the text displayed in the terminal. ASCII art has also being added to create a welcoming atmosphere and remind us of retro games.<br></p>

<h1>Flowchart</h1>
<image src="./assets/images/flowchart.png"><br>

<h1>Features</h1>
<h2>Welcome Message </h2>
<p>A brief introduction and welcome message is displayed together with the ASCII art of a pet dog. The user is given information about how to approach the game and what is the purpose of it. This is meant to be as simple and intuitive as possible.<br></p>
<image src="./assets/images/welcome-screen1.png"><br>

<h2>Name, breed, age</h2>
<p>Three questions are displayed to create an instance of the Dog class. At the beginning the user can customise their game experience by assigning the dog a name, breed and age group they prefer. The questions about name and breed are open questions, the user can type what he wishes. There is a validation system that prevent the user from leaving the string empty or blank. The question about the age group is a three-option question, this has also a validation system that doesn't allow the user to answer something different from A,B or C. <br>
The question about the breed is deliberately left without validation as to the breed type of the dog, in order to leave as much freedom as possible to the user. An alternative would have been to compare the answer against a predefined list of breeds (eliminating case sensitivity), but this could have created unnecessary and meaningless issues with the user's answer (considering the many breeds and mixed breeds).<br>
The chosen age group will affect directly the go_walk function with different scenarios.<br> 
After answering the questions, the dog introduces itself, this will give the user a feedback about their name and breed choices. <br>
Through the randrange function, the dog is assigned random levels of hunger, excitement and cleanliness. <br>
By clicking enter, the game starts.</p><br>
<image src="./assets/images/name-breed-age2.png"><br>

<h2>Main Menu</h2>
<p>The main menu has very intuitive and essential features: it is possible to choose to do with the virtual pet by clicking an option from 0 to 7. This menu reappears in loop everytime the user select a number and the scenario is displayed. The menu also has a validation system in case the user choose something different than 0-7.</p><br>
<image src="./assets/images/main-menu3.png"><br>

<h2>Food Feature</h2>
<p>By clicking the number 1, the user is given a feedback from the virtual pet. The pet will always thank the user for the food given, and according to the hunger level (provided initially by the randrange function) two other feedbacks can be displayed:<br>
"Please feed me more"<br>
"Thank you. I am full!"</p><br>
<image src="./assets/images/food.png"><br>

<h2>Talk Feature</h2>
<p>By clicking the number 2, the user can have an idea of the actual state of the virtual pet and what is needed to change/improve its state. The dog also will say a random word from a vocabulary list that could be updated by the user using the teach function. <br>
Talking with the dog, it will return its name and its description/state: <br>
f"{self.name} doggo is happy! *wiggles tale* (´♡‿♡`)"<br>
f"{self.name} doggo is hungry (＞﹏＜)"<br>
f"{self.name} doggo is sad and bored... (｡T ω T｡)"<br>
f"{self.name} doggo is stinky... (￣▽￣*)ゞ"<br>
f"{self.name} doggo is quiet... (*＾ω＾)人(＾ω＾*)"<br>
This is essential for the user to have an idea of how to proceed with the game. <br>
For example: <br>
<image src="./assets/images/talk1.png"><br>
And also: <br>
<image src="./assets/images/talk2.png"><br>
In this case the user should be pushed to play with the dog (option 4). <br>
<image src="./assets/images/talk3.png"><br>
In this other case the user should be encouraged to give the dog a bath (option 5).<br>
<image src="./assets/images/talk4.png"><br>
This is - for example - the feedback given by the virtual pet once the the user understand the pet need and decides to give the dog a bath. </p><br>

<h2>Teach a word</h2>
<p>By clicking 3, the user can teach a word to the dog. This word will be added to the list of words the do knows and will display in a random way when the command "talk with the dog" is chosen. The question has a validation method and the string cannot be blank or empty. </p><br>
<image src="./assets/images/teach.png"><br>

<h2>Play Feature</h2>
<p>By clicking 4, the user can make the dog play. The dog will always provide a feedback of enjoyment "Let's play, Woof!" and according to its random level of excitement it could also provide other 2 feedbacks:<br>
"I am sad and bored...(｡T ω T｡)", this should push the user to play again with the virtual pet.<br>
"I am so happy when you play with me! (´♡‿♡`)"</p><br>
<image src="./assets/images/play.png"><br>

<h2>Bath Feature</h2>
<p>By clicking 5, the user can give the virtual pet a bath. The response would generally be "I do not like baths". Depending also by the random level of cleaningness of the dog, other feedback could be provided:<br>
"I rolled in the mud (>ω^)"<br>
"Now I am fresh and clean (☆▽☆)"</p><br>
<image src="./assets/images/bath.png"><br>

<h2>Teach a command</h2>
<p>By clicking 6, the user can teach the dog a command. Instructions are provided: to learn a command, the dog needs practice. It is necessary to input the same command throught the game for 3 times for the dog to learn. A validation method has been implemented so that the string cannot be empty nor blank, and case sensitivity has been eliminated. This way, there is no difference if the user is trying to teach the dog the command "sit" or "Sit". <br>
For the first two times the same word is input, the game will display "I am trying to learn the command: '{learn_command}'... Please keep teaching me.", while the third time the game will display "I have learnt the command '{learn_command}', Thank you!"</p><br>
<image src="./assets/images/command1.png"><br>
<image src="./assets/images/command2.png"><br>

<h2>Go for a Walk</h2>
<p>By clicking 7, the user can bring the virtual pet for a walk. This function is directly dependent on the chosen group age. Difference group ages will have difference responses to the invite for a walk from the user. <br>
If the virtual dog is a puppy, the response is:<br>
<image src="./assets/images/walk-puppy.png"><br>
If the virtual dog is a young dog, the response is: <br>
<image src="./assets/images/walk-young-dog.png"><br>
In this case, the young dog meets on its way a friend. The type of animal and name of the friends are chosen through the "choice" function that selects a random element from a prepared list. The young dog could meet different type of animals (dog, cat, parrot...) with different names. <br>
If the virtual dog is an older dog, the response is: 
<image src="./assets/images/walk-older-dog.png"><br>
In this case, the dog appears to be tired. The preference is for staying at home cuddling with the owner. The dog also looks for a snack, and through the function choice it asks if it could be feeded with a random food from a list. The user can then decide with a three-option question if giving the requested food, not giving it or feeding the pet with something else. Both the three-option question and the open question have validation methods. <br>
In all cases, the walking or relaxing is simulated by slowing the time and adding some dots to the narration. </p><br>

<h2>Exit the game</h2>
<p>By clicking 0, the user can decide to exit the game, continue the game or restart the game from the beginning. This is a three-option question with a validation method. <br>
<image src="./assets/images/zero-choice.png"><br>
By exiting, the loop breaks and a message displays:<br>
<image src="./assets/images/exit-game.png"><br>
By continuing, the game continues and the main menu appears again. <br>
By restarting, the main function is returned and the game restart from the introduction and the three main questions of name, breed, age. </p><br>

<h2>Validation Methods</h2>
</p>Through the game different validation methods are implemented. <br>
- For the open questions, the "no_empty_string" function is used. This function provides a feedback to the user if the input is either blank or empty. The strip() method is used to check if the string is composed only by white spaces. If the string is empty or blank, a message is diplayed to the terminal "The input cannot be empty. Please enter a valid input.". <br>
- For the three-option questions (A,B,C), the three_choice_input is implemented. Answers could only be A, B or C (case sensitivity is eliminated by using the .upper() method), otherwise a message is displayed to the user "Please input a valid option. Enter 'A', 'B' or 'C'". <br>
- In the main menu, the validation is guaranteed by the if else statment, where "else" is paired with "Please input a valid option". </p><br>
<image src="./assets/images/empty-input.png"><br>
<image src="./assets/images/3-options-validation.png"><br>
<image src="./assets/images/validation-menu.png"><br>

<h2>Time Related Functions and Slow Typing</h2>
<p>To slow down the narration and create a typing effect, different time related functions have been implemented. <br>
- The function sleep() is used to create pauses in the game to give the appearance of the dog performing actions over time and to slow down the narration to give the user to follow the game easily. <br>
- The slow_typing function is implemented to create a typing effect which enhance the user experience and makes the game easier to follow.
- The __clock_tick function is essential to the game. It is called in the game after every other function to simulate the passage of time and make the levels of hunger, excitement and cleaningness of the dog decrease after every action. Every action requires an amount of energy, this changes the pet attributes through the game. </p><br> 

<h2>Case sensitivity</h2>
<p>Where the user is required to provide an input, case sensitivity has been eliminated by using the .upper() or .lower() method.</p><br>

<h1>Technologies used</h1>
<p>Phyton: the application is entirely written in Phyton. <br>
HTML and CSS: HTML and CSS were used to style the layout of the page. <br>
Javascript: it was used by Code Institute to set up the terminal. <br>
Github: it was used to store the repository of the project (pushed from VSCode). <br>
VSCode: it was used for the coding process and to push the code to github. <br>
Heroku: it was used for deployment of the application. <br>
Git: version control through VSCode.</p><br>

<h1>Modules imported</h1>
<p>- randrange: <br>
This function is imported from the random module. <br>
It is used to generate a random integer within a specified range. In my project it is used to initialize and manipulate attributes of the Dog class (food, excitement, and bath).<br>
- choice: <br>
This function is imported from the random module. <br>
It is used to select a random element from a list. In my project it is used to make random choices (selecting a random pet type or friend name during the walk).<br>
- sleep: <br>
Imported from the time module. <br>
It introduces a delay (in seconds) in the execution of a programme. In my project it is used to create pauses in the game to give the appearance of the dog performing actions over time and to slow down the narration to give the user to follow the game easily.<br>
- sys: <br>
Sys is used to manipulate a standard output, allowing to create a typing effect by printing characters one at a time. This again is to slow down the narration to give the user to follow the game easily. <br>
- time: <br>
The entire time module was imported. <br>
It provides various time-related functions. In my project it is used in conjunction with sleep to control the typing effect.<br></p><br>

<h1>Bugs and Errors </h1>
- Background not showing when the app is deployed: <br>
<br>
I fixed this bug moving the CSS styiling inside the index.html file (between style tags) instead of having a separated stylesheet. The background pictures cannot be saved only locally, but needs to be stored online. Trying to save a picture for the backroung of the terminal in an asset folder will result in an error (file not found).<br>
<br>
- The dog learns the command after the 3rd time it is repeated, but the command was actually learnt after the 4th time: <br>
<br>
The 3rd time the command was input by the user, the function was not increasing the integer before checking the count. By fixing this issue the bug was also fixed. <br>
<br>
- The dog needs to learn a command even if the command is written in a different way (e.g. "sit" and "Sit"): <br><br>
To eliminate case sensitivity I added the .lower() method to the input. 
<br>
<br>
<p>The project follows the PEP8 style guidelines and passes the CI Phyton Linter https://pep8ci.herokuapp.com with no errors or warnings.</p><br>
<image src="./assets/images/phyton-linter.png"><br>

<h1>Deployment</h1>
<h2>Version Control</h2>
<p>The website was created in VSCode and pushed to github to the repository "DoggoPal". <br>
- git add: preliminary step before committing new elements. <br>
- git commit -m "": commit changes to the repository.<br>
- git push: push the committed code to the GitHub repository. <br></p>
<h2>Deploy to Heroku</h2>
<p>The project was deployed to the cloud platform Heroku<br></p>
<p>Deployment steps:<br>
- In order for the project to run on Heroku, we  need Heroku to install the dependencies we used in the project. The list of dependencies will go in our requirements.txt file here. To create our list of requirements, we  use the following command in the terminal 'Pip3 freeze > requirements.txt'. In my project the requirements.txt file is empty because no dependencies were installed. This in the beginning was giving issue with the deployment (bug explained at the end of the section). Commit and push the changes to githhub.<br>
- Set up an Heroku account<br>
- On the dashboard, click "Create new app"<br>
- Name the App with a unique name ans select your region (EU/USA) and click "create app"<br>
-  It's important to get the settings section done before you deploying the code, click the settings tab on the top-left.<br>
-  Config Var section: if applicable (not the case of this project) add elements from .gitignore. To add as an additional config var: the key is PORT and the value is 8000. If you do not add this, thedeployment may fail. Click "Add".<br>
- Add buildpacks to the application: install more dependencies. Click "Add buildpack" and add Python, select that and then click “Save changes”. The second buildpack is called node.js, select that and click “Save”. Make sure the two buildpacks are in this order (phyton and then node.js).<br>
- Select Deployment method: Github <br>
- Confirm connceting with Github <br>
- Search the repository name to connect with Github (in this case "DoggoPal"). Click "Search" and "Connect".
- Enable automatic deploy: this way Heroku will rebuild the app every time a new change is pushed to Github.<br>
- It is also possible to use the manual deploy. Using the manual deploy is very useful if we want to see immediatly new elements we have just pushed to Github.<br>
- The site should show “App was successfully deployed” message and a button to view the deployed app. <br>
<br>
Deployment issue: during the first manual deployment of the app I experienced an issue related to the dependencies and the file requirements.txt. This was the issue displayed:
<image src="./assets/images/deployment-issue.png"><br>
VSCode is a local programme that is not already contained within a virtual environment (unlike Gitpod and Codeanywhere). Taking this into account, if we run the command pip3 freeze > requirements.txt, VSCode will install all packages on local (even what is not needed for the project). The issue could be solved by removing the added dependencies (since for this project I was not working with any) or set up a virtual environment for VSCode.<br>
</p>

<h1>Credits</h1>
<p>The initial part of the game was made through this game building video:
https://www.youtube.com/watch?v=7m6O9zqZFZ8 <br>
Empty and blank string in Phyton: https://www.scaler.com/topics/check-if-string-empty-python/#method3 <br>
About the sleep function: https://www.freecodecamp.org/news/the-python-sleep-function-how-to-make-python-wait-a-few-seconds-before-continuing-with-example-commands/#:~:text=You%20can%20use%20Python%27s%20sleep,pauses%20between%20words%20or%20graphics. <br>
Slow typing: https://stackoverflow.com/questions/4099422/printing-slowly-simulate-typing <br>
How to use Randome choice() method: https://www.w3schools.com/python/ref_random_choice.asp <br> 
Website used to create the flowchart: https://lucid.app <br>
Text by me and corrected (English mistakes, vocabulary) with DeepL and ChatGPT. <br>
Pictures from open source website: https://unsplash.com <br>
Japanese Emoji: http://kaomoji.ru/en/#hugging <br>
ASCII art: https://fsymbols.com/text-art/ <br>
https://www.asciiart.eu/text-to-ascii-art <br>
Font: https://fonts.google.com <br>
A big thank you to the Student Support of Code Institute and my facilitator who have been extremely helpful. <br>
A big thank you also to the Slack Community and particularly my brilliant classmates and their advice. </p><br>
