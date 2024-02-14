SELECT
    HOUR(DATETIME) AS HOUR,
    COUNT(*) AS 'COUNT'
FROM ANIMAL_OUTS
WHERE DATE_FORMAT(DATETIME, '%H-%i') BETWEEN '08:59' AND '19:59'
GROUP BY HOUR
ORDER BY HOUR