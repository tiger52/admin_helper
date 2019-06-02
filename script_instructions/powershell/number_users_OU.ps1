$svcuser = Get-ADUser -Filter * -SearchBase "OU=CO,OU=NADRA,DC=nadrabank,DC=jsc,DC=local"
$svcuser.count