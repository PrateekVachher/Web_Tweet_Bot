
def analytics(ip):
	import MySQLdb
	print "reached analytics"
	# Open database connection
	db = MySQLdb.connect("vachher.ddns.net","remote","Welcome@1234","TweetBotHeroku" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# Prepare SQL query to UPDATE required records
	sql = "INSERT INTO SiteHits (ipaddr) VALUES ('%s')" % (ip)
	print sql
	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Commit your changes in the database
	   db.commit()
	except:
	   # Rollback in case there is any error
	   db.rollback()

	# disconnect from server
	db.close()



def tweetcall(name,ipaddr,defaulttweet,modifiedtweet):
	import MySQLdb
	print "reached analytics"
	# Open database connection
	db = MySQLdb.connect("vachher.ddns.net","remote","Welcome@1234","TweetBotHeroku" )

	# prepare a cursor object using cursor() method
	cursor = db.cursor()

	# Prepare SQL query to UPDATE required records
	sql = "INSERT INTO TweetCount (Name,ipaddr,DefaultTweet,ModifiedTweet) VALUES ('%s', '%s', '%s', '%s')" % (name,ipaddr,defaulttweet,modifiedtweet)
	print sql
	try:
	   # Execute the SQL command
	   cursor.execute(sql)
	   # Commit your changes in the database
	   db.commit()
	except:
	   # Rollback in case there is any error
	   db.rollback()

	# disconnect from server
	db.close()


def antiabuse(tweet):
	database = ['fuck', 'asshole', 'shit', 'gay', 'fucker', 'ass', 'prateek']
	final = ""
	tweet=tweet.split()
	for k in tweet:
		if k.lower() in database:
			final += k[0]
			final += "*" * (len(k)-2)
			final += k[-1]
		else:
			final += k
		final += " "

	return final[:-1]


def antiname(name):
	database = ['prateek','vachher']
	name = name.split()
	for k in name:
		if k.lower() in database:
			return True
		else:
			return False
