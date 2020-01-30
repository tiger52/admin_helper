import ldap
try:
	lcon = ldap.open("10.166.6.100")
	
	# you should  set this to ldap.VERSION2 if you're using a v2 directory
	lcon.protocol_version = ldap.VERSION3	
	# Pass in a valid username and password to get 
	# privileged directory access.
	# If you leave them as empty strings or pass an invalid value
	# you will still bind to the server but with limited privileges.
	
	username = "cn=ldapadm, dc=dev, dc=company"
	password  = "1q2w3e4r"
	
	# Any errors will throw an ldap.LDAPError exception 
	# or related exception so you can ignore the result
	lcon.simple_bind(username, password)
        print "ldap conected"
except ldap.LDAPError, e:
	print e
	# handle error however you like

ldap_base = "ou=People,dc=dev,dc=company"
#query = "(ou=People)"
#query = '(objectClass=account)'
query = 'cn=*'
result = lcon.search_s(ldap_base, ldap.SCOPE_SUBTREE, query)

for dn in result:
    print dn

