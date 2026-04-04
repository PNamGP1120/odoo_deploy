FROM odoo:17

USER root

COPY ./extra-addons /mnt/extra-addons
COPY ./entrypoint.sh /entrypoint.sh
COPY ./config/odoo.conf /etc/odoo/odoo.conf

RUN chmod +x /entrypoint.sh && chown -R odoo:odoo /mnt/extra-addons /entrypoint.sh /etc/odoo/odoo.conf

USER odoo

EXPOSE 8069

CMD ["/entrypoint.sh"]