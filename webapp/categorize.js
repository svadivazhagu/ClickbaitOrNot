var bayes = require('bayes')
var fs = require('fs')
var classifier = JSON.parse(fs.readFileSync('./state.json').toString());
var revivedClassifier = bayes.fromJson(classifier)
var videos = JSON.parse(fs.readFileSync('./scraped_data.json').toString)

function categorize(classifier, videos ) {
    /*
        @param classifier json state
        @returns a list of titles and their thumbnails

        var results = []
        for i in titles:
            let category = classifier.categorize(titles[i]);
            let video = {"title" : titles[i][title], "category" : category}
            results.push(video)
        return results
    */
    
    var results = []
    for (let i = 0; i<videos.length;i++) {
        let reaction = classifier.categorize(videos[i]["title"]);
        let video = {"title" : titles[i][title], "reaction" : category};
        results.push(video)
    }
    return results;
}