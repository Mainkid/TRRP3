from concurrent import futures
import logging
import psycopg2
import math
import time
import configparser
import grpc
import route_guide_pb2
import route_guide_pb2_grpc
import route_guide_resources

def connect_to_psql():
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read(r"server_config.ini")
    psql_con = psycopg2.connect(
        database=config["postgres"]["database"],
        user=config["postgres"]["user"],
        password=config["postgres"]["password"],
        host=config["postgres"]["host"],
        port=config["postgres"]["port"]
    )
    return (psql_con.cursor(),psql_con)



def genreTable(result):
    psql_cur.execute("SELECT COUNT(*) FROM genre WHERE genre_name= %s",  (result,))
    # print(psql_cur.fetchone()[0])
    if (psql_cur.fetchone()[0] == 0):
        psql_cur.execute("INSERT INTO genre (genre_name) VALUES (%s)",  (result,))
    #psql_con.commit()


def countryTable(result):
    psql_cur.execute("SELECT COUNT(*) FROM country WHERE country_name=(%s)",  (result,))
    if (psql_cur.fetchone()[0] == 0):
        psql_cur.execute("INSERT INTO country (country_name) VALUES (%s)",  (result,))
    #psql_con.commit()


def hallTable(id_hall,hall_type,capacity):
    psql_cur.execute("SELECT COUNT(*) FROM hall WHERE id_hall=(%s)",  (id_hall,))
    # print(psql_cur.fetchone()[0])
    if (psql_cur.fetchone()[0] == 0):
        psql_cur.execute("INSERT INTO hall (id_hall,hall_type,capacity) VALUES ( %s,%s,%s)",  (
        id_hall, hall_type, capacity))
    #psql_con.commit()


def filmTable(genre,country,raiting,title):

    psql_cur.execute("SELECT COUNT(*) FROM film WHERE title=(%s) ",  (title,)
                         )
    if (psql_cur.fetchone()[0] == 0):
        psql_cur.execute("INSERT INTO film (id_genre,id_country,title,raiting) VALUES("
                         "(SELECT id_genre FROM genre WHERE genre_name=%s),"
                         "(SELECT id_country FROM country WHERE country_name=%s),"
                         "%s,%s)",  (genre, country, title, raiting))
    #psql_con.commit()


def sessionTable(hall, film,time):
    psql_cur.execute("SELECT COUNT(*) FROM session WHERE id_film=(SELECT id_film FROM film WHERE title=%s) AND"
                     " id_hall=%s AND time=%s",  (film, hall, time)
                    )
    if (psql_cur.fetchone()[0] == 0):
        psql_cur.execute("INSERT INTO session (id_film,id_hall,time) VALUES"
                         "((SELECT id_film FROM film WHERE title=%s), %s,%s)", (film, str(hall), str(time))
                            )

    #send_msg('Success!')
    psql_con.commit()


class RouteGuideServicer(route_guide_pb2_grpc.RouteGuideServicer):
    """Provides methods that implement functionality of route guide server."""

    def __init__(self):
        pass

    def AddCountry(self, request_iterator, context):
        for request in request_iterator:
            countryTable(request.name)
        return route_guide_pb2.Result(result="OK")


    def AddSession(self, request_iterator, context):
        for request in request_iterator:
            sessionTable(request.hall, request.film, request.time)
        return route_guide_pb2.Result(result="OK")

    def AddFilm(self, request_iterator, context):
        for request in request_iterator:
            filmTable(request.genre,request.country,request.rating,request.title)
        return route_guide_pb2.Result(result="OK")

    def AddGenre(self, request_iterator, context):
        for request in request_iterator:
            genreTable(request.name)
        return route_guide_pb2.Result(result="OK")

    def AddHall(self, request_iterator, context):
        for request in request_iterator:
            hallTable(request.hall_no,request.hall_type,request.capacity)
        return route_guide_pb2.Result(result="OK")




def serve():
    config = configparser.ConfigParser()  # создаём объекта парсера
    config.read(r"server_config.ini")
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    route_guide_pb2_grpc.add_RouteGuideServicer_to_server(
        RouteGuideServicer(), server)
    server.add_insecure_port('[::]:'+config['server']['port'])

    server.start()
    server.wait_for_termination()


if __name__ == '__main__':
    psql_cur, psql_con = connect_to_psql()
    logging.basicConfig()
    serve()
