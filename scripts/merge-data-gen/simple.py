import os, random

def getInstanceFile(dirname):
  files = os.listdir(dirname)
  c = 1 + len(filter(lambda a: (a.find('instance.sim.1000000') >= 0), files))
  return os.path.join(dirname, 'instance.sim.1000000.' + str(c))


depth = 10
countAtLevels = []
for i in range(depth):
  countAtLevels.append(random.randint(2, 8))

instancefile = getInstanceFile('/home/arjun/data/cuenet/nodemerge')
# instancefile = '/home/arjun/data/cuenet/nodemerge/prime.sim.1000000'
maxnode = 1000000

writer = open(instancefile, 'w')
writer.write('/data/osm/uci.roadnet 1 10000 ')
for item in countAtLevels: writer.write(' %d ' % item )
writer.write('\n## 171169284\n')
writer.write('$$ 1822416005\n')
writer.write('0_0,0,10000000,R\n')

#countAtLevels = [8, 2, 8, 2, 6, 2, 5, 3, 5, 4]

print countAtLevels, reduce(lambda a, b: a*b, countAtLevels), instancefile

prod = 1
for k in xrange(len(countAtLevels)):
  count = countAtLevels[k]
  prod = prod * count
  for i in xrange(prod):
    #print str(k) + '_' + str(i%(prod/countAtLevels[k])), '->', str(k+1) + '_' + str(i)
    writer.write(str(k) + '_' + str(i%(prod/countAtLevels[k])) + ' -> ' + str(k+1) + '_' + str(i))
    writer.write('\n')
    maxnode -= 1
    if maxnode == 0: break
  if maxnode == 0: break

writer.write('.\n')
writer.close()
