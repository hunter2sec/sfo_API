# API for Sword Fighter Online
## A made up online game
Created with JWT-enabled Django Rest Framework.
### Items
Items are in-game items that can be bought or sold.

## Usage Examples:
Check `/api/` for a list of resources.

### regular token
```bash
curl -X POST -H "Content-Type: application/json" -d '{"username":"user1","password":"coolpass"}' http://localhost:8000/api/token/get/
```

### admin token
```bash
curl -X POST -H "Content-Type: application/json" -d '{"username":"admin","password":"coolpass"}' http://localhost:8000/api/token/get/
```

### getting all items (requires basic auth)
```bash
curl -H "Authorization: JWT <token>" http://localhost:8000/api/items/
```

### getting all users (requires admin privileges)
```bash
curl -H "Authorization: JWT <token>" http://localhost:8000/api/users/
```
