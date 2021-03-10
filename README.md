# Movie Recommendation System
 
 > Authors: \<[Piyush Mundhra](https://github.com/piyushmundhra)\>
  \<[Jimmy Han](https://github.com/jhan136)\>
  \<[Srikar Voleti](https://github.com/vsrikar08)\>
 
## Project Description
 > We are creating a movie recommendation system. A lot of services and products that we use have recommendation systems: such as Amazon and its product recommendations, YouTube and its video recommendations, etc. Therefore it seems like this is an important program to understand and be familiar with. 
 > We plan to use the following languages and tools for this project:
 >   * We plan to use Python, when working with large data sets and machine learning, its most sensible to use Python. 
 > 
 > In terms of how the program will work, we have the user rate a set of 4 movies, from which we will try to "calculate" their taste. We plan to output movies we think they will like most (from where they can also opt to ask for another recommendation). They can also choose to receive recommendations based on specific movies by inputting an IMDb id.
 > 
 > We will be using the following design patterns to organize this project:
 >   * We are using the Facade Design Pattern. We plan to develop an algorithm that helps us suggest a movie to a user. We do not want to overcomplicate the user experience, so we will have to be a way to hide the algorithm behind the user interface. We think it may be hard to get sufficient information from the user in a terminal based program, so we plan on finding a way to train the recommender system to use a small set of movies to understand the user's taste. 
 >   * We are also going to use the Template Method. Training a neural network or an SVM for the purpose of building a recommender system requires several algorithms such as forward propagation, backward propagation, and gradient descent. Rather than implementing all of these together, we plan to have a skeletal algorithm call each of these as required. We anticipate that it may be hard to stitch all of these together so we plan on working on this problem from the top down, which will help ensure prioritization of their coherence as opposed to individual functionality (which is also important, of course).
 >   * We are also going to use the Strategy Design Pattern. The main components of this design pattern are the compositor and compositions. We plan to have a lot of information behind the scenes and not all of this will be presented to the user. This means that we need a way to store the data in an organized fashion so that we can neatly present our predictions to the user. We feel that the best way to do this
## Diagram 
 > ![composite pattern](https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/Final%20Project%20OMT%20(2).png)

 > The program will be using a Recommender class that will be the underlying algorithm for movie recommendations. We will be using public datasets to train the model. An object of this class will be a member of the Options class, which is derived from the userOptions abstract class. We plan on making multiple derived classes from the userOptions class so that the user can choose different filtering critera based on their needs. We will then create a main function that will have a harness using the userOptions class and interact with the user using the command line.
 
 ## Screenshots
 > The recommender system should start by asking the user for one of two options. The first option, chosen by inputting "0", would have movies recommended to them based off of whether they like or dislike a selection of movies presented to them.\
 > <br />
 >  &nbsp;&nbsp;<img src = https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/screenshots/userTaste%20photo.png width="450"/>\
 >  <br />
 >  The second option, chosen by inputting "1",  would have movies recommended to the user based off of a movie they already like. The user starts by selecting the amount of movies that will be recommended to them, which can be anywhere from 1 to 10. After which, they input the movie of their choice, via IMDB ID.\
 >  <br />
 >     &nbsp;&nbsp;<img src=https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/screenshots/options2_apocalypsenow.png width="450"/> \
 >     <br />
 >     &nbsp;&nbsp;<img src=https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/screenshots/Screenshot%20(57).png width="450"/> \
 >     <br />
 >     In any case where input is not what is intended, the user will be prompted to enter a valid input. \
 >     <br />
 >     &nbsp;&nbsp;<img src=https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/screenshots/Screenshot%20(50).png width="450"/>\
 >     <br />
 >     &nbsp;&nbsp;<img src=https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/screenshots/Screenshot%20(52).png width="450"/>\
 >     <br />
 >     &nbsp;&nbsp;<img src=https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/screenshots/Screenshot%20(54).png width="450"/>\
 >     <br />
 >     Finally, at the end of both options, the user will be prompted for whether they would like to reset the program, see more recommendations, or exit out of the system.
 ## Installation/Usage
 > Instructions on installing and running your application: 
 > * Python environment details:
 >   * The program required you to be running Python 3.0 or above. This can be checked with <code>$ python --version</code>
 > * Dependancies
 >   * Pandas: Once we are sure that the installation is Python 3.0 or above, we import pandas using <code>$ pip install pandas</code>.
 > * Downloading and running program:
 >   * After that, we git clone the repository, which can be found in our github page. 
 >   * Then we go into the repository. using <code> $ cd final-project-svole001-jhan136-pund001 </code>.
 > Running the program:
 > We then run the python code by using <code> $ python3 \_\_main\_\_.py </code>, our main executable file. 
 > * Details of utilizing features:
 >   * If you are using the option that asks you to rate movies, you can only get recommendations up to the number of movies you state you like.
 >   * If you are specifying an IMDb id to generate recommendations, you can keep regenerating the recommendation list (this should not change)
 >   * The rest of the program includes prompts and is self expanatory.
 
 ## Memory checks
 > A memory leak happens when memory is specifically allocated and never deallocated. When strictly speaking of Python code, memory leaks are not possible because of Python's garbage collecter (aka GC). In Python, memory leaks can only occur from the Python interpreter or and libraries or modules written in C/C++. In this project, 100% of our code is done using Python, without any strong references. This means that the only possible sources of memory leaks are outside the scope of this project. In addition, the only modules used are major Python libraries. Based on all of this, we concluded that our code cannot have any memory leaks based on the information we found regarding Python and memory.
 
 ## Testing
 > The testing of our project was conducted in two ways: manual testing and python's built in unittest library. Manual testing had to be used because many of our methods were based on user input and command line interaction. To test these we thought of edge cases and tested them. 
 > * First, we discuss the testing for the Recommender class. This class has unit tests that thoroughly tested edge cases and invalid inputs for imdbToMovie() and has_movie(). For imdbToMovie(), we test several forms of invalid inputs, also test to see if it correctly converts the first, last, and random median movie. For has_movie(), the testing conducted is nearly the same. To test the getRecommendation() function, we used the function in our implemented userOptions derived classes and made sure that we were getting recommendations. This is not possible to test with unit tests since it depends on user input and can't be predicted.
 > * This part of the section goes over our testing for Options1. The unit tests for Options1 tested the is_not_integer() function thoroughly. Below is a description of the manual testing of Options1. This includes testing general and edge cases for invalid user input.
 >   * The first screenshot shows our test of invalid inputs of the initial prompt, we tested all edge cases and made sure that the program was correctly handling them. In this test, the following are the ordered inputs: '\n', '-', 'f', '-1', '-2'. 
 >   * <img src = https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/screenshots/initialPrompt.png width="450" />
 >   * Similarly, the next screenshot shows testing of invalid inputs for the movie rating segment of our Options1 derived class. Again, theordered inputs: '\n', '-', 'f', '-1', '-2'. We only include a screenshot of the testing done for the first movie, but the same tests were conducted for each consequent movie that has to be rated by the user. 
 >   * <img src = https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/screenshots/movieInvalidEntry.png width="450" />
 >   * Next, we had to test our getUserRecs() functionality for Options1. This derived class specifies that it will only give recommendations a number of times up to the number of movies the user liked (If the user likes 3 movies then we can only give up to 3 recommendations). So we tested this in three ways, the user liked no movies, the user likes all movies, or the user likes some movies. The following screenshots show the successful executions of our program on all three input categories. 
 >     * First we test to make sure the program works when a user likes no movies: 
 >     * <img src = https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/screenshots/nomoviesliked.png width="450"/>
 >     * Then we test to make sure the program works when a user likes all the movies: 
 >     * <img src=https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/screenshots/allmoviesliked1.png width="450"/> 
 >     * <img src=https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/screenshots/allmoviesliked2.png width="450"/> 
 >     * <img src=https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/screenshots/allmoviesliked3.png width="450"/>
 >     * Lastly, we tested to make sure the program works when a user likes some movies: 
 >     * <img src=https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/screenshots/somemoviesliked.png width="450"/>
 >     * The following screenshot checks to make sure that the exit program option succeeds for options1
 >     * <img src=https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/screenshots/options1exit.png width="450" />
 >  * This part of the section goes over our testing for Options2. The unit tests for Options2 also tested the is_not_integer() function thoroughly. Below is a description of the manual testing of Options2. The Options2 class depends on the Recommender class (whose testing is done separately) to verify user input.
 >     * The image below shows an initial testing of getUserOptions()'s command line interaction. This function should only accept integer values between 1 and 10, rejecting all other types of values
 >     * <img src=https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/screenshots/nummovies.png width="450"/>
 >     * The next image shows testing of getUserTaste()'s command line interaction. This function should only accept movies that are within Recommender's data. It relies on the has_movie() function in the Recommender class. It helps us verify a couple things: we know that the invalid inputs are being handled correcly and we also can see that it is recommending the correct amount of movies. An issue this helps us identify is that the first movie recommended is the movie we based our recommendations on. This is not a bug and is rather a byproduct of our recommendation algorithm, which utilizes pairwise correlation. 
 >     * <img src=https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/screenshots/getimdbidtest.png width="450"/>
 >     * The image below is a test of the getUserRec() function. In Options2, it should reload the recommendations based on the previously specified movie. It also tests the restart program option given to the user. Both of these tests are successful.
 >     * <img src=https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/screenshots/options1getrec.png width="450"/>
 >     * The following screenshot checks to make sure that the exit program option succeeds for Options2
 >     * <img src=https://github.com/cs100/final-project-svole001-jhan136-pund001/blob/master/screenshots/options1exit.png width="450" />
