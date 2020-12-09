**Improved flask app**

This is a further development of the CS50 finance app.

The app has been re-written using flask blueprints using flask blueprints. THis makes the app more modular and its easier to add or remove elements.

I have also added some additional functions:
    - displaying savings rates
    - displaying an interactive graphy of savings rates
    - showing key economic information that is relevant for investing (including interactive graphs)

*Future development*

I am planning on splitting to app into two microservices: 

1 will act as a front end and contain the saving/economic data. The other will contain all the backend information for the CS50 finance app. 


*Key sources*

SQL alchemy:
    - db.session.update : 
    - using SQL queries directly: https://stackoverflow.com/questions/17972020/how-to-execute-raw-sql-in-flask-sqlalchemy-app
    - adding variables to sql queries: https://chartio.com/resources/tutorials/how-to-execute-raw-sql-in-sqlalchemy/
    - the SQLalchemy result to a json/dictionary: https://stackoverflow.com/questions/20743806/sqlalchemy-execute-return-resultproxy-as-tuple-not-dict
    - pandas to json: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.to_json.html

Flask:
    - layout: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world
    - blueprints: https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xv-a-better-application-structure

Getting economic data in pandas:
    - http://jeremymikecz.com/498/4_wbdata.html

Javascript:
    - datatables: https://datatables.net/
                  https://datatables.net/manual/options
                  https://stackoverflow.com/questions/50919478/get-ajax-to-fill-datatables-with-json-data-sent-from-flask-and-separately-render/50937257
    - using altair/vegalite in a html page: https://github.com/lemoncyb/flasked-altair