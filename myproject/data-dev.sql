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
    id bigint NOT NULL,
    name text NOT NULL,
    city text NOT NULL,
    state text NOT NULL,
    phone text NOT NULL,
    genres text NOT NULL,
    image_link text,
    website_link text,
    facebook_link text,
    seeking_venue boolean,
    seeking_venue_description text
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
-- Name: roles; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.roles (
    id integer NOT NULL,
    name character varying(50) NOT NULL
);


ALTER TABLE public.roles OWNER TO vagrant;

--
-- Name: roles_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.roles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.roles_id_seq OWNER TO vagrant;

--
-- Name: roles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.roles_id_seq OWNED BY public.roles.id;


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
-- Name: user_roles; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.user_roles (
    user_id integer,
    role_id integer,
    id integer NOT NULL
);


ALTER TABLE public.user_roles OWNER TO vagrant;

--
-- Name: user_roles_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.user_roles_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.user_roles_id_seq OWNER TO vagrant;

--
-- Name: user_roles_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.user_roles_id_seq OWNED BY public.user_roles.id;


--
-- Name: users; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.users (
    id integer NOT NULL,
    email character varying(255) NOT NULL,
    password character varying(255) NOT NULL,
    name character varying(100) NOT NULL
);


ALTER TABLE public.users OWNER TO vagrant;

--
-- Name: users_id_seq; Type: SEQUENCE; Schema: public; Owner: vagrant
--

CREATE SEQUENCE public.users_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.users_id_seq OWNER TO vagrant;

--
-- Name: users_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: vagrant
--

ALTER SEQUENCE public.users_id_seq OWNED BY public.users.id;


--
-- Name: venue; Type: TABLE; Schema: public; Owner: vagrant
--

