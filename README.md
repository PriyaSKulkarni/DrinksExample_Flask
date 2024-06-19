# DrinksExample_Flask

# Drinks API

This is a simple Flask API for managing a list of drinks. It allows you to add, view, and delete drinks from a SQLite database.

## Setup and Installation

1. **Clone the repository:**
    ```sh
    git clone <repository-url>
    cd <repository-directory>  
    ```

2. **Create a virtual environment and activate it:**
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. **Install the required packages:**
    ```sh
    pip install -r requirements.txt
    ```

4. **Initialize the database:**
    ```sh
    flask shell
    >>> from app import db
    >>> db.create_all()
    >>> exit()
    ```

## Running the Application

1. **Start the Flask development server:**
    ```sh
    flask run
    ```

2. The API will be available at `http://127.0.0.1:5000`.

## API Endpoints

### 1. Get All Drinks
**Endpoint:** `GET /drinks`

**Response:**
```json
{
  "drinks": [
    {
      "name": "Drink Name",
      "description": "Drink Description"
    },
    ...
  ]
}
```

### 2. Get a Specific Drink
**Endpoint:** `GET /drinks/<id>`

**Parameters:**
- `id`: The ID of the drink.

**Response:**
```json
{
  "name": "Drink Name",
  "description": "Drink Description"
}
```

### 3. Add a New Drink
**Endpoint:** `POST /drinks`

**Request Body:**
```json
{
  "name": "New Drink Name",
  "description": "New Drink Description"
}
```

**Response:**
```json
{
  "id": new_drink_id
}
```

### 4. Delete a Drink
**Endpoint:** `DELETE /drinks/<id>`

**Parameters:**
- `id`: The ID of the drink.

**Response:**
```json
{
  "Message": "Deleted"
}
```
or
```json
{
  "error": "not found"
}
```

## Example Usage

**Adding a Drink:**
```sh
curl -X POST -H "Content-Type: application/json" -d '{"name":"Coca-Cola", "description":"A popular soda."}' http://127.0.0.1:5000/drinks
```

**Getting All Drinks:**
```sh
curl http://127.0.0.1:5000/drinks
```

**Getting a Specific Drink:**
```sh
curl http://127.0.0.1:5000/drinks/1
```

**Deleting a Drink:**
```sh
curl -X DELETE http://127.0.0.1:5000/drinks/1
```

