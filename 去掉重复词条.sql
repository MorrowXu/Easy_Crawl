CREATE VIEW view_to_id AS SELECT
	id
FROM
	`baike_key`
GROUP BY
	key_word;

SELECT
	*
FROM
	view_to_id;

CREATE TABLE view_to_table AS SELECT
	*
FROM
	baike_key
WHERE
	id IN (SELECT id FROM `view_to_id`);

SELECT
	*
FROM
	`view_to_table`;
