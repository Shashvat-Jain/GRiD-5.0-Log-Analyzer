require("dotenv").config();
const express = require("express");
const cors = require("cors");
const app = express();
const User = require("./Data/user.json");

app.get("/", (req, res) => {
  res.send(User);
});

app.get("/:id", (req, res) => {
  res.send(User[req.params.id]);
});

app.get("/:id/role", (req, res) => {
  res.send(User[req.params.id].role);
});

app.get("/:id/position", (req, res) => {
  res.send(User[req.params.id].position);
});

app.get("/services", (req, res) => {
  var services = [];
  for (var i = 0; i < User.length; i++) {
    console.log(User[i].service);
    services.push(User[i].service);
  }
  services = new Set(services);
  res.send(Array.from(services));
});

app.get("/positions", (req, res) => {
  var positions = [];
  for (var i = 0; i < User.length; i++) {
    positions.push(User[i].position);
  }
  positions = new Set(positions);
  res.send(Array.from(positions));
});

app.get("/roles", (req, res) => {
  var roles = [];
  for (var i = 0; i < User.length; i++) {
    roles.push(User[i].role);
  }
  roles;
  roles = new Set(roles);
  res.send(Array.from(roles));
});

app.get("/:id/platform", (req, res) => {
  res.send(User[req.params.id].platform);
});

app.listen(process.env.PORT, () => {
  console.log(`Server is running on port ${process.env.PORT}`);
});
