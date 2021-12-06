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
import configparser

columns= {}

filmList=[]
countryList=[]
genreList=[]
hallList=[]
sessionList=[]

def generate_route(feature_list):
    for i in range(0, len(feature_list)):
        feature = feature_list[i]
        yield feature


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
            genre=route_guide_pb2.Genre(name=result[0])
            genreList.append(genre)
            #rpc_Add_Genre(stub,result[0])



def fill_country_table(stub):
    country_list=[]
    global using_rabbitMQ
    with sq.connect("DB.db") as con:
        cur = con.cursor()
        cur.execute("SELECT DISTINCT film_country FROM Table_film")
        for result in cur:
            country = route_guide_pb2.Country(name=result[0])
            countryList.append(country)



def fill_hall_table(stub):
    hall_list=[]
    global using_rabbitMQ
    with sq.connect("DB.db") as con:
        cur = con.cursor()
        cur.execute("SELECT DISTINCT hall_no, hall_type, hall_capacity FROM Table_film")
        for result in cur:
            hall = route_guide_pb2.Hall(hall_no=result[0], capacity=result[2], hall_type=result[1])
            hallList.append(hall)
            #rpc_Add_Hall(stub,result[0],result[2],result[1])


def fill_film_table(stub):
    film_list=[]
    global using_rabbitMQ
    with sq.connect("DB.db") as con:
        cur = con.cursor()
        cur.execute("SELECT  DISTINCT film_name, raiting, genre_name,"
                    "film_country from Table_film")
        for result in cur:
            film=route_guide_pb2.Film(genre=result[2],country=result[3],title=result[0],rating=result[1])
            filmList.append(film)
            #rpc_Add_Film(stub,result[2],result[3],result[0],result[1])




def fill_session_table(stub):
    session_list=[]
    global using_rabbitMQ
    with sq.connect("DB.db") as con:
        cur = con.cursor()
        cur.execute("SELECT film_name, hall_no, time FROM Table_film")
        for result in cur:
            session1=route_guide_pb2.Session(hall=result[1],film=result[0],time=result[2])
            sessionList.append(session1)
            #rpc_Add_Session(stub,result[1],result[0],result[2])





def rpc_Add_Country(stub,feature_list):
    #country = route_guide_pb2.Country(name=country_name)
    iterator=generate_route(feature_list)
    response=stub.AddCountry(iterator)
    print(response.result)


def rpc_Add_Genre(stub,feature_list):
    #genre = route_guide_pb2.Genre(name=genre_name)
    iterator = generate_route(feature_list)
    response=stub.AddGenre(iterator)
    print(response.result)


def rpc_Add_Hall(stub,feature_list):
    #hall = route_guide_pb2.Hall(hall_no=hall_no, capacity=capacity,hall_type=hall_type)
    iterator = generate_route(feature_list)
    response=stub.AddHall(iterator)
    print(response.result)


def rpc_Add_Film(stub,feature_list):
    #film = route_guide_pb2.Film(genre=genre,country=country,title=title,rating=raiting)
    iterator = generate_route(feature_list)
    response=stub.AddFilm(iterator)
    print(response.result)


def rpc_Add_Session(stub,feature_list):
    #session1=route_guide_pb2.Session(hall=hall,film=film,time=datetime)
    iterator = generate_route(feature_list)
    response=stub.AddSession(iterator)
    print(response.result)



def run():
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read(r"client_config.ini")
    with grpc.insecure_channel(config['server']['host']+':'+config['server']['port']) as channel:

        stub = route_guide_pb2_grpc.RouteGuideStub(channel)
        fill_country_table(stub)
        fill_genre_table(stub)
        fill_hall_table(stub)
        fill_film_table(stub)
        fill_session_table(stub)
        rpc_Add_Country(stub,countryList)
        rpc_Add_Genre(stub,genreList)
        rpc_Add_Hall(stub,hallList)
        rpc_Add_Film(stub,filmList)
        rpc_Add_Session(stub,sessionList)



if __name__ == '__main__':
    logging.basicConfig()
    run()