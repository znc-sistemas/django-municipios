--
-- PostgreSQL database dump
--

SET client_encoding = 'UTF8';
SET standard_conforming_strings = off;
SET check_function_bodies = false;
SET client_min_messages = warning;
SET escape_string_warning = off;

SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: uf; Type: TABLE; Schema: public; Owner: cadu; Tablespace: 
--

CREATE TABLE uf (
    id_ibge integer NOT NULL,
    uf character varying(2) NOT NULL,
    nome character varying(20) NOT NULL,
    regiao character varying(20) NOT NULL,
    the_geom geometry NOT NULL,
    CONSTRAINT enforce_dims_the_geom CHECK ((ndims(the_geom) = 2)),
    CONSTRAINT enforce_geotype_the_geom CHECK (((geometrytype(the_geom) = 'MULTIPOLYGON'::text) OR (the_geom IS NULL))),
    CONSTRAINT enforce_srid_the_geom CHECK ((srid(the_geom) = 929102))
);


ALTER TABLE public.uf OWNER TO cadu;

--
-- Name: codigo_uf_pkey; Type: CONSTRAINT; Schema: public; Owner: cadu; Tablespace: 
--

ALTER TABLE ONLY uf
    ADD CONSTRAINT codigo_uf_pkey PRIMARY KEY (id_ibge);


--
-- Name: ibge_id_index; Type: INDEX; Schema: public; Owner: cadu; Tablespace: 
--

CREATE INDEX ibge_id_index ON uf USING btree (id_ibge);

ALTER TABLE uf CLUSTER ON ibge_id_index;


--
-- Name: uf_index; Type: INDEX; Schema: public; Owner: cadu; Tablespace: 
--

CREATE INDEX uf_index ON uf USING btree (uf);


--
-- Name: uf_the_geom_id; Type: INDEX; Schema: public; Owner: cadu; Tablespace: 
--

CREATE INDEX uf_the_geom_id ON uf USING gist (the_geom);


--
-- PostgreSQL database dump complete
--

