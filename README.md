# Movie Recommendation System
 
 > Authors: \<[Piyush Mundhra](https://github.com/piyushmundhra)\>
  \<[Jimmy Han](https://github.com/jhan136)\>
  \<[Srikar Voleti](https://github.com/vsrikar08)\>
 
## Project Description
 > We are creating a movie recommendation system. A lot of services and products that we use have recommendation systems: such as Amazon and its product recommendations, YouTube and its video recommendations, etc. Therefore it seems like this is an important program to understand and be familiar with. 
 > We plan to use the following languages and tools for this project:
 >   * We plan to use Python, when working with large data sets and machine learning, its most sensible to use Python. 
 > 
 > In terms of how the program will work, we plan to have the user rate a set of 10-15 movies, from which we will try to "calculate" their taste. We plan to output the movie we think they will like most (from where they can also opt to ask for another recommendation). 
 > 
 > We will be using the following design patterns to organize this project:
 >   * We are using the Facade Design Pattern. We plan to develop an algorithm that helps us suggest a movie to a user. We do not want to overcomplicate the user experience, so we will have to be a way to hide the algorithm behind the user interface. We think it may be hard to get sufficient information from the user in a terminal based program, so we plan on finding a way to train the recommender system to use a small set of movies to understand the user's taste. 
 >   * We are also going to use the Template Method. Training a neural network or an SVM for the purpose of building a recommender system requires several algorithms such as forward propagation, backward propagation, and gradient descent. Rather than implementing all of these together, we plan to have a skeletal algorithm call each of these as required. We anticipate that it may be hard to stitch all of these together so we plan on working on this problem from the top down, which will help ensure prioritization of their coherence as opposed to individual functionality (which is also important, of course).
 >   * We are also going to use the Strategy Design Pattern. The main components of this design pattern are the compositor and compositions. We plan to have a lot of information behind the scenes and not all of this will be presented to the user. This means that we need a way to store the data in an organized fashion so that we can neatly present our predictions to the user. We feel that the best way to do this
## Diagram 
 > ![composite pattern](https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/Final%20Project%20OMT%20(2).png)

 > The program will be using a Recommender class that will be the underlying algorithm for movie recommendations. We will be using public datasets to train the model. An object of this class will be a member of the Options class, which is derived from the userOptions abstract class. We plan on making multiple derived classes from the userOptions class so that the user can choose different filtering critera based on their needs. We will then create a main function that will have a harness using the userOptions class and interact with the user using the command line.

 > ## Final deliverable
 > All group members will give a demo to the TA during lab time. The TA will check the demo and the project GitHub repository and ask a few questions to all the team members. 
 > Before the demo, you should do the following:
 > * Complete the sections below (i.e. Screenshots, Installation/Usage, Testing)
 > * Plan one more sprint (that you will not necessarily complete before the end of the quarter). Your In-progress and In-testing columns should be empty (you are not doing more work currently) but your TODO column should have a full sprint plan in it as you have done before. This should include any known bugs (there should be some) or new features you would like to add. These should appear as issues/cards on your Kanban board. 
 
 ## Screenshots
 > Screenshots of the input/output after running your application
 ## Installation/Usage
 > Instructions on installing and running your application
 ## Testing
 > The testing of our project was conducted in two ways: manual testing and python's built in unittest library. Manual testing had to be used because many of our methods were based on user input and command line interaction. To test these we thought of edge cases and tested them. 
 > * This part of the section goes over our manual testing for Options2
 >   * The first screenshot shows our test of invalid inputs of the initial prompt, we tested all edge cases and made sure that the program was correctly handling them. In this test, the following are the ordered inputs: '\n', '-', 'f', '-1', '-2'. ![initial prompt invalid input](https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/screenshots/initialPrompt.png)
 >   * Similarly, the next screenshot shows testing of invalid inputs for the movie rating segment of our Options2 derived class. Again, theordered inputs: '\n', '-', 'f', '-1', '-2'. We only include a screenshot of the testing done for the first movie, but the same tests were conducted for each consequent movie that has to be rated by the user. ![invalid movie rating](https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/screenshots/movieInvalidEntry.png)
 >   * Next, we had to test our getUserRecs() functionality for Options2. This derived class specifies that it will only give recommendations up to the number of movies the user liked. So we tested this in three ways, the user liked no movies, the user likes all movies, or the user likes some movies. The following screenshots show the successful executions of our program on all three input categories. 
 >     * First we test to make sure the program works when a user likes no movies: ![num movies liked test](https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/screenshots/nomoviesliked.png)
 >     * Then we test to make sure the program works when a user likes all the movies: ![num movies liked test2](https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/screenshots/allmoviesliked1.png) ![num movies liked test2](https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/screenshots/allmoviesliked2.png) ![num movies liked test2](https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/screenshots/allmoviesliked3.png)
 >     * Lastly, we tested to make sure the program works when a user likes some movies: ![num movies liked test2](https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/screenshots/somemoviesliked.png)
 
