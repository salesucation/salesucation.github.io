FROM unit:latest
COPY ./dist/client /usr/share/unit/webpage
COPY ./unit-config.json /docker-entrypoint.d/config.json
CMD ["unitd","--no-daemon","--control","0.0.0.0:8080"]