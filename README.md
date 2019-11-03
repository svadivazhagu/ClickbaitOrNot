# Clickbait or Not
### WHACK 2019 Submission
### Surya Vadivazhagu (svadivazhagu), Alex Wurts (ajwurts) Kellan Cupid (sirkupid)
---
Clickbait or Not is a Chrome extension that applies the Naive Bayesian Classifier to the current problem of 'clickbait' videos on YouTube. More information about clickbait can be found [here](https://en.wikipedia.org/wiki/Clickbait).

We leveraged the open-source [Bayes](https://github.com/ttezel/bayes) library for JavaScript to implement this project as  Chrome extension available as soon as the extension exits the 'Pending Review' process on Chrome Web Store.

## Here is the general workflow of the extension:

- User's YouTube page is loaded
- Scraper function runs and collects metadata about videos in current view.
- Data is processed and text analysis/modification is performed allowing punctuation and capitalization to be included at the end of the string.
- Processed video title is sent into the Naive Bayes classifier to have an output determined.
- Output boolean (clickbait/non-clickbait) is sent back up to front-end and HTML element corresponding to the video's title is modified as per the classifier's decision (red = clickbait, green = not).
- When more YouTube videos are loaded (i.e. scrolling down on feed, searching) this workflow is run again. 


We  leveraged Naive Bayes far beyond its traditional application by considering punctuation and capitalization of words included in a video's title in our text processing. This helps influence the classifier's decision even more so and makes it a universal decision that crosses languages. We find our extension works on videos in other languages, just because the classifier has been trained so well to identify patterns in clickbait videos.


## Training the Naive Bayes Classifier

Example labeled video title (before text processing) : [HOW TO FIND GOLD EVERY TIME IN ANY CREEK!!!!! 
](https://www.youtube.com/watch?v=U70lhTElr_I)

After text processing : HOW TO FIND GOLD EVERY TIME IN ANY CREEK !!!!!

We took Naive Bayes to new heights with this program by separating the punctuation from the actual title itself - this way, our classifier learns that 5 exclamation marks is indicative of a clickbait video, whereas without any text processing the phrase 'CREEK!!!!!' would be considered clickbait and other videos of a similar nature who include many exclamation marks (a common feature in clickbait videos) would not be considered clickbait.


## Statistics and Distribution of Categorized Results

We found that the most common click-baited word was '!' with 29 occurrences - supporting the research conducted at the [2017 Web and Big Data Int'l Joint Conference](https://books.google.com/books?id=o1ovDwAAQBAJ&lpg=PA75&ots=LHPHM8g6Iw&dq=clickbait%20lots%20of%20exclamation%20mark&pg=PA75#v=onepage&q&f=false)
Next, we had the number '10' as the second most occurring phrase in clickbait titles - this is explained by many 'Top 10' videos that have many clickbait traits.




