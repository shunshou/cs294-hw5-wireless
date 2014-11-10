sudo wget http://node-arm.herokuapp.com/node_latest_armhf.deb
sudo dpkg -i node_latest_armhf.deb
sudo npm install -g express --save
sudo npm install rpi-gpio

Check IP address http://checkip.dyndns.org/ (This is where the server resides if you don't disconnect the Pi -- can SSH, etc.)
128.32.63.163

rtsp://128.32.63.163:8554/

raspivid -o - -t 0 -hf -w 800 -h 400 -fps 24 |cvlc -vvv stream:///dev/stdin --sout '#standard{access=http,mux=ts,dst=:8160}' :demux=h264
-----

11/8/14 - Homework

pi going out all handled by python
pi coming in all handled by nodejs

pi send Gchat or Twitter + send put request to database
pi uploads rtmp to youtube livestream (or local?) 
you stare at youtube, see person; can change lock/unlock option --> push back to pi

Pi NodeJS setup
Button press GPIO NodeJS
Send Tweet?
Stream vid
Push to webserver

Webserver displays stream
Shows status using jQuery
Jquery --> JSON 
open/close button (detect change)

Pi receive request --> change motor

https://www.npmjs.org/package/python-shell
http://nodejs.org/api/child_process.html
http://www.dzone.com/snippets/execute-unix-command-nodejs
https://www.youtube.com/watch?v=k_4OYTXSmwo
https://www.npmjs.org/~sarfata
http://www.midnightcheese.com/2014/02/raspberry-pi-plus-node-dot-js-plus-socket-dot-io-plus-twitter-streaming-api-equals-internet-bliss/
https://www.npmjs.org/package/rpi-gpio

http://expressjs.com/api.html#response

http://stackoverflow.com/questions/5710358/how-to-get-post-query-in-express-node-js


post/get are client methods


curl -H "Content-Type: application/json" -d '{"name":"xyz","color":"red"}' http://localhost:5000/

// assuming POST: name=foo&color=red            <-- URL encoding
//
// or       POST: {"name":"foo","color":"red"}  <-- JSON encoding


moment.js


<html lang="ja" xmlns:ng="http://angularjs.org" id="ng-app" ng-app="simplechat">
<head>
<link rel="stylesheet" href="//netdna.bootstrapcdn.com/bootswatch/3.1.1/united/bootstrap.min.css">
</head>
<body style="background-color:#999">
<div class="container" ng-controller="ChatCtrl">

<div class="row">
<h1>simple chat</h1>

<div class="col-sm-12" style="padding:0px">
  <div class="input-group">
    <input type="text" class="form-control" ng-model="input_body" placeholder="message...">
    <span class="input-group-btn">
      <span ng-click="post()" type="button" class="btn btn-primary">post</span>
    </span>
  </div><!-- /input-group -->
</div><!-- /.col-lg-6 -->

<div id="feed" class="col-sm-12 well" style="background-color:#fff; height: 400px;
overflow: scroll;">
  <div ng-repeat="post in posts | orderBy:'-id' ">{{post.body}}</div>
</div>

</div>

<script src="//code.jquery.com/jquery-2.0.3.min.js"></script>
<script src="//netdna.bootstrapcdn.com/bootstrap/3.1.1/js/bootstrap.min.js"></script>
<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.2.3/angular.min.js"></script>
<script src="//ajax.googleapis.com/ajax/libs/angularjs/1.2.3/angular-resource.js"></script>
<script>
  var host = location.origin.replace(/^http/, 'ws')
  var ws = new WebSocket(host);

  angular.module('simplechat', ["ngResource"])

  .controller('ChatCtrl', function($scope, $resource, $http){
    $resource("/get_post").query(function(ret){
      $scope.posts = ret;
      console.log($scope.posts);
    });

    $scope.post = function(){
      ws.send(JSON.stringify({
        type: 'add',
        body: $scope.input_body
      }));
      $scope.input_body = '';
    }

    ws.onmessage = function (event) {
      console.log('test');
      var post = JSON.parse(event.data);
      $scope.posts.unshift(post);
      $scope.$apply();
    };

  });




  wss.on("connection", function(ws) {
  var id = setInterval(function() {
    ws.send(JSON.stringify(new Date()), function() {  })
  }, 1000)

  console.log("websocket connection open")

  ws.on("close", function() {
    console.log("websocket connection close")
    clearInterval(id)
  })
})




http://www.makeuseof.com/tag/how-to-build-a-raspberry-pi-twitter-bot/





</script>
</body>
</html>





<!-- TWITTER PHOTO --> 
<!-- raspistill -w 600 -h 400 -o visitor.jpg -->