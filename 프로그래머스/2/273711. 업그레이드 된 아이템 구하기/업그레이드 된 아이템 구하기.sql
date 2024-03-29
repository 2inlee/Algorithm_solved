SELECT CHILD.ITEM_ID, CHILD.ITEM_NAME, CHILD.RARITY
FROM ITEM_INFO AS PARENT
JOIN ITEM_TREE AS IT ON IT.PARENT_ITEM_ID = PARENT.ITEM_ID
JOIN ITEM_INFO AS CHILD ON IT.ITEM_ID = CHILD.ITEM_ID
WHERE PARENT.RARITY = 'RARE'
ORDER BY CHILD.ITEM_ID DESC