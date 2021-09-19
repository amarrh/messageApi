# REST API Messaging service 
Secure messaging implementation for Notification center

## Description

REST API created with Django REST Framework for message exchange between users. 

Messages have 3 importance levels (H, M or L) and are comprised of short summary (up to 25 characters long) and text message (up to 256 characters long). The service keeps track of message being read or unread by the user. Users can write new messages, and are allowed to read/delete only the messages they've sent or received.

SQLite3 database is used for storing the data.

## Visuals

![alt_text](https://i.imgur.com/hJ7bKro.png)

![alt_text](https://i.imgur.com/1PrXHOI.png)

![alt_text](https://i.imgur.com/VhFhrnR.png)

## Contributing
Pull requests are welcome. 
