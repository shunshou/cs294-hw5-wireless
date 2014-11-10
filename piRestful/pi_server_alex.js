// Turn servo left/right depending on POST value received
var pythonshell = require('python-shell');

function doorLock(value) {
	console.log("open_door is " + value);
	// Servo left; else right
	if (value == '1') {
		pythonshell.run('pwmOn.py', function(err) {
			if (err) throw err;
		});
	} else {
		pythonshell.run('pwmOff.py', function(err) {
			if (err) throw err;
		});	
	}
};

// Setuo server
var express = require('express');
var app = express();
var bodyParser = require('body-parser');

// indicates which files/directories are world viewable (/ for index; /public for scripts, stylesheets, etc.)
app.use(express.static(__dirname + '/public'));

// JSON interpreter
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

// Allow Herokuapp to access (POST, etc.) via AJAX -- CRITICAL!!!
app.use(function(req, res, next){
	res.setHeader('Access-Control-Allow-Origin', 'http://morning-basin-3078.herokuapp.com');
	res.setHeader('Access-Control-Allow-Methods', 'GET, POST, OPTIONS, PUT, PATCH, DELETE'); 
	res.setHeader('Access-Control-Allow-Headers', 'X-Requested-With, content-type');
	res.setHeader('Access-Control-Allow-Credentials', true);
	next();
});

// Set access port
var port = process.env.PORT || 5000;

/* 
var router = express.Router();

router.use(function(req, res, next) {
	console.log('Middleware');
	next();
});

router.get('/', function(req, res) {
	res.json({ message: 'it works'});
});
*/

// Process POST (open_door)
app.post('/', function(req, res) {
	console.log('Post received!');
	var postVal = req.body.open_door; 
	console.log(postVal);
	doorLock(postVal);
	res.json({ message: 'Value received'});
});

/*
router.route('/util') 
	.post(function(req, res) {
		var postVal = req.body.open_door; //;req.body.value;
		console.log(postVal);
		doorLock(postVal);
	res.json({ message: 'value recieved'});
	})
	.get(function(req, res) {
		var getVal = "placeholder";
		res.json({ value: getVal });
	});
*/

// app.use('/api', router);

app.listen(port);
console.log('Port ' + port);

