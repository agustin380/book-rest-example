### Challenge: "RESTful Book" Web Service

You should:
- Use Flask or Falcon as your framework
- Support the following entity types:
    - Book
    - Chapter

A Book is a collection of zero or more Chapters.  
By making HTTP requests, one should be able to do the following:

- Get a list of all existing Books in your database
- Get a list of all Chapters within a single Book
- Create a new Book (with required "Title" and "Author" fields)
- Create Chapters (with a required "Name" field) which - will belong to an existing Book
- Change the "Name" field of an existing Chapter
- Delete an existing Chapter
- Update the Title and/or Author fields of the Book
- Delete an existing Book
