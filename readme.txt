Summary of Satellite Imagery Tool:

High level overview of the project:
1.) A user can create an instance of an analysis via a form (this model includes relevant information to create a query to Google EE, i.e. NE coordinate, SW coordinate, filter, etc.)
2.) Once the user inputs a new analysis, the Google EE script runs on that query informing users if there are available images / indicating if the new analysis is valid and stored (TO DO)
3.) There is a script function that runs that Google EE queries, it goes through every instance of the analysis instances and makes a query storing it in Google Firebase Storage. The images for each query will be named in the following format as a way to extract these images in the front end: "___case___.___type_of_analysis___.____date___"
4.) Once the images are exported to the firebase storage, the front end can display these images

What needs to be done:
1.) The front end design to match the wire frame
2.) Automatic querying and form validation once the form is submitted
3.) Using Google EE server side
4.) Async running of the query
5.) Researching Google EE to make sure that the queries are correct (currently some of the images are blurry)

How to make Google EE queries using the script:

REQUIREMENTS

To run the Google EE script, you need to (1) get authentication from Google EE and (2) creating virtual environment using Conda (follow instructions here: https://developers.google.com/earth-engine/python_install-conda.html)

In this virtual environment, I also installs all of the Django requirements / super shell extension

Once the requirements are satisfied you can run the script via a shell (note the Google firebase storage must be configured to a different port because it will direct it to me)

On the localhost: access visualization of images via: localhost:8000; access the form via localhost:8000/create-analysis





