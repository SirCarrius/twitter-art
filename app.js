var express = require('express');
var path = require('path');
var logger = require('morgan');
var async = require('async');
var brain = require('brain');
var config = require('./config');
var routes = require('./routes')
GLOBAL.io = require('socket.io')(server);

var app = express();
var server = require('http').createServer(app);
app.set('port', process.env.PORT || 3000);

app.use('/', routes);

var net = new brain.NeuralNetwork();

net.train([{input: { r: 0.03, g: 0.7, b: 0.5 }, output: { black: 1 }},
           {input: { r: 0.16, g: 0.09, b: 0.2 }, output: { white: 1 }},
           {input: { r: 0.5, g: 0.5, b: 1.0 }, output: { white: 1 }}],
           {
            log: true
           });

var output = net.run({ r: 1, g: 0.4, b: 0 });
console.log(output);

server = app.listen(app.get('port'), function () {
  console.log('Express server listening on port ' + server.address().port);
});

app.use(logger('dev'));
app.use(require('less-middleware')(path.join(__dirname, 'public')));
app.use(express.static(path.join(__dirname, 'public')));