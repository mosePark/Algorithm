-- 코드를 입력하세요
SELECT t1.REST_ID,
        t1.REST_NAME,
        t1.FOOD_TYPE,
        t1.FAVORITES,
        t1.ADDRESS,
        ROUND(AVG(t2.REVIEW_SCORE), 2) AS 'SCORE'
    FROM REST_INFO as t1
    INNER JOIN REST_REVIEW as t2
    ON t1.REST_ID = t2.REST_ID
    WHERE t1.ADDRESS LIKE '서울%'
    GROUP BY t1.REST_ID
    ORDER BY SCORE DESC, FAVORITES DESC;