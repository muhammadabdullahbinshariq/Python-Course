CREATE TABLE students (
    student_id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    age INTEGER,
    grade_level INTEGER,
    gpa REAL,
    major TEXT
);

INSERT INTO students (student_id, name, age, grade_level, gpa, major) VALUES
(101, 'Alice Smith', 20, 2, 3.85, 'Computer Science'),
(102, 'Bob Jones', 22, 4, 2.90, 'Data Analytics'),
(103, 'Charlie Brown', 19, 1, 3.40, 'Information Technology'),
(104, 'Diana Prince', 21, 3, 3.95, 'Computer Science'),
(105, 'Evan Wright', 20, 2, 3.15, 'Data Analytics');

UPDATE students 
SET gpa = 3.10 
WHERE student_id = 102;

DELETE FROM students 
WHERE student_id = 103;

SELECT * 
FROM students 
WHERE major = 'Computer Science';

SELECT name, gpa, major 
FROM students 
WHERE gpa > 3.5;

SELECT name, major, gpa 
FROM students 
ORDER BY gpa DESC;

SELECT * 
FROM students 
ORDER BY name ASC;

SELECT major, AVG(gpa) AS average_gpa
FROM students
GROUP BY major;