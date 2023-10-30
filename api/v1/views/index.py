#!/usr/bin/python3
<<<<<<< HEAD
# -*- coding: utf-8 -*-
"""
@authors: Frank Galos.
          Uchechukwu Ogbodo
"""
from flask import jsonify, Blueprint
from models import storage
from api.v1.views import app_views
from models.state import State


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def get_status():
    """ check the status of route """
    return jsonify({'status': 'OK'})

@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def object_status():
    """Create a endpoint that retrieves the number of each objects by type
    """
    objects = {"amenities": 'Amenity', "cities": 'City', "places": 'Place',
               "reviews": 'Review', "states": 'State', "users": 'User'}
    for key, value in objects.items():
        objects[key] = storage.count(value)
    return jsonify(objects)
=======
'''
Create a route `/status` on the object app_views.
'''


from flask import jsonify
from api.v1.views import app_views
from models import storage


@app_views.route('/status', methods=['GET'])
def api_status():
    '''
    Returns a JSON response for RESTful API health.
    '''
    response = {'status': 'OK'}
    return jsonify(response)


@app_views.route('/stats', methods=['GET'])
def get_stats():
    '''
    Retrieves the number of each objects by type.
    '''
    stats = {
        'amenities': storage.count('Amenity'),
        'cities': storage.count('City'),
        'places': storage.count('Place'),
        'reviews': storage.count('Review'),
        'states': storage.count('State'),
        'users': storage.count('User')
    }
    return jsonify(stats)
>>>>>>> e0ff08e (updated)
