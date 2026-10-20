-- 1. Overall Late Delivery Rate

SELECT
    COUNT(*) AS total_orders,
    SUM(CASE
        WHEN Late_delivery_risk = 1 THEN 1
        ELSE 0
    END) AS late_orders,
    ROUND(
        SUM(CASE
            WHEN Late_delivery_risk = 1 THEN 1
            ELSE 0
        END) * 100.0 / COUNT(*),
        2
    ) AS late_delivery_rate
FROM cleaned_supply_chain;