SELECT
	X.*
FROM
	(
		SELECT
			key_word,
			id,
			COUNT(*) num
		FROM
			`baike_key`
		GROUP BY
			key_word
	) AS X
WHERE
	X.num > 1
ORDER BY
	num;
