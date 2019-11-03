function defaultTokenizer(item) {

    var new_str = '';
    var counts = {}
  
    var lowerCount = 0;
    var upperCount = 0
    for (let i = 0; i < item.length; i++) {
        if ((item[i] === ' ')) {
            new_str += item[i]
        } else if ((item[i] >= "A" && item[i] <= "Z")) {
            new_str += item[i];
            upperCount += 1;
        } else if ((item[i] >= 'a' && item <= 'z')) {
            new_str += item[i];
            lowerCount += 1;
        } else if (item[i] >= "0" && item[i] <= "9") {
            new_str += item[i]
        } else if (item[i] !== '"' && item[i] !== "'") {
            if (counts[item[i]]) {
                counts[item[i]] += 1
            } else {
                counts[item[i]] = 1
            }
        }
    }
  
    for (let key in counts) {
        new_str += ' ';
        for (let i = 0; i < counts[key]; i++) {
            new_str += key
        }
    }
    new_str += ' ' + 'z90312e' + ((upperCount / (lowerCount + upperCount)) > 0.5 )
    new_str = new_str.split(' ').filter(x => x !== '')
  
    return new_str;
  }


  var data = ["Grinded So Hard I Became A God in Super Life RPG",
  "Do Not Drop Food Cans in Hot Burning Oil!",
  "My Mom Entered Without Knocking And Saw Me And My Stepdad",
  "Olympic Cyclist vs $28 Aldi Bike Trainer",
  "WORLD'S TALLEST SWING! *Over 280 feet*",
  "You Know It's GNARLY When There's a WARNING!"]


  console.log(defaultTokenizer(data[4]).join(' '))