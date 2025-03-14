# Delete node from proxmox cluster

Для начала удалим ее из кластера на первом сервере:

```
pvecm nodes
pvecm del [node name]
```

После чего нода будет отсоединена от кластера. Теперь переходим на сломанную ноду и отключаем на ней следующие сервисы:

```
systemctl stop pvestatd.service && \
systemctl stop pvedaemon.service && \
systemctl stop pve-cluster.service && \
systemctl stop corosync && \
systemctl stop pve-cluster
```

Proxmox кластер хранит информацию о себе в sqlite базе, ее также необходимо очистить:

```bash
sqlite3 /var/lib/pve-cluster/config.db
delete from tree where name = 'corosync.conf';
.quit
```

Данные о коросинке успешно удалены. Удалим оставшиеся файлы, для этого необходимо запустить кластерную файловую систему в standalone режиме:

```bash
pmxcfs -l; \
rm /etc/pve/corosync.conf; \
rm -r /etc/corosync/*; \
rm /var/lib/corosync/*; \
rm -rf /etc/pve/nodes/*
```

Перезапускаем сервер (это необязательно, но перестрахуемся: все сервисы по итогу должны быть запущены и работать корректно. Чтобы ничего не упустить делаем перезапуск). После включения мы получим пустую ноду без какой-либо информации о предыдущем кластере и можем начать подключение вновь.

```
systemctl status pvestatd.service
systemctl status pvedaemon.service
systemctl status pve-cluster.service
systemctl status corosync
systemctl status pve-cluster
```

```
systemctl start pvestatd.service
systemctl start pvedaemon.service
systemctl start pve-cluster.service
systemctl start corosync
systemctl start pve-cluster
```
