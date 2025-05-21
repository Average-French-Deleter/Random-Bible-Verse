import random

verseNumber = random.randint(1,1532)

quote = (
  ((1,31), "Genesis 1", (verseNumber)),
  ((32,56), "Genesis 2", (verseNumber-31)),
  ((57,80), "Genesis 3", (verseNumber-56)),
  ((81,106), "Genesis 4", (verseNumber-80)),
  ((107,138), "Genesis 5", (verseNumber-106)),
  ((139,160), "Genesis 6", (verseNumber-138)),
  ((161,184), "Genesis 7", (verseNumber-160)),
  ((185,206), "Genesis 8", (verseNumber-184)),
  ((207,235), "Genesis 9", (verseNumber-206)),
  ((236,267), "Genesis 10", (verseNumber-235)),
  ((268,299), "Genesis 11", (verseNumber-267)),
  ((300,319), "Genesis 12", (verseNumber-299)),
  ((320,337), "Genesis 13", (verseNumber-319)),
  ((338,361), "Genesis 14", (verseNumber-337)),
  ((362,382), "Genesis 15", (verseNumber-361)),
  ((383,398), "Genesis 16", (verseNumber-382)),
  ((399,425), "Genesis 17", (verseNumber-398)),
  ((436,458), "Genesis 18", (verseNumber-425)),
  ((459,496), "Genesis 19", (verseNumber-458)),
  ((497,514), "Genesis 20", (verseNumber-496)),
  ((515,548), "Genesis 21", (verseNumber-514)),
  ((549,572), "Genesis 22", (verseNumber-548)),
  ((573,592), "Genesis 23", (verseNumber-572)),
  ((593,659), "Genesis 24", (verseNumber-592)),
  ((660,693), "Genesis 25", (verseNumber-659)),
  ((694,728), "Genesis 26", (verseNumber-693)),
  ((729,774), "Genesis 27", (verseNumber-728)),
  ((775,796), "Genesis 28", (verseNumber-774)),
  ((797,831), "Genesis 29", (verseNumber-796)),
  ((833,874), "Genesis 30", (verseNumber-831)),
  ((877,929), "Genesis 31", (verseNumber-874)),
  ((933,961), "Genesis 32", (verseNumber-929)),
  ((966,981), "Genesis 33", (verseNumber-961)),
  ((986,1012), "Genesis 34", (verseNumber-981)),
  ((1018,1041), "Genesis 35", (verseNumber-1012)),
  ((1048,1084), "Genesis 36", (verseNumber-1041)),
  ((1091,1120), "Genesis 37", (verseNumber-1084)),
  ((1127,1150), "Genesis 38", (verseNumber-1120)),
  ((1157,1173), "Genesis 39", (verseNumber-1150)),
  ((1180,1196), "Genesis 40", (verseNumber-1173)),
  ((1197,1253), "Genesis 41", (verseNumber-1196)),
  ((1260,1291), "Genesis 42", (verseNumber-1253)),
  ((1298,1325), "Genesis 43", (verseNumber-1291)),
  ((1332,1359), "Genesis 44", (verseNumber-1325)),
  ((1366,1387), "Genesis 45", (verseNumber-1359)),
  ((1395,1421), "Genesis 46", (verseNumber-1387)),
  ((1429,1452), "Genesis 47", (verseNumber-1421)),
  ((1460,1474), "Genesis 48", (verseNumber-1452)),
  ((1482,1507), "Genesis 49", (verseNumber-1474)),
  ((1515,1533), "Genesis 50", (verseNumber-1507))
  )
  
chapter, verseNumberChapter = next((chapter, verseNumberChapter) for (low, high), chapter, (verseNumberChapter) in quote if low <= verseNumber <= high)
with open("King James Bible.txt") as f:
    lines = f.readlines()
    verse = lines[verseNumber-1].strip()
    print (f"{verse}\n{chapter}:{verseNumberChapter}")