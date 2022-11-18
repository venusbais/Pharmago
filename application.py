import shutil

import scrapperfile as sc
from flask import Flask, render_template, redirect, url_for
from flask import request
from werkzeug.utils import secure_filename

import json
# import src.modelcall


app = Flask(__name__)

dataa = []


@app.get('/')
def test_get():
    return render_template("index.html")


@app.post('/receive')
def test():
    if request.method == 'POST':
        file = request.files['file']
        # if allowed_file(file.filename) == True:
        # temp_name = secure_filename(file.filename.replace(" ", ""))
        file.save(secure_filename(file.filename.replace(" ", "")))

        shutil.move(r"C:\Users\ATHARVA\Downloads\My Final Project\src\word.png", r"C:\Users\ATHARVA\Downloads\My Final Project\data\word.png")

        return redirect(url_for('results_displayer'))

    else:
        return json.dumps("LOL")


@app.route("/results")
def results_displayer(smod= "none"):
    # data_to_insert = [
    #     [(14.42, 'Dolo 500mg Tablet', 'https://pharmeasy.in/online-medicine-order/dolo-500mg-tablet-19749'),
    #      (17.51, 'Paracip 650mg Tablet', 'https://pharmeasy.in/online-medicine-order/paracip-650mg-tablet-6878'),
    #      (19.42, "P 650mg Tablets 10'S", 'https://pharmeasy.in/online-medicine-order/p-650mg-tab-10-s-169787')],
    #     [(14.73, "Crocin Tablet 10's", 'https://www.apollopharmacy.in/otc/crocin-tablet-10-s?doNotTrack=true'),
    #      (16.97, "Crocin 500 mg Tablet 15's", 'https://www.apollopharmacy.in/otc/crocin-500mg-tablet?doNotTrack=true'),
    #      (18.4, "Paracetamol 500 Tablet 10's",
    #       'https://www.apollopharmacy.in/otc/paracetamol-500mg-tab-10-s-kaithy?doNotTrack=true')]]

    # data_to_insert= sc.master_scrapper("crocin")
    # REMEMBER THAT YOU HAVE TO LINK THE MODELS OUTPUT HERE. PARACETAMOL IS JUST A PLACE HOLDER FOR NOW.'''
    a = smod.modelcallerandtextreturner()
    finans = sc.response_corrector(a)
    global dataa
    dataa = sc.master_scrapper(finans)
    data_to_insert = dataa

    return render_template("finalpage.html", data_to_insert=data_to_insert)

if __name__ == "__main__":
    app.debug = True
    app.run()
