
# Web-service to capture riddles.

## Welcome to my test web project with riddles.

The main goal of this project is to build a web-service that alows us to take a riddles from https://jservice.io/api/random?count=1 (count is a number of riggles which we want to get).

## Prepare system

At the first step I want to explain to you how to prepare your system for launching.
If you have processing PGADMIN or Postgresql-server you have to stop them both to clear necessary ports (such as 80 and 5432 which are used by both services).

You can ask me how, it's simply:
 - open your terminal (if you use ubuntu or another lunix-based OS);
 - insert next command 'sudo systemctl stop [name_of_service]'.
 
 If you're Windows user try Google-search.

## Up the container from .yaml
 
 Next step - come into project-file and insert command for docker-compose:
 	- docker compose up
 	- enjoy
 	
P.S.
	To check up your database I added PGADMIN into this service:
	- email: test@gmail.com
	- password: 1234
	
Then register your server:
	- choose name of server by yourself (maybe you choose something like unicorn :-) )
	- host name/address - 172.18.0.2

 Here's a set of configurations.
 ![Screenshot from 2023-10-15 19-43-09](https://github.com/GorRatsy/riddles_capture/assets/93947333/1c86ff98-612f-4075-966f-b9f060058e9f)

		or something else - you can find it in docker-destop or by teminal
		using next comand 'docker inspect [name_of_container]' (advice get to the bottom)

  You will get the same result with command beyond. This is example from docker-desktop.
  ![Screenshot from 2023-10-15 19-42-50](https://github.com/GorRatsy/riddles_capture/assets/93947333/a82024a7-a7cf-4f94-adc3-23fd66981f78)

		

I hope that you know simple SQL-requests.
Thank you for your time. Enjoy.
