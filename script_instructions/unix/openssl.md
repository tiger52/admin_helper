# create your own centre certification
## create you own root certificate CA
```
openssl genrsa -out myCA.key 2048
openssl req -x509 -new -nodes -key myCA.key -sha256 -days 3650 -out myCA.pem
```
## now create certificate for your app signed by our root CA
```
openssl genrsa -out mydomain.local.key 2048
openssl req -new -key mydomain.local.key -subj "/CN=mydomain.local" -out mydomain.local.csr
openssl x509 -req -in mydomain.local.csr -CA myCA.pem -CAkey myCA.key -CAcreateserial -out mydomain.local.crt -days 3650
```
## and if you need pfx (certificate in binary view)
```
openssl pkcs12 -export -out mydomain.local.pfx -inkey mydomain.local.key -in mydomain.local.crt -certfile mydomain.local.crt
```
