--
-- PostgreSQL database dump
--

-- Dumped from database version 10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)
-- Dumped by pg_dump version 10.12 (Ubuntu 10.12-0ubuntu0.18.04.1)

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
-- Name: answer; Type: TABLE; Schema: public; Owner: pi
--

CREATE TABLE public.answer (
    id integer NOT NULL,
    submission_time timestamp without time zone,
    vote_number integer,
    question_id integer,
    message text,
    image text
);


ALTER TABLE public.answer OWNER TO pi;

--
-- Name: answer_id_seq; Type: SEQUENCE; Schema: public; Owner: pi
--

CREATE SEQUENCE public.answer_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.answer_id_seq OWNER TO pi;

--
-- Name: answer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pi
--

ALTER SEQUENCE public.answer_id_seq OWNED BY public.answer.id;


--
-- Name: comment; Type: TABLE; Schema: public; Owner: pi
--

CREATE TABLE public.comment (
    id integer NOT NULL,
    question_id integer,
    answer_id integer,
    message text,
    submission_time timestamp without time zone,
    edited_count integer
);


ALTER TABLE public.comment OWNER TO pi;

--
-- Name: comment_id_seq; Type: SEQUENCE; Schema: public; Owner: pi
--

CREATE SEQUENCE public.comment_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.comment_id_seq OWNER TO pi;

--
-- Name: comment_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pi
--

ALTER SEQUENCE public.comment_id_seq OWNED BY public.comment.id;


--
-- Name: question; Type: TABLE; Schema: public; Owner: pi
--

CREATE TABLE public.question (
    id integer NOT NULL,
    submission_time timestamp without time zone,
    view_number integer,
    vote_number integer,
    title text,
    message text,
    image text
);


ALTER TABLE public.question OWNER TO pi;

--
-- Name: question_id_seq; Type: SEQUENCE; Schema: public; Owner: pi
--

CREATE SEQUENCE public.question_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.question_id_seq OWNER TO pi;

--
-- Name: question_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pi
--

ALTER SEQUENCE public.question_id_seq OWNED BY public.question.id;


--
-- Name: question_tag; Type: TABLE; Schema: public; Owner: pi
--

CREATE TABLE public.question_tag (
    question_id integer NOT NULL,
    tag_id integer NOT NULL
);


ALTER TABLE public.question_tag OWNER TO pi;

--
-- Name: tag; Type: TABLE; Schema: public; Owner: pi
--

CREATE TABLE public.tag (
    id integer NOT NULL,
    name text
);


ALTER TABLE public.tag OWNER TO pi;

--
-- Name: tag_id_seq; Type: SEQUENCE; Schema: public; Owner: pi
--

CREATE SEQUENCE public.tag_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.tag_id_seq OWNER TO pi;

--
-- Name: tag_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: pi
--

ALTER SEQUENCE public.tag_id_seq OWNED BY public.tag.id;


--
-- Name: answer id; Type: DEFAULT; Schema: public; Owner: pi
--

ALTER TABLE ONLY public.answer ALTER COLUMN id SET DEFAULT nextval('public.answer_id_seq'::regclass);


--
-- Name: comment id; Type: DEFAULT; Schema: public; Owner: pi
--

ALTER TABLE ONLY public.comment ALTER COLUMN id SET DEFAULT nextval('public.comment_id_seq'::regclass);


--
-- Name: question id; Type: DEFAULT; Schema: public; Owner: pi
--

ALTER TABLE ONLY public.question ALTER COLUMN id SET DEFAULT nextval('public.question_id_seq'::regclass);


--
-- Name: tag id; Type: DEFAULT; Schema: public; Owner: pi
--

ALTER TABLE ONLY public.tag ALTER COLUMN id SET DEFAULT nextval('public.tag_id_seq'::regclass);


--
-- Data for Name: answer; Type: TABLE DATA; Schema: public; Owner: pi
--

COPY public.answer (id, submission_time, vote_number, question_id, message, image) FROM stdin;
1	2017-04-28 16:49:00	4	1	You need to use brackets: my_list = []	\N
2	2017-04-25 14:42:00	35	1	Look it up in the Python docs	images/image2.jpg
54	2020-03-06 13:12:32	\N	24	ANSWER\r\n	\N
55	2020-03-08 09:24:55	\N	44	shsuh	\N
56	2020-03-09 11:35:15	\N	45	Elo	\N
6	2020-03-05 12:50:26	\N	1	Elo	\N
35	2020-03-06 00:54:42	\N	33	Stay at home.	\N
49	2020-03-06 02:06:16	\N	24	It really works guys	\N
50	2020-03-06 03:32:42	\N	37	U need to find it	\N
51	2020-03-06 04:00:15	\N	38	Start coding 	\N
38	2020-03-06 00:59:16	\N	33	wash your handsdwasadsad	\N
\.


--
-- Data for Name: comment; Type: TABLE DATA; Schema: public; Owner: pi
--

COPY public.comment (id, question_id, answer_id, message, submission_time, edited_count) FROM stdin;
1	0	\N	Please clarify the question as it is too vague!	2017-05-01 05:49:00	\N
2	\N	1	I think you could use my_list = list() as well.	2017-05-02 16:55:00	\N
3	33	\N	Nice question.	2020-03-06 01:38:25	\N
4	24	\N	:p	2020-03-06 01:41:01	\N
6	37	\N	Not True	2020-03-06 03:32:54	\N
7	38	\N	Good luck	2020-03-06 03:59:54	\N
11	33	\N	.....	2020-03-06 09:55:52	\N
12	44	\N	sdds	2020-03-08 09:25:01	\N
13	45	\N	eee	2020-03-09 11:35:22	\N
\.


