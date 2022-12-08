from flask import Flask,jsonify,render_template
import tweepy
import mysql.connector
# establishing the connection
# conn = mysql.connector.connect(
#     user='root', password='', host='127.0.0.1', database='pythondatabase')
# Creating a cursor object using the cursor() method
client = tweepy.Client(bearer_token="AAAAAAAAAAAAAAAAAAAAAKNtiwEAAAAAdKgSTfJZfcRIBLS78YdJC7EpRC8%3Doz6BSsE7AG6aMn4M7HA9Yt5ktgylYVyrRkuiVTN0zC1X2Zr2nT")
# cursor = conn.cursor()
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "This is Python App"
@app.route('/name/<string>')
def getname(string):
    return "The product is " + str(string)
@app.route('/tweetdata/<string:n>')
def armstrong(n):
    tweets = client.get_users_tweets(n)
    alldata = {};
    mainid = 0;
    for tweet in tweets.data:
        print(tweet)
        alldata.update({mainid: tweet.text})
        mainid += 1
    for data in alldata.items():
        singledata = data[1];
        insert_stmt = (
            "INSERT INTO twitterdata(tweet)"
            "VALUES (%s)"
        )
        insertdata = (singledata,)
        try:
            cursor.execute(insert_stmt, insertdata)
            conn.commit()
        except:
            conn.rollback()
    # result = {
    #     "Number": n,
    #     "Armstrong": True,
    #     "Server IP": "122.234.213.53"
    # }
    return jsonify(alldata)
if __name__ == "__main__":
    app.run(debug="True")
    # Debug/Development
    # app.run(debug=True, host="0.0.0.0", port="5000")
    # Production
    # serve(app, host="0.0.0.0", port=8080)
    # http_server = WSGIServer(('https://cfashion.in/', 5000), app)
    # http_server.serve_forever()