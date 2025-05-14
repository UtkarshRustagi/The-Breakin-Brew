// require("dotenv").config();
// const express = require("express");
// const mongoose = require("mongoose");
// const cors = require("cors");
// const bodyParser = require("body-parser");

// const app = express();
// const PORT = process.env.PORT || 5000;

// // Middleware
// app.use(cors());
// app.use(bodyParser.json());

// // MongoDB Connection
// mongoose
//   .connect(process.env.MONGO_URI, { useNewUrlParser: true, useUnifiedTopology: true })
//   .then(() => console.log("Connected to MongoDB"))
//   .catch((err) => console.error("Error connecting to MongoDB:", err));

// // User Schema
// const UserSchema = new mongoose.Schema({
//   username: String,
//   password: String, // Note: Use bcrypt to hash passwords in a real application
// });

// const User = mongoose.model("User", UserSchema);

// // Login Route
// app.post("/login", async (req, res) => {
//   const { username, password } = req.body;
//   const user = await User.findOne({ username, password });

//   if (user) {
//     res.json({ message: "Login successful" });
//   } else {
//     res.status(401).json({ message: "Invalid credentials" });
//   }
// });

// // Start Server
// app.listen(PORT, () => {
//   console.log(`Server running on port ${PORT}`);
// });




const { MongoClient, ServerApiVersion } = require("mongodb");

// Replace the placeholder with your Atlas connection string or localhost
const uri = "mongodb://localhost:27017";

// Name of your specific database
const dbName = "CoffeeHouse";  // <-- Replace 'yourDatabaseName' with your actual database name

// Create a MongoClient
const client = new MongoClient(uri, {
  serverApi: {
    version: ServerApiVersion.v1,
    strict: true,
    deprecationErrors: true,
  },
});

async function run() {
  try {
    // Connect the client to the server
    await client.connect();

    // Connect to the specific database
    const database = client.db(dbName);

    // Optional: list collections to verify database connection
    const collections = await database.listCollections().toArray();
    console.log(`Connected to database: ${dbName}`);
    console.log("Collections in this database:", collections.map(col => col.name));
    
    // Additional ping to be extra sure
    await database.command({ ping: 1 });
    console.log("Pinged the database. Successfully connected!");
    
  } finally {
    // Ensure that the client will close when you finish/error
    await client.close();
  }
}

run().catch(console.dir);
