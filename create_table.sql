SELECT * FROM user_course
SELECT get_course_id_by_email('aman@mail.ru');


CREATE TABLE payments
	(
		id SERIAL PRIMARY KEY,
		course_id INTEGER REFERENCES user_course(id),
		amount INTEGER,
		pay_date DATE
	);
	

CREATE PROCEDURE id_payment()