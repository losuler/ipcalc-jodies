Name:           ipcalc-jodies
Version:        0.41
Release:        4%{?dist}
Summary:        IPv4 Address Calculator

License:        GPLv2
URL:            http://jodies.de/ipcalc
Source0:        http://jodies.de/ipcalc-archive/ipcalc-%{version}.tar.gz
BuildArch:      noarch

%description
ipcalc takes an IP address and netmask and calculates the resulting
broadcast, network, Cisco wildcard mask, and host range. By giving a
second netmask, you can design subnets and supernets. It is also
presents the subnetting results as easy-to-understand binary values.

Enter your netmask(s) in CIDR notation (/25) or dotted decimals
(255.255.255.0). Inverse netmasks are recognized. If you omit the
netmask ipcalc uses the default netmask for the class of your network.

%prep
%autosetup -n ipcalc-%{version}

%install
install -Dm0755 ipcalc %{buildroot}%{_bindir}/%{name}

%files
%license license
%doc changelog contributors
%{_bindir}/%{name}

%changelog
* Sun Jan 10 2021 losuler <losuler@posteo.net> - 0.41-4
- Use SHA512 in sources file

* Wed Aug 21 2019 Artem Polishchuk <ego.cordatus@gmail.com> - 0.41-3
- Initial package

