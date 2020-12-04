import os
from flask import current_app, render_template, jsonify, request, redirect, url_for
from app.stat import bp
from app.stat.stat_functions import inflat_db, gdp_db, latest_date, inflat_date, gdp_date, chart
from app.stat.stat_forms import choose_form
import altair as alt

@bp.route('/econ', methods=['GET','POST'])
def econ():
    # add option to choose different locations
    print("Hi!!!!")
    inf = inflat_date()
    print(inf)
    gdp = gdp_date()
    print(gdp)
    form = choose_form()
    if request.method == 'POST' and form.validate():
        ind = request.form.get("target_indicator")
        if ind == "GDP growth":
            # https://stackoverflow.com/questions/59703356/displaying-data-on-the-same-page-a-form-in-flask
            df = gdp_db()
            y = "GDP per capita growth (annual %)"
            print(y)
            print(df)
            ind_chart = chart(df,y)
        elif ind == "Interest rate":
            df = inflat_db()
            y = "InflationConsumerPrices"
            ind_chart = chart(df,y)
        # add debt
        else:
            return redirect(url_for("index"))
        ind_chart.save("app/static/chart.json")
        return redirect(url_for("stat.test"))
    return render_template('stat/econ.html', form = form, inf = inf, gdp = gdp)

@bp.route('/gdp_table')
def gdp_table():
    db = gdp_db()
    print(db)
    JSON = db.to_json(orient='table',index=False)
    return JSON

@bp.route('/inf_table')
def inf_table():
    db = inflat_db()
    print(db)
    JSON = db.to_json(orient='table',index=False)
    return JSON

@bp.route('/test')
def test():
    return render_template("stat/test.html")

@bp.route("/econ_chart")
def econ_chart():
    fl = open("app/static/chart.json", "r")
    json = fl.read()
    fl.close()
    return json


