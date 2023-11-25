CREATE TABLE PC_SPECS (
  id VARCHAR PRIMARY KEY,
  operating_system VARCHAR NOT NULL,
  cpu_architecture VARCHAR NOT NULL,
  cpu_type VARCHAR NOT NULL,
  cpu_cores VARCHAR NOT NULL,
  ram_size VARCHAR NOT NULL
);

CREATE TABLE BUBBLESORT (
  sample_size VARCHAR NOT NULL,
  run_time VARCHAR NOT NULL,
  pc_specs_id VARCHAR NOT NULL,
  FOREIGN KEY (pc_specs_id) REFERENCES PC_SPECS(id)
);

CREATE TABLE MERGESORT (
  sample_size VARCHAR NOT NULL,
  run_time VARCHAR NOT NULL,
  pc_specs_id VARCHAR NOT NULL,
  FOREIGN KEY (pc_specs_id) REFERENCES PC_SPECS(id)
);

CREATE TABLE QUICKSORT (
  sample_size VARCHAR NOT NULL,
  run_time VARCHAR NOT NULL,
  pc_specs_id VARCHAR NOT NULL,
  FOREIGN KEY (pc_specs_id) REFERENCES PC_SPECS(id)
);

CREATE OR REPLACE VIEW AllBubbleSortInfo AS
SELECT b.sample_size, b.run_time, p.operating_system, p.cpu_architecture, p.cpu_type, p.cpu_cores, p.ram_size FROM BUBBLESORT b
JOIN PC_SPECS p ON p.id = b.pc_specs_id;

CREATE OR REPLACE VIEW AllMergeSortInfo AS
SELECT b.sample_size, b.run_time, p.operating_system, p.cpu_architecture, p.cpu_type, p.cpu_cores, p.ram_size FROM MERGESORT b
JOIN PC_SPECS p ON p.id = b.pc_specs_id;

CREATE OR REPLACE VIEW AllQuickSortInfo AS
SELECT b.sample_size, b.run_time, p.operating_system, p.cpu_architecture, p.cpu_type, p.cpu_cores, p.ram_size FROM QUICKSORT b
JOIN PC_SPECS p ON p.id = b.pc_specs_id;

SELECT * FROM PC_SPECS;
SELECT * FROM BUBBLESORT;
SELECT * FROM MERGESORT;
SELECT * FROM QUICKSORT;

SELECT * FROM AllBubbleSortInfo;
SELECT * FROM AllMergeSortInfo;
SELECT * FROM AllQuickSortInfo;

SELECT b.sample_size, b.run_time, p.operating_system, p.cpu_architecture, p.cpu_type, p.cpu_cores, p.ram_size FROM BUBBLESORT b
JOIN PC_SPECS p ON p.id = b.pc_specs_id;


COPY PC_SPECS FROM 'C:/Users/andre/Desktop/Pastas/Programas/CESUPA/Probabilidade e Estatistica/VS Code/Projeto Giras/src/results/specs.csv'
DELIMITER ',' CSV HEADER;


COPY BUBBLESORT FROM 'C:/Users/andre/Desktop/Pastas/Programas/CESUPA/Probabilidade e Estatistica/VS Code/Projeto Giras/src/results/bubble.csv'
DELIMITER ',' CSV HEADER;


COPY MERGESORT FROM 'C:/Users/andre/Desktop/Pastas/Programas/CESUPA/Probabilidade e Estatistica/VS Code/Projeto Giras/src/results/merge.csv'
DELIMITER ',' CSV HEADER;


COPY QUICKSORT FROM 'C:/Users/andre/Desktop/Pastas/Programas/CESUPA/Probabilidade e Estatistica/VS Code/Projeto Giras/src/results/quick.csv'
DELIMITER ',' CSV HEADER;

DELETE FROM PC_SPECS;
DELETE FROM QUICKSORT;
DELETE FROM MERGESORT;
DELETE FROM BUBBLESORT;