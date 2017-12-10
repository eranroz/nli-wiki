/* database to store page slices and their transcriptions */
CREATE TABLE pageSlices (
	id int(10) unsigned NOT NULL AUTO_INCREMENT PRIMARY KEY,
	book varchar(512),
	page int(8) unsigned,
	sliceidx int(8) unsigned,
	x int unsigned,
	y int unsigned,
	w int unsigned,
	h int unsigned,
	transcribe BLOB
)

