-- Top prospects

SELECT
lead_id,
annual_revenue,
credit_score,
annual_revenue * credit_score AS revenue_score
FROM prospects
ORDER BY revenue_score DESC
LIMIT 100;


-- Conversion rate by industry

SELECT
industry_score,
AVG(converted) AS conversion_rate
FROM prospects
GROUP BY industry_score
ORDER BY conversion_rate DESC;


-- Revenue ranking

SELECT
lead_id,
annual_revenue,
RANK() OVER (ORDER BY annual_revenue DESC) AS revenue_rank
FROM prospects;