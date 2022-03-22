DROP DATABASE if exists bikes;
CREATE DATABASE bikes WITH ENCODING 'UTF8';
\connect bikes;

CREATE TYPE USERTYPE AS ENUM ('Subscriber', 'Customer');
CREATE TYPE GENDER AS ENUM (0, 1, 2);
CREATE TABLE rawdata(
  tripduration            INT,
  starttime               TIMESTAMP,
  stoptime                TIMESTAMP,
  start_station_id        SMALLINT,
  start_station_name      VARCHAR(255),
  start_station_latitude  FLOAT(8),
  start_station_longitude FLOAT(8),
  end_station_id          SMALLINT,
  end_station_name        VARCHAR(255),
  end_station_latitude    FLOAT(8),
  end_station_longitude   FLOAT(8) ,
  bike_id                 INT,
  user_type               USERTYPE,
  birth_year              SMALLINT,
  gender                  GENDER
);