from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/kontakt')
def kontakt():
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)

@app.route('/sitemap.xml')
def sitemap():
    return '''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0/9/sitemap.xsd">
  <url><loc>https://www.lwvending.pl/</loc><priority>1.0</priority></url>
  <url><loc>https://www.lwvending.pl/kontakt</loc><priority>0.8</priority></url>
</urlset>''', 200, {'Content-Type': 'application/xml'}