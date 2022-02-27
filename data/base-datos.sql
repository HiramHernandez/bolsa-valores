-- Database: bolsavalores

-- DROP DATABASE bolsavalores;

CREATE DATABASE bolsavalores
    WITH 
    OWNER = postgres
    ENCODING = 'UTF8'
    LC_COLLATE = 'en_US.utf8'
    LC_CTYPE = 'en_US.utf8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;



-- Table: public.empresas

-- DROP TABLE public.empresas;

CREATE TABLE IF NOT EXISTS public.empresas
(
    guid uuid NOT NULL DEFAULT uuid_generate_v1(),
    name character varying(50) COLLATE pg_catalog."default",
    description character varying(100) COLLATE pg_catalog."default",
    simbolo character varying(10) COLLATE pg_catalog."default",
    valores_mercado character varying(10)[] COLLATE pg_catalog."default",
    CONSTRAINT empresas_pkey PRIMARY KEY (guid)
)

TABLESPACE pg_default;

ALTER TABLE public.empresas
    OWNER to postgres;