-- displays the average temperature (Fahrenheit) by city ordered by temperature (descending)
CREATE TABLE avg_temperatures (
  city VARCHAR(255) NOT NULL,
  avg_temp FLOAT NOT NULL
);
INSERT INTO avg_temperatures (city, avg_temp) VALUES
  ('Chandler', 72.8627),
  ('Gilbert', 71.8088),
  ('Pismo beach', 71.5147),
  ('San Francisco', 71.4804),
  ('Sedona', 70.7696),
  ('Phoenix', 70.5882),
  ('Oakland', 70.5637),
  ('Sunnyvale', 70.5245),
  ('Chicago', 70.4461),
  ('San Diego', 70.1373),
  ('Glendale', 70.1225),
  ('Sonoma', 70.0392),
  ('Yuma', 69.3873),
  ('San Jose', 69.2990),
  ('Tucson', 69.0245),
  ('Joliet', 68.6716),
  ('Naperville', 68.1029),
  ('Tempe', 67.0441),
  ('Peoria', 66.5392);
