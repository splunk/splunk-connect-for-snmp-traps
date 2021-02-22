from splunk_connect_for_snmp_traps.mongo import OidsRepository

#TODO as for now this is just a demo on how to use WalkedHostsRepository
#TODO final version should use fixures to run MongoDB in Docker
def main():
    mongo_config = {'host': 'localhost', 'port': 27017, 'database': 'snmp_traps', 'collection': 'oids'}

    mongo = OidsRepository(mongo_config)

    mongo.clear()
    mongo.add_oid('1.3.6.4.1.2.3.4.5.6.7.8')
    print(mongo.contains_oid('1.3.6.4.1.2.3.4.5.6.7.8'))

    mongo.delete_oid('1.3.6.4.1.2.3.4.5.6.7.8')
    print(mongo.contains_oid('1.3.6.4.1.2.3.4.5.6.7.8'))


if __name__ == '__main__':
    main()
