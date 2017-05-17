# README - opensenate #

Client for manipulating Brazilian federal senate open data.

### Install ###

* Git clone project
* Run `python setup.py install`
* Run `python manage.py test` (when developing)

### Test ###

* Use TDD when developing 
* `python setup.py test`

### Usage ###
##### GET Senators #####
    from opensenate import SenatorClient
    senator_client = SenatorClient()
    senators = senator_client.get()
    