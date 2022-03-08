/*
-- create tables
CREATE TABLE name_table (
  StudentID TEXT PRIMARY KEY,
  Name TEXT NOT NULL
);

CREATE TABLE mark_table (
  StudentID TEXT PRIMARY KEY,
  Total_marks INTEGER NOT NULL
);

-- insert some values
INSERT INTO name_table VALUES ('V001', 'Abe');
INSERT INTO name_table VALUES ('V002', 'Abhay');
INSERT INTO name_table VALUES ('V003', 'Acelin');
INSERT INTO name_table VALUES ('V004', 'Adelphos');

INSERT INTO mark_table VALUES ('V001', 95);
INSERT INTO mark_table VALUES ('V002', 80);
INSERT INTO mark_table VALUES ('V003', 74);
INSERT INTO mark_table VALUES ('V004', 81);
*/

-- Q1-a)
SELECT m.StudentID, n.Name
FROM mark_table m, name_table n
WHERE m.StudentID = n.StudentID AND
      m.Total_marks > (SELECT m1.Total_marks
                       FROM mark_table m1
                       WHERE m1.StudentID = 'V002');
