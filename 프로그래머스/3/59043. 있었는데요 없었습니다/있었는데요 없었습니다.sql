-- 코드를 입력하세요
SELECT t1.ANIMAL_ID,
        t1.NAME

    FROM ANIMAL_INS as t1
    INNER JOIN ANIMAL_OUTS as t2
    ON t1.ANIMAL_ID	= t2.ANIMAL_ID
    WHERE t1.DATETIME > t2.DATETIME
    ORDER BY t1.DATETIME