SELECT EMP_NO, EMP_NAME, GRADE,
       CASE 
         WHEN GRADE = 'S' THEN SAL * 0.2
         WHEN GRADE = 'A' THEN SAL * 0.15
         WHEN GRADE = 'B' THEN SAL * 0.1
         WHEN GRADE = 'C' THEN SAL * 0
       END AS BONUS
FROM (
    SELECT 
        t12.EMP_NO, 
        t12.EMP_NAME, 
        t12.SAL,
        CASE 
          WHEN SUM(t3.SCORE)/2 >= 96 THEN 'S'
          WHEN SUM(t3.SCORE)/2 >= 90 THEN 'A'
          WHEN SUM(t3.SCORE)/2 >= 80 THEN 'B'
          ELSE 'C'
        END AS GRADE
    FROM (
        SELECT 
            t2.DEPT_ID, 
            t2.DEPT_NAME_KR, 
            t2.DEPT_NAME_EN, 
            t2.LOCATION, 
            t1.EMP_NO, 
            t1.EMP_NAME, 
            t1.POSITION, 
            t1.EMAIL, 
            t1.COMP_TEL, 
            t1.HIRE_DATE, 
            t1.SAL
        FROM HR_EMPLOYEES AS t1
        JOIN HR_DEPARTMENT AS t2
          ON t1.DEPT_ID = t2.DEPT_ID
    ) AS t12
    JOIN HR_GRADE AS t3
      ON t12.EMP_NO = t3.EMP_NO
    GROUP BY t12.EMP_NO
) AS sub;
