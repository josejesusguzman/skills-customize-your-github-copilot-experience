# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn to build modern, production-ready REST APIs using the FastAPI framework by implementing routes, request/response models, error handling, and data validation for a task management application.

## 📝 Tasks

### 🛠️ Create API Routes and Models

#### Description
Set up a FastAPI application with basic routes and define Pydantic models for structured data handling to create a foundation for a task management API.

#### Requirements
Completed program should:

- Initialize a FastAPI application instance.
- Define a `Task` Pydantic model with fields: `id`, `title`, `description`, and `completed` (boolean).
- Create GET and POST routes to retrieve and create tasks.
- Use an in-memory list to store tasks (no database required for this task).
- Return tasks in JSON format with appropriate HTTP status codes.

### 🛠️ Implement CRUD Operations

#### Description
Expand the API to support full Create, Read, Update, and Delete operations for tasks with proper error handling for missing resources.

#### Requirements
Completed program should:

- Implement GET route to retrieve a single task by ID.
- Implement PUT route to update an existing task.
- Implement DELETE route to remove a task.
- Return 404 error when a task ID is not found.
- Generate unique task IDs automatically for new tasks.

### 🛠️ Add Data Validation and Error Handling

#### Description
Enhance the API with comprehensive input validation and informative error responses to ensure data integrity and improve user experience.

#### Requirements
Completed program should:

- Validate that required fields (title) are provided in requests.
- Return 400 error with descriptive messages for invalid input.
- Validate that task data conforms to the Pydantic model.
- Provide meaningful error messages in responses (e.g., `{"detail": "Task not found"}`).
- Test all routes using FastAPI's built-in interactive documentation at `/docs`.
