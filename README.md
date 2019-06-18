# Code Examples:

### regular token
curl -X POST -H "Content-Type: application/json" -d '{"username":"hacker","password":"fakepassword"}' http://localhost:8000/api/token/get/

### admin token
curl -X POST -H "Content-Type: application/json" -d '{"username":"admin","password":"fakepassword"}' http://localhost:8000/api/token/get/

### getting all items (requires basic auth)
curl -H "Authorization: JWT <token>" http://localhost:8000/api/items/

### getting all users (requires admin privileges)
curl -H "Authorization: JWT <token>" http://localhost:8000/api/users/