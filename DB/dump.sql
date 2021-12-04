--
-- PostgreSQL database dump
--

-- Dumped from database version 13.4
-- Dumped by pg_dump version 13.4

-- Started on 2021-11-20 13:14:39

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

--
-- TOC entry 3025 (class 1262 OID 24817)
-- Name: Film; Type: DATABASE; Schema: -; Owner: postgres
--

CREATE DATABASE "Film" WITH TEMPLATE = template0 ENCODING = 'UTF8';


ALTER DATABASE "Film" OWNER TO postgres;

\connect "Film"

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 207 (class 1259 OID 24863)
-- Name: country; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.country (
    id_country integer NOT NULL,
    country_name text NOT NULL
);


ALTER TABLE public.country OWNER TO postgres;

--
-- TOC entry 206 (class 1259 OID 24861)
-- Name: Country_id_country_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Country_id_country_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Country_id_country_seq" OWNER TO postgres;

--
-- TOC entry 3026 (class 0 OID 0)
-- Dependencies: 206
-- Name: Country_id_country_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Country_id_country_seq" OWNED BY public.country.id_country;


--
-- TOC entry 201 (class 1259 OID 24831)
-- Name: film; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.film (
    id_film integer NOT NULL,
    id_genre integer NOT NULL,
    id_country integer NOT NULL,
    raiting text NOT NULL,
    title text NOT NULL
);


ALTER TABLE public.film OWNER TO postgres;

--
-- TOC entry 200 (class 1259 OID 24829)
-- Name: Film_id_film_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Film_id_film_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Film_id_film_seq" OWNER TO postgres;

--
-- TOC entry 3027 (class 0 OID 0)
-- Dependencies: 200
-- Name: Film_id_film_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Film_id_film_seq" OWNED BY public.film.id_film;


--
-- TOC entry 203 (class 1259 OID 24842)
-- Name: genre; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.genre (
    id_genre integer NOT NULL,
    genre_name text NOT NULL
);


ALTER TABLE public.genre OWNER TO postgres;

--
-- TOC entry 202 (class 1259 OID 24840)
-- Name: Genre_id_genre_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public."Genre_id_genre_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Genre_id_genre_seq" OWNER TO postgres;

--
-- TOC entry 3028 (class 0 OID 0)
-- Dependencies: 202
-- Name: Genre_id_genre_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public."Genre_id_genre_seq" OWNED BY public.genre.id_genre;


--
-- TOC entry 204 (class 1259 OID 24851)
-- Name: hall; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.hall (
    id_hall integer NOT NULL,
    capacity integer NOT NULL,
    hall_type text NOT NULL
);


ALTER TABLE public.hall OWNER TO postgres;

--
-- TOC entry 205 (class 1259 OID 24856)
-- Name: session; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.session (
    id_film integer NOT NULL,
    id_hall integer NOT NULL,
    "time" timestamp without time zone NOT NULL,
    id_session integer NOT NULL
);


ALTER TABLE public.session OWNER TO postgres;

--
-- TOC entry 208 (class 1259 OID 24875)
-- Name: session_id_session_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

CREATE SEQUENCE public.session_id_session_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.session_id_session_seq OWNER TO postgres;

--
-- TOC entry 3029 (class 0 OID 0)
-- Dependencies: 208
-- Name: session_id_session_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: postgres
--

ALTER SEQUENCE public.session_id_session_seq OWNED BY public.session.id_session;


--
-- TOC entry 2879 (class 2604 OID 24866)
-- Name: country id_country; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.country ALTER COLUMN id_country SET DEFAULT nextval('public."Country_id_country_seq"'::regclass);


--
-- TOC entry 2876 (class 2604 OID 24834)
-- Name: film id_film; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.film ALTER COLUMN id_film SET DEFAULT nextval('public."Film_id_film_seq"'::regclass);


--
-- TOC entry 2877 (class 2604 OID 24845)
-- Name: genre id_genre; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genre ALTER COLUMN id_genre SET DEFAULT nextval('public."Genre_id_genre_seq"'::regclass);


--
-- TOC entry 2878 (class 2604 OID 24877)
-- Name: session id_session; Type: DEFAULT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.session ALTER COLUMN id_session SET DEFAULT nextval('public.session_id_session_seq'::regclass);


--
-- TOC entry 2889 (class 2606 OID 24871)
-- Name: country Country_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.country
    ADD CONSTRAINT "Country_pkey" PRIMARY KEY (id_country);


--
-- TOC entry 2881 (class 2606 OID 24839)
-- Name: film Film_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.film
    ADD CONSTRAINT "Film_pkey" PRIMARY KEY (id_film);


--
-- TOC entry 2883 (class 2606 OID 24850)
-- Name: genre Genre_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.genre
    ADD CONSTRAINT "Genre_pkey" PRIMARY KEY (id_genre);


--
-- TOC entry 2885 (class 2606 OID 24855)
-- Name: hall Hall_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.hall
    ADD CONSTRAINT "Hall_pkey" PRIMARY KEY (id_hall);


--
-- TOC entry 2887 (class 2606 OID 24885)
-- Name: session session_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.session
    ADD CONSTRAINT session_pkey PRIMARY KEY (id_session);


-- Completed on 2021-11-20 13:14:47

--
-- PostgreSQL database dump complete
--

