"""Atheris harness: one entry per valid tinyfuzz chain."""
import sys
from pathlib import Path
import atheris

with atheris.instrument_imports():
    sys.path.insert(0, str(Path("cpython/Lib").resolve()))
    import ipaddress

IGNORE = (ValueError, TypeError, AttributeError, OSError, LookupError,
          AssertionError, EOFError, ModuleNotFoundError, OverflowError,
          NameError, SyntaxError)


def decode(t, data):
    s = data.decode("utf-8", "replace")
    if s.startswith("%&$%"):
        s = s[4:].split("%&$%")[0]
    if t == "int":
        try:
            return int(s)
        except ValueError:
            return 0
    if t == "float":
        try:
            return float(s)
        except ValueError:
            return 0.0
    if t == "bool":
        return bool(s)
    return s


def chain_0(data):
    fuzz_input = decode('bytes', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_address(fuzz_input)
    except IGNORE:
        pass

def chain_3(data):
    fuzz_input = decode('int', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_network(fuzz_input)
    except IGNORE:
        pass

def chain_6(data):
    fuzz_input = decode('bytes', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_interface(fuzz_input)
    except IGNORE:
        pass

def chain_14(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Address(fuzz_input)
    except IGNORE:
        pass

def chain_18(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Interface(fuzz_input)
    except IGNORE:
        pass

def chain_24(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Network(fuzz_input)
    except IGNORE:
        pass

def chain_29(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv6Address(fuzz_input)
    except IGNORE:
        pass

def chain_35(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv6Interface(fuzz_input)
    except IGNORE:
        pass

def chain_41(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv6Network(fuzz_input)
    except IGNORE:
        pass

def chain_46(data):
    fuzz_input = decode('bytes', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_address(fuzz_input)
        result1 = ipaddress.get_mixed_type_key(result0)
    except IGNORE:
        pass

def chain_47(data):
    fuzz_input = decode('bytes', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_address(fuzz_input)
        obj0 = ipaddress._BaseAddress()
        result1 = obj0.__eq__(result0)
    except IGNORE:
        pass

def chain_49(data):
    fuzz_input = decode('bytes', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_address(fuzz_input)
        obj0 = ipaddress._BaseNetwork()
        result1 = obj0.__lt__(result0)
    except IGNORE:
        pass

def chain_50(data):
    fuzz_input = decode('bytes', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_address(fuzz_input)
        obj0 = ipaddress._BaseNetwork()
        result1 = obj0.__eq__(result0)
    except IGNORE:
        pass

def chain_52(data):
    fuzz_input = decode('bytes', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_address(fuzz_input)
        obj0 = ipaddress._BaseNetwork()
        result1 = obj0.address_exclude(result0)
    except IGNORE:
        pass

def chain_60(data):
    fuzz_input = decode('bytes', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_address(fuzz_input)
        obj0 = ipaddress._BaseNetwork()
        result1 = obj0.subnets(result0)
    except IGNORE:
        pass

def chain_142(data):
    fuzz_input = decode('int', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_network(fuzz_input)
        result1 = ipaddress.get_mixed_type_key(result0)
    except IGNORE:
        pass

def chain_143(data):
    fuzz_input = decode('int', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_network(fuzz_input)
        obj0 = ipaddress._BaseAddress()
        result1 = obj0.__eq__(result0)
    except IGNORE:
        pass

def chain_144(data):
    fuzz_input = decode('int', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_network(fuzz_input)
        obj0 = ipaddress._BaseAddress()
        result1 = obj0.__lt__(result0)
    except IGNORE:
        pass

def chain_146(data):
    fuzz_input = decode('int', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_network(fuzz_input)
        obj0 = ipaddress._BaseNetwork()
        result1 = obj0.__eq__(result0)
    except IGNORE:
        pass

def chain_148(data):
    fuzz_input = decode('int', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_network(fuzz_input)
        obj0 = ipaddress._BaseNetwork()
        result1 = obj0.address_exclude(result0)
    except IGNORE:
        pass

def chain_157(data):
    fuzz_input = decode('int', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_network(fuzz_input)
        result1 = ipaddress._split_optional_netmask(result0)
    except IGNORE:
        pass

def chain_158(data):
    fuzz_input = decode('int', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_network(fuzz_input)
        obj0 = ipaddress._IPAddressBase()
        result1 = obj0._split_addr_prefix(result0)
    except IGNORE:
        pass

def chain_160(data):
    fuzz_input = decode('int', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_network(fuzz_input)
        obj0 = ipaddress._BaseNetwork()
        result1 = obj0.subnets(result0)
    except IGNORE:
        pass

def chain_185(data):
    fuzz_input = decode('int', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_network(fuzz_input)
        result1 = ipaddress._split_optional_netmask(fuzz_input)
    except IGNORE:
        pass

def chain_188(data):
    fuzz_input = decode('int', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_network(fuzz_input)
        result1 = ipaddress.get_mixed_type_key(fuzz_input)
    except IGNORE:
        pass

def chain_190(data):
    fuzz_input = decode('int', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_network(fuzz_input)
        obj0 = ipaddress._BaseAddress()
        result1 = obj0.__eq__(fuzz_input)
    except IGNORE:
        pass

def chain_191(data):
    fuzz_input = decode('int', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_network(fuzz_input)
        obj0 = ipaddress._BaseAddress()
        result1 = obj0.__lt__(fuzz_input)
    except IGNORE:
        pass

def chain_192(data):
    fuzz_input = decode('int', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_network(fuzz_input)
        obj0 = ipaddress._BaseNetwork()
        result1 = obj0.__lt__(fuzz_input)
    except IGNORE:
        pass

def chain_193(data):
    fuzz_input = decode('int', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_network(fuzz_input)
        obj0 = ipaddress._BaseNetwork()
        result1 = obj0.__eq__(fuzz_input)
    except IGNORE:
        pass

def chain_196(data):
    fuzz_input = decode('int', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_network(fuzz_input)
        obj0 = ipaddress._BaseNetwork()
        result1 = obj0.address_exclude(fuzz_input)
    except IGNORE:
        pass

def chain_278(data):
    fuzz_input = decode('bool', data)
    try:
        import ipaddress
        arg0 = '2001:658:22a:cafe:200::1/64'
        result0 = ipaddress.ip_network(arg0, fuzz_input)
        obj0 = ipaddress._BaseNetwork()
        result1 = obj0.__eq__(result0)
    except IGNORE:
        pass

def chain_295(data):
    fuzz_input = decode('bool', data)
    try:
        import ipaddress
        arg0 = '1.1.1.1/24'
        result0 = ipaddress.ip_network(arg0, fuzz_input)
        obj0 = ipaddress._BaseAddress()
        result1 = obj0.__eq__(result0)
    except IGNORE:
        pass

def chain_323(data):
    fuzz_input = decode('bool', data)
    try:
        import ipaddress
        arg0 = '1.1.1.1/16'
        result0 = ipaddress.ip_network(arg0, fuzz_input)
        obj0 = ipaddress._BaseAddress()
        result1 = obj0.__lt__(arg0)
    except IGNORE:
        pass

def chain_340(data):
    fuzz_input = decode('bytes', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_interface(fuzz_input)
        result1 = ipaddress._split_optional_netmask(result0)
    except IGNORE:
        pass

def chain_341(data):
    fuzz_input = decode('bytes', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_interface(fuzz_input)
        result1 = ipaddress.get_mixed_type_key(result0)
    except IGNORE:
        pass

def chain_342(data):
    fuzz_input = decode('bytes', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_interface(fuzz_input)
        obj0 = ipaddress._IPAddressBase()
        result1 = obj0._split_addr_prefix(result0)
    except IGNORE:
        pass

def chain_343(data):
    fuzz_input = decode('bytes', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_interface(fuzz_input)
        obj0 = ipaddress._BaseAddress()
        result1 = obj0.__eq__(result0)
    except IGNORE:
        pass

def chain_345(data):
    fuzz_input = decode('bytes', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_interface(fuzz_input)
        obj0 = ipaddress._BaseNetwork()
        result1 = obj0.__lt__(result0)
    except IGNORE:
        pass

def chain_346(data):
    fuzz_input = decode('bytes', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_interface(fuzz_input)
        obj0 = ipaddress._BaseNetwork()
        result1 = obj0.__eq__(result0)
    except IGNORE:
        pass

def chain_355(data):
    fuzz_input = decode('bytes', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_interface(fuzz_input)
        obj0 = ipaddress._BaseNetwork()
        result1 = obj0.subnets(result0)
    except IGNORE:
        pass

def chain_372(data):
    fuzz_input = decode('bytes', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_interface(fuzz_input)
        result1 = ipaddress._split_optional_netmask(fuzz_input)
    except IGNORE:
        pass

def chain_373(data):
    fuzz_input = decode('bytes', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_interface(fuzz_input)
        result1 = ipaddress.get_mixed_type_key(fuzz_input)
    except IGNORE:
        pass

def chain_375(data):
    fuzz_input = decode('bytes', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_interface(fuzz_input)
        obj0 = ipaddress._BaseAddress()
        result1 = obj0.__eq__(fuzz_input)
    except IGNORE:
        pass

def chain_376(data):
    fuzz_input = decode('bytes', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_interface(fuzz_input)
        obj0 = ipaddress._BaseAddress()
        result1 = obj0.__lt__(fuzz_input)
    except IGNORE:
        pass

def chain_377(data):
    fuzz_input = decode('bytes', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_interface(fuzz_input)
        obj0 = ipaddress._BaseNetwork()
        result1 = obj0.__lt__(fuzz_input)
    except IGNORE:
        pass

def chain_378(data):
    fuzz_input = decode('bytes', data)
    try:
        import ipaddress
        result0 = ipaddress.ip_interface(fuzz_input)
        obj0 = ipaddress._BaseNetwork()
        result1 = obj0.__eq__(fuzz_input)
    except IGNORE:
        pass

def chain_477(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        result0 = ipaddress._split_optional_netmask(fuzz_input)
        obj0 = ipaddress._BaseV6()
        result1 = obj0._compress_hextets(result0)
    except IGNORE:
        pass

def chain_490(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        result0 = ipaddress._split_optional_netmask(fuzz_input)
        result1 = ipaddress.ip_interface(fuzz_input)
    except IGNORE:
        pass

def chain_505(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        result0 = ipaddress._split_optional_netmask(fuzz_input)
        result1 = ipaddress.ip_network(fuzz_input)
    except IGNORE:
        pass

def chain_668(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Address(fuzz_input)
        obj1 = ipaddress._BaseNetwork()
        result0 = obj1.subnets(obj0)
    except IGNORE:
        pass

def chain_672(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Address(fuzz_input)
        result0 = ipaddress.get_mixed_type_key(fuzz_input)
    except IGNORE:
        pass

def chain_673(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Address(fuzz_input)
        obj1 = ipaddress._BaseAddress()
        result0 = obj1.__eq__(fuzz_input)
    except IGNORE:
        pass

def chain_674(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Address(fuzz_input)
        obj1 = ipaddress._BaseAddress()
        result0 = obj1.__lt__(fuzz_input)
    except IGNORE:
        pass

def chain_675(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Address(fuzz_input)
        obj1 = ipaddress._BaseNetwork()
        result0 = obj1.__lt__(fuzz_input)
    except IGNORE:
        pass

def chain_676(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Address(fuzz_input)
        obj1 = ipaddress._BaseNetwork()
        result0 = obj1.__eq__(fuzz_input)
    except IGNORE:
        pass

def chain_678(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Address(fuzz_input)
        obj1 = ipaddress._BaseNetwork()
        result0 = obj1.address_exclude(fuzz_input)
    except IGNORE:
        pass

def chain_764(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Interface(fuzz_input)
        obj1 = ipaddress._BaseNetwork()
        result0 = obj1.subnets(obj0)
    except IGNORE:
        pass

def chain_766(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Interface(fuzz_input)
        result0 = ipaddress.ip_interface(fuzz_input)
    except IGNORE:
        pass

def chain_767(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Interface(fuzz_input)
        result0 = ipaddress._split_optional_netmask(fuzz_input)
    except IGNORE:
        pass

def chain_768(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Interface(fuzz_input)
        result0 = ipaddress.get_mixed_type_key(fuzz_input)
    except IGNORE:
        pass

def chain_770(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Interface(fuzz_input)
        obj1 = ipaddress._BaseAddress()
        result0 = obj1.__eq__(fuzz_input)
    except IGNORE:
        pass

def chain_771(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Interface(fuzz_input)
        obj1 = ipaddress._BaseAddress()
        result0 = obj1.__lt__(fuzz_input)
    except IGNORE:
        pass

def chain_772(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Interface(fuzz_input)
        obj1 = ipaddress._BaseNetwork()
        result0 = obj1.__lt__(fuzz_input)
    except IGNORE:
        pass

def chain_773(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Interface(fuzz_input)
        obj1 = ipaddress._BaseNetwork()
        result0 = obj1.__eq__(fuzz_input)
    except IGNORE:
        pass

def chain_775(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Interface(fuzz_input)
        result0 = obj0.__eq__(fuzz_input)
    except IGNORE:
        pass

def chain_776(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Interface(fuzz_input)
        result0 = obj0.__lt__(fuzz_input)
    except IGNORE:
        pass

def chain_782(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Interface(fuzz_input)
        result0 = obj0.__str__()
    except IGNORE:
        pass

def chain_785(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Interface(fuzz_input)
        result0 = obj0.__hash__()
    except IGNORE:
        pass

def chain_897(data):
    fuzz_input = decode('int', data)
    try:
        import ipaddress
        arg0 = 1
        obj0 = ipaddress.IPv4Interface(arg0)
        result0 = obj0.__eq__(fuzz_input)
        result1 = ipaddress.ip_network(fuzz_input)
    except IGNORE:
        pass

def chain_939(data):
    fuzz_input = decode('str', data)
    try:
        import ipaddress
        arg0 = '1.1.1.1/24'
        obj0 = ipaddress.IPv4Interface(arg0)
        result0 = obj0.__eq__(fuzz_input)
        result1 = ipaddress.ip_network(fuzz_input)
    except IGNORE:
        pass

def chain_950(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Network(fuzz_input)
        obj1 = ipaddress._BaseNetwork()
        result0 = obj1.subnets(obj0)
    except IGNORE:
        pass

def chain_952(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Network(fuzz_input)
        result0 = ipaddress.ip_network(fuzz_input)
    except IGNORE:
        pass

def chain_953(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Network(fuzz_input)
        result0 = ipaddress._split_optional_netmask(fuzz_input)
    except IGNORE:
        pass

def chain_956(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Network(fuzz_input)
        result0 = ipaddress.get_mixed_type_key(fuzz_input)
    except IGNORE:
        pass

def chain_958(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Network(fuzz_input)
        obj1 = ipaddress._BaseAddress()
        result0 = obj1.__eq__(fuzz_input)
    except IGNORE:
        pass

def chain_959(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Network(fuzz_input)
        obj1 = ipaddress._BaseAddress()
        result0 = obj1.__lt__(fuzz_input)
    except IGNORE:
        pass

def chain_960(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Network(fuzz_input)
        obj1 = ipaddress._BaseNetwork()
        result0 = obj1.__lt__(fuzz_input)
    except IGNORE:
        pass

def chain_961(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Network(fuzz_input)
        obj1 = ipaddress._BaseNetwork()
        result0 = obj1.__eq__(fuzz_input)
    except IGNORE:
        pass

def chain_964(data):
    fuzz_input = decode('float', data)
    try:
        import ipaddress
        obj0 = ipaddress.IPv4Network(fuzz_input)
        obj1 = ipaddress._BaseNetwork()
        result0 = obj1.address_exclude(fuzz_input)
    except IGNORE:
        pass

CHAINS = [chain_0, chain_3, chain_6, chain_14, chain_18, chain_24, chain_29, chain_35, chain_41, chain_46, chain_47, chain_49, chain_50, chain_52, chain_60, chain_142, chain_143, chain_144, chain_146, chain_148, chain_157, chain_158, chain_160, chain_185, chain_188, chain_190, chain_191, chain_192, chain_193, chain_196, chain_278, chain_295, chain_323, chain_340, chain_341, chain_342, chain_343, chain_345, chain_346, chain_355, chain_372, chain_373, chain_375, chain_376, chain_377, chain_378, chain_477, chain_490, chain_505, chain_668, chain_672, chain_673, chain_674, chain_675, chain_676, chain_678, chain_764, chain_766, chain_767, chain_768, chain_770, chain_771, chain_772, chain_773, chain_775, chain_776, chain_782, chain_785, chain_897, chain_939, chain_950, chain_952, chain_953, chain_956, chain_958, chain_959, chain_960, chain_961, chain_964]

def TestOneInput(data):
    if not data:
        return
    CHAINS[data[0] % len(CHAINS)](data[1:])


atheris.Setup(sys.argv, TestOneInput)
atheris.Fuzz()
