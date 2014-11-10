//set up server
var pythonshell = require('python-shell');

function doorLock(value) {
	console.log("value is " + value);
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

var express = require('express');
var app = express();
var bodyParser = require('body-parser');

// indicates which files/directories are world viewable (/ for index; /public for scripts, stylesheets, etc.)
app.use(express.static(__dirname + '/public'));

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());

var port = process.env.PORT || 8080;

var router = express.Router();

router.use(function(req, res, next) {
	console.log('Middleware');
	next();
});

router.get('/', function(req, res) {
	res.json({ message: 'it works'});
});

app.post('/', function(req, res) {
	/*res.json({ message: 'it works'});
	console.log('Middleware');
});
*/

console.log('test');


//router.route('/util') 
	//.post(function(req, res) {
		var postVal = req.body.value;
		console.log(postVal);
		doorLock(postVal);
	res.json({ message: 'value recieved'});
	//})
	
	/*.get(function(req, res) {
		var getVal = "placeholder";
		res.json({ value: getVal });*/

		
	});



app.use('/api', router);

app.listen(port);
console.log('Port ' + port);
