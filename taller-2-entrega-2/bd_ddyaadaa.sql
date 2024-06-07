CREATE TABLE IF NOT EXISTS registros_mh_ceclsgo (
	id_insert int AUTO_INCREMENT NOT NULL UNIQUE, --valor automatico generado por la BD
	id_grupo int NOT NULL, 		--el numero del grupo, por ejemplo 11
	mh_nombre text NOT NULL, 	-- el nombre de la MH por ejemplo 'Bat Algorithm Optimization'
	num_ejecucion int NOT NULL, 	-- valor que ira de 1 a 31, dependiendo de la ejecicion que este registrando
	num_iteracion int NOT NULL, 	--valor que ira de 1 a 5000, dependiendo de la iteracion que este registrando
	num_soluciones int NOT NULL, 	-- valor de soluciones conisderadas para la MH, por ejemplo 30
	seed int NOT NULL, 		-- valor numerico que representa la semilla, se utiliza el valor en tiempo ms
	fitness double NOT NULL, 	--valor del mejor fitness que va encontrando la MH por cada iteracion
	tiempo_ms text NOT NULL, 	--valor del tiempo al terminar cada iteracion
	cec_funcion int NOT NULL, 	-- numero de la funcion de la cec que se esta resolviendo, valor ira de 1 a 15
	cec_bks double NOT NULL, 	-- valor del optimo a encontrar (bks = best know solution), se obtiene de los valores de la cec
	cec_upper double NOT NULL,	-- valor del espacio de busqueda superior, valor lo entrega cec
	cec_lower double NOT NULL,	-- valor del espacio de busqueda inferior, valor lo entrega cec
	cec_dimension double NOT NULL,	-- cantidad de valores que requiere la funcion para trabajar, valor lo entrega cec
	mh_param_1 double NOT NULL,	-- valor que utilizaran para el parametro 1 de la MH
	mh_param_1_des text NOT NULL,	-- nombre y explicacion del parametro que se esta guardando, por ejemplo "frecuencia, valor usado por los murcielagos para la busqueda"
	mh_param_2 double NOT NULL,	-- valor utilizado para el parametro 2 de la MH
	mh_param_2_des text NOT NULL,	-- nombre y explicacion del parametro 2, por ejemplo "radio, valor usado usado por los murcielagos para...."
	mh_param_3 double,		-- misma logica anterior hasta el parametro 8
	mh_param_3_des text,
	mh_param_4 double,
	mh_param_4_des text,
	mh_param_5 double,
	mh_param_5_des text,
	mh_param_6 double,
	mh_param_6_des text,
	mh_param_7 double,
	mh_param_7_des text,
	mh_param_8 double,
	mh_param_8_des text,
	PRIMARY KEY (id_insert)
);