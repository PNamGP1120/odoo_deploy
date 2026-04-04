#!/usr/bin/env bash
set -e

cat > /tmp/odoo-render.conf <<EOF
[options]
admin_passwd = ${ODOO_ADMIN_PASSWD:-admin123456}
db_host = ${DB_HOST}
db_port = ${DB_PORT:-5432}
db_user = ${DB_USER}
db_password = ${DB_PASSWORD}
list_db = False
addons_path = /mnt/extra-addons,/usr/lib/python3/dist-packages/odoo/addons
data_dir = /var/lib/odoo
proxy_mode = True
http_port = 8069
EOF

if [ "${INIT_ODOO_DB:-false}" = "true" ]; then
  exec odoo -c /tmp/odoo-render.conf -d "${ODOO_DB_NAME}" -i base --without-demo=all
else
  exec odoo -c /tmp/odoo-render.conf -d "${ODOO_DB_NAME}"
fi