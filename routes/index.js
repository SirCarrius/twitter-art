var express = require('express');
var router = express.Router();
var Twitter = require('node-twitter');
var config = require('../config');
var sentiment = require('sentiment');

var twitterSearchClient = new Twitter.SearchClient(
  config.setup.twitter_key,
  config.setup.twitter_secret,
  config.setup.twitter_token,
  config.setup.twitter_token_secret
);

router.get('/', function(req, res) {
  twitterSearchClient.search({
    'q': '',
    'geocode': '40.342815,74.657893,100km',
    'result_type': 'recent',
    'count': 100,
    'lang': 'en'
  }, function(error, result) {
    if (error) {
      res.end();
      console.log('Error: ' + (error.code ? error.code + ' ' + error.message : error.message));
    }
    if (result) {
      res.send(result);
      console.log(result);
    }
  });
});

module.exports = router;
