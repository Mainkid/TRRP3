# Copyright 2015 gRPC authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""The Python implementation of the gRPC route guide client."""

from __future__ import print_function

import logging
import random

import grpc
import route_guide_pb2
import route_guide_pb2_grpc
import sqlite3 as sq

columns= {}

def generate_dictionary():
    with sq.connect("DB.db") as con:
        cur=con.cursor()
        res=cur.execute("SELECT * FROM Table_film")
        for i in range(0,len(cur.description)):
            columns[i]=cur.description[i][0]

def fill_genre_table(stub):

    with sq.connect("DB.db") as con:
        cur = con.cursor()
        cur.execute("SELECT DISTINCT genre_name FROM Table_film")
        for result in cur:
            rpc_Add_Genre(stub,result[0])



def fill_country_table(stub):
    country_list=[]
    global using_rabbitMQ
    with sq.connect("DB.db") as con:
        cur = con.cursor()
        cur.execute("SELECT DISTINCT film_country FROM Table_film")
        for result in cur:
            rpc_Add_Country(stub,result[0])



def fill_hall_table(stub):
    hall_list=[]
    global using_rabbitMQ
    with sq.connect("DB.db") as con:
        cur = con.cursor()
        cur.execute("SELECT DISTINCT hall_no, hall_type, hall_capacity FROM Table_film")
        for result in cur:
            rpc_Add_Hall(stub,result[0],result[2],result[1])


def fill_film_table(stub):
    film_list=[]
    global using_rabbitMQ
    with sq.connect("DB.db") as con:
        cur = con.cursor()
        cur.execute("SELECT  DISTINCT film_name, raiting, genre_name,"
                    "film_country from Table_film")
        for result in cur:
            #film_list.append(list(result))
            rpc_Add_Film(stub,result[2],result[3],result[0],result[1])
            data = {"Table": "film",
                    "Arr": list(result)}



def fill_session_table(stub):
    session_list=[]
    global using_rabbitMQ
    with sq.connect("DB.db") as con:
        cur = con.cursor()
        cur.execute("SELECT film_name, hall_no, time FROM Table_film")
        for result in cur:
            rpc_Add_Session(stub,result[1],result[0],result[2])
            data = {"Table": "session",
                    "Arr": list(result)}



def rpc_Add_Country(stub,country_name):
    country = route_guide_pb2.Country(name=country_name)
    response=stub.AddCountry(country)
    print(response)


def rpc_Add_Genre(stub,genre_name):
    genre = route_guide_pb2.Genre(name=genre_name)
    response=stub.AddGenre(genre)
    print(response)


def rpc_Add_Hall(stub,hall_no,capacity,hall_type):
    hall = route_guide_pb2.Hall(hall_no=hall_no, capacity=capacity,hall_type=hall_type)
    response=stub.AddHall(hall)
    print(response)


def rpc_Add_Film(stub,genre,country,title,raiting):
    film = route_guide_pb2.Film(genre=genre,country=country,title=title,rating=raiting)
    response=stub.AddFilm(film)
    print(response)


def rpc_Add_Session(stub,hall,film,datetime):
    session1=route_guide_pb2.Session(hall=hall,film=film,time=datetime)
    response=stub.AddSession(session1)
    print(response)



def run():
    # NOTE(gRPC Python Team): .close() is possible on a channel and should be
    # used in circumstances in which the with statement does not fit the needs
    # of the code.
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = route_guide_pb2_grpc.RouteGuideStub(channel)
        fill_country_table(stub)
        fill_genre_table(stub)
        fill_hall_table(stub)
        fill_film_table(stub)
        fill_session_table(stub)


if __name__ == '__main__':
    logging.basicConfig()
    run()