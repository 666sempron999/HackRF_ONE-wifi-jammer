#!/usr/bin/python3

from wifi import Cell, Scheme


def get_wifi_parametrs():
    cell = Cell.all('wlan0')

    results = []
    for i in cell:
        inside = []
        # print('{} - {}'.format('SSID', i.ssid))
        # print('{} - ({})'.format('Signal', i.signal))
        # print('{} - {}'.format('Quality', i.quality))
        # print('{} - {}'.format('Frequency', i.frequency))
        # print('{} - {}'.format('bitrates', i.bitrates[-1]))
        # print('{} - {}'.format('encrypted', i.encrypted))
        # print('{} - {}'.format('channel', i.channel))
        # print('{} - {}'.format('MAC address', i.address))
        # print('{} - {}'.format('Mode', i.mode))
        # print("---------------------------------------")
        
        freq_st = i.frequency
        number = freq_st.split()[0]
        freq = int(float(number)*1000000000)

        inside.append(i.ssid)
        inside.append(freq)
        results.append(inside)

    return results


def main():
    wifi_envirom = get_wifi_parametrs()
    print(wifi_envirom)
    # print(wifi_envirom[0][1])
    # st = wifi_envirom[0][1]
    # st_freq = (st.split()[0])
    # print(int(float(st_freq)*1000000000))
    # print(2462000000)
if __name__ == '__main__':
    main()