
SELECT ROUND((total_money * 0.005)) AS salary_per_month FROM staff_info
ALTER TABLE staff_info
ADD salary_per_year INTEGER
  DEFAULT 0
SELECT * FROM staff_info
UPDATE staff_info
SET ticket_sold_per_month = ticket_sold / 12
SELECT (total_money / ticket_sold) AS per_ticket_avg_price FROM staff_info
ALTER TABLE staff_info
ADD per_ticket_avg_price FLOAT
ALTER TABLE staff_info
ADD ticket_sold_per_month INTEGER
SELECT * FROM joined_info