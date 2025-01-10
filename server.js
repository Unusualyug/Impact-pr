const express = require("express");
const mongoose = require("mongoose");
const bodyParser = require("body-parser");
const cors = require("cors");

// Initialize express app
const app = express();

// Middleware
app.use(cors());
app.use(bodyParser.json());

// MongoDB connection
mongoose
  .connect("mongodb://localhost:27017/phonebook", {
    useNewUrlParser: true,
    useUnifiedTopology: true,
  })
  .then(() => console.log("MongoDB connected"))
  .catch((err) => console.log(err));

// Contact Schema
const contactSchema = new mongoose.Schema({
  name: { type: String, required: true },
  phone: { type: String, required: true },
});

const Contact = mongoose.model("Contact", contactSchema);

// Get all contacts
app.get("/api/contacts", async (req, res) => {
  try {
    const contacts = await Contact.find();
    res.json(contacts);
  } catch (err) {
    res.status(500).json({ message: "Server Error" });
  }
});

// Add a new contact
app.post("/api/contacts", async (req, res) => {
  const { name, phone } = req.body;
  const newContact = new Contact({ name, phone });

  try {
    await newContact.save();
    res.json(newContact);
  } catch (err) {
    res.status(400).json({ message: "Unable to save contact" });
  }
});

// Delete a contact
app.delete("/api/contacts/:id", async (req, res) => {
  try {
    const contact = await Contact.findByIdAndDelete(req.params.id);
    if (!contact) {
      return res.status(404).json({ message: "Contact not found" });
    }
    res.json({ message: "Contact deleted" });
  } catch (err) {
    res.status(500).json({ message: "Server Error" });
  }
});

// Edit a contact
app.put("/api/contacts/:id", async (req, res) => {
  const { name, phone } = req.body;
  try {
    const contact = await Contact.findByIdAndUpdate(
      req.params.id,
      { name, phone },
      { new: true }
    );
    if (!contact) {
      return res.status(404).json({ message: "Contact not found" });
    }
    res.json(contact);
  } catch (err) {
    res.status(500).json({ message: "Server Error" });
  }
});

// Search contacts by name
app.get("/api/search", async (req, res) => {
  const { name } = req.query;
  try {
    const contacts = await Contact.find({ name: new RegExp(name, "i") });
    res.json(contacts);
  } catch (err) {
    res.status(500).json({ message: "Server Error" });
  }
});

// Sort contacts by name
app.get("/api/sort", async (req, res) => {
  try {
    const contacts = await Contact.find().sort({ name: 1 });
    res.json(contacts);
  } catch (err) {
    res.status(500).json({ message: "Server Error" });
  }
});

// Start the server
const PORT = process.env.PORT || 5000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
