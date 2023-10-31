#!/usr/bin/python3
<<<<<<< HEAD
<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 14:42:23 2020
@author: Robinson Montes
         Mauricio Olarte
"""
=======
=======
>>>>>>> origin/main
'''
Creates a Blueprint instance with `url_prefix` set to `/api/v1`.
'''


<<<<<<< HEAD
>>>>>>> e0ff08e (updated)
=======
>>>>>>> origin/main
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

<<<<<<< HEAD
<<<<<<< HEAD

if (__name__ == 'api.v1.views'):
    from api.v1.views.index import *
    from api.v1.views.states import *
    from api.v1.views.cities import *
    from api.v1.views.amenities import *
    from api.v1.views.users import *
    from api.v1.views.places import *
    from api.v1.views.places_reviews import *
=======
=======
>>>>>>> origin/main
from api.v1.views.index import *
from api.v1.views.states import *
from api.v1.views.cities import *
from api.v1.views.amenities import *
from api.v1.views.users import *
from api.v1.views.places import *
from api.v1.views.places_reviews import *
from api.v1.views.places_amenities import *
<<<<<<< HEAD
>>>>>>> e0ff08e (updated)
=======
>>>>>>> origin/main
