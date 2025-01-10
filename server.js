const express = require("express");
const mongoose = require("mongoose");
const path = require("path");
const bodyParser = require("body-parser");
const cors = require("cors");

const app = express();

// Serve static files like CSS, JS, images
app.use(express.static(path.join(__dirname, "public")));

app.set("view engine", "ejs");
app.set("views", path.join(__dirname, "views"));
app.use(cors());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true })); // Needed to parse form data

// Connect to MongoDB
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

// Home Route (All contacts)
app.get("/contact", async (req, res) => {
  try {
    const contacts = await Contact.find();
    res.render("contact", { contacts });
  } catch (err) {
    res.status(500).json({ message: "Server Error" });
  }
});

// Add Route (Add a new contact)
app.get("/add", (req, res) => {
  res.render("add");
});

// Add a new contact (POST request)
app.post("/api/contacts", async (req, res) => {
  const { name, phone } = req.body; // Extracting data from the form
  const newContact = new Contact({ name, phone });

  try {
    await newContact.save();
    res.redirect("/contact"); // Correct redirection to /contact after successful contact addition
  } catch (err) {
    console.error(err); // Log any errors that might happen
    res.status(400).json({ message: "Unable to save contact" });
  }
});

// Edit Route (Edit an existing contact)
app.get("/edit/:id", async (req, res) => {
  try {
    const contact = await Contact.findById(req.params.id);
    res.render("edit", { contact });
  } catch (err) {
    res.status(500).json({ message: "Contact not found" });
  }
});

// Edit a contact (PUT request)
app.post("/api/contacts/:id", async (req, res) => {
  const { name, phone } = req.body;
  try {
    await Contact.findByIdAndUpdate(req.params.id, { name, phone });
    res.redirect("/contact"); // Correct redirection to /contact after editing
  } catch (err) {
    res.status(500).json({ message: "Server Error" });
  }
});

// Delete a contact (DELETE request)
app.post("/api/contacts/:id/delete", async (req, res) => {
  try {
    await Contact.findByIdAndDelete(req.params.id);
    res.redirect("/contact"); // Correct redirection to /contact after deletion
  } catch (err) {
    res.status(500).json({ message: "Server Error" });
  }
});

// Search Route (Search contacts by name)
app.get("/search", async (req, res) => {
  const { name } = req.query;
  try {
    const contacts = await Contact.find({ name: new RegExp(name, "i") });
    res.render("search", { contacts });
  } catch (err) {
    res.status(500).json({ message: "Server Error" });
  }
});

// Sort Route (Sort contacts by name)
app.get("/sort", async (req, res) => {
  try {
    const contacts = await Contact.find().sort({ name: 1 });
    res.render("sort", { contacts });
  } catch (err) {
    res.status(500).json({ message: "Server Error" });
  }
});

// Start the server
const PORT = 3000;
app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
