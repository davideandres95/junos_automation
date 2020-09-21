FROM crpd:latest

ADD launch.sh /
ADD sshd_config /

ADD juniper.conf /
# ADD license.conf /

RUN echo 'root:lab123' | chpasswd

CMD ["bash", "/launch.sh"]
