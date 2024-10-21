-- print the table description for first_table in th hbtn_0c_0 database
SELECT
	t.TABLE_NAME AS 'Table',
	CONCAT('CREATE TABLE `', t.TABLE_NAME, '` (',
		GROUP_CONCAT(CONCAT('`', c.COLUMN_NAME, '` ', c.COLUMN_TYPE) ORDER BY c.ORDINAL_POSITION SEPARATOR ', '),
		') ENGINE=', t.ENGINE, ' DEFAULT CHARSET=', SUBSTRING_INDEX(t.TABLE_COLLATION, '_', 1)) AS 'Create Table'
FROM
	information_schema.TABLES t
JOIN
	information_schema.COLUMNS c
ON
	t.TABLE_SCHEMA = 'hbtn_0c_0' AND t.TABLE_NAME = 'first_table'
WHERE
	c.TABLE_SCHEMA = 'hbtn_0c_0' AND c.TABLE_NAME = 'first_table'
GROUP BY
	t.TABLE_NAME, t.ENGINE, t.TABLE_COLLATION;
