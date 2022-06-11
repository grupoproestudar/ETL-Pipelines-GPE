/*TESTING QUERIES FROM  PYTHON*/
SELECT 
    *
FROM
    GPE_DATABASE.Applicants;
    
SELECT 
    *
FROM
    GPE_DATABASE.Students;

SELECT 
    *
FROM
    Volunteers;
    
SELECT 
    *
FROM
    Exams;

/*DELETING RECORDS FROM TABLE*/
DELETE  FROM GPE_DATABASE.Applicants;
DELETE FROM Volunteers;
DELETE FROM Students;

/*DELETING COLUMNS FROM TABLE*/
ALTER TABLE Applicants
DROP COLUMN people_living_with_you,
DROP COLUMN avg_income
;


/* ALTERING TABLES PROPERTIES*/
ALTER TABLE Students
ALTER start_date set default null,
ALTER end_date set default null,
ALTER volunteer_id set default null
;

/*INSERTING NEW RECORDS INTO TABLES*/
-- VOLUNTEERS TABLES
INSERT INTO Volunteers VALUES (1, 'MURILLO PINOTTI', null, null, 'Administração Pública', 'UNESP',8,1, null, null);
INSERT INTO Volunteers VALUES (2, 'CARLOS HENRIQUE', null, null, 'Química','UNESP',4,2, '2017-01-01', null);
INSERT INTO Volunteers VALUES (3, 'RODOLFO LIMA', 'naruto.lima.silva@usp.br','16 997230422',
							'Eng. Materiais e Manufatura', 'USP',11,4, '2018-06-05', null);

-- TEAM TABLES
insert into GPE_DATABASE.Team (team_name) 
values	('Portuguese'),
		('Mathematics'),
        ('Physics'),
        ('Chemistry'),
        ('Biology'),
        ('History'),
        ('Geography'),
        ('Board'),
        ('Markting'),
        ('Assistance'),
        ('IT'),
        ('Pedagogy')
;

-- ROLES TABLE
insert into GPE_DATABASE.Roles (role_name)
	values ('Principal'),
			('Vice Principal'),
            ('Teacher'),
            ('Coordinator'),
            ('Support')
;

/*UPDATING VALUES*/
UPDATE GPE_DATABASE.Students
SET NSE = 0.3825, start_date = 2021-01-01 , end_date = 2022-01-01, volunteer_id = 2
WHERE student_code = 100222;