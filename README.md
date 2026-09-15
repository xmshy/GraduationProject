Project Structure
```
   ├── main.py              # FastAPI Proxy Interceptor Source Code
   ├── Dockerfile           # Gateway Container Specs
   ├── docker-compose.yml   # Multi-Container Topology (WAF + Honeypot)
└── README.md            # Execution & Deployment Docs
```

-------------------------------------------------------------------------
```Run with Docker Compose
#Build and start services in detached mode
```
```docker compose up --build -d```

#Verify running containers
   ```docker ps```

#Stream live interception logs
   ```docker compose logs -f```

#Stop and tear down environment
   ```docker compose down```
   
---------------------------------------------------------------------------
Testing Interception
Test incoming HTTP requests against the Gateway using curl:

  1. Normal GET Request Test:
      ```curl http://localhost:8000/api/v1/status```
   2. POST Payload Interception Test:
      ```curl -X POST http://localhost:8000/login -d "username=admin' OR 1=1--"```
