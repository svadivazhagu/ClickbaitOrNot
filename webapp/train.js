var bayes = require('../chrome_ext/node_modules/bayes')
var fs = require('fs')


var classifier =  bayes()

/* create a function where (labeled data):
    -> @param json file, each elt is [title, reaction] -> [str, str]
    ->@return classifier's JSON filepath after serialization
*/

function trainClassifier(data_fp){
    var data = JSON.parse(fs.readFileSync('../formattedInput.json').toString());
    for (var i = 0; i< data.length; i++){
        classifier.learn(data[i].title, data[i].reaction)
    }

    var stateJson = classifier.toJson()
    fs.writeFile("state.json", stateJson, function(err) {
        if(err){
            console.log(err);
        }
    });
}

trainClassifier()