CREATE TABLE public.venue (
    id bigint NOT NULL,
    name text NOT NULL,
    address text NOT NULL,
    city text NOT NULL,
    state text NOT NULL,
    phone text NOT NULL,
    genres text NOT NULL,
    image_link text,
    website_link text,
    facebook_link text,
    seeking_talent boolean,
    seeking_talent_description text
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
-- Name: roles id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.roles ALTER COLUMN id SET DEFAULT nextval('public.roles_id_seq'::regclass);


--
-- Name: show id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.show ALTER COLUMN id SET DEFAULT nextval('public.show_id_seq'::regclass);


--
-- Name: user_roles id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.user_roles ALTER COLUMN id SET DEFAULT nextval('public.user_roles_id_seq'::regclass);


--
-- Name: users id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.users ALTER COLUMN id SET DEFAULT nextval('public.users_id_seq'::regclass);


--
-- Name: venue id; Type: DEFAULT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.venue ALTER COLUMN id SET DEFAULT nextval('public.venue_id_seq'::regclass);


--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.alembic_version (version_num) FROM stdin;
1d97ce2d29f8
\.


--
-- Data for Name: artist; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.artist (id, name, city, state, phone, genres, image_link, website_link, facebook_link, seeking_venue, seeking_venue_description) FROM stdin;
1	Rodgers, Sanchez and Jenkins	Wrightstad	AL	612-234-5804	{Jazz}	https://dummyimage.com/100x1014	www.RodgersSanchezandJenkins.com	www.fcebook.com/RodgersSanchezandJenkins	f	
2	Wilson-Rodriguez	Kimberlymouth	SC	389-649-7097	{Jazz}	https://placekitten.com/113/199	www.WilsonRodriguez.com	www.fcebook.com/WilsonRodriguez	t	places which love music and enjoy it
3	Hartman and Sons	Lake Gabrielle	RI	298-642-8664	{Folk}	https://placekitten.com/84/801	www.HartmanandSons.com	www.fcebook.com/HartmanandSons	f	
4	Ferguson-Rich	Toddstad	IL	766-072-9677	{Reggae}	https://placekitten.com/846/695	www.FergusonRich.com	www.fcebook.com/FergusonRich	f	
5	Gonzalez and Sons	Michaelmouth	WI	008-068-3975	{Blues}	https://placekitten.com/540/65	www.GonzalezandSons.com	www.fcebook.com/GonzalezandSons	t	Affordable places for performance
6	Martin-Smith	Williamsburgh	DE	767-622-5921	{"Rock n Roll"}	https://picsum.photos/338/150	www.MartinSmith.com	www.fcebook.com/MartinSmith	f	
7	Sanchez-Davis	Ewingstad	DE	902-448-9752	{Funk}	https://picsum.photos/968/553	www.SanchezDavis.com	www.fcebook.com/SanchezDavis	t	places which love music and enjoy it
8	Jones, Schmidt and Smith	North Jacquelineberg	OH	195-123-7276	{Other}	https://picsum.photos/1017/784	www.JonesSchmidtandSmith.com	www.fcebook.com/JonesSchmidtandSmith	f	
9	Melendez and Sons	North Matthew	RI	756-721-8667	{R&B}	https://dummyimage.com/13x1013	www.MelendezandSons.com	www.fcebook.com/MelendezandSons	t	places which love music and enjoy it
10	Doyle, Miller and Moreno	West Mariahburgh	MD	465-053-8798	{Classical}	https://picsum.photos/545/857	www.DoyleMillerandMoreno.com	www.fcebook.com/DoyleMillerandMoreno	f	
11	Rice-Orozco	West Mark	GA	241-105-3041	{"Musical Theatre"}	https://placekitten.com/656/782	www.RiceOrozco.com	www.fcebook.com/RiceOrozco	t	Any performing places in USA
12	Owens, Flores and Turner	Grantstad	NY	822-079-8980	{Other}	https://placekitten.com/785/304	www.OwensFloresandTurner.com	www.fcebook.com/OwensFloresandTurner	f	
13	Shaffer-Bryan	Danielstad	IA	039-116-4282	{Folk}	https://dummyimage.com/534x816	www.ShafferBryan.com	www.fcebook.com/ShafferBryan	t	places which love music and enjoy it
14	Jones-Smith	Lake Janiceland	MD	614-824-6816	{Instrumental}	https://picsum.photos/740/763	www.JonesSmith.com	www.fcebook.com/JonesSmith	f	
15	Reeves, Bonilla and Ramirez	Port Joseph	CA	115-882-9719	{Folk}	https://placeimg.com/44/574/any	www.ReevesBonillaandRamirez.com	www.fcebook.com/ReevesBonillaandRamirez	t	Any performing places in USA
16	Roman, Chavez and Daniels	New Christopherfort	LA	255-696-1746	{Pop}	https://placekitten.com/804/951	www.RomanChavezandDaniels.com	www.fcebook.com/RomanChavezandDaniels	f	
17	Bradshaw-Pace	Thomaston	MT	098-038-6838	{Alternative}	https://picsum.photos/31/221	www.BradshawPace.com	www.fcebook.com/BradshawPace	t	Any performing places in USA
18	Johnson, Mccann and Hughes	Tylershire	TX	586-843-1619	{Punk}	https://placeimg.com/391/89/any	www.JohnsonMccannandHughes.com	www.fcebook.com/JohnsonMccannandHughes	t	Affordable places for performance
19	Nelson-White	Lake Donnaland	DC	959-132-0338	{Folk}	https://placeimg.com/340/604/any	www.NelsonWhite.com	www.fcebook.com/NelsonWhite	f	
20	Jenkins, Adams and Moore	New Willietown	NM	612-936-1267	{Blues}	https://picsum.photos/910/506	www.JenkinsAdamsandMoore.com	www.fcebook.com/JenkinsAdamsandMoore	f	
21	Guns N Petals	San Francisco	CA	326-123-5000	{"Rock n Roll"}	https://images.unsplash.com/photo-1549213783-8284d0336c4f?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=300&q=80	https://www.gunsnpetalsband.com	https://www.facebook.com/GunsNPetals	t	Looking for shows to perform at in the San Francisco Bay Area!
22	Matt Quevedo	New York	NY	300-400-5000	{Jazz}	https://images.unsplash.com/photo-1495223153807-b916f75de8c5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=334&q=80		https://www.facebook.com/mattquevedo923251523	f	
23	The Wild Sax Band	San Francisco	CA	432-325-5432	{Classical,Jazz}	https://images.unsplash.com/photo-1558369981-f9ca78462e61?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=794&q=80			f	
\.


--
-- Data for Name: roles; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.roles (id, name) FROM stdin;
1	ADMIN
3	VENUE
4	ARTIST
\.


--
-- Data for Name: show; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.show (id, artist_id, venue_id, start_time) FROM stdin;
1	23	21	2019-05-21 21:30:00
2	22	23	2019-06-15 23:00:00
3	21	21	2035-04-01 20:00:00
4	21	22	2035-04-08 20:00:00
5	21	23	2035-04-15 20:00:00
6	19	5	2025-12-30 22:00:00
7	3	16	2019-03-21 19:00:30
8	15	3	2022-01-03 12:00:00
9	2	9	2026-07-11 17:00:20
10	3	1	2019-10-08 19:00:20
\.


--
-- Data for Name: user_roles; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.user_roles (user_id, role_id, id) FROM stdin;
5	1	4
6	3	5
7	4	6
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.users (id, email, password, name) FROM stdin;
5	admin2022@gmail.com	sha256$qM5O6DBePH3Ld7aN$c8dd8b54baed6dffd8d1a6679fd7a095c27aa79fcee5f94464e739e4c6c8c662	admin
6	venue2022@gmail.com	sha256$GT2MobnzFqfNHrFB$253e2aba2a977d02aeff8365fc3a7e05d095db8e139267c493fa18aff5da429e	venue
7	artist2022@gmail.com	sha256$qMklKaiCKlh8PX8o$51271a932af804ec6253e230591246788b8df2ae29f0e8bfbd31ac294ac5dd66	artist
\.


--
-- Data for Name: venue; Type: TABLE DATA; Schema: public; Owner: vagrant
--

COPY public.venue (id, name, address, city, state, phone, genres, image_link, website_link, facebook_link, seeking_talent, seeking_talent_description) FROM stdin;
1	Plan B Running	53960 Dixon Passage	West Phillipmouth	MA	995-997-1291	{Reggae}	https://placeimg.com/893/99/any	www.PlanBRunning.com	www.fcebook.com/PlanBRunning	t	No expereinced is not problem; we are looking for musicians who has passion, even just new to the field
2	Holy Accustic	38426 Herrera Forks	North Denise	IA	980-168-6750	{"Heavy Metal"}	https://picsum.photos/658/949	www.HolyAccustic.com	www.fcebook.com/HolyAccustic	t	Talented artist who is willing to perform and share music
3	Mr. & Mrs. Bun	97744 Mcdaniel Lakes	North Emilyshire	UT	902-598-8473	{Pop}	https://placekitten.com/697/59	www.MrMrsBun.com	www.fcebook.com/MrMrsBun	f	
4	Spanked Puppy	837 John Burg Apt. 385	West Jennifershire	MO	590-291-1691	{Other}	https://picsum.photos/156/189	www.SpankedPuppy.com	www.fcebook.com/SpankedPuppy	f	
5	Hot Chix Boston	3670 Hendricks Villages Apt. 368	East Cynthia	TN	622-131-1626	{Other}	https://placekitten.com/669/211	www.HotChixBoston.com	www.fcebook.com/HotChixBoston	t	Talented artist who is willing to perform and share music
6	Egg Slut	162 Richardson Club Suite 345	New Kennethberg	OR	704-649-6401	{Jazz}	https://dummyimage.com/702x346	www.EggSlut.com	www.fcebook.com/EggSlut	f	
7	Holy Accustic	6253 Matthew Freeway	Port Reginaldberg	WI	321-721-9023	{Reggae}	https://placeimg.com/1012/241/any	www.HolyAccustic.com	www.fcebook.com/HolyAccustic	t	its a great and friendly place for performers
8	Phlavz	725 Carr Keys Apt. 786	Kiaramouth	DC	437-096-8776	{Instrumental}	https://dummyimage.com/427x504	www.Phlavz.com	www.fcebook.com/Phlavz	f	
9	Foulmouthed Brewing	106 Roberta Corners	Lake Carriestad	MD	558-308-5357	{"Musical Theatre"}	https://placekitten.com/756/400	www.FoulmouthedBrewing.com	www.fcebook.com/FoulmouthedBrewing	t	Talented artist who is willing to perform and share music
10	Egg Slut	9415 Melissa Motorway	Christopherfurt	MD	351-162-5866	{Instrumental}	https://dummyimage.com/979x594	www.EggSlut.com	www.fcebook.com/EggSlut	f	
11	Meet Classical	2342 Anna Trail	West Rebecca	NY	458-005-3941	{Punk}	https://picsum.photos/269/812	www.MeetClassical.com	www.fcebook.com/MeetClassical	t	its a great and friendly place for performers
12	Bun Huggers Old Fashion	4765 Jordan Meadows Apt. 970	Gentryland	NC	927-729-4278	{Pop}	https://picsum.photos/131/284	www.BunHuggersOldFashion.com	www.fcebook.com/BunHuggersOldFashion	t	No expereinced is not problem; we are looking for musicians who has passion, even just new to the field
13	Hot Chix Boston	941 Jon Views	South Manuelview	FL	848-633-3259	{Pop}	https://placekitten.com/932/119	www.HotChixBoston.com	www.fcebook.com/HotChixBoston	f	
14	Fat Baby	509 Heather Trail Suite 727	East Rodneyside	MN	796-893-8408	{"Musical Theatre"}	https://dummyimage.com/149x238	www.FatBaby.com	www.fcebook.com/FatBaby	f	
15	un·cooked	7626 Brenda Roads Suite 481	Williamport	MT	897-482-8789	{Blues}	https://placeimg.com/628/498/any	www.uncooked.com	www.fcebook.com/uncooked	t	No expereinced is not problem; we are looking for musicians who has passion, even just new to the field
16	Foulmouthed Brewing	709 Amy Neck Suite 023	Vargaston	CA	232-854-0659	{Country}	https://placeimg.com/374/486/any	www.FoulmouthedBrewing.com	www.fcebook.com/FoulmouthedBrewing	t	No expereinced is not problem; we are looking for musicians who has passion, even just new to the field
17	Phlavz	4383 Parker Crescent	Jenniferbury	WA	410-477-8930	{Pop}	https://picsum.photos/209/110	www.Phlavz.com	www.fcebook.com/Phlavz	f	
18	Hot Chix Boston	52605 Luna Rue Suite 581	Port Joshua	CA	805-512-5767	{Alternative}	https://placekitten.com/398/1008	www.HotChixBoston.com	www.fcebook.com/HotChixBoston	f	
19	Bun Huggers Old Fashion	15376 Michelle Ranch Suite 449	North Christina	CA	925-043-1575	{Electronic}	https://placekitten.com/125/731	www.BunHuggersOldFashion.com	www.fcebook.com/BunHuggersOldFashion	t	No expereinced is not problem; we are looking for musicians who has passion, even just new to the field
20	Egg Slut	5817 Graham Way Apt. 980	West Ryanbury	AZ	582-476-5190	{"Musical Theatre"}	https://placeimg.com/8/1017/any	www.EggSlut.com	www.fcebook.com/EggSlut	f	
21	The Musical Hop	1015 Folsom Street	San Francisco	CA	123-123-1234	{Blues,Folk,Hip-Hop}	https://images.unsplash.com/photo-1543900694-133f37abaaa5?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=400&q=60	https://www.themusicalhop.com	https://www.facebook.com/TheMusicalHop	t	We are on the lookout for a local artist to play every two weeks. Please call us.
22	The Dueling Pianos Bar	335 Delancey Street	New York	NY	914-003-1132	{Blues,Electronic,Funk}	https://images.unsplash.com/photo-1497032205916-ac775f0649ae?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=750&q=80	https://www.theduelingpianos.com	https://www.facebook.com/theduelingpianos	f	
23	Park Square Live Music & Coffee	34 Whiskey Moore Ave	San Francisco	CA	415-000-1234	{Alternative,Folk}	https://images.unsplash.com/photo-1485686531765-ba63b07845a7?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=747&q=80	https://www.parksquarelivemusicandcoffee.com	https://www.facebook.com/ParkSquareLiveMusicAndCoffee	f	
\.


--
-- Name: artist_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.artist_id_seq', 3, true);


--
-- Name: roles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.roles_id_seq', 4, true);


--
-- Name: show_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.show_id_seq', 10, true);


--
-- Name: user_roles_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.user_roles_id_seq', 8, true);


--
-- Name: users_id_seq; Type: SEQUENCE SET; Schema: public; Owner: vagrant
--

SELECT pg_catalog.setval('public.users_id_seq', 10, true);


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
-- Name: roles roles_name_key; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_name_key UNIQUE (name);


--
-- Name: roles roles_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.roles
    ADD CONSTRAINT roles_pkey PRIMARY KEY (id);


--
-- Name: show show_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.show
    ADD CONSTRAINT show_pkey PRIMARY KEY (id);


--
-- Name: user_roles user_roles_id_key; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.user_roles
    ADD CONSTRAINT user_roles_id_key UNIQUE (id);


--
-- Name: users users_email_key; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_email_key UNIQUE (email);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (id);


--
-- Name: venue venue_pkey; Type: CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.venue
    ADD CONSTRAINT venue_pkey PRIMARY KEY (id);


--
-- Name: show show_artist_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.show
    ADD CONSTRAINT show_artist_id_fkey FOREIGN KEY (artist_id) REFERENCES public.artist(id) ON DELETE CASCADE;


--
-- Name: show show_venue_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.show
    ADD CONSTRAINT show_venue_id_fkey FOREIGN KEY (venue_id) REFERENCES public.venue(id) ON DELETE CASCADE;


--
-- Name: user_roles user_roles_role_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.user_roles
    ADD CONSTRAINT user_roles_role_id_fkey FOREIGN KEY (role_id) REFERENCES public.roles(id) ON DELETE CASCADE;


--
-- Name: user_roles user_roles_user_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: vagrant
--

ALTER TABLE ONLY public.user_roles
    ADD CONSTRAINT user_roles_user_id_fkey FOREIGN KEY (user_id) REFERENCES public.users(id) ON DELETE CASCADE;


--
-- PostgreSQL database dump complete
--

