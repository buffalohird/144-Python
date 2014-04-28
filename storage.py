import time
import csv




class Storage:
  def __init__(self):
    self.hello = []

  # given a file name of a csv will read it and return that data when Storage.readRun() is called
  def readRun(self, inputFile):
    try:
      with open(inputFile, "rU") as csvFile:
        returnPoints = []
        csvReader = csv.reader(csvFile)

        if csvReader == []:
          print "empty reader"
          time.sleep(100)
        for row in csvReader:
          returnPoints.append(row)

        return returnPoints
    except IOError:
      print "IOERROR is raised. Error opening file %s with logger.py" % (str(inputFile)) 


  # given a list of lists to save and a file name will save csv of lists to name
  def saveRun(self, outputData, outputFile):
    with open(outputFile, 'w+') as writeFile:
      csvWriter = csv.writer(writeFile)
      for row in self.data:
        csvWriter.writerow(row)


storage = Storage()
print storage.readRun('test1.csv')



