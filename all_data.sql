-- SELECT * FROM user_students


SELECT * FROM user_course as course
INNER JOIN user_students as students
ON course.students_id = students.id
INNER JOIN user_mentor as mentor
ON course.mentor_id = mentor.id


