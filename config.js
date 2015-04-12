"use strict";

var fs = require('fs');
if (fs.existsSync('./config.json')) {
    var configData = require('./config.json');
    module.exports = configData;
} else {
    var configTemplate = require('./config.template.json');
    for (var category in configTemplate) { //iterate through each config category
        if (!configTemplate.hasOwnProperty(category) || configTemplate[category] == "_comment") continue;
        for (var key in configTemplate[category]) { //retrieve items in each category
            if (!configTemplate[category].hasOwnProperty(key) || configTemplate[category][key] == "_comment") continue;
            if (!process.env.hasOwnProperty(key)) throw new Error('Missing environment variable ' + key);
            configTemplate[category][key] = process.env[key];
        }
    }
    module.exports = configTemplate;
}