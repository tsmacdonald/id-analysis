import config

with open(config.conll_file) as conll, open(config.output_file, 'w') as out:
  for line in conll:
    fields = line.split()
    if len(fields) >= 2:
      out.write(fields[1] + '\n')
