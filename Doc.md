### Tests for the Flask Shopping List API

Here are the **Postman tests** and **cURL commands** for testing each API endpoint.

---

#### 1. **Get All Items**

**Postman Test**:
- Method: `GET`
- URL: `http://127.0.0.1:5000/items`
- Headers: None
- Body: None
- Expected Response: List of all items (JSON array).

**cURL Command**:
```bash
curl -X GET http://127.0.0.1:5000/items
```

---

#### 2. **Add a New Item**

**Postman Test**:
- Method: `POST`
- URL: `http://127.0.0.1:5000/items`
- Headers: `Content-Type: application/json`
- Body (raw JSON):
```json
{
  "item_name": "Milk",
  "quantity": 2
}
```
- Expected Response: Success message with item ID.

**cURL Command**:
```bash
curl -X POST http://127.0.0.1:5000/items \
-H "Content-Type: application/json" \
-d '{"item_name": "Milk", "quantity": 2}'
```

---

#### 3. **Update an Item**

**Postman Test**:
- Method: `PUT`
- URL: `http://127.0.0.1:5000/items/1`
- Headers: `Content-Type: application/json`
- Body (raw JSON):
```json
{
  "item_name": "Eggs",
  "quantity": 12
}
```
- Expected Response: Success message.

**cURL Command**:
```bash
curl -X PUT http://127.0.0.1:5000/items/1 \
-H "Content-Type: application/json" \
-d '{"item_name": "Eggs", "quantity": 12}'
```

---

#### 4. **Delete an Item**

**Postman Test**:
- Method: `DELETE`
- URL: `http://127.0.0.1:5000/items/1`
- Headers: None
- Body: None
- Expected Response: Success message.

**cURL Command**:
```bash
curl -X DELETE http://127.0.0.1:5000/items/1
```

---

#### 5. **Get a Single Item**

**Postman Test**:
- Method: `GET`
- URL: `http://127.0.0.1:5000/items/1`
- Headers: None
- Body: None
- Expected Response: Details of the item with ID 1.

**cURL Command**:
```bash
curl -X GET http://127.0.0.1:5000/items/1
```
