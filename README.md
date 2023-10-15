
# Web-service to capture riddles.

## Welcome to my test web project with riddles.

The main goal of this project is to build a web-service that alows us to take a riddles from https://jservice.io/api/random?count=1 (count is a number of riggles which we want to get).

## Prepare system

At the first step prepare your system for launching.
If you have processing PGADMIN or Postgresql-server you have to stop them both to clear necessary ports (such as 80 and 5432 which are used by both containers).

* open your terminal (if you use ubuntu or another lunix-based OS);
* insert next command 'sudo systemctl stop [name_of_service]'.
 

## Up the container from .yaml
 
 Next step - come into project-file and insert command for docker-compose:
 * docker compose up

## Web-service usage
* Enter into your browser Address - http://localhost:5000
* Then insert how much riddles do you want to get
* Press button 'Get riggles'
Server will return you IDs of riddles which were added into database.


There is PGADMIN in service that alows to manage database clearly.
Address - http://localhost:80
Data for verification:
* email: test@gmail.com
* password: 1234
	
Then register your server:
* choose name of server by yourself. Name is not imoprtant;
* host name/address - 172.18.0.2;
	or something else - you can find it in docker-destop or by teminal
	using next comand 'docker inspect [name_of_container]' (advice get to the bottom)
* port - 5432;
* password - 1234;
* username - postgres.
 

Here's a set of configurations.
 
 ![Screenshot from 2023-10-15 19-43-09](https://github.com/GorRatsy/riddles_capture/assets/93947333/1c86ff98-612f-4075-966f-b9f060058e9f)


You will get the same result with command beyond. This is example from docker-desktop.
  
  ![Screenshot from 2023-10-15 19-42-50](https://github.com/GorRatsy/riddles_capture/assets/93947333/a82024a7-a7cf-4f94-adc3-23fd66981f78)

		
Thank you for your time. Enjoy.
