# \<Movie Recommendation System\>
 > Your author list below should include links to all members GitHub (remove existing author).
 
 > Authors: \<[Piyush Mundhra](https://github.com/piyushmundhra)\>
  \<[Jimmy Han](https://github.com/jhan136)\>
  \<[Srikar Voleti](https://github.com/vsrikar08)\>
 
 > You will be forming a group of **THREE** students and working on an interesting project. A list of proposed project ideas that have been successful in previous quarters is given in the project specifications link on iLearn. You can select an idea from the list and decide which design patterns you will use to implement it. If you want to propose your own original idea, you will have to contact an instructor to discuss the project and obtain written permission before you submit your project proposal. Your project needs to implement two design patterns.The project work should be divided almost equally among team members and each member is expected to work on at least one design pattern (more than one partner may work on a pattern) and some of its test cases. You can of course help each other, but it needs to be clear who will be responsible for which patterns and for which features.
 > 
## Project Description
 > We are creating a movie recommendation system. A lot of services and products that we use have recommendation systems: such as Amazon and its product recommendations, YouTube and its video recommendations, etc. Therefore it seems like this is an important program to understand and be familiar with. 
 > We plan to use the following languages and tools for this project:
 >   * We plan to use Python, when working with large data sets and machine learning, its most sensible to use Python. 
 >   * [toolname](link) - Short description
 > We plan to have the user rate a set of 10-15 movies, from which we will try to "calculate" their taste. We plan to output the movie we think they will like most (from where they can also opt to ask for another recommendation). 
 > We will be using the following design patterns to organize this project:
 >   * We are using the Facade Design Patter. We plan to develop an algorithm that helps us suggest a movie to a user. We do not want to overcomplicate the user experience, so we will have to be a way to hide the algorithm behind the user interface. We think it may be hard to get sufficient information from the user in a terminal based program, so we plan on finding a way to train the recommender system to use a small set of movies to understand the user's taste. 
 >   * We are also going to use the Template Method. Training a neural network or an SVM for the purpose of building a recommender system requires several algorithms such as forward propagation, backward propagation, and gradient descent. Rather than implementing all of these together, we plan to have a skeletal algorithm call each of these as required. We anticipate that it may be hard to stitch all of these together so we plan on working on this problem from the top down, which will help ensure prioritization of their coherence as opposed to individual functionality (which is also important, of course).
 >   * We are also going to use the Strategy Design Pattern. The main components of this design pattern are the compositor and compositions. We plan to have a lot of information behind the scenes and not all of this will be presented to the user. This means that we need a way to store the data in an organized fashion so that we can neatly present our predictions to the user. We feel that the best way to do this is by using a Strategy Design Pattern

 > ## Phase II
 > In addition to completing the "Class Diagram" section below, you will need to 
 > * Set up your GitHub project board as a Kanban board for the project. It should have columns that map roughly to 
 >   * Backlog, TODO, In progress, In testing, Done
 >   * You can change these or add more if you'd like, but we should be able to identify at least these.
 > * There is no requirement for automation in the project board but feel free to explore those options.
 > * Create an "Epic" (note) for each feature and each design pattern and assign them to the appropriate team member. Place these in the `Backlog` column
 > * Complete your first *sprint planning* meeting to plan out the next 7 days of work.
 >   * Create smaller development tasks as issues and assign them to team members. Place these in the `Backlog` column.
 >   * These cards should represent roughly 7 days worth of development time for your team, taking you until your first meeting with the TA
## Class Diagram
 > Include a class diagram(s) for each design pattern and a description of the diagram(s). Your class diagram(s) should include all the main classes you plan for the project. This should be in sufficient detail that another group could pick up the project this point and successfully complete it. Use proper OMT notation (as discussed in the course slides). You may combine multiple design patterns into one diagram if you'd like, but it needs to be clear which portion of the diagram represents which design pattern (either in the diagram or in the description). 
 
 > ## Phase III
 > You will need to schedule a check-in with the TA (during lab hours or office hours). Your entire team must be present. 
 > * Before the meeting you should perform a sprint plan like you did in Phase II
 > * In the meeting with your TA you will discuss: 
 >   - How effective your last sprint was (each member should talk about what they did)
 >   - Any tasks that did not get completed last sprint, and how you took them into consideration for this sprint
 >   - Any bugs you've identified and created issues for during the sprint. Do you plan on fixing them in the next sprint or are they lower priority?
 >   - What tasks you are planning for this next sprint.

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
 > How was your project tested/validated? If you used CI, you should have a "build passing" badge in this README.
 
