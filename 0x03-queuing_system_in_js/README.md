# Queuing System in JS - Redis Client Setup

This project demonstrates how to set up a Redis client using Node.js with Babel and ES6 syntax. It connects to a Redis server, logs connection success or failure, and handles basic Redis interactions.

## Task Overview

### Task 1: Node Redis Client

In this task, you will install Redis and a Node.js Redis client (`node_redis`), then create a simple script that connects to the Redis server. If the connection is successful, the script will log a success message; otherwise, it will log an error message.

### Requirements

- You must have a running Redis server.
- You will need to set up a Node.js environment with `babel-node` and the required dependencies.
- The client will log messages based on whether the Redis connection was successful or failed.

## Setup Instructions

Follow these steps to set up the project:

### 1. Clone the Repository

If you haven't already, clone the repository to your local machine:

```bash
git clone https://github.com/kweenDev/alx-backend.git
cd alx-backend/0x03-queuing_system_in_js
```

### 2. Install Redis

### 3. Intall Node.js and NPM

Ensure that you have `Node.js` and `npm` installed. You can install them from the [official Node.js website](https://nodejs.org)

### 4. Initialize Project and Install Dependencies

1; In your project directory, initialize a new Node.js project:

```bash
npm init -y
```

2; Install the required packages:

```bash
npm install redis
npm install --save-dev @babel/core @babel/cli @babel/preset-env nodemon @babel/node
```

3; Create a `.babelrc` file in your project directoy with the following content:

```json
{
    "presets": ["@babel/preset-env"]
}
```

### 5. Create the Redis Client Script

Create a new file named `0-redis_client.js` in the project directory with the following content:

```javascript
import redis from "redis";

// Create a Redis client
const client = redis.createClient();

// Event listeners for the Redis client
client.on("connect", () => {
    console.log("Redis client connected to the server");
});

client.on("error", (err) => {
    console.error(`Redis client not connected to the server: ${err.message}`);
});
```

### 6. Update `package.json`

Modify the `scripts` section of your `package.json` to include the following:

```json
{
    "scripts": {
        "dev": "nodemon --exec babel-node --presets @babel/preset-env"
    }
}
```

### 7. Run the Redis Client Script

Ensure that Redis is running, then execute the script:

```bash
npm run dev 0-redis_client.js
```

You should see the following output if the connection is successful:

```arduino
Redis client connected to the server
```

If there is a connection issue, you will see an error message like this:

```vbnet
Redis client not connected to the server: Error: Redis connection to 127.0.0.1:6379 failed - connect ECONNREFUSED 127.0.0.1:6379
```

## Troubleshooting

- **Redis Server Not Running:** Ensure Redis is installed and running on your machine. You can verify this by running `ps aux | grep redis-server` or checking the Task Manager on Windows.
- **Babel Issues:** If Babel is not correctly transpiling yyour code, ensure that the `@babel/preset-env` preset is installed, and the `.babelrc` file is correctly configured.

## Author

Refiloe Radebe
