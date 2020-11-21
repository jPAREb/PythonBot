------------------------------
--          TAULES          --
------------------------------
------------------------------
--          usuaris         --
--          tweets          --
--      tweets normals      --
--      tweets usuaris      --
--      tweets resposta     --
--         seguidors        --
--         unfollow         --
--       estadistiques      --
--      usuaris blocats     --
------------------------------


\c template1
drop DATABASE bandera_cat;
create DATABASE bandera_cat;
\c bandera_cat

--RELACIO ID USUARIS I NOM [1]
CREATE TABLE usuaris(
    id VARCHAR PRIMARY KEY,
    Nom varchar
);

--ES GUARDEN ELS TWEETS [2]
create TABLE tweets(
    id VARCHAR PRIMARY KEY NOT NULL,
    missatge VARCHAR
);

--TWEETS NORMALS [3]
CREATE SEQUENCE id_tw_normals;
CREATE TABLE "tweets normals"(
    id INT NOT NULL DEFAULT NEXTVAL('id_tw_normals'), 
    tweet VARCHAR,
    "data" DATE,
    "hora" TIME,
    FOREIGN KEY (tweet) REFERENCES tweets(id)
);

--RELACIO TWEETS QUE EM RESPONEN DIRECTAMENT O M'ETIQUETEN [4]
CREATE SEQUENCE id_tw_usuaris;
create TABLE "tweets usuaris"(
    id INT NOT NULL DEFAULT NEXTVAL('id_tw_usuaris'), 
    tweet VARCHAR,
    usuari VARCHAR,
    "data" DATE,
    "hora" TIME,
    FOREIGN KEY (usuari) REFERENCES usuaris(id),
    FOREIGN KEY (tweet) REFERENCES tweets(id)
);

--TWEETS EN QUE EL BOT RESPON [5]
CREATE SEQUENCE id_tw_resposta;
CREATE TABLE "tweets resposta"(
    id INT NOT NULL DEFAULT NEXTVAL('id_tw_resposta'),
    tweet VARCHAR,
    "usuari resposta" VARCHAR,
    "data" DATE,
    "hora" TIME,
    FOREIGN KEY (tweet) REFERENCES tweets(id),
    FOREIGN KEY ("usuari resposta") REFERENCES usuaris(id)
);

--SEGUIDORS ACTUALS [6]
CREATE SEQUENCE id_seguidors;
create TABLE seguidors(
    id INT NOT NULL DEFAULT NEXTVAL('id_seguidors'),
    usuari VARCHAR,
    "data" DATE,
    hora TIME,
    FOREIGN KEY (usuari) REFERENCES usuaris(id)
);

--GENT QUE HA DEIXAT DE SEGUIR [7]
CREATE SEQUENCE id_unfollow;
create TABLE unfollow(
    id INT NOT NULL DEFAULT NEXTVAL('id_unfollow'),
    usuari VARCHAR,
    "data" DATE,
    hora TIME,
    FOREIGN KEY (usuari) REFERENCES usuaris(id)
);

--RETWEETS I LIKES PER TWEET [8]
CREATE SEQUENCE id_estadistiques;
create TABLE estadistiques(
    id INT NOT NULL DEFAULT NEXTVAL('id_estadistiques'),
    "id tweet" VARCHAR,
    "m'agrada" INTEGER,
    "retweet" INTEGER,
    "data" DATE,
    "hora" TIME,
    FOREIGN KEY ("id tweet") REFERENCES tweets(id)
);

--USUARIS BLOCATS [9]
CREATE SEQUENCE id_usu_block;
CREATE TABLE "usuaris blocats"(
    id INT NOT NULL DEFAULT NEXTVAL('id_usu_block'),
    usuari VARCHAR,
    motiu VARCHAR,
    "data" DATE,
    hora TIME,
    FOREIGN KEY (usuari) REFERENCES usuaris(id)
);

CREATE SEQUENCE paraules_trending;
CREATE TABLE "paraules trending"(
    id INT NOT NULL DEFAULT NEXTVAL('paraules_trending'),
    paraula VARCHAR
);


------------------------------
--          TAULES          --
------------------------------
------------------------------
--          usuaris         --
--          tweets          --
--      tweets normals      --
--      tweets usuaris      --
--      tweets resposta     --
--         seguidors        --
--         unfollow         --
--       estadistiques      --
--      usuaris blocats     --
------------------------------
