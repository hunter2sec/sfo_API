# API for Sword Fighter Online
## A made up online game
Created with JWT-enabled Django Rest Framework.

## Usage Examples:

### regular token
curl -X POST -H "Content-Type: application/json" -d '{"username":"user1","password":"coolpass"}' http://localhost:8000/api/token/get/

### admin token
curl -X POST -H "Content-Type: application/json" -d '{"username":"admin","password":"coolpass"}' http://localhost:8000/api/token/get/

### getting all items (requires basic auth)
curl -H "Authorization: JWT <token>" http://localhost:8000/api/items/

### getting all users (requires admin privileges)
curl -H "Authorization: JWT <token>" http://localhost:8000/api/users/
