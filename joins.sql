SELECT 
  Vendor,
  DATE_DIFF(`Delivered to Client Date`, `Scheduled Delivery Date`, DAY) AS delay_days
FROM `smartsupply-ai.smartsupply.shipments`;