SELECT rr.REST_ID, ri.REST_NAME, ri.FOOD_TYPE, ri.FAVORITES, ri.ADDRESS, rr.SCORE
FROM REST_INFO ri inner join (SELECT REST_ID, round(AVG(REVIEW_SCORE),2) as SCORE from REST_REVIEW group by REST_ID)rr
on ri.REST_ID = rr.REST_ID 
where ri.ADDRESS Like '서울%'
order by rr.SCORE desc, ri.FAVORITES desc