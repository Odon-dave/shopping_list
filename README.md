
---

### README: Shopping List API Documentation

---

# Shopping List API

A simple Flask API to manage a shopping list. The API allows you to create, retrieve, update, and delete shopping items.

## Features
- Add items to a shopping list.
- Retrieve all items or a specific item by ID.
- Update item details.
- Delete items from the shopping list.

---

## Endpoints

### **1. Get All Items**
- **URL**: `/items`
- **Method**: `GET`
- **Response**:
  ```json
  [
    {
      "id": 1,
      "item_name": "Milk",
      "quantity": 2
    },
    {
      "id": 2,
      "item_name": "Bread",
      "quantity": 1
    }
  ]
  ```

---

### **2. Add a New Item**
- **URL**: `/items`
- **Method**: `POST`
- **Request Body**:
  ```json
  {
    "item_name": "Milk",
    "quantity": 2
  }
  ```
- **Response**:
  ```json
  {
    "message": "Item added successfully",
    "id": 1
  }
  ```

---

### **3. Update an Item**
- **URL**: `/items/<item_id>`
- **Method**: `PUT`
- **Request Body**:
  ```json
  {
    "item_name": "Eggs",
    "quantity": 12
  }
  ```
- **Response**:
  ```json
  {
    "message": "Item updated successfully"
  }
  ```

---

### **4. Delete an Item**
- **URL**: `/items/<item_id>`
- **Method**: `DELETE`
- **Response**:
  ```json
  {
    "message": "Item deleted successfully"
  }
  ```

---

### **5. Get a Single Item**
- **URL**: `/items/<item_id>`
- **Method**: `GET`
- **Response**:
  ```json
  {
    "id": 1,
    "item_name": "Milk",
    "quantity": 2
  }
  ```

---

## Running the Application

### Prerequisites
- Python 3.7+
- Flask library
- SQLite (comes pre-installed with Python)

### Installation
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Install dependencies:
   ```bash
   pip install flask
   ```
3. Run the app:
   ```bash
   python app.py
   ```

### Database Initialization
The database is automatically initialized when you run the app for the first time. It creates a `shopping_list.db` file and a `shopping_list` table.

---

## Testing the API
- Use **Postman** or **cURL** to test the endpoints (examples provided above).
- Ensure the server is running before sending requests.

---

## Error Handling
- **404 Not Found**: Returned if an item or endpoint does not exist.
- **500 Internal Server Error**: Returned for unexpected server errors.
- **400 Bad Request**: Returned for invalid inputs (e.g., missing `item_name`).

---