create or replace table NYC_filtered_data.final_table as
(
  select 
  dtd.pickup_weekday,
  dtd.pickup_year,
  dtd.dropoff_weekday,
  dtd.dropoff_year,
  ft.fare_amount,
  ft.extra,
  ft.mta_tax,
  ft.tip_amount,
  ft.tolls_amount,
  ft.improvement_surcharge,
  ft.total_amount,
  ft.trip_distance,
  vendors.Vendor_name,
  dtd.pickup_time,
  dtd.pickup_date,
  dtd.dropoff_time,
  dtd.dropoff_date,
  dtd.pickup_month,
  dtd.dropoff_month,
  pt.payment_type_name,
  pkd.pickup_longitude,
  pkd.pickup_latitude,
  rcds.rate_code_name,
  df.dropoff_longitude,
  df.dropoff_latitude
  from `NYC_filtered_data.fact_table` as ft
  join NYC_filtered_data.vendors on vendors.Vendor_id = ft.VendorID
  join (SELECT distinct * FROM `NYC-data-engineering-391611.NYC_filtered_data.datetime_details`) as dtd on dtd.datetime_id = ft.datetime_id
  join NYC_filtered_data.pickup_details as pkd on pkd.pickup_id = ft.pickup_id
join (SELECT distinct * FROM `NYC-data-engineering-391611.NYC_filtered_data.ratecodes`) as rcds on rcds.rate_code_id = ft.RatecodeID
  join (SELECT distinct * FROM `NYC-data-engineering-391611.NYC_filtered_data.payment_types`) as pt on pt.payment_type_id = ft.payment_type
  join (SELECT distinct * FROM `NYC-data-engineering-391611.NYC_filtered_data.dropoff_details`) as df on df.dropoff_id = ft.dropoff_id
);
