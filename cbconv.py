

with open('clickbait.txt', 'r') as cb:
  
  reading = cb.read()[1:-1].split(',')
  rem_qus = list(map(lambda x: x[1:].replace('"', ''), reading))
  filtered = list(filter(lambda x: x != '', rem_qus))


  data = filtered
  print(filtered)
  with open('testoutput.csv', 'a') as out:
    for d in data:
      out.write('1,' + d + ',cb\n')