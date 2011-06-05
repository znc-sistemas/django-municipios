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
-- Name: municipio; Type: TABLE; Schema: public; Owner: cadu; Tablespace: 
--

CREATE TABLE municipio (
    id integer NOT NULL,
    codigo_ibge character varying(16) NOT NULL,
    nome character varying(150) NOT NULL,
    uf_sigla character varying(2) NOT NULL,
    the_geom geometry NOT NULL,
    uf integer NOT NULL,
    nome_abreviado character varying,
    CONSTRAINT enforce_dims_the_geom CHECK ((ndims(the_geom) = 2)),
    CONSTRAINT enforce_geotype_the_geom CHECK (((geometrytype(the_geom) = 'MULTIPOLYGON'::text) OR (the_geom IS NULL))),
    CONSTRAINT enforce_srid_the_geom CHECK ((srid(the_geom) = 929102))
);


ALTER TABLE public.municipio OWNER TO cadu;

--
-- Name: municipio_pkey; Type: CONSTRAINT; Schema: public; Owner: cadu; Tablespace: 
--

ALTER TABLE ONLY municipio
    ADD CONSTRAINT municipio_pkey PRIMARY KEY (id);


--
-- Name: cod_ibge_index; Type: INDEX; Schema: public; Owner: cadu; Tablespace: 
--

CREATE UNIQUE INDEX cod_ibge_index ON municipio USING btree (codigo_ibge);

ALTER TABLE municipio CLUSTER ON cod_ibge_index;


--
-- Name: municipio_the_geom_id; Type: INDEX; Schema: public; Owner: cadu; Tablespace: 
--

CREATE INDEX municipio_the_geom_id ON municipio USING gist (the_geom);


--
-- Name: municipio_uf_id; Type: INDEX; Schema: public; Owner: cadu; Tablespace: 
--

CREATE INDEX municipio_uf_id ON municipio USING btree (uf);


--
-- Name: municipio_uf_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: cadu
--

ALTER TABLE ONLY municipio
    ADD CONSTRAINT municipio_uf_id_fkey FOREIGN KEY (uf_id) REFERENCES uf(id_ibge);


--
-- PostgreSQL database dump complete
--

