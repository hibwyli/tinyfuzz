# Chain 0
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)

===

# Chain 1
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)

===

# Chain 2
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)

===

# Chain 3
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)

===

# Chain 4
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)

===

# Chain 5
import ipaddress
arg0 = IPv4Network('0.0.0.3/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)

===

# Chain 6
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)

===

# Chain 7
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)

===

# Chain 8
import ipaddress
result0 = ipaddress.v4_int_to_packed(fuzz_input)

===

# Chain 9
import ipaddress
result0 = ipaddress.v6_int_to_packed(fuzz_input)

===

# Chain 10
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)

===

# Chain 11
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)

===

# Chain 12
import ipaddress
arg0 = 755
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)

===

# Chain 13
import ipaddress
arg0 = 201
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)

===

# Chain 14
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)

===

# Chain 15
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)

===

# Chain 16
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)

===

# Chain 17
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)

===

# Chain 18
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)

===

# Chain 19
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)

===

# Chain 20
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)

===

# Chain 21
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)

===

# Chain 22
import ipaddress
arg0 = IPv6Interface('::/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)

===

# Chain 23
import ipaddress
arg0 = IPv6Interface('::/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)

===

# Chain 24
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)

===

# Chain 25
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)

===

# Chain 26
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)

===

# Chain 27
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)

===

# Chain 28
import ipaddress
arg0 = IPv4Network('0.0.0.2/32')
obj0 = ipaddress.IPv4Network(arg0, fuzz_input)

===

# Chain 29
import ipaddress
obj0 = ipaddress.IPv6Address(fuzz_input)

===

# Chain 30
import ipaddress
obj0 = ipaddress.IPv6Address(fuzz_input)

===

# Chain 31
import ipaddress
obj0 = ipaddress.IPv6Address(fuzz_input)

===

# Chain 32
import ipaddress
obj0 = ipaddress.IPv6Address(fuzz_input)

===

# Chain 33
import ipaddress
arg0 = IPv6Address('::5')
obj0 = ipaddress.IPv6Address(arg0)
result0 = obj0.__eq__(fuzz_input)

===

# Chain 34
import ipaddress
arg0 = IPv6Address('::4')
obj0 = ipaddress.IPv6Address(arg0)
result0 = obj0.__eq__(fuzz_input)

===

# Chain 35
import ipaddress
obj0 = ipaddress.IPv6Interface(fuzz_input)

===

# Chain 36
import ipaddress
obj0 = ipaddress.IPv6Interface(fuzz_input)

===

# Chain 37
import ipaddress
obj0 = ipaddress.IPv6Interface(fuzz_input)

===

# Chain 38
import ipaddress
obj0 = ipaddress.IPv6Interface(fuzz_input)

===

# Chain 39
import ipaddress
arg0 = IPv6Interface('::3/128')
obj0 = ipaddress.IPv6Interface(arg0)
result0 = obj0.__eq__(fuzz_input)

===

# Chain 40
import ipaddress
arg0 = IPv6Interface('::1/128')
obj0 = ipaddress.IPv6Interface(arg0)
result0 = obj0.__eq__(fuzz_input)

===

# Chain 41
import ipaddress
obj0 = ipaddress.IPv6Network(fuzz_input)

===

# Chain 42
import ipaddress
obj0 = ipaddress.IPv6Network(fuzz_input)

===

# Chain 43
import ipaddress
obj0 = ipaddress.IPv6Network(fuzz_input)

===

# Chain 44
import ipaddress
obj0 = ipaddress.IPv6Network(fuzz_input)

===

# Chain 45
import ipaddress
arg0 = 256.3651853784563
obj0 = ipaddress.IPv6Network(arg0, fuzz_input)

===

# Chain 46
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.get_mixed_type_key(result0)

===

# Chain 47
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 48
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 49
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 50
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 51
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__contains__(result0)

===

# Chain 52
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 53
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 54
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 55
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 56
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 57
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 58
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.address_exclude(result0)

===

# Chain 59
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 60
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
arg0 = IPv6Address('::4')
result1 = ipaddress.summarize_address_range(result0, arg0)

===

# Chain 61
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
arg0 = IPv6Address('::')
result1 = ipaddress.summarize_address_range(arg0, result0)

===

# Chain 62
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.get_mixed_type_key(result0)

===

# Chain 63
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 64
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 65
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 66
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 67
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__contains__(result0)

===

# Chain 68
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 69
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 70
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 71
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 72
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 73
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 74
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.subnets(result0)

===

# Chain 75
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.supernet(result0)

===

# Chain 76
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.address_exclude(result0)

===

# Chain 77
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 78
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.get_mixed_type_key(result0)

===

# Chain 79
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 80
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 81
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 82
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 83
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__contains__(result0)

===

# Chain 84
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 85
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 86
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 87
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 88
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 89
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 90
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.address_exclude(result0)

===

# Chain 91
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 92
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
arg0 = IPv6Address('::4')
result1 = ipaddress.summarize_address_range(result0, arg0)

===

# Chain 93
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
arg0 = IPv6Address('::2')
result1 = ipaddress.summarize_address_range(arg0, result0)

===

# Chain 94
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.get_mixed_type_key(result0)

===

# Chain 95
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 96
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 97
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 98
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 99
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__contains__(result0)

===

# Chain 100
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 101
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 102
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 103
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 104
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 105
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 106
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.subnets(result0)

===

# Chain 107
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.supernet(result0)

===

# Chain 108
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.address_exclude(result0)

===

# Chain 109
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 110
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.get_mixed_type_key(result0)

===

# Chain 111
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 112
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 113
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 114
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 115
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__contains__(result0)

===

# Chain 116
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 117
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 118
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 119
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 120
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 121
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 122
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.address_exclude(result0)

===

# Chain 123
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 124
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
arg0 = IPv6Address('::5')
result1 = ipaddress.summarize_address_range(result0, arg0)

===

# Chain 125
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
arg0 = IPv6Address('::4')
result1 = ipaddress.summarize_address_range(arg0, result0)

===

# Chain 126
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.get_mixed_type_key(result0)

===

# Chain 127
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 128
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 129
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 130
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 131
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__contains__(result0)

===

# Chain 132
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 133
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 134
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 135
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 136
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 137
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 138
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.subnets(result0)

===

# Chain 139
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.supernet(result0)

===

# Chain 140
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.address_exclude(result0)

===

