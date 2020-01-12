
/* ___________________________________________________________________ */
/* script de base datos para DB_bus para la extracción de trayectorias */
/* ___________________________________________________________________ */

/* Atributos de la tabla monitoring */
Name:  public."Process_monitoring"
Attributes: id,  date, time, lap, latitud, longitud, velocity, navigation, vehicle_id_id


/* Seleccionar vehiculo por dia */
SELECT * FROM public."Process_monitoring"
WHERE date = '2019-03-03' AND vehicle_id_id = 'CC34'

/* Seleccionar todas las fechas presentas en la tabla sin repetición */
SELECT DISTINCT date FROM public."Process_monitoring"
ORDER BY date


38 empresas aproximadamentes en la provincia de cusco. 16 es el aprox 42.1 % de todas las conseciones para el servicio transporte público.


/* Exportar consulta sql a un file csv x dia */
COPY (
	  SELECT * FROM public."Process_monitoring"
	  WHERE date >= '2019-04-01' AND date <= '2019-04-30'
	  ORDER BY date, vehicle_id_id, time
	  LIMIT 60000
	 ) TO 'D:\DataSets\Pregrado\BD_Bus\csv_files\Abril19_ordenado_X_dia_60000.csv' DELIMITER ',' csv
	 
HEADER;


/* Exportar consulta sql a un file csv x vehiculo */
COPY (
	  SELECT * FROM public."Process_monitoring"
	  WHERE date >= '2019-04-01' AND date <= '2019-04-30'
	  ORDER BY vehicle_id_id, date, time
	 ) TO 'D:\DataSets\Pregrado\BD_Bus\Abril19\Abril19.csv' DELIMITER ',' csv
HEADER;

COPY 11706236 rows, Query returned successfully in 1 min 7 secs.


/* Exportar consulta sql a un file csv x empresa */

COPY (
	 SELECT user_id, latitud, logitud,fecha FROM fotografia ORDER BY user_id,fecha
	 ) TO 'D:\tuples_points2.csv' DELIMITER ',' csv
HEADER;

-- contar numero de puntos de trayectoria (falta ordenar de mayor a menor)
WITH results AS (SELECT COUNT(1) AS contador FROM fotografia GROUP BY user_id)
SELECT contador, COUNT(contador) from results GROUP BY contador

SELECT COUNT(user_id) FROM fotografia 


