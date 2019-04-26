# Derived from official mariadb image
FROM mariadb

# Add database env
ENV MYSQL_ROOT_PASSWORD=1
ENV MYSQL_DATABASE=idp

# Add mysql config file
COPY conf.cnf /etc/mysql/conf.d/

# Add the content of the sql/ directory to the image
# All scripts in docker-entrypoint-initdb.d/ are automatically
# executed during container startup in alphabetical order
COPY sql/ /docker-entrypoint-initdb.d/
