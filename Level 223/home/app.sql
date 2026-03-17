
SELECT DISTINCT payment_date FROM payment
ORDER BY datetime, salary_per_year DESC
JOIN staff
	ON staff.email = staff_info.email

UPDATE staff_info
	SET datetime = staff.last_update

UPDATE staff_info
SET datetime = staff.last_update
FROM staff
WHERE staff.email = staff_info.email

ALTER TABLE staff_info
ADD datetime TEXT