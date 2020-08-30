var express = require("express")
var app = express()
var port = 3000

var data = {
    tri: {
        acier: 0,
        alu: 0,
        pet: 0,
        verre: 0,
        tetra: 0
    },
    name: "manu",
    id: "manuidqr"
}

// GET method route
app.get('/connection', function (req, res) {
    res.send(data)
  })
  
// POST method route
app.post('/connection', function (req, res) {
    res.send('POST request to the homepage')
  })

app.listen(port, () => {
    console.log(`started at http://localhost:${port}`)
  })