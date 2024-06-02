# shiny-happiness


### Running the server

- Install docker using steps mentioned [here](https://docs.docker.com/engine/install/).
- In your terminal run"
```sh
docker compose up --build 
```
- You can use any client to make request
- Check if server is up 
```sh
curl http://localhost:2121/ready
```

### Connecting to DB
You can use any CLI or UI clients to login to the local database.
```sh
PGPASSWORD=password psql -h localhost -U postgres mydatabase
```

