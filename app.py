from flask import Flask, render_template
import script #occupations script

#this is a constructor call
#creating an instance of a class
app = Flask(__name__) 

#tells apache what to do when browser requests access from root of flask app
@app.route("/")
def helloWorld():
    return '''
Hello! Welcome to my webpage.<br><br>
Feel free to <a href="page0">click</a>
<a href="page1">around</a>'''

@app.route("/page0")
def page0():
    return '''
<a href="http://orteil.dashnet.org/cookieclicker" target="_blank">Here\'s a fun \'lil game for you</a>.<br><br>
Or, <a href="/">go back</a>
    '''

@app.route("/page1")
def page1():
    return '''
<a href="https://www.reddit.com/r/etymology/comments/32jf5d/what_is_the_origin_of_the_phrase_be_there_or_be/cqbwxqq" target="_blank">Did you know?</a><br><br>
<a href="/">Go back</a>
    '''

d = script.getDict()

@app.route("/occupations")
def occu():
    return render_template("occupations.html", foo = "Occupations", dic = d, choose = script.choose(d))

coll = [1, 3, 3, 7]

@app.route("/template")
def test_tmplt():
    return render_template("template.html", foo = "HELLLOOOOO", fool = coll)

if __name__ == "__main__":
    app.debug = True
    app.run()
