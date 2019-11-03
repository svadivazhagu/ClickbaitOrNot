var express = require('express')
var app = express()

app.get('/', function (req, res) {
    res.send('Hello World')
})

app.get('/load', function (req, res) {
    
}) 