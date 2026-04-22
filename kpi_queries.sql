SELECT 
  `Shipment Mode`,
  AVG(`Unit Price`) AS avg_unit_price
FROM `smartsupply-ai.smartsupply.shipments`
GROUP BY `Shipment Mode`
ORDER BY avg_unit_price DESC;
SELECT 
  Country,
  AVG(DATE_DIFF(`Delivered to Client Date`, `Scheduled Delivery Date`, DAY)) AS avg_delay
FROM `smartsupply-ai.smartsupply.shipments`
GROUP BY Country
ORDER BY avg_delay DESC;