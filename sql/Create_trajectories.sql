CREATE VIEW view_trajectories AS
SELECT user_id, COUNT(user_id) AS counts FROM fotografia GROUP BY user_id ORDER BY counts DESC

SELECT COUNT(*) FROM view_trajectories

select * from view_trajectories
LIMIT 1000

COPY (
	  SELECT user_id, latitud, logitud, fecha, titulo, nrolikes, url
	  FROM fotografia AS t1
	  WHERE t1.user_id IN (
	  			SELECT user_id FROM view_trajectories
	  			LIMIT 1000
	  		 )
	  ORDER BY t1.user_id

	 ) TO 'D:\points_trajectory.csv' DELIMITER ',' csv
HEADER;
