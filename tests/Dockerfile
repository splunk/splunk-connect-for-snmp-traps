#Splunk Connect for Syslog (SC4S) by Splunk, Inc.
#
#To the extent possible under law, the person who associated CC0 with
#Splunk Connect for Syslog (SC4S) has waived all copyright and related or neighboring rights
#to Splunk Connect for Syslog (SC4S).
#
#You should have received a copy of the CC0 legalcode along with this
#work.  If not, see <http://creativecommons.org/publicdomain/zero/1.0/>.
FROM python:3.8

COPY tests/requirements.txt /
RUN pip3 install -r /requirements.txt
RUN pip3 install pytest-xdist
COPY tests/entrypoint.sh /
COPY tests/pytest-ci.ini /
COPY splunk_connect_for_snmp_traps/ /splunk_connect_for_snmp_traps/
COPY config.yaml /
COPY lookups/ /lookups/
CMD /entrypoint.sh

