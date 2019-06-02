--how to see active SQL Server connections?

SELECT 	DB_NAME(dbid) as DBName, 
		COUNT(dbid) as NumberOfConnections,
		loginame as LoginName
FROM sys.sysprocesses
WHERE dbid > 0
GROUP BY dbid, loginame

--And this gives the total:
SELECT COUNT(dbid) as TotalConnections
FROM sys.sysprocesses
WHERE dbid > 0
	
--If you need more detail, run:
sp_who2 'Active'