# Chain 141
import ipaddress
result0 = ipaddress.ip_address(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 142
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress._split_optional_netmask(result0)

===

# Chain 143
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.get_mixed_type_key(result0)

===

# Chain 144
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress._split_addr_prefix(result0)

===

# Chain 145
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 146
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 147
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 148
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 149
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__contains__(result0)

===

# Chain 150
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.overlaps(result0)

===

# Chain 151
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.address_exclude(result0)

===

# Chain 152
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.compare_networks(result0)

===

# Chain 153
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.subnet_of(result0)

===

# Chain 154
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.supernet_of(result0)

===

# Chain 155
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 156
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 157
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 158
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 159
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 160
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.subnets(result0)

===

# Chain 161
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.supernet(result0)

===

# Chain 162
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress._split_optional_netmask(result0)

===

# Chain 163
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
arg0 = IPv6Address('::5')
result1 = ipaddress.summarize_address_range(result0, arg0)

===

# Chain 164
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
arg0 = IPv6Address('::3')
result1 = ipaddress.summarize_address_range(arg0, result0)

===

# Chain 165
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.get_mixed_type_key(result0)

===

# Chain 166
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
arg0 = IPv4Network('0.0.0.0/32')
result1 = ipaddress._split_addr_prefix(result0, arg0)

===

# Chain 167
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 168
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 169
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 170
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 171
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__contains__(result0)

===

# Chain 172
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.overlaps(result0)

===

# Chain 173
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.address_exclude(result0)

===

# Chain 174
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.compare_networks(result0)

===

# Chain 175
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
arg0 = IPv4Network('0.0.0.0/32')
result1 = ipaddress._is_subnet_of(result0, arg0)

===

# Chain 176
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
arg0 = IPv4Network('0.0.0.0/32')
result1 = ipaddress._is_subnet_of(arg0, result0)

===

# Chain 177
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.subnet_of(result0)

===

# Chain 178
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.supernet_of(result0)

===

# Chain 179
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 180
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 181
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 182
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 183
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 184
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 185
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress._split_optional_netmask(fuzz_input)

===

# Chain 186
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
arg0 = IPv6Address('::1')
result1 = ipaddress.summarize_address_range(fuzz_input, arg0)

===

# Chain 187
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
arg0 = IPv6Address('::5')
result1 = ipaddress.summarize_address_range(arg0, fuzz_input)

===

# Chain 188
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.get_mixed_type_key(fuzz_input)

===

# Chain 189
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
arg0 = IPv4Network('0.0.0.3/32')
result1 = ipaddress._split_addr_prefix(fuzz_input, arg0)

===

# Chain 190
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 191
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 192
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 193
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 194
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__contains__(fuzz_input)

===

# Chain 195
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.overlaps(fuzz_input)

===

# Chain 196
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.address_exclude(fuzz_input)

===

# Chain 197
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.compare_networks(fuzz_input)

===

# Chain 198
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
arg0 = IPv4Network('0.0.0.4/32')
result1 = ipaddress._is_subnet_of(fuzz_input, arg0)

===

# Chain 199
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
arg0 = IPv4Network('0.0.0.2/32')
result1 = ipaddress._is_subnet_of(arg0, fuzz_input)

===

# Chain 200
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.subnet_of(fuzz_input)

===

# Chain 201
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.supernet_of(fuzz_input)

===

# Chain 202
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 203
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 204
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__init__(fuzz_input)

===

# Chain 205
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 206
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 207
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 208
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress._split_optional_netmask(result0)

===

# Chain 209
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.get_mixed_type_key(result0)

===

# Chain 210
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress._split_addr_prefix(result0)

===

# Chain 211
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 212
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 213
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 214
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 215
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__contains__(result0)

===

# Chain 216
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.overlaps(result0)

===

# Chain 217
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.address_exclude(result0)

===

# Chain 218
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.compare_networks(result0)

===

# Chain 219
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.subnet_of(result0)

===

# Chain 220
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.supernet_of(result0)

===

# Chain 221
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 222
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 223
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 224
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 225
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 226
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.subnets(result0)

===

# Chain 227
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.supernet(result0)

===

# Chain 228
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress._split_optional_netmask(result0)

===

# Chain 229
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
arg0 = IPv6Address('::3')
result1 = ipaddress.summarize_address_range(result0, arg0)

===

# Chain 230
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
arg0 = IPv6Address('::1')
result1 = ipaddress.summarize_address_range(arg0, result0)

===

# Chain 231
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.get_mixed_type_key(result0)

===

# Chain 232
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
arg0 = IPv4Network('0.0.0.2/32')
result1 = ipaddress._split_addr_prefix(result0, arg0)

===

# Chain 233
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 234
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 235
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 236
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 237
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__contains__(result0)

===

# Chain 238
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.overlaps(result0)

===

# Chain 239
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.address_exclude(result0)

===

# Chain 240
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.compare_networks(result0)

===

# Chain 241
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
arg0 = IPv4Network('0.0.0.0/32')
result1 = ipaddress._is_subnet_of(result0, arg0)

===

# Chain 242
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
arg0 = IPv4Network('0.0.0.1/32')
result1 = ipaddress._is_subnet_of(arg0, result0)

===

# Chain 243
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.subnet_of(result0)

===

# Chain 244
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.supernet_of(result0)

===

# Chain 245
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 246
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 247
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 248
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 249
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 250
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 251
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress._split_optional_netmask(fuzz_input)

===

# Chain 252
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
arg0 = IPv6Address('::1')
result1 = ipaddress.summarize_address_range(fuzz_input, arg0)

===

# Chain 253
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
arg0 = IPv6Address('::1')
result1 = ipaddress.summarize_address_range(arg0, fuzz_input)

===

# Chain 254
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.get_mixed_type_key(fuzz_input)

===

# Chain 255
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
arg0 = IPv4Network('0.0.0.4/32')
result1 = ipaddress._split_addr_prefix(fuzz_input, arg0)

===

# Chain 256
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 257
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 258
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 259
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 260
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__contains__(fuzz_input)

===

# Chain 261
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.overlaps(fuzz_input)

===

# Chain 262
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.address_exclude(fuzz_input)

===

# Chain 263
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.compare_networks(fuzz_input)

===

# Chain 264
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
arg0 = IPv4Network('0.0.0.2/32')
result1 = ipaddress._is_subnet_of(fuzz_input, arg0)

===

# Chain 265
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
arg0 = IPv4Network('0.0.0.4/32')
result1 = ipaddress._is_subnet_of(arg0, fuzz_input)

===

# Chain 266
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.subnet_of(fuzz_input)

===

# Chain 267
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.supernet_of(fuzz_input)

===

# Chain 268
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 269
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 270
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__init__(fuzz_input)

===

# Chain 271
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 272
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 273
import ipaddress
result0 = ipaddress.ip_network(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 274
import ipaddress
arg0 = IPv4Network('0.0.0.0/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress._split_optional_netmask(result0)

===

# Chain 275
import ipaddress
arg0 = IPv4Network('0.0.0.3/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.get_mixed_type_key(result0)

===

# Chain 276
import ipaddress
arg0 = IPv4Network('0.0.0.0/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress._split_addr_prefix(result0)

===

# Chain 277
import ipaddress
arg0 = IPv4Network('0.0.0.3/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 278
import ipaddress
arg0 = IPv4Network('0.0.0.4/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 279
import ipaddress
arg0 = IPv4Network('0.0.0.1/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 280
import ipaddress
arg0 = IPv4Network('0.0.0.1/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 281
import ipaddress
arg0 = IPv4Network('0.0.0.5/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__contains__(result0)

===

# Chain 282
import ipaddress
arg0 = IPv4Network('0.0.0.3/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.overlaps(result0)

===

# Chain 283
import ipaddress
arg0 = IPv4Network('0.0.0.3/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.address_exclude(result0)

===

# Chain 284
import ipaddress
arg0 = IPv4Network('0.0.0.4/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.compare_networks(result0)

===

# Chain 285
import ipaddress
arg0 = IPv4Network('0.0.0.4/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.subnet_of(result0)

===

# Chain 286
import ipaddress
arg0 = IPv4Network('0.0.0.3/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.supernet_of(result0)

===

# Chain 287
import ipaddress
arg0 = IPv4Network('0.0.0.2/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 288
import ipaddress
arg0 = IPv4Network('0.0.0.5/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 289
import ipaddress
arg0 = IPv4Network('0.0.0.5/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 290
import ipaddress
arg0 = IPv4Network('0.0.0.0/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 291
import ipaddress
arg0 = IPv4Network('0.0.0.3/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 292
import ipaddress
arg0 = IPv4Network('0.0.0.5/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.subnets(result0)

===

# Chain 293
import ipaddress
arg0 = IPv4Network('0.0.0.0/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.supernet(result0)

===

# Chain 294
import ipaddress
arg0 = IPv4Network('0.0.0.2/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress._split_optional_netmask(result0)

===

# Chain 295
import ipaddress
arg0 = IPv4Network('0.0.0.1/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
arg1 = IPv6Address('::3')
result1 = ipaddress.summarize_address_range(result0, arg1)

===

# Chain 296
import ipaddress
arg0 = IPv4Network('0.0.0.1/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
arg1 = IPv6Address('::2')
result1 = ipaddress.summarize_address_range(arg1, result0)

===

# Chain 297
import ipaddress
arg0 = IPv4Network('0.0.0.2/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.get_mixed_type_key(result0)

===

# Chain 298
import ipaddress
arg0 = IPv4Network('0.0.0.4/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
arg1 = IPv4Network('0.0.0.4/32')
result1 = ipaddress._split_addr_prefix(result0, arg1)

===

# Chain 299
import ipaddress
arg0 = IPv4Network('0.0.0.0/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 300
import ipaddress
arg0 = IPv4Network('0.0.0.4/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 301
import ipaddress
arg0 = IPv4Network('0.0.0.5/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 302
import ipaddress
arg0 = IPv4Network('0.0.0.5/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 303
import ipaddress
arg0 = IPv4Network('0.0.0.1/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__contains__(result0)

===

# Chain 304
import ipaddress
arg0 = IPv4Network('0.0.0.0/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.overlaps(result0)

===

# Chain 305
import ipaddress
arg0 = IPv4Network('0.0.0.0/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.address_exclude(result0)

===

# Chain 306
import ipaddress
arg0 = IPv4Network('0.0.0.1/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.compare_networks(result0)

===

# Chain 307
import ipaddress
arg0 = IPv4Network('0.0.0.2/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
arg1 = IPv4Network('0.0.0.2/32')
result1 = ipaddress._is_subnet_of(result0, arg1)

===

# Chain 308
import ipaddress
arg0 = IPv4Network('0.0.0.4/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
arg1 = IPv4Network('0.0.0.4/32')
result1 = ipaddress._is_subnet_of(arg1, result0)

===

# Chain 309
import ipaddress
arg0 = IPv4Network('0.0.0.1/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.subnet_of(result0)

===

# Chain 310
import ipaddress
arg0 = IPv4Network('0.0.0.1/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.supernet_of(result0)

===

# Chain 311
import ipaddress
arg0 = IPv4Network('0.0.0.0/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 312
import ipaddress
arg0 = IPv4Network('0.0.0.2/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 313
import ipaddress
arg0 = IPv4Network('0.0.0.4/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 314
import ipaddress
arg0 = IPv4Network('0.0.0.2/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 315
import ipaddress
arg0 = IPv4Network('0.0.0.1/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 316
import ipaddress
arg0 = IPv4Network('0.0.0.5/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 317
import ipaddress
arg0 = IPv4Network('0.0.0.3/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress._split_optional_netmask(arg0)

===

# Chain 318
import ipaddress
arg0 = IPv4Network('0.0.0.4/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
arg1 = IPv6Address('::2')
result1 = ipaddress.summarize_address_range(arg0, arg1)

===

# Chain 319
import ipaddress
arg0 = IPv4Network('0.0.0.1/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
arg1 = IPv6Address('::3')
result1 = ipaddress.summarize_address_range(arg1, arg0)

===

# Chain 320
import ipaddress
arg0 = IPv4Network('0.0.0.5/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.get_mixed_type_key(arg0)

===

# Chain 321
import ipaddress
arg0 = IPv4Network('0.0.0.0/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
arg1 = IPv4Network('0.0.0.0/32')
result1 = ipaddress._split_addr_prefix(arg0, arg1)

===

# Chain 322
import ipaddress
arg0 = IPv4Network('0.0.0.0/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__eq__(arg0)

===

# Chain 323
import ipaddress
arg0 = IPv4Network('0.0.0.4/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__lt__(arg0)

===

# Chain 324
import ipaddress
arg0 = IPv4Network('0.0.0.1/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__lt__(arg0)

===

# Chain 325
import ipaddress
arg0 = IPv4Network('0.0.0.0/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__eq__(arg0)

===

# Chain 326
import ipaddress
arg0 = IPv4Network('0.0.0.5/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__contains__(arg0)

===

# Chain 327
import ipaddress
arg0 = IPv4Network('0.0.0.5/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.overlaps(arg0)

===

# Chain 328
import ipaddress
arg0 = IPv4Network('0.0.0.4/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.address_exclude(arg0)

===

# Chain 329
import ipaddress
arg0 = IPv4Network('0.0.0.3/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.compare_networks(arg0)

===

# Chain 330
import ipaddress
arg0 = IPv4Network('0.0.0.3/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
arg1 = IPv4Network('0.0.0.3/32')
result1 = ipaddress._is_subnet_of(arg0, arg1)

===

# Chain 331
import ipaddress
arg0 = IPv4Network('0.0.0.5/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
arg1 = IPv4Network('0.0.0.5/32')
result1 = ipaddress._is_subnet_of(arg1, arg0)

===

# Chain 332
import ipaddress
arg0 = IPv4Network('0.0.0.3/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.subnet_of(arg0)

===

# Chain 333
import ipaddress
arg0 = IPv4Network('0.0.0.5/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.supernet_of(arg0)

===

# Chain 334
import ipaddress
arg0 = IPv4Network('0.0.0.1/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__eq__(arg0)

===

# Chain 335
import ipaddress
arg0 = IPv4Network('0.0.0.2/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__lt__(arg0)

===

# Chain 336
import ipaddress
arg0 = IPv4Network('0.0.0.4/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__init__(arg0)

===

# Chain 337
import ipaddress
arg0 = IPv4Network('0.0.0.4/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__eq__(arg0)

===

# Chain 338
import ipaddress
arg0 = IPv4Network('0.0.0.1/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__eq__(arg0)

===

# Chain 339
import ipaddress
arg0 = IPv4Network('0.0.0.5/32')
result0 = ipaddress.ip_network(arg0, fuzz_input)
result1 = ipaddress.__lt__(arg0)

===

# Chain 340
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress._split_optional_netmask(result0)

===

# Chain 341
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.get_mixed_type_key(result0)

===

# Chain 342
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress._split_addr_prefix(result0)

===

# Chain 343
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 344
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 345
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 346
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 347
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__contains__(result0)

===

# Chain 348
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 349
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 350
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 351
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 352
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 353
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 354
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 355
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.subnets(result0)

===

# Chain 356
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.supernet(result0)

===

# Chain 357
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress._split_optional_netmask(result0)

===

# Chain 358
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.get_mixed_type_key(result0)

===

# Chain 359
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
arg0 = IPv4Network('0.0.0.0/32')
result1 = ipaddress._split_addr_prefix(result0, arg0)

===

# Chain 360
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 361
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 362
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 363
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 364
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__contains__(result0)

===

# Chain 365
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 366
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 367
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 368
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 369
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 370
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 371
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 372
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress._split_optional_netmask(fuzz_input)

===

# Chain 373
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.get_mixed_type_key(fuzz_input)

===

# Chain 374
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
arg0 = IPv4Network('0.0.0.2/32')
result1 = ipaddress._split_addr_prefix(fuzz_input, arg0)

===

# Chain 375
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 376
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 377
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 378
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 379
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__contains__(fuzz_input)

===

# Chain 380
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__init__(fuzz_input)

===

# Chain 381
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 382
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 383
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 384
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__init__(fuzz_input)

===

# Chain 385
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 386
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 387
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress._split_optional_netmask(result0)

===

# Chain 388
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.get_mixed_type_key(result0)

===

# Chain 389
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress._split_addr_prefix(result0)

===

# Chain 390
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 391
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 392
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 393
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 394
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__contains__(result0)

===

# Chain 395
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 396
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 397
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 398
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 399
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 400
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 401
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 402
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.subnets(result0)

===

# Chain 403
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.supernet(result0)

===

# Chain 404
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress._split_optional_netmask(result0)

===

# Chain 405
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.get_mixed_type_key(result0)

===

# Chain 406
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
arg0 = IPv4Network('0.0.0.5/32')
result1 = ipaddress._split_addr_prefix(result0, arg0)

===

# Chain 407
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 408
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 409
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 410
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 411
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__contains__(result0)

===

# Chain 412
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 413
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 414
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 415
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 416
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 417
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 418
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__lt__(result0)

===

# Chain 419
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress._split_optional_netmask(fuzz_input)

===

# Chain 420
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.get_mixed_type_key(fuzz_input)

===

# Chain 421
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
arg0 = IPv4Network('0.0.0.0/32')
result1 = ipaddress._split_addr_prefix(fuzz_input, arg0)

===

# Chain 422
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 423
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 424
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 425
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 426
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__contains__(fuzz_input)

===

# Chain 427
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__init__(fuzz_input)

===

# Chain 428
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 429
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 430
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 431
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__init__(fuzz_input)

===

# Chain 432
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 433
import ipaddress
result0 = ipaddress.ip_interface(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 434
import ipaddress
result0 = ipaddress.v4_int_to_packed(fuzz_input)
result1 = ipaddress.ip_address(result0)

===

# Chain 435
import ipaddress
result0 = ipaddress.v4_int_to_packed(fuzz_input)
result1 = ipaddress.ip_interface(result0)

===

# Chain 436
import ipaddress
result0 = ipaddress.v4_int_to_packed(fuzz_input)
result1 = ipaddress._split_addr_prefix(result0)

===

# Chain 437
import ipaddress
result0 = ipaddress.v4_int_to_packed(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 438
import ipaddress
result0 = ipaddress.v4_int_to_packed(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 439
import ipaddress
result0 = ipaddress.v4_int_to_packed(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 440
import ipaddress
result0 = ipaddress.v4_int_to_packed(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 441
import ipaddress
result0 = ipaddress.v4_int_to_packed(fuzz_input)
result1 = ipaddress.subnets(result0)

===

# Chain 442
import ipaddress
result0 = ipaddress.v4_int_to_packed(fuzz_input)
result1 = ipaddress.supernet(result0)

===

# Chain 443
import ipaddress
result0 = ipaddress.v4_int_to_packed(fuzz_input)
result1 = ipaddress.ip_address(result0)

===

# Chain 444
import ipaddress
result0 = ipaddress.v4_int_to_packed(fuzz_input)
result1 = ipaddress.ip_interface(result0)

===

# Chain 445
import ipaddress
result0 = ipaddress.v4_int_to_packed(fuzz_input)
arg0 = -598
result1 = ipaddress._check_packed_address(result0, arg0)

===

# Chain 446
import ipaddress
result0 = ipaddress.v4_int_to_packed(fuzz_input)
arg0 = IPv4Network('0.0.0.0/32')
result1 = ipaddress._split_addr_prefix(result0, arg0)

===

# Chain 447
import ipaddress
result0 = ipaddress.v4_int_to_packed(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 448
import ipaddress
result0 = ipaddress.v4_int_to_packed(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 449
import ipaddress
result0 = ipaddress.v4_int_to_packed(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 450
import ipaddress
result0 = ipaddress.v4_int_to_packed(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 451
import ipaddress
result0 = ipaddress.v4_int_to_packed(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 452
import ipaddress
result0 = ipaddress.v4_int_to_packed(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 453
import ipaddress
result0 = ipaddress.v6_int_to_packed(fuzz_input)
result1 = ipaddress.ip_address(result0)

===

# Chain 454
import ipaddress
result0 = ipaddress.v6_int_to_packed(fuzz_input)
result1 = ipaddress.ip_interface(result0)

===

# Chain 455
import ipaddress
result0 = ipaddress.v6_int_to_packed(fuzz_input)
result1 = ipaddress._split_addr_prefix(result0)

===

# Chain 456
import ipaddress
result0 = ipaddress.v6_int_to_packed(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 457
import ipaddress
result0 = ipaddress.v6_int_to_packed(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 458
import ipaddress
result0 = ipaddress.v6_int_to_packed(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 459
import ipaddress
result0 = ipaddress.v6_int_to_packed(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 460
import ipaddress
result0 = ipaddress.v6_int_to_packed(fuzz_input)
result1 = ipaddress.subnets(result0)

===

# Chain 461
import ipaddress
result0 = ipaddress.v6_int_to_packed(fuzz_input)
result1 = ipaddress.supernet(result0)

===

# Chain 462
import ipaddress
result0 = ipaddress.v6_int_to_packed(fuzz_input)
result1 = ipaddress.ip_address(result0)

===

# Chain 463
import ipaddress
result0 = ipaddress.v6_int_to_packed(fuzz_input)
result1 = ipaddress.ip_interface(result0)

===

# Chain 464
import ipaddress
result0 = ipaddress.v6_int_to_packed(fuzz_input)
arg0 = 224
result1 = ipaddress._check_packed_address(result0, arg0)

===

# Chain 465
import ipaddress
result0 = ipaddress.v6_int_to_packed(fuzz_input)
arg0 = IPv4Network('0.0.0.0/32')
result1 = ipaddress._split_addr_prefix(result0, arg0)

===

# Chain 466
import ipaddress
result0 = ipaddress.v6_int_to_packed(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 467
import ipaddress
result0 = ipaddress.v6_int_to_packed(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 468
import ipaddress
result0 = ipaddress.v6_int_to_packed(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 469
import ipaddress
result0 = ipaddress.v6_int_to_packed(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 470
import ipaddress
result0 = ipaddress.v6_int_to_packed(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 471
import ipaddress
result0 = ipaddress.v6_int_to_packed(fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 472
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress._find_address_range(result0)

===

# Chain 473
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress._collapse_addresses_internal(result0)

===

# Chain 474
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.collapse_addresses(result0)

===

# Chain 475
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 476
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 477
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress._compress_hextets(result0)

===

# Chain 478
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 479
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 480
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.subnets(result0)

===

# Chain 481
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.supernet(result0)

===

# Chain 482
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress._find_address_range(result0)

===

# Chain 483
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress._collapse_addresses_internal(result0)

===

# Chain 484
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.collapse_addresses(result0)

===

# Chain 485
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 486
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 487
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
arg0 = [980.2991689595008, 998.8123159459847, 173.89241979359804]
result1 = ipaddress._compress_hextets(result0, arg0)

===

# Chain 488
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 489
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 490
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.ip_network(fuzz_input)

===

# Chain 491
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
arg0 = IPv6Address('::')
result1 = ipaddress.summarize_address_range(fuzz_input, arg0)

===

# Chain 492
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
arg0 = IPv6Address('::4')
result1 = ipaddress.summarize_address_range(arg0, fuzz_input)

===

# Chain 493
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.get_mixed_type_key(fuzz_input)

===

# Chain 494
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
arg0 = IPv4Network('0.0.0.1/32')
result1 = ipaddress._split_addr_prefix(fuzz_input, arg0)

===

# Chain 495
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 496
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 497
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 498
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 499
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__contains__(fuzz_input)

===

# Chain 500
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.overlaps(fuzz_input)

===

# Chain 501
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.address_exclude(fuzz_input)

===

# Chain 502
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.compare_networks(fuzz_input)

===

# Chain 503
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
arg0 = IPv4Network('0.0.0.3/32')
result1 = ipaddress._is_subnet_of(fuzz_input, arg0)

===

# Chain 504
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
arg0 = IPv4Network('0.0.0.2/32')
result1 = ipaddress._is_subnet_of(arg0, fuzz_input)

===

# Chain 505
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.subnet_of(fuzz_input)

===

# Chain 506
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.supernet_of(fuzz_input)

===

# Chain 507
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 508
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 509
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__init__(fuzz_input)

===

# Chain 510
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 511
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 512
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 513
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.ip_interface(fuzz_input)

===

# Chain 514
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__init__(fuzz_input)

===

# Chain 515
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__init__(fuzz_input)

===

# Chain 516
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress._find_address_range(result0)

===

# Chain 517
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress._collapse_addresses_internal(result0)

===

# Chain 518
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.collapse_addresses(result0)

===

# Chain 519
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 520
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 521
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress._compress_hextets(result0)

===

# Chain 522
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 523
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 524
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.subnets(result0)

===

# Chain 525
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.supernet(result0)

===

# Chain 526
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress._find_address_range(result0)

===

# Chain 527
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress._collapse_addresses_internal(result0)

===

# Chain 528
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.collapse_addresses(result0)

===

# Chain 529
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 530
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 531
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
arg0 = [822, 709, 690, -154]
result1 = ipaddress._compress_hextets(result0, arg0)

===

# Chain 532
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 533
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 534
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.ip_network(fuzz_input)

===

# Chain 535
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
arg0 = IPv6Address('::2')
result1 = ipaddress.summarize_address_range(fuzz_input, arg0)

===

# Chain 536
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
arg0 = IPv6Address('::5')
result1 = ipaddress.summarize_address_range(arg0, fuzz_input)

===

# Chain 537
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.get_mixed_type_key(fuzz_input)

===

# Chain 538
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
arg0 = IPv4Network('0.0.0.3/32')
result1 = ipaddress._split_addr_prefix(fuzz_input, arg0)

===

# Chain 539
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 540
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 541
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 542
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 543
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__contains__(fuzz_input)

===

# Chain 544
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.overlaps(fuzz_input)

===

# Chain 545
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.address_exclude(fuzz_input)

===

# Chain 546
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.compare_networks(fuzz_input)

===

# Chain 547
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
arg0 = IPv4Network('0.0.0.3/32')
result1 = ipaddress._is_subnet_of(fuzz_input, arg0)

===

# Chain 548
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
arg0 = IPv4Network('0.0.0.4/32')
result1 = ipaddress._is_subnet_of(arg0, fuzz_input)

===

# Chain 549
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.subnet_of(fuzz_input)

===

# Chain 550
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.supernet_of(fuzz_input)

===

# Chain 551
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 552
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 553
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__init__(fuzz_input)

===

# Chain 554
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 555
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 556
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 557
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.ip_interface(fuzz_input)

===

# Chain 558
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__init__(fuzz_input)

===

# Chain 559
import ipaddress
result0 = ipaddress._split_optional_netmask(fuzz_input)
result1 = ipaddress.__init__(fuzz_input)

===

# Chain 560
import ipaddress
arg0 = 552
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.ip_address(result0)

===

# Chain 561
import ipaddress
arg0 = 975
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.v4_int_to_packed(result0)

===

# Chain 562
import ipaddress
arg0 = 998
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.v6_int_to_packed(result0)

===

# Chain 563
import ipaddress
arg0 = -276
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress._check_int_address(result0)

===

# Chain 564
import ipaddress
arg0 = 306
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress._ip_int_from_prefix(result0)

===

# Chain 565
import ipaddress
arg0 = 796
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress._prefix_from_ip_int(result0)

===

# Chain 566
import ipaddress
arg0 = 443
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress._report_invalid_netmask(result0)

===

# Chain 567
import ipaddress
arg0 = -497
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress._split_addr_prefix(result0)

===

# Chain 568
import ipaddress
arg0 = -60
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.__eq__(result0)

===

# Chain 569
import ipaddress
arg0 = -308
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.__add__(result0)

===

# Chain 570
import ipaddress
arg0 = -306
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.__sub__(result0)

===

# Chain 571
import ipaddress
arg0 = -68
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.__getitem__(result0)

===

# Chain 572
import ipaddress
arg0 = 78
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress._make_netmask(result0)

===

# Chain 573
import ipaddress
arg0 = -860
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress._string_from_ip_int(result0)

===

# Chain 574
import ipaddress
arg0 = -549
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.__init__(result0)

===

# Chain 575
import ipaddress
arg0 = -865
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.__init__(result0)

===

# Chain 576
import ipaddress
arg0 = 391
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.__eq__(result0)

===

# Chain 577
import ipaddress
arg0 = -894
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress._make_netmask(result0)

===

# Chain 578
import ipaddress
arg0 = -707
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress._string_from_ip_int(result0)

===

# Chain 579
import ipaddress
arg0 = 101
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.__init__(result0)

===

# Chain 580
import ipaddress
arg0 = -17
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.__eq__(result0)

===

# Chain 581
import ipaddress
arg0 = -819
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.__init__(result0)

===

# Chain 582
import ipaddress
arg0 = -151
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.__eq__(result0)

===

# Chain 583
import ipaddress
arg0 = 693
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.ip_address(result0)

===

# Chain 584
import ipaddress
arg0 = 782
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.ip_network(result0)

===

# Chain 585
import ipaddress
arg0 = 68
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.v4_int_to_packed(result0)

===

# Chain 586
import ipaddress
arg0 = -587
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.v6_int_to_packed(result0)

===

# Chain 587
import ipaddress
arg0 = 157
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress._check_int_address(result0)

===

# Chain 588
import ipaddress
arg0 = 713
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
arg1 = b'\xfa\x89\xfd\xd8!<SF]\x1d&\xba\x96\xb5\x8e\xf3q\xc7\xcd\x98$\x19\x0e8\xc5;\xce\x03fv'
result1 = ipaddress._check_packed_address(arg1, result0)

===

# Chain 589
import ipaddress
arg0 = 3
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
arg1 = -186
result1 = ipaddress._ip_int_from_prefix(result0, arg1)

===

# Chain 590
import ipaddress
arg0 = -712
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
arg1 = -59
result1 = ipaddress._prefix_from_ip_int(result0, arg1)

===

# Chain 591
import ipaddress
arg0 = -307
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
arg1 = 511
result1 = ipaddress._report_invalid_netmask(result0, arg1)

===

# Chain 592
import ipaddress
arg0 = 996
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
arg1 = IPv4Network('0.0.0.3/32')
result1 = ipaddress._split_addr_prefix(result0, arg1)

===

# Chain 593
import ipaddress
arg0 = -611
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.__eq__(result0)

===

# Chain 594
import ipaddress
arg0 = -259
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.__add__(result0)

===

# Chain 595
import ipaddress
arg0 = -800
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.__sub__(result0)

===

# Chain 596
import ipaddress
arg0 = -523
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.__getitem__(result0)

===

# Chain 597
import ipaddress
arg0 = -136
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.subnets(result0)

===

# Chain 598
import ipaddress
arg0 = -630
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.subnets(result0)

===

# Chain 599
import ipaddress
arg0 = 603
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.supernet(result0)

===

# Chain 600
import ipaddress
arg0 = -230
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.supernet(result0)

===

# Chain 601
import ipaddress
arg0 = -162
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
arg1 = 587
result1 = ipaddress._make_netmask(result0, arg1)

===

# Chain 602
import ipaddress
arg0 = 414
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
arg1 = 213
result1 = ipaddress._string_from_ip_int(result0, arg1)

===

# Chain 603
import ipaddress
arg0 = 213
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.__init__(result0)

===

# Chain 604
import ipaddress
arg0 = -984
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.__init__(result0)

===

# Chain 605
import ipaddress
arg0 = -435
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.__eq__(result0)

===

# Chain 606
import ipaddress
arg0 = -750
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.__init__(result0)

===

# Chain 607
import ipaddress
arg0 = 590
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
arg1 = -366
result1 = ipaddress._make_netmask(result0, arg1)

===

# Chain 608
import ipaddress
arg0 = 650
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress._string_from_ip_int(result0)

===

# Chain 609
import ipaddress
arg0 = -612
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.__init__(result0)

===

# Chain 610
import ipaddress
arg0 = 835
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.__eq__(result0)

===

# Chain 611
import ipaddress
arg0 = -200
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.__init__(result0)

===

# Chain 612
import ipaddress
arg0 = 870
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.__eq__(result0)

===

# Chain 613
import ipaddress
arg0 = -859
result0 = ipaddress._count_righthand_zero_bits(fuzz_input, arg0)
result1 = ipaddress.__init__(result0)

===

# Chain 614
import ipaddress
arg0 = 929
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.ip_address(result0)

===

# Chain 615
import ipaddress
arg0 = 362
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.v4_int_to_packed(result0)

===

# Chain 616
import ipaddress
arg0 = -903
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.v6_int_to_packed(result0)

===

# Chain 617
import ipaddress
arg0 = 147
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress._check_int_address(result0)

===

# Chain 618
import ipaddress
arg0 = 342
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress._ip_int_from_prefix(result0)

===

# Chain 619
import ipaddress
arg0 = -476
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress._prefix_from_ip_int(result0)

===

# Chain 620
import ipaddress
arg0 = 67
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress._report_invalid_netmask(result0)

===

# Chain 621
import ipaddress
arg0 = 852
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress._split_addr_prefix(result0)

===

# Chain 622
import ipaddress
arg0 = 324
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 623
import ipaddress
arg0 = 536
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.__add__(result0)

===

# Chain 624
import ipaddress
arg0 = -803
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.__sub__(result0)

===

# Chain 625
import ipaddress
arg0 = 668
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.__getitem__(result0)

===

# Chain 626
import ipaddress
arg0 = -307
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress._make_netmask(result0)

===

# Chain 627
import ipaddress
arg0 = -162
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress._string_from_ip_int(result0)

===

# Chain 628
import ipaddress
arg0 = -906
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 629
import ipaddress
arg0 = -115
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 630
import ipaddress
arg0 = -901
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 631
import ipaddress
arg0 = 978
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress._make_netmask(result0)

===

# Chain 632
import ipaddress
arg0 = 382
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress._string_from_ip_int(result0)

===

# Chain 633
import ipaddress
arg0 = -486
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 634
import ipaddress
arg0 = 985
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 635
import ipaddress
arg0 = 826
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 636
import ipaddress
arg0 = -771
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 637
import ipaddress
arg0 = -341
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.ip_address(result0)

===

# Chain 638
import ipaddress
arg0 = -540
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.ip_network(result0)

===

# Chain 639
import ipaddress
arg0 = -663
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.v4_int_to_packed(result0)

===

# Chain 640
import ipaddress
arg0 = -221
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.v6_int_to_packed(result0)

===

# Chain 641
import ipaddress
arg0 = 703
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress._check_int_address(result0)

===

# Chain 642
import ipaddress
arg0 = -862
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
arg1 = b'\xd8\xf9\\`'
result1 = ipaddress._check_packed_address(arg1, result0)

===

# Chain 643
import ipaddress
arg0 = 912
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
arg1 = -189
result1 = ipaddress._ip_int_from_prefix(result0, arg1)

===

# Chain 644
import ipaddress
arg0 = 99
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
arg1 = 704
result1 = ipaddress._prefix_from_ip_int(result0, arg1)

===

# Chain 645
import ipaddress
arg0 = 720
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
arg1 = 422
result1 = ipaddress._report_invalid_netmask(result0, arg1)

===

# Chain 646
import ipaddress
arg0 = -668
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
arg1 = IPv4Network('0.0.0.0/32')
result1 = ipaddress._split_addr_prefix(result0, arg1)

===

# Chain 647
import ipaddress
arg0 = -367
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 648
import ipaddress
arg0 = -750
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.__add__(result0)

===

# Chain 649
import ipaddress
arg0 = 315
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.__sub__(result0)

===

# Chain 650
import ipaddress
arg0 = 83
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.__getitem__(result0)

===

# Chain 651
import ipaddress
arg0 = 736
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.subnets(result0)

===

# Chain 652
import ipaddress
arg0 = -19
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.subnets(result0)

===

# Chain 653
import ipaddress
arg0 = -493
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.supernet(result0)

===

# Chain 654
import ipaddress
arg0 = -852
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.supernet(result0)

===

# Chain 655
import ipaddress
arg0 = 880
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
arg1 = -272
result1 = ipaddress._make_netmask(result0, arg1)

===

# Chain 656
import ipaddress
arg0 = -225
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
arg1 = -840
result1 = ipaddress._string_from_ip_int(result0, arg1)

===

# Chain 657
import ipaddress
arg0 = 434
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 658
import ipaddress
arg0 = 152
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 659
import ipaddress
arg0 = -849
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 660
import ipaddress
arg0 = -663
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 661
import ipaddress
arg0 = -686
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
arg1 = 'KRINBTe'
result1 = ipaddress._make_netmask(result0, arg1)

===

# Chain 662
import ipaddress
arg0 = 924
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress._string_from_ip_int(result0)

===

# Chain 663
import ipaddress
arg0 = -949
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 664
import ipaddress
arg0 = -882
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 665
import ipaddress
arg0 = 251
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 666
import ipaddress
arg0 = -737
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.__eq__(result0)

===

# Chain 667
import ipaddress
arg0 = -899
result0 = ipaddress._count_righthand_zero_bits(arg0, fuzz_input)
result1 = ipaddress.__init__(result0)

===

# Chain 668
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.subnets(obj0)

===

# Chain 669
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.supernet(obj0)

===

# Chain 670
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
arg0 = IPv6Address('::2')
result0 = ipaddress.summarize_address_range(fuzz_input, arg0)

===

# Chain 671
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
arg0 = IPv6Address('::4')
result0 = ipaddress.summarize_address_range(arg0, fuzz_input)

===

# Chain 672
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.get_mixed_type_key(fuzz_input)

===

# Chain 673
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 674
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 675
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 676
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 677
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__contains__(fuzz_input)

===

# Chain 678
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.address_exclude(fuzz_input)

===

# Chain 679
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 680
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 681
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 682
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 683
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 684
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.packed()

===

# Chain 685
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_reserved()

===

# Chain 686
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_private()

===

# Chain 687
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_global()

===

# Chain 688
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_multicast()

===

# Chain 689
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_unspecified()

===

# Chain 690
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_loopback()

===

# Chain 691
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_link_local()

===

# Chain 692
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.subnets(obj0)

===

# Chain 693
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.supernet(obj0)

===

# Chain 694
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
arg0 = IPv6Address('::4')
result0 = ipaddress.summarize_address_range(fuzz_input, arg0)

===

# Chain 695
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
arg0 = IPv6Address('::1')
result0 = ipaddress.summarize_address_range(arg0, fuzz_input)

===

# Chain 696
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.get_mixed_type_key(fuzz_input)

===

# Chain 697
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 698
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 699
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 700
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 701
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__contains__(fuzz_input)

===

# Chain 702
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.address_exclude(fuzz_input)

===

# Chain 703
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 704
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 705
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 706
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 707
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 708
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.packed()

===

# Chain 709
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_reserved()

===

# Chain 710
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_private()

===

# Chain 711
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_global()

===

# Chain 712
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_multicast()

===

# Chain 713
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_unspecified()

===

# Chain 714
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_loopback()

===

# Chain 715
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_link_local()

===

# Chain 716
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.subnets(obj0)

===

# Chain 717
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.supernet(obj0)

===

# Chain 718
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
arg0 = IPv6Address('::4')
result0 = ipaddress.summarize_address_range(fuzz_input, arg0)

===

# Chain 719
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
arg0 = IPv6Address('::4')
result0 = ipaddress.summarize_address_range(arg0, fuzz_input)

===

# Chain 720
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.get_mixed_type_key(fuzz_input)

===

# Chain 721
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 722
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 723
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 724
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 725
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__contains__(fuzz_input)

===

# Chain 726
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.address_exclude(fuzz_input)

===

# Chain 727
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 728
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 729
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 730
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 731
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 732
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.packed()

===

# Chain 733
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_reserved()

===

# Chain 734
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_private()

===

# Chain 735
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_global()

===

# Chain 736
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_multicast()

===

# Chain 737
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_unspecified()

===

# Chain 738
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_loopback()

===

# Chain 739
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_link_local()

===

# Chain 740
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.subnets(obj0)

===

# Chain 741
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.supernet(obj0)

===

# Chain 742
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
arg0 = IPv6Address('::4')
result0 = ipaddress.summarize_address_range(fuzz_input, arg0)

===

# Chain 743
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
arg0 = IPv6Address('::3')
result0 = ipaddress.summarize_address_range(arg0, fuzz_input)

===

# Chain 744
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.get_mixed_type_key(fuzz_input)

===

# Chain 745
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 746
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 747
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 748
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 749
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__contains__(fuzz_input)

===

# Chain 750
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.address_exclude(fuzz_input)

===

# Chain 751
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 752
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 753
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 754
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 755
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 756
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.packed()

===

# Chain 757
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_reserved()

===

# Chain 758
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_private()

===

# Chain 759
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_global()

===

# Chain 760
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_multicast()

===

# Chain 761
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_unspecified()

===

# Chain 762
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_loopback()

===

# Chain 763
import ipaddress
obj0 = ipaddress.IPv4Address(fuzz_input)
result0 = obj0.is_link_local()

===

# Chain 764
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.subnets(obj0)

===

# Chain 765
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.supernet(obj0)

===

# Chain 766
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.ip_interface(fuzz_input)

===

# Chain 767
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress._split_optional_netmask(fuzz_input)

===

# Chain 768
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.get_mixed_type_key(fuzz_input)

===

# Chain 769
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
arg0 = IPv4Network('0.0.0.1/32')
result0 = ipaddress._split_addr_prefix(fuzz_input, arg0)

===

# Chain 770
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 771
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 772
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 773
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 774
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__contains__(fuzz_input)

===

# Chain 775
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 776
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 777
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 778
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__init__(fuzz_input)

===

# Chain 779
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 780
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 781
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.hostmask()

===

# Chain 782
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.__str__()

===

# Chain 783
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
arg0 = IPv4Network('0.0.0.2/32')
result0 = obj0.__eq__(arg0)

===

# Chain 784
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
arg0 = IPv4Network('0.0.0.3/32')
result0 = obj0.__lt__(arg0)

===

# Chain 785
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.__hash__()

===

# Chain 786
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.ip()

===

# Chain 787
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.with_prefixlen()

===

# Chain 788
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.with_netmask()

===

# Chain 789
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.with_hostmask()

===

# Chain 790
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.subnets(obj0)

===

# Chain 791
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.supernet(obj0)

===

# Chain 792
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.ip_interface(fuzz_input)

===

# Chain 793
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress._split_optional_netmask(fuzz_input)

===

# Chain 794
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.get_mixed_type_key(fuzz_input)

===

# Chain 795
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
arg0 = IPv4Network('0.0.0.4/32')
result0 = ipaddress._split_addr_prefix(fuzz_input, arg0)

===

# Chain 796
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 797
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 798
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 799
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 800
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__contains__(fuzz_input)

===

# Chain 801
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 802
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 803
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 804
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__init__(fuzz_input)

===

# Chain 805
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 806
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 807
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.hostmask()

===

# Chain 808
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.__str__()

===

# Chain 809
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
arg0 = IPv4Network('0.0.0.5/32')
result0 = obj0.__lt__(arg0)

===

# Chain 810
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.__hash__()

===

# Chain 811
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.ip()

===

# Chain 812
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.with_prefixlen()

===

# Chain 813
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.with_netmask()

===

# Chain 814
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.with_hostmask()

===

# Chain 815
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.subnets(obj0)

===

# Chain 816
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.supernet(obj0)

===

# Chain 817
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.ip_interface(fuzz_input)

===

# Chain 818
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress._split_optional_netmask(fuzz_input)

===

# Chain 819
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.get_mixed_type_key(fuzz_input)

===

# Chain 820
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
arg0 = IPv4Network('0.0.0.5/32')
result0 = ipaddress._split_addr_prefix(fuzz_input, arg0)

===

# Chain 821
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 822
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 823
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 824
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 825
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__contains__(fuzz_input)

===

# Chain 826
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 827
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 828
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 829
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__init__(fuzz_input)

===

# Chain 830
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 831
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 832
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.hostmask()

===

# Chain 833
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.__str__()

===

# Chain 834
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
arg0 = IPv4Network('0.0.0.5/32')
result0 = obj0.__lt__(arg0)

===

# Chain 835
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.__hash__()

===

# Chain 836
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.ip()

===

# Chain 837
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.with_prefixlen()

===

# Chain 838
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.with_netmask()

===

# Chain 839
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.with_hostmask()

===

# Chain 840
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.subnets(obj0)

===

# Chain 841
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.supernet(obj0)

===

# Chain 842
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.ip_interface(fuzz_input)

===

# Chain 843
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress._split_optional_netmask(fuzz_input)

===

# Chain 844
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.get_mixed_type_key(fuzz_input)

===

# Chain 845
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
arg0 = IPv4Network('0.0.0.0/32')
result0 = ipaddress._split_addr_prefix(fuzz_input, arg0)

===

# Chain 846
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 847
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 848
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 849
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 850
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__contains__(fuzz_input)

===

# Chain 851
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 852
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 853
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 854
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__init__(fuzz_input)

===

# Chain 855
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 856
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 857
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.hostmask()

===

# Chain 858
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.__str__()

===

# Chain 859
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
arg0 = IPv4Network('0.0.0.5/32')
result0 = obj0.__eq__(arg0)

===

# Chain 860
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
arg0 = IPv4Network('0.0.0.5/32')
result0 = obj0.__lt__(arg0)

===

# Chain 861
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.__hash__()

===

# Chain 862
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.ip()

===

# Chain 863
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.with_prefixlen()

===

# Chain 864
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.with_netmask()

===

# Chain 865
import ipaddress
obj0 = ipaddress.IPv4Interface(fuzz_input)
result0 = obj0.with_hostmask()

===

# Chain 866
import ipaddress
arg0 = IPv6Interface('::2/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
arg1 = IPv4Network('0.0.0.0/32')
result1 = ipaddress.ip_network(arg1, result0)

===

# Chain 867
import ipaddress
arg0 = IPv6Interface('::3/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
arg1 = IPv4Network('0.0.0.1/32')
result1 = ipaddress.__init__(arg1, result0)

===

# Chain 868
import ipaddress
arg0 = IPv6Interface('::4/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
arg1 = 669
result1 = ipaddress.__init__(arg1, result0)

===

# Chain 869
import ipaddress
arg0 = IPv6Interface('::4/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.ip_network(fuzz_input)

===

# Chain 870
import ipaddress
arg0 = IPv6Interface('::2/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress._split_optional_netmask(fuzz_input)

===

# Chain 871
import ipaddress
arg0 = IPv6Interface('::2/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
arg1 = IPv6Address('::4')
result1 = ipaddress.summarize_address_range(fuzz_input, arg1)

===

# Chain 872
import ipaddress
arg0 = IPv6Interface('::3/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
arg1 = IPv6Address('::3')
result1 = ipaddress.summarize_address_range(arg1, fuzz_input)

===

# Chain 873
import ipaddress
arg0 = IPv6Interface('::5/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.get_mixed_type_key(fuzz_input)

===

# Chain 874
import ipaddress
arg0 = IPv6Interface('::4/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
arg1 = IPv4Network('0.0.0.4/32')
result1 = ipaddress._split_addr_prefix(fuzz_input, arg1)

===

# Chain 875
import ipaddress
arg0 = IPv6Interface('::5/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 876
import ipaddress
arg0 = IPv6Interface('::3/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 877
import ipaddress
arg0 = IPv6Interface('::/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 878
import ipaddress
arg0 = IPv6Interface('::2/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 879
import ipaddress
arg0 = IPv6Interface('::3/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__contains__(fuzz_input)

===

# Chain 880
import ipaddress
arg0 = IPv6Interface('::4/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.overlaps(fuzz_input)

===

# Chain 881
import ipaddress
arg0 = IPv6Interface('::/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.address_exclude(fuzz_input)

===

# Chain 882
import ipaddress
arg0 = IPv6Interface('::/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.compare_networks(fuzz_input)

===

# Chain 883
import ipaddress
arg0 = IPv6Interface('::4/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
arg1 = IPv4Network('0.0.0.3/32')
result1 = ipaddress._is_subnet_of(fuzz_input, arg1)

===

# Chain 884
import ipaddress
arg0 = IPv6Interface('::4/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
arg1 = IPv4Network('0.0.0.1/32')
result1 = ipaddress._is_subnet_of(arg1, fuzz_input)

===

# Chain 885
import ipaddress
arg0 = IPv6Interface('::3/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.subnet_of(fuzz_input)

===

# Chain 886
import ipaddress
arg0 = IPv6Interface('::4/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.supernet_of(fuzz_input)

===

# Chain 887
import ipaddress
arg0 = IPv6Interface('::2/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 888
import ipaddress
arg0 = IPv6Interface('::3/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__init__(fuzz_input)

===

# Chain 889
import ipaddress
arg0 = IPv6Interface('::/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 890
import ipaddress
arg0 = IPv6Interface('::/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 891
import ipaddress
arg0 = IPv6Interface('::/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 892
import ipaddress
arg0 = IPv6Interface('::3/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__init__(fuzz_input)

===

# Chain 893
import ipaddress
arg0 = IPv6Interface('::1/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__init__(fuzz_input)

===

# Chain 894
import ipaddress
arg0 = IPv6Interface('::2/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.ip_interface(fuzz_input)

===

# Chain 895
import ipaddress
arg0 = IPv6Interface('::/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__init__(fuzz_input)

===

# Chain 896
import ipaddress
arg0 = IPv6Interface('::4/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress._find_address_range(fuzz_input)

===

# Chain 897
import ipaddress
arg0 = IPv6Interface('::2/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress._collapse_addresses_internal(fuzz_input)

===

# Chain 898
import ipaddress
arg0 = IPv6Interface('::1/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.collapse_addresses(fuzz_input)

===

# Chain 899
import ipaddress
arg0 = IPv6Interface('::/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
arg1 = ['li3TdV0&E']
result1 = ipaddress._compress_hextets(fuzz_input, arg1)

===

# Chain 900
import ipaddress
arg0 = IPv6Interface('::/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = obj0.hostmask()

===

# Chain 901
import ipaddress
arg0 = IPv6Interface('::1/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = obj0.__str__()

===

# Chain 902
import ipaddress
arg0 = IPv6Interface('::5/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
arg1 = IPv4Network('0.0.0.3/32')
result1 = obj0.__lt__(arg1)

===

# Chain 903
import ipaddress
arg0 = IPv6Interface('::5/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = obj0.__hash__()

===

# Chain 904
import ipaddress
arg0 = IPv6Interface('::4/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = obj0.ip()

===

# Chain 905
import ipaddress
arg0 = IPv6Interface('::3/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = obj0.with_prefixlen()

===

# Chain 906
import ipaddress
arg0 = IPv6Interface('::3/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = obj0.with_netmask()

===

# Chain 907
import ipaddress
arg0 = IPv6Interface('::2/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = obj0.with_hostmask()

===

# Chain 908
import ipaddress
arg0 = IPv6Interface('::3/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
arg1 = IPv4Network('0.0.0.0/32')
result1 = ipaddress.ip_network(arg1, result0)

===

# Chain 909
import ipaddress
arg0 = IPv6Interface('::1/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
arg1 = IPv4Network('0.0.0.2/32')
result1 = ipaddress.__init__(arg1, result0)

===

# Chain 910
import ipaddress
arg0 = IPv6Interface('::4/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
arg1 = 844
result1 = ipaddress.__init__(arg1, result0)

===

# Chain 911
import ipaddress
arg0 = IPv6Interface('::3/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.ip_network(fuzz_input)

===

# Chain 912
import ipaddress
arg0 = IPv6Interface('::5/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress._split_optional_netmask(fuzz_input)

===

# Chain 913
import ipaddress
arg0 = IPv6Interface('::1/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
arg1 = IPv6Address('::5')
result1 = ipaddress.summarize_address_range(fuzz_input, arg1)

===

# Chain 914
import ipaddress
arg0 = IPv6Interface('::/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
arg1 = IPv6Address('::')
result1 = ipaddress.summarize_address_range(arg1, fuzz_input)

===

# Chain 915
import ipaddress
arg0 = IPv6Interface('::5/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.get_mixed_type_key(fuzz_input)

===

# Chain 916
import ipaddress
arg0 = IPv6Interface('::3/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
arg1 = IPv4Network('0.0.0.5/32')
result1 = ipaddress._split_addr_prefix(fuzz_input, arg1)

===

# Chain 917
import ipaddress
arg0 = IPv6Interface('::5/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 918
import ipaddress
arg0 = IPv6Interface('::5/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 919
import ipaddress
arg0 = IPv6Interface('::1/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 920
import ipaddress
arg0 = IPv6Interface('::1/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 921
import ipaddress
arg0 = IPv6Interface('::1/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__contains__(fuzz_input)

===

# Chain 922
import ipaddress
arg0 = IPv6Interface('::2/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.overlaps(fuzz_input)

===

# Chain 923
import ipaddress
arg0 = IPv6Interface('::/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.address_exclude(fuzz_input)

===

# Chain 924
import ipaddress
arg0 = IPv6Interface('::4/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.compare_networks(fuzz_input)

===

# Chain 925
import ipaddress
arg0 = IPv6Interface('::4/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
arg1 = IPv4Network('0.0.0.2/32')
result1 = ipaddress._is_subnet_of(fuzz_input, arg1)

===

# Chain 926
import ipaddress
arg0 = IPv6Interface('::/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
arg1 = IPv4Network('0.0.0.0/32')
result1 = ipaddress._is_subnet_of(arg1, fuzz_input)

===

# Chain 927
import ipaddress
arg0 = IPv6Interface('::1/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.subnet_of(fuzz_input)

===

# Chain 928
import ipaddress
arg0 = IPv6Interface('::1/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.supernet_of(fuzz_input)

===

# Chain 929
import ipaddress
arg0 = IPv6Interface('::/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 930
import ipaddress
arg0 = IPv6Interface('::/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__init__(fuzz_input)

===

# Chain 931
import ipaddress
arg0 = IPv6Interface('::2/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 932
import ipaddress
arg0 = IPv6Interface('::5/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__eq__(fuzz_input)

===

# Chain 933
import ipaddress
arg0 = IPv6Interface('::2/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__lt__(fuzz_input)

===

# Chain 934
import ipaddress
arg0 = IPv6Interface('::5/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__init__(fuzz_input)

===

# Chain 935
import ipaddress
arg0 = IPv6Interface('::/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__init__(fuzz_input)

===

# Chain 936
import ipaddress
arg0 = IPv6Interface('::4/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.ip_interface(fuzz_input)

===

# Chain 937
import ipaddress
arg0 = IPv6Interface('::5/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.__init__(fuzz_input)

===

# Chain 938
import ipaddress
arg0 = IPv6Interface('::2/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress._find_address_range(fuzz_input)

===

# Chain 939
import ipaddress
arg0 = IPv6Interface('::2/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress._collapse_addresses_internal(fuzz_input)

===

# Chain 940
import ipaddress
arg0 = IPv6Interface('::5/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = ipaddress.collapse_addresses(fuzz_input)

===

# Chain 941
import ipaddress
arg0 = IPv6Interface('::1/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
arg1 = [-210.75561180018076]
result1 = ipaddress._compress_hextets(fuzz_input, arg1)

===

# Chain 942
import ipaddress
arg0 = IPv6Interface('::4/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = obj0.hostmask()

===

# Chain 943
import ipaddress
arg0 = IPv6Interface('::3/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = obj0.__str__()

===

# Chain 944
import ipaddress
arg0 = IPv6Interface('::3/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
arg1 = IPv4Network('0.0.0.4/32')
result1 = obj0.__lt__(arg1)

===

# Chain 945
import ipaddress
arg0 = IPv6Interface('::4/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = obj0.__hash__()

===

# Chain 946
import ipaddress
arg0 = IPv6Interface('::/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = obj0.ip()

===

# Chain 947
import ipaddress
arg0 = IPv6Interface('::3/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = obj0.with_prefixlen()

===

# Chain 948
import ipaddress
arg0 = IPv6Interface('::5/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = obj0.with_netmask()

===

# Chain 949
import ipaddress
arg0 = IPv6Interface('::4/128')
obj0 = ipaddress.IPv4Interface(arg0)
result0 = obj0.__eq__(fuzz_input)
result1 = obj0.with_hostmask()

===

# Chain 950
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.subnets(obj0)

===

# Chain 951
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.supernet(obj0)

===

# Chain 952
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.ip_network(fuzz_input)

===

# Chain 953
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress._split_optional_netmask(fuzz_input)

===

# Chain 954
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
arg0 = IPv6Address('::3')
result0 = ipaddress.summarize_address_range(fuzz_input, arg0)

===

# Chain 955
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
arg0 = IPv6Address('::4')
result0 = ipaddress.summarize_address_range(arg0, fuzz_input)

===

# Chain 956
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.get_mixed_type_key(fuzz_input)

===

# Chain 957
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
arg0 = IPv4Network('0.0.0.5/32')
result0 = ipaddress._split_addr_prefix(fuzz_input, arg0)

===

# Chain 958
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 959
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 960
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 961
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 962
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.__contains__(fuzz_input)

===

# Chain 963
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.overlaps(fuzz_input)

===

# Chain 964
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.address_exclude(fuzz_input)

===

# Chain 965
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.compare_networks(fuzz_input)

===

# Chain 966
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
arg0 = IPv4Network('0.0.0.3/32')
result0 = ipaddress._is_subnet_of(fuzz_input, arg0)

===

# Chain 967
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
arg0 = IPv4Network('0.0.0.5/32')
result0 = ipaddress._is_subnet_of(arg0, fuzz_input)

===

# Chain 968
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.subnet_of(fuzz_input)

===

# Chain 969
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.supernet_of(fuzz_input)

===

# Chain 970
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 971
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 972
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 973
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 974
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 975
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = obj0.is_global()

===

# Chain 976
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.subnets(obj0)

===

# Chain 977
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.supernet(obj0)

===

# Chain 978
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.ip_network(fuzz_input)

===

# Chain 979
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress._split_optional_netmask(fuzz_input)

===

# Chain 980
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
arg0 = IPv6Address('::2')
result0 = ipaddress.summarize_address_range(fuzz_input, arg0)

===

# Chain 981
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
arg0 = IPv6Address('::4')
result0 = ipaddress.summarize_address_range(arg0, fuzz_input)

===

# Chain 982
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.get_mixed_type_key(fuzz_input)

===

# Chain 983
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
arg0 = IPv4Network('0.0.0.4/32')
result0 = ipaddress._split_addr_prefix(fuzz_input, arg0)

===

# Chain 984
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 985
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 986
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 987
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 988
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.__contains__(fuzz_input)

===

# Chain 989
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.overlaps(fuzz_input)

===

# Chain 990
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.address_exclude(fuzz_input)

===

# Chain 991
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.compare_networks(fuzz_input)

===

# Chain 992
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
arg0 = IPv4Network('0.0.0.0/32')
result0 = ipaddress._is_subnet_of(fuzz_input, arg0)

===

# Chain 993
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
arg0 = IPv4Network('0.0.0.0/32')
result0 = ipaddress._is_subnet_of(arg0, fuzz_input)

===

# Chain 994
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.subnet_of(fuzz_input)

===

# Chain 995
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.supernet_of(fuzz_input)

===

# Chain 996
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 997
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.__lt__(fuzz_input)

===

# Chain 998
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)

===

# Chain 999
import ipaddress
obj0 = ipaddress.IPv4Network(fuzz_input)
result0 = ipaddress.__eq__(fuzz_input)