CREATE TABLE results (
  sorting_type varchar,
  sample_size int,
  runtime varchar
);

COPY results
FROM 'C:\Users\andre\Desktop\Pastas\Programas\CESUPA\Probabilidade e Estatistica\VS Code\Projeto Giras\src\results\output.csv' WITH DELIMITER ',' CSV HEADER;

SELECT *
FROM results;