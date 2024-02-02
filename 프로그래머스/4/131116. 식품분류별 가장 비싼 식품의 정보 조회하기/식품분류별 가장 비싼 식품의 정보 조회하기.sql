SELECT CATEGORY, PRICE AS MAX_PRICE, PRODUCT_NAME
FROM FOOD_PRODUCT fp1
WHERE CATEGORY IN ('과자', '국', '김치', '식용유')
AND PRICE = (
    SELECT MAX(fp2.PRICE)
    FROM FOOD_PRODUCT fp2
    WHERE fp2.CATEGORY = fp1.CATEGORY
)
ORDER BY PRICE DESC;