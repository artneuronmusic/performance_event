--
-- PostgreSQL database dump
--

-- Dumped from database version 10.21 (Ubuntu 10.21-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.21 (Ubuntu 10.21-0ubuntu0.18.04.1)

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
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO vagrant;

--
-- Name: artist; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.artist (
    id integer NOT NULL,
    name character varying(120) NOT NULL,
    city character varying(120) NOT NULL,
    state character varying(120) NOT NULL,
    phone character varying(120) NOT NULL,
    genres character varying(200)[] NOT NULL,
    website_link character varying(200),
    facebook_link character varying(120),
    image_link character varying(500),
    seeking_venue boolean,
    seeking_venue_description character varying(200)
);


ALTER TABLE public.artist OWNER TO vagrant;

--
-- Name: artist_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.artist_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.artist_id_seq OWNER TO vagrant;

--
-- Name: artist_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.artist_id_seq OWNED BY public.artist.id;


--
-- Name: show; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.show (
    id integer NOT NULL,
    artist_id integer,
    venue_id integer,
    start_time timestamp without time zone NOT NULL
);


ALTER TABLE public.show OWNER TO vagrant;

--
-- Name: show_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.show_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.show_id_seq OWNER TO vagrant;

--
-- Name: show_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.show_id_seq OWNED BY public.show.id;


--
-- Name: venue; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.venue (
    id integer NOT NULL,
    name character varying(120) NOT NULL,
    address character varying(120) NOT NULL,
    city character varying(120) NOT NULL,
    state character varying(120) NOT NULL,
    phone character varying(120) NOT NULL,
    genres character varying(200)[] NOT NULL,
    website_link character varying(200),
    facebook_link character varying(120),
    seeking_talent boolean,
    seeking_talent_description character varying(200),
    image_link character varying(500)
);


ALTER TABLE public.venue OWNER TO vagrant;

--
-- Name: venue_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.venue_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.venue_id_seq OWNER TO vagrant;

--
-- Name: venue_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.venue_id_seq OWNED BY public.venue.id;


--
-- Name: artist id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.artist ALTER COLUMN id SET DEFAULT nextval('public.artist_id_seq'::regclass);


--
-- Name: show id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.show ALTER COLUMN id SET DEFAULT nextval('public.show_id_seq'::regclass);


--
-- Name: venue id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.venue ALTER COLUMN id SET DEFAULT nextval('public.venue_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.alembic_version (version_num) FROM stdin;
c8260e0e9d20
\.


--
-- Data for Name: artist; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.artist (id, name, city, state, phone, genres, website_link, facebook_link, image_link, seeking_venue, seeking_venue_description) FROM stdin;
1	Guns N Petals	San Francisco	CA	326-123-5000	{"Rock n Roll"}	https://www.gunsnpetalsband.com	https://www.facebook.com/GunsNPetals	https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80	t	Looking for shows to perform at in the San Francisco Bay Area!
2	Matt Quevedo	New York	NY	300-400-5000	{Jazz}		https://www.facebook.com/mattquevedo923251523	https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80	f	
3	The Wild Sax Band	San Francisco	CA	432-325-5432	{Classical,Jazz}			https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80	f	
\.


--
-- Data for Name: show; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.show (id, artist_id, venue_id, start_time) FROM stdin;
1	3	1	2019-05-21 21:30:00
2	2	3	2019-06-15 23:00:00
3	1	1	2035-04-01 20:00:00
4	1	2	2035-04-08 20:00:00
5	1	3	2035-04-15 20:00:00
\.


--
-- Data for Name: venue; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.venue (id, name, address, city, state, phone, genres, website_link, facebook_link, seeking_talent, seeking_talent_description, image_link) FROM stdin;
1	The Musical Hop	1015 Folsom Street	San Francisco	CA	123-123-1234	{Blues,Folk,Hip-Hop}	https://www.themusicalhop.com	https://www.facebook.com/TheMusicalHop	t	We are on the lookout for a local artist to play every two weeks. Please call us.	https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60
2	The Dueling Pianos Bar	335 Delancey Street	New York	NY	914-003-1132	{Blues,Electronic,Funk}	https://www.theduelingpianos.com	https://www.facebook.com/theduelingpianos	f		https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80
3	Park Square Live Music & Coffee	34 Whiskey Moore Ave	San Francisco	CA	415-000-1234	{Alternative,Folk}	https://www.parksquarelivemusicandcoffee.com	https://www.facebook.com/ParkSquareLiveMusicAndCoffee	f		https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80
\.


--
-- Name: artist_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.artist_id_seq', 3, true);


--
-- Name: show_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.show_id_seq', 5, true);


--
-- Name: venue_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.venue_id_seq', 3, true);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: artist artist_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.artist
    ADD CONSTRAINT artist_pkey PRIMARY KEY (id);


--
-- Name: show show_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.show
    ADD CONSTRAINT show_pkey PRIMARY KEY (id);


--
-- Name: venue venue_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.venue
    ADD CONSTRAINT venue_pkey PRIMARY KEY (id);


--
-- Name: show show_artist_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.show
    ADD CONSTRAINT show_artist_id_fkey FOREIGN KEY (artist_id) REFERENCES public.artist(id);


--
-- Name: show show_venue_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.show
    ADD CONSTRAINT show_venue_id_fkey FOREIGN KEY (venue_id) REFERENCES public.venue(id);


--
-- PostgreSQL database dump complete
--