--
-- Data for Name: question; Type: TABLE DATA; Schema: public; Owner: pi
--

COPY public.question (id, submission_time, view_number, vote_number, title, message, image) FROM stdin;
0	2017-04-28 08:29:00	29	7	How to make lists in Python?	I am totally new to this, any hints?	\N
2	2017-05-01 10:41:00	1364	57	Drawing canvas with an image picked with Cordova Camera Plugin	I'm getting an image from device and drawing a canvas with filters using Pixi JS. It works all well using computer to get an image. But when I'm on IOS, it throws errors such as cross origin issue, or that I'm trying to use an unknown format.\n	\N
44	2020-03-08 09:24:46	\N	\N	How to use sql?	            ......	\N
45	2020-03-09 11:34:55	\N	\N	how are you?	koronawirus\r\n            	\N
46	2020-03-17 20:32:53	\N	\N	Eluwina	Eloszka	\N
1	2017-04-29 09:19:00	15	10	Wordpress loading multiple jQuery Versions	I developed a plugin that uses the jquery booklet plugin (http://builtbywill.com/booklet/#/) this plugin binds a function to $ so I cann call $(".myBook").booklet();\n\nI could easy managing the loading order with wp_enqueue_script so first I load jquery then I load booklet so everything is fine.\n\nBUT in my theme i also using jquery via webpack so the loading order is now following:\n\njquery\nbooklet\napp.js (bundled file with webpack, including jquery)	images/image1.png
24	2020-03-05 12:52:41	\N	\N	How to use sql?	SELECT book FROM library\r\n            \r\n            	\N
37	2020-03-06 03:32:25	\N	\N	Jumanji	How to make it ?	\N
38	2020-03-06 03:59:24	\N	\N	Wonderful 2.0	How to learn programming?\r\n            	\N
40	2020-03-06 09:54:55	\N	\N	Jumanji 2.0	czesc            	\N
33	2020-03-05 22:30:10	\N	\N	Koronawirus	           \r\n            	\N
41	2020-03-06 13:11:45	\N	\N	How to use sql?	            aS	\N
\.


--
-- Data for Name: question_tag; Type: TABLE DATA; Schema: public; Owner: pi
--

COPY public.question_tag (question_id, tag_id) FROM stdin;
0	1
1	3
2	3
\.


--
-- Data for Name: tag; Type: TABLE DATA; Schema: public; Owner: pi
--

COPY public.tag (id, name) FROM stdin;
1	python
2	sql
3	css
\.


--
-- Name: answer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pi
--

SELECT pg_catalog.setval('public.answer_id_seq', 57, true);


--
-- Name: comment_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pi
--

SELECT pg_catalog.setval('public.comment_id_seq', 13, true);


--
-- Name: question_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pi
--

SELECT pg_catalog.setval('public.question_id_seq', 46, true);


--
-- Name: tag_id_seq; Type: SEQUENCE SET; Schema: public; Owner: pi
--

SELECT pg_catalog.setval('public.tag_id_seq', 3, true);


--
-- Name: answer pk_answer_id; Type: CONSTRAINT; Schema: public; Owner: pi
--

ALTER TABLE ONLY public.answer
    ADD CONSTRAINT pk_answer_id PRIMARY KEY (id);


--
-- Name: comment pk_comment_id; Type: CONSTRAINT; Schema: public; Owner: pi
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT pk_comment_id PRIMARY KEY (id);


--
-- Name: question pk_question_id; Type: CONSTRAINT; Schema: public; Owner: pi
--

ALTER TABLE ONLY public.question
    ADD CONSTRAINT pk_question_id PRIMARY KEY (id);


--
-- Name: question_tag pk_question_tag_id; Type: CONSTRAINT; Schema: public; Owner: pi
--

ALTER TABLE ONLY public.question_tag
    ADD CONSTRAINT pk_question_tag_id PRIMARY KEY (question_id, tag_id);


--
-- Name: tag pk_tag_id; Type: CONSTRAINT; Schema: public; Owner: pi
--

ALTER TABLE ONLY public.tag
    ADD CONSTRAINT pk_tag_id PRIMARY KEY (id);


--
-- Name: comment fk_answer_id; Type: FK CONSTRAINT; Schema: public; Owner: pi
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT fk_answer_id FOREIGN KEY (answer_id) REFERENCES public.answer(id);


--
-- Name: answer fk_question_id; Type: FK CONSTRAINT; Schema: public; Owner: pi
--

ALTER TABLE ONLY public.answer
    ADD CONSTRAINT fk_question_id FOREIGN KEY (question_id) REFERENCES public.question(id);


--
-- Name: question_tag fk_question_id; Type: FK CONSTRAINT; Schema: public; Owner: pi
--

ALTER TABLE ONLY public.question_tag
    ADD CONSTRAINT fk_question_id FOREIGN KEY (question_id) REFERENCES public.question(id);


--
-- Name: comment fk_question_id; Type: FK CONSTRAINT; Schema: public; Owner: pi
--

ALTER TABLE ONLY public.comment
    ADD CONSTRAINT fk_question_id FOREIGN KEY (question_id) REFERENCES public.question(id);


--
-- Name: question_tag fk_tag_id; Type: FK CONSTRAINT; Schema: public; Owner: pi
--

ALTER TABLE ONLY public.question_tag
    ADD CONSTRAINT fk_tag_id FOREIGN KEY (tag_id) REFERENCES public.tag(id);


--
-- PostgreSQL database dump complete
--

