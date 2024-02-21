https://docs.docker.com/engine/reference/commandline/compose/

#for interactive app

docker compose run <servicename>

#docker compose up (for non interactive app)

#Build or rebuild service

docker compose build 

#Stop or remove containers

docker compose down

docker compose exec 	#Execute a command in a running container.

#List running containers

docker compose ps

"""
Remember:

If you made any changes in application file or Docker file


Always run :

docker compose build to get latest changes

"""
