import-module activedirectory

Get-ADUser -Filter * -SearchBase "OU=Users,OU=COMMITTEE,OU=CO,OU=NADRA,DC=nadrabank,DC=jsc,DC=local" -Server 172.17.25.10 -Credential nadrabank\admin_bsv -Properties cn, mail, DisplayName, SamAccountName,givenName,sn, departmentNumber, employeeNumber, personalTitle, Title, Company, Department,telephoneNumber,physicalDeliveryOfficeName,distinguishedName,pager,OfficePhone,MobilePhone,HomePhone,LastLogon,lastLogonTimestamp, whenCreated, description,extensionAttribute9,extensionAttribute1,extensionAttribute10,extensionAttribute11,extensionAttribute12,extensionAttribute13,extensionAttribute14,division,middleName,employeeID|select cn, mail, DisplayName, SamAccountName,givenName,sn, departmentNumber, employeeNumber, personalTitle, Title, Company, Department,telephoneNumber,physicalDeliveryOfficeName,distinguishedName,pager,OfficePhone,MobilePhone,HomePhone,LastLogon,lastLogonTimestamp, whenCreated, description,extensionAttribute9,extensionAttribute1,extensionAttribute10,extensionAttribute11,extensionAttribute12,extensionAttribute13,extensionAttribute14,division,middleName,employeeID | Export-Csv d:\temp\adcsv.csv -Encoding utf8 -Delimiter ";"

Get-ADUser -f {sn -eq 'Babik'} -Properties extensionAttribute9, employeeNumber



#вот пример того как можно вытащить из ад имя+айпи компа
Get-ADComputer -Filter * -Properties ipv4Address, OperatingSystem, OperatingSystemServicePack, description,LastLogonTimeStamp,Enabled,DistinguishedName |
select  name,ipv4Address, DistinguishedName, OperatingSystem, OperatingSystemServicePack, description,Enabled,@{Name="LastLogOn"; Expression={[DateTime]::FromFileTime($_.lastLogonTimestamp)}}|
Export-Csv -Encoding UTF8 -Delimiter ";" d:\temp\computer_in_ad.csv

#список груп в которых находиться юзверь
(Get-ADUser -f {sn -eq 'Chervinchuk'} -Properties MemberOf | Select-Object MemberOf).memberof