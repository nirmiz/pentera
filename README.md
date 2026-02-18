Docker SSH & Python Server Setup

Start containers:
```
docker-compose up --build -d
```

SSH into the SSH server:
```
ssh -p 2222 sshuser@localhost
```

From inside SSH container, access Python server:
```
curl python-server:5050
```

View logs:
```
docker logs python-server
or
cat logs/access.log
```

Stop containers:
```
docker-compose down
```

Note: Port 5050 is NOT exposed to host - only accessible from the SSH container.

