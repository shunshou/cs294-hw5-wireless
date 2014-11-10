// Setup server
var WebSocketServer = require('ws').Server
  , http = require('http')
  , express = require('express')
  , app = express()
  , port = process.env.PORT || 5000;

// If you want postgresql database
//  pg = require('pg')

// nodejs timestamp
var moment = require('moment');

// indicates which files/directories are world viewable (/ for index; /public for scripts, stylesheets, etc.)
app.use(express.static(__dirname + '/'));
app.use(express.static(__dirname + '/public'));

// Original middleware for parsing data (in tutorial script)
app.use(express.bodyParser());
app.use(express.methodOverride());

// Middleware to parse post data (JSON)
app.use(express.json());       // to support JSON-encoded bodies
app.use(express.urlencoded()); // to support URL-encoded bodies

// Create server
var server = http.createServer(app);
server.listen(port);

// Console feedback
console.log('http server listening on %d', port);

var wss = new WebSocketServer({server: server});

/* Part of tutorial script for accessing database

wss.on('connection', function(ws) {
  ws.on('message', function(data){
    var data = JSON.parse(data);
    switch (data.type) {
      case 'add':
        pg.connect(process.env.DATABASE_URL, function(err, client, done) {
          client.query('INSERT INTO "post" (body) values(%s)'.replace('%s', "'"+data.body+"'"), function(err, result) {
            done();
            if(err) return console.error(err);
          });
        });
        wss.clients.forEach(function(client) {
          client.send(JSON.stringify(data));
        });
        break;
      default:
        break;
    }
  });
});

app.get('/get_post', function(req, res) {
  pg.connect(process.env.DATABASE_URL, function(err, client, done) {
    client.query('SELECT * FROM post', function(err, result) {
      done();
      if(err) return console.error(err);
      res.send(result.rows);
    });
  });
});
*/

// Example POST checking
// assuming POST: name=foo&color=red            <-- URL encoding
// or       POST: {"name":"foo","color":"red"}  <-- JSON encoding
// curl -H "Content-Type: application/json" -d '{"name":"xyz","color":"red"}' http://localhost:5000/

// Posted to index
app.post('/', function(req, res) {
    
    /* Post Test Code

    var name = req.body.name,
        color = req.body.color;
    console.log(JSON.stringify(req.body));
    console.log('name: %s, color %s', name, color);

    */ 

    // curl -H "Content-Type: application/json" -d '{"bell_rang":"true"}' http://localhost:5000/

    var bell_rang = req.body.bell_rang;
    // make sure bell actually rang (not random msg)
    if (bell_rang == "1"){
      // Send timestamp of post in clean format for viewing
      wss.clients.forEach(function(client) {
        //client.send(color);
        client.send(moment().subtract(8, 'hours').format('MMMM Do YYYY, h:mm:ss a'));
      });
      res.send('Bell rang :) ! \r\n'); 
    }
    else{
      res.send(':( \r\n');
    }

    // For sending back to POST-er
    //res.send(moment().format('MMMM Do YYYY, h:mm:ss a')+'\r\n');
    //res.send(req.body); 

});

// Look into res.sendfile