var express = require('express');

var app = express();

app.set('view engine', 'ejs');
app.use('/assets', express.static('public'));

app.get('/', function(req,res) {
    res.sendFile(__dirname + '/index.html');
});

app.get('/contact', function(req,res) {
    res.send('contact');
});

app.get('/profile/:id', function(req,res) {
    res.render('profile', {person: req.params.id});
});


app.listen(3000);

