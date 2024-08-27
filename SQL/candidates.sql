CREATE TABLE candidates (
    "First Name" TEXT,
    "Last Name" TEXT,
    "Email" TEXT,
    "Application Date" DATE,
    "Country" TEXT,
    "YOE" INTEGER,
    "Seniority" TEXT,
    "Technology" TEXT,
    "Code Challenge Score" INTEGER,
    "Technical Interview Score" INTEGER);

COPY candidates FROM 'tu/ruta/hacia/el/archivo/candidates.csv' DELIMITER ';' CSV HEADER;