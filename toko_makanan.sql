PGDMP     "                    z            toko_makanan    14.1    14.1     ?           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            ?           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            ?           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            ?           1262    32779    toko_makanan    DATABASE     p   CREATE DATABASE toko_makanan WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE = 'English_United States.1252';
    DROP DATABASE toko_makanan;
                postgres    false            ?            1259    32797    makanan    TABLE     ?   CREATE TABLE public.makanan (
    kode_makanan integer NOT NULL,
    nama character varying(31) NOT NULL,
    harga character varying(31) NOT NULL,
    jenis_makanan character varying(31) NOT NULL
);
    DROP TABLE public.makanan;
       public         heap    postgres    false            ?          0    32797    makanan 
   TABLE DATA           K   COPY public.makanan (kode_makanan, nama, harga, jenis_makanan) FROM stdin;
    public          postgres    false    209   ?       \           2606    32801    makanan makanan_pkey 
   CONSTRAINT     \   ALTER TABLE ONLY public.makanan
    ADD CONSTRAINT makanan_pkey PRIMARY KEY (kode_makanan);
 >   ALTER TABLE ONLY public.makanan DROP CONSTRAINT makanan_pkey;
       public            postgres    false    209            ?   '   x?326?Ȭ?J?42500??*??Vp??O?????? ?o?     