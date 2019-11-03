

function tokenize(item) {

  var new_str = '';
  var counts = {}

  for (let i = 0; i < item.length; i++) {
    if ((item[i] === ' ') || (item[i] >= "A" && item[i] <= "Z") || (item[i] >= 'a' && item <= 'z')) {
      new_str += item[i]
    } else if (item[i] >= "0" && item[i] <= "9") {
      new_str += item[i]

    } else {
      if (counts[item[i]]) {
        counts[item[i]] += 1
      } else {
       counts[item[i]] = 1
      }
    }
  }

  for (let key in counts) {
    console.log(key, counts[key])
    new_str += ' ';
    for (let i = 0; i < counts[key]; i++) {
      new_str +=  key
    }
  }

  new_str = new_str.split(' ').filter(x => x !== '').join(' ')

  return new_str;
}

var test = "How does your body know you're full? - Hilary Coller"
console.log(format(test))