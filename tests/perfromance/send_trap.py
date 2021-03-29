import time
import utils

from pysnmp.hlapi import *


# from metrics import Metrics
# metrics = Metrics()

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# def send_trap():
#     iterator = sendNotification(
#         SnmpEngine(),
#         CommunityData('public', mpModel=0),
#         UdpTransportTarget(('demo.snmplabs.com', 162)),
#         ContextData(),
#         'trap',
#         NotificationType(
#             ObjectIdentity('1.3.6.1.6.3.1.1.5.2')
#         ).addVarBinds(
#             ('1.3.6.1.6.3.1.1.4.3.0', '1.3.6.1.4.1.20408.4.1.1.2'),
#             ('1.3.6.1.2.1.1.1.0', OctetString('my system'))
#         ).loadMibs(
#             'SNMPv2-MIB'
#         )
#     )
#
#     errorIndication, errorStatus, errorIndex, varBinds = next(iterator)
#
#     if errorIndication:
#         print(errorIndication)

def send_trap(host, port, object_identity, *var_binds):
    iterator = sendNotification(
        SnmpEngine(),
        CommunityData('public', mpModel=0),
        UdpTransportTarget((host, port)),
        ContextData(),
        'trap',
        NotificationType(
            ObjectIdentity(object_identity)
        ).addVarBinds(
            *var_binds
        ).loadMibs(
            'SNMPv2-MIB'
        )
    )

    errorIndication, errorStatus, errorIndex, varBinds = next(iterator)

    if errorIndication:
        print(errorIndication)


def send_trap_loop(shared_value_between_processes, log_dir, duration_sec, name):
    index = 0
    start = time.time()
    while True:
        string = f"{name}:test perf_{index}"
        # print(string)
        varbind1 = ('1.3.6.1.6.3.1.1.4.3.0', '1.3.6.1.4.1.20408.4.1.1.2')
        varbind2 = ('1.3.6.1.2.1.1.1.0', OctetString(string))
        send_trap("10.202.2.209", 162, '1.3.6.1.6.3.1.1.5.2', varbind1, varbind2)
        index += 1
        # if index == 10:
        #     break
        if time.time() - start > duration_sec:
            # metrics.add_entry_to_table(name, index)
            shared_value_between_processes.value = shared_value_between_processes.value + index
            print(f"Saving no.of traps send for {name}")
            utils.save_data(log_dir + name + ".txt", index)
            break
    return index


if __name__ == '__main__':
    print_hi('PyCharm')
    # send trap
    start_time = time.time()
    # varbind1 = ('1.3.6.1.6.3.1.1.4.3.0', '1.3.6.1.4.1.20408.4.1.1.2')
    # varbind2 = ('1.3.6.1.2.1.1.1.0', OctetString('my system'))
    # send_trap("10.202.2.209", 162, '1.3.6.1.6.3.1.1.5.2', varbind1, varbind2)

    how_many = send_trap_loop(10, "test")
    duration = time.time() - start_time
    print(f"Sending event took: {duration}, no. of messages: {how_many}")
    print(f"time needed to send single event: {duration / how_many}")
    print(f"events per sec: {how_many / duration}")
