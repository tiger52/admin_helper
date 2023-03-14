--- проверить статус лицензии
select GET_COMPLIANCE_STATUS();

--- список таблиц и занимаемого места
select anchor_table_name, ROUND(SUM(used_bytes) / ( 1024^3 ), 4) AS used_compressed_gb from column_storage where anchor_table_name in (select table_name from v_catalog.tables) GROUP by anchor_table_name order by used_compressed_gb;

select schema_name as table_schema,
       anchor_table_name as table_name,
       round(sum(used_bytes)/(1024^3), 2) as used_gb
from v_monitor.storage_containers sc
join v_catalog.projections p
     on sc.projection_id = p.projection_id
group by table_schema,
         table_name
order by used_gb desc;


select schema_name as table_schema,
       anchor_table_name as table_name,
       round(sum(used_bytes)/(1024^3), 2) as used_gb
from v_monitor.storage_containers sc
join v_catalog.projections p
     on sc.projection_id = p.projection_id
group by table_schema,
         table_name
order by table_name desc;

--- обьем памяти занимаемый всеми таблицами
select  ROUND(SUM(used_bytes) / ( 1024^3 ), 4) AS used_compressed_gb from column_storage where anchor_table_name in (select table_name from v_catalog.tables);

-- список проекций и занимаемое место 
select projection_name, ROUND(SUM(used_bytes) / ( 1024^3 ), 4) AS used_compressed_gb
from projection_storage where projection_name in (select projection_name from v_catalog.projections)
GROUP BY projection_name ORDER BY used_compressed_gb;


SELECT schema_name
          ,projection_name
          ,count(*) num_ros
          ,sum(total_row_count) num_rows
          ,sum(deleted_row_count) num_deld_rows
          ,sum(delete_vector_count) Num_dv
          ,(sum(deleted_row_count) / sum(total_row_count) * 100)::INT percentage_del_rows
FROM storage_containers
GROUP BY 1, 2
HAVING sum(deleted_row_count) > 0
ORDER BY 5 DESC;

SELECT projection_name,
    round(sum(used_bytes)/(1024^2), 2) as used_mb 
FROM storage_containers
GROUP BY projection_name
ORDER BY used_mb desc;

---
SELECT ROUND(SUM(size_bytes) / ( 1024^3 ), 1) AS size_gb, object_type, object_name FROM user_audits WHERE object_schema = 'public' GROUP BY object_name;

--- show create table
select EXPORT_OBJECTS( '/home/dbadmin/sends.sql', 'sends');
\d sends

--- show connections
SELECT user_name, node_name, current_statement, client_type FROM sessions;
SELECT node_name, transaction_id, statement_id, user_name, start_timestamp, request_duration_ms, memory_acquired_mb, substr(request, 1, 100) AS request FROM v_monitor.query_requests WHERE transaction_id = transaction_id AND statement_id = statement_id;
SELECT node_name, transaction_id, statement_id, user_name, start_timestamp, request_duration_ms, memory_acquired_mb, substr(request, 1, 100) AS request FROM v_monitor.query_requests INNER JOIN sessions ON v_monitor.query_requests.transaction_id = sessions.transaction_id;

--- show databases
SELECT database_name FROM v_catalog.databases;
---
EXPORT TO PARQUET(directory='/home/dbadmin/backup') AS SELECT * FROM public.unsubscribe_webpush;


---
CONNECT TO VERTICA mailfier USER dbadmin PASSWORD '12qwaszx' ON '192.168.104.111',5433;
EXPORT TO VERTICA mailfier.unsubscribe_webpush AS SELECT * FROM public.unsubscribe_webpush;

--- AUDIT
SELECT AUDIT(''); vs SELECT ROUND(SUM(used_bytes) / ( 1024^3 ), 4) from projection_storage;



SELECT AUDIT('public','table');
\x
SELECT * FROM user_audits WHERE object_schema = 'public';
SELECT size_bytes,object_name,audited_object_name,error_tolerance_percent FROM user_audits WHERE object_schema = 'public';
SELECT ROUND(SUM(size_bytes) / ( 1024^3 ), 1) AS size_gb, object_type, object_name FROM user_audits WHERE object_schema = 'public' GROUP BY object_name,object_type ORDER BY size_gb DESC;
SELECT ROUND(SUM(size_bytes) / ( 1024^3 ), 4) AS size_gb from user_audits;

# after deleted records you should reread raw size
select audit_license_size();

SELECT manage_epoch();


SELECT n.node_name, n.node_state, n.node_address, sysdate - MAX(ns.event_timestamp) AS uptime
FROM node_states ns JOIN nodes n ON n.node_name = ns.node_name
WHERE ns.node_state = 'UP'
GROUP BY n.node_name, n.node_state, n.node_address
ORDER BY n.node_name;


admintools -t list_allnodes
admintools -t view_cluster

GRANT ALL PRIVILEGES ON DATABASE mailfier TO vkholod WITH GRANT OPTION;
SELECT user_name, all_roles, is_super_user, is_locked, lock_time FROM v_catalog.users ORDER BY user_name;

GRANT ALL PRIVILEGES ON ALL TABLE TO vkholod WITH GRANT OPTION;
GRANT SELECT ON ALL TABLES IN SCHEMA <schema  name> TO <user name>;
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO vkholod;

ALTER USER vkholod TEMPSPACECAP '20G';
SELECT user_name, all_roles, is_super_user, is_locked, lock_time FROM v_catalog.users WHERE user_name = 'vkholod' ORDER BY user_name;
SELECT grantor,privileges_description,object_name,object_type,grantee FROM grants WHERE grantee = 'vkholod' order by object_name;
CREATE USER mdoroncev IDENTIFIED BY 'nig8Akjioc';
GRANT USAGE ON SCHEMA PUBLIC to mdoroncev;



vkholod
Lcw9edlsd1A33f!ff
CREATE TABLE tmp_create_for_vlada
as (
    SELECT *
    FROM sends
    WHERE sends.project_id = 16930
    and sends.created_at between '2021-09-15' and '2021-10-13 23:59:59'
);



admintools -t db_status -s ALL
admintools -t stop_node -s v_mailfier_node0002
admintools -t list_allnodes
admintools -t list_host
admintools -t list_node
admintools -t view_cluster
admintools -t restart_node -s 78.46.91.55 -d dbadmin -p $PASS -F


  818  /opt/vertica/bin/vbr --config-file /opt/dbadmin/cp_cluster_snapshot.ini --task copycluster && wait | ssh dbadmin@192.168.104.107 "/opt/vertica/bin/admintools -t start_db -p '12qwaszx' -d mailfier "



EXPORT TO PARQUET (directory = '/home/dbadmin/parquet/sends_custom') OVER (PARTITION BY created_at GROUP BY ) AS SELECT * from sends_custom;


DELETE FROM user_fields_text WHERE created_at < 2021-12-15;
SELECT created_at FROM user_fields_text WHERE created_at < 2021-12-15 ORDER BY created_at desc;
SELECT created_at FROM user_fields_text WHERE created_at < '2021-12-15'
EXPORT TO PARQUET (directory = '/home/dbadmin/parquet/user_fields_text_2021-12-15') AS SELECT * FROM user_fields_text WHERE created_at < '2021-12-15';
