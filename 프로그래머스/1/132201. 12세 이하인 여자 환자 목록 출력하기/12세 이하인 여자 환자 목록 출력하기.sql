SELECT 
    PT_NAME, 
    PT_NO, 
    GEND_CD, 
    AGE, 
    IF(TLNO IS NULL, 'NONE', TLNO) AS TLNO
    -- IF(조건문, 참일 때, 참이 아닐 때) AS TLNO -> 해당 조건을 적용한 걸 다시 TLNO 컬럼에 넣음
FROM 
    PATIENT
WHERE 
    AGE <= 12 AND GEND_CD = 'W'
ORDER BY 
    AGE DESC, 
    PT_NAME ASC;
