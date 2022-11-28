SELECT lang.name,  SUM(pay.amount) FROM payments as pay
JOIN user_language as lang
ON pay.course_id = lang.id
GROUP BY lang.